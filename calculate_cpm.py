# Function to perform the CPM calculation
def calculate_cpm(file_path):
    tasks = {}
    with open(file_path) as fhand:
        for line in fhand:
            singleElement = line.strip().split(',')
            task_id = singleElement[0]
            tasks['task' + task_id] = {
                'id': singleElement[0],
                'activity': singleElement[1],
                'name': singleElement[2],
                'duration': int(singleElement[3]),
                'dependencies': singleElement[4].strip().split(';') if singleElement[4] else ['none'],
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
            task['ES'] = 0
            task['EF'] = task['duration']
        else:
            for dep_id in task['dependencies']:
                dep_task = tasks['task' + dep_id]
                task['ES'] = max(task['ES'], dep_task['EF'] + 1)
            task['ES'] -= 1
            task['EF'] = task['ES'] + task['duration']

    # Backward Pass
    all_tasks = list(tasks.values())
    for task in reversed(all_tasks):
        if task['LF'] == 0:
            task['LF'] = task['EF']
            task['LS'] = task['ES']
        for dep_id in task['dependencies']:
            if dep_id != 'none':
                dep_task = tasks['task' + dep_id]
                dep_task['LF'] = min(dep_task['LF'], task['LS']) if dep_task['LF'] else task['LS']
                dep_task['LS'] = dep_task['LF'] - dep_task['duration']
                dep_task['float'] = dep_task['LS'] - dep_task['ES']

    for task in tasks.values():
        if task['float'] == 0:
            task['isCritical'] = True

    return tasks