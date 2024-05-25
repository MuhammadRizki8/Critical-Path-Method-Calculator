import tkinter as tk
from tkinter import ttk, filedialog
import networkx as nx
import matplotlib.pyplot as plt

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
                'dependencies': singleElement[3].strip().split(';') if singleElement[3] else ['none'],
                'ES': 0,
                'EF': 0,
                'LS': 0,
                'LF': 0,
                'float': 0,
                'isCritical': False
            }

    # Forward Pass
    for task in tasks.values():
        if 'none' in task['dependencies']:
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
            if dep_id != 'none':
                dep_task = tasks['task' + dep_id]
                dep_task['LF'] = min(dep_task['LF'], task['LS'] - 1) if dep_task['LF'] else task['LS'] - 1
                dep_task['LS'] = dep_task['LF'] - dep_task['duration'] + 1
                dep_task['float'] = dep_task['LF'] - dep_task['EF']

    for task in tasks.values():
        if task['float'] == 0:
            task['isCritical'] = True

    return tasks

# Function to visualize the critical path as a graph
def visualize_critical_path_graph(tasks):
    G = nx.Graph()

    for task in tasks.values():
        G.add_node(task['id'], label=task['id'], duration=task['duration'], critical=task['isCritical'])

    for task in tasks.values():
        for dep_id in task['dependencies']:
            if dep_id != 'none':
                G.add_edge(dep_id, task['id'])

    pos = nx.spring_layout(G)

    plt.figure(figsize=(12, 8))

    critical_edges = [(u, v) for u, v in G.edges if tasks['task' + u]['isCritical'] and tasks['task' + v]['isCritical']]
    non_critical_edges = [(u, v) for u, v in G.edges if not (tasks['task' + u]['isCritical'] and tasks['task' + v]['isCritical'])]

    # Draw nodes
    node_colors = ['red' if task['isCritical'] else 'lightblue' for task in tasks.values()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)

    # Draw edges
    nx.draw_networkx_edges(G, pos, edgelist=non_critical_edges, arrowstyle='-|>', arrowsize=10, edge_color='black')
    nx.draw_networkx_edges(G, pos, edgelist=critical_edges, arrowstyle='-|>', arrowsize=10, edge_color='red')

    # Draw labels
    nx.draw_networkx_labels(G, pos, labels=nx.get_node_attributes(G, 'label'), font_size=8)
    edge_labels = {(u, v): f'{tasks["task" + v]["duration"]}' for u, v in G.edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    plt.title('Critical Path Method (CPM)')
    plt.show()

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
        for task in self.tasks.values():
            self.tree.insert("", "end", values=(task['id'], task['name'], task['duration'], task['dependencies'], task['ES'], task['EF'], task['LS'], task['LF'], task['float'], task['isCritical']))
            
    def visualize(self):
        if self.tasks:
            visualize_critical_path_graph(self.tasks)

if __name__ == "__main__":
    app = CPMApp()
    app.mainloop()
