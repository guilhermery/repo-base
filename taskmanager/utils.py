# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def format_task(task):
    status = "[x]" if task["done"] else "[ ]"
    priority = task["priority"].upper()
    task_id = task["id"]
    title = task["title"]

    return f"{status} | {priority} | #{task_id} - {title}"

def filter_tasks(tasks, show_done=True, priority=None):
    priority_filter = priority.lower() if priority is not None else None
    filtered_tasks = []

    for task in tasks:
        if not show_done and task["done"]:
            continue

        if priority_filter is not None and task["priority"].lower() != priority_filter:
            continue

        filtered_tasks.append(task)

    return filtered_tasks
    