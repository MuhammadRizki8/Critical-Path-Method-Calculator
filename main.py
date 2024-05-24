import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import csv

# Function to perform the CPM calculation
def calculate_cpm(file_path):
    tasks = {}
    with open(file_path) as fhand:
        for line in fhand:
            singleElement = line.strip().split(',')
            task_id = singleElement[0]
            tasks['task' + task_id] = {
                'id': singleElement[0],
                'name': singleElement[1],
                'duration': int(singleElement[2]),
                'dependencies': singleElement[3].strip().split(';') if singleElement[3] else ['-1'],
                'ES': 0,
                'EF': 0,
                'LS': 0,
                'LF': 0,
                'float': 0,
                'isCritical': False
            }

    # Forward Pass
    for task in tasks.values():
        if '-1' in task['dependencies']:
            task['ES'] = 1
            task['EF'] = task['duration']
        else:
            for dep_id in task['dependencies']:
                dep_task = tasks['task' + dep_id]
                task['ES'] = max(task['ES'], dep_task['EF'] + 1)
            task['EF'] = task['ES'] + task['duration'] - 1

    # Backward Pass
    all_tasks = list(tasks.values())
    for task in reversed(all_tasks):
        if task['LF'] == 0:
            task['LF'] = task['EF']
            task['LS'] = task['ES']
        for dep_id in task['dependencies']:
            if dep_id != '-1':
                dep_task = tasks['task' + dep_id]
                dep_task['LF'] = min(dep_task['LF'], task['LS'] - 1) if dep_task['LF'] else task['LS'] - 1
                dep_task['LS'] = dep_task['LF'] - dep_task['duration'] + 1
                dep_task['float'] = dep_task['LF'] - dep_task['EF']

    for task in tasks.values():
        if task['float'] == 0:
            task['isCritical'] = True

    return tasks

# GUI setup
class CPMApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CPM Calculator")
        self.geometry("1000x600")

        self.upload_button = tk.Button(self, text="Upload File", command=self.upload_file)
        self.upload_button.pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Duration", "ES", "EF", "LS", "LF", "Float", "Critical"), show='headings')
        self.tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.CENTER, width=100)

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.run_cpm(file_path)

    def run_cpm(self, file_path):
        tasks = calculate_cpm(file_path)
        for i in self.tree.get_children():
            self.tree.delete(i)
        for task in tasks.values():
            self.tree.insert("", "end", values=(task['id'], task['name'], task['duration'], task['ES'], task['EF'], task['LS'], task['LF'], task['float'], task['isCritical']))

if __name__ == "__main__":
    app = CPMApp()
    app.mainloop()
