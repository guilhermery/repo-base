# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def format_task(task):
    status = "✅" if task.get("done") else "⏳"
    
    priority = task['priority'].upper()
    
    # Reordenando os elementos para o terceiro commit
    return f"#{task['id']} | {status} [{priority}] {task['title']}"

def filter_tasks(tasks, show_done=True):
    if show_done:
        return tasks
    return [t for t in tasks if not t["done"]]
