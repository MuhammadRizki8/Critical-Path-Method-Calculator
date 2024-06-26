import tkinter as tk
from tkinter import ttk, filedialog
from calculate_cpm import calculate_cpm
from visualize import visualize_critical_path_graph
# GUI setup
class CPMApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CPM Calculator")
        self.geometry("1200x800")

        self.upload_button = tk.Button(self, text="Upload File", command=self.upload_file)
        self.upload_button.pack(pady=10)
        
        self.visualize_button = tk.Button(self, text="Visualize Critical Path", command=self.visualize)
        self.visualize_button.pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Duration", "Dependencies", "ES", "EF", "LS", "LF", "Float", "Critical"), show='headings')
        self.tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.CENTER, width=100)
        
        self.tasks = None

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.run_cpm(file_path)

    def run_cpm(self, file_path):
        self.tasks = calculate_cpm(file_path)
        for i in self.tree.get_children():
            self.tree.delete(i)
        id_to_activity = {task['id']: task['activity'] for task in self.tasks.values()}
        for task in self.tasks.values():
            dependencies_as_activities = [id_to_activity[dep_id] for dep_id in task['dependencies'] if dep_id in id_to_activity]
            if not dependencies_as_activities:
                dependencies_as_activities = ['none']
            else:
                dependencies_as_activities = ' & '.join(dependencies_as_activities)

            self.tree.insert("", "end", values=(task['activity'], task['name'], task['duration'], dependencies_as_activities, task['ES'], task['EF'], task['LS'], task['LF'], task['float'], task['isCritical']))
            
    def visualize(self):
        if self.tasks:
            visualize_critical_path_graph(self.tasks)

if __name__ == "__main__":
    app = CPMApp()
    app.mainloop()
