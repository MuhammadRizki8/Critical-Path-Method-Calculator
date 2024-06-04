import plotly.graph_objs as go
from plotly.subplots import make_subplots
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def visualize_critical_path_graph(tasks):
    G = nx.DiGraph()  # Use DiGraph for directed graph

    # Add a Start node
    G.add_node('Start', label='Start', duration=0, critical=True)
    
    for task in tasks.values():
        G.add_node(task['id'], label=task['activity'], duration=task['duration'], critical=task['isCritical'])

    for task in tasks.values():
        if 'none' in task['dependencies']:
            G.add_edge('Start', task['id'])
        else:
            for dep_id in task['dependencies']:
                if dep_id != 'none':
                    G.add_edge(dep_id, task['id'])

    # Use pygraphviz layout with left-to-right orientation
    A = nx.nx_agraph.to_agraph(G)
    A.layout(prog='dot', args='-Grankdir=LR')
    pos = nx.nx_agraph.graphviz_layout(G, prog='dot', args='-Grankdir=LR')

    plt.figure(figsize=(12, 8))

    # Draw all nodes and edges
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=400)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges, arrowsize=10)
    nx.draw_networkx_labels(G, pos, labels=nx.get_node_attributes(G, 'label'), font_size=8)
    edge_labels = {(u, v): f'{G.nodes[v]["duration"]}' for u, v in G.edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    # Highlight critical path nodes and edges
    critical_nodes = [node for node in G.nodes if G.nodes[node].get('critical', False)]
    critical_edges = [(u, v) for u, v in G.edges if G.nodes[u].get('critical', False) and G.nodes[v].get('critical', False)]

    nx.draw_networkx_nodes(G, pos, nodelist=critical_nodes, node_color='red', node_size=400)
    nx.draw_networkx_edges(G, pos, edgelist=critical_edges, edge_color='red', arrowsize=10)

    # Highlight the Start node
    nx.draw_networkx_nodes(G, pos, nodelist=['Start'], node_color='green', node_size=400)

    # Create legend
    red_patch = mpatches.Patch(color='red', label='Critical Path')
    blue_patch = mpatches.Patch(color='lightblue', label='Non-Critical Path')
    green_patch = mpatches.Patch(color='green', label='Start Node')
    plt.legend(handles=[red_patch, blue_patch, green_patch], loc='best')

    plt.title('Combined Project Visualization with Critical Path')
    plt.show()

def visualize_critical_path_graph_plotly(tasks):
    G = nx.DiGraph()

    for task in tasks.values():
        G.add_node(task['id'], label=task['id'], duration=task['duration'], critical=task['isCritical'])

    for task in tasks.values():
        for dep_id in task['dependencies']:
            if dep_id != 'none':
                G.add_edge(dep_id, task['id'])

    pos = nx.spring_layout(G)

    edge_trace = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_trace.append(go.Scatter(
            x=[x0, x1, None],
            y=[y0, y1, None],
            line=dict(width=2, color='red' if tasks['task' + edge[0]]['isCritical'] and tasks['task' + edge[1]]['isCritical'] else 'black'),
            hoverinfo='none',
            mode='lines'))

    node_trace = go.Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers+text',
        textposition='top center',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            size=10,
            colorbar=dict(
                thickness=15,
                title='Task Duration',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    for node in G.nodes():
        x, y = pos[node]
        node_trace['x'] += tuple([x])
        node_trace['y'] += tuple([y])
        node_trace['text'] += tuple([f"{tasks['task' + node]['id']}: {tasks['task' + node]['duration']}"])

    fig = go.Figure(data=edge_trace + [node_trace],
                    layout=go.Layout(
                        title='Critical Path Method (CPM)',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        annotations=[dict(
                            text="",
                            showarrow=False,
                            xref="paper", yref="paper")],
                        xaxis=dict(showgrid=False, zeroline=False),
                        yaxis=dict(showgrid=False, zeroline=False)))

    fig.show()