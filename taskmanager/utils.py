# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def format_task(task):
    status = "[X]" if task["done"] else "[]"
    priority = task["priority"].upper()
    return f"{status} | {priority} | #{task['id']} - {task['title']}"

def filter_tasks(tasks, show_done=True, priority=None):
    filtered_tasks = tasks

    if not show_done:
        filtered_tasks = [t for t in filtered_tasks if not t["done"]]

    if priority is not None:
        filtered_tasks = [
            t for t in filtered_tasks
            if t["priority"].lower() == priority.lower()
        ]

    return filtered_tasks
