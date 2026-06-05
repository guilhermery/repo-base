# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def format_task(task):
    # Trocando os colchetes por emojis para o segundo commit
    status = "✅" if task.get("done") else "⏳"
    
    priority = task['priority'].upper()
    
    return f"{status} [{priority}] #{task['id']}: {task['title']}"

def filter_tasks(tasks, show_done=True):
    if show_done:
        return tasks
    return [t for t in tasks if not t["done"]]
