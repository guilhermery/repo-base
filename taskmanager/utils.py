# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def format_task(task):
    """
    Formata uma tarefa para exibição.

    Exibe o ID, status, prioridade e título da tarefa
    em uma string formatada.
    """
    status = "?" if task.get("done") else "?"
    priority = task["priority"].upper()

    return f"#{task['id']} | {status} [{priority}] {task['title']}"

def filter_tasks(tasks, show_done=True, priority=None):
    """
    Filtra tarefas com base no status de conclusão e prioridade.

    Args:
        tasks (list): Lista de tarefas.
        show_done (bool): Se True, retorna todas as tarefas.
                          Se False, retorna apenas as pendentes.
        priority (str): Prioridade usada como filtro opcional.

    Returns:
        list: Lista de tarefas filtradas.
    """
    filtered_tasks = tasks

    if not show_done:
        filtered_tasks = [t for t in filtered_tasks if not t["done"]]

    if priority is not None:
        filtered_tasks = [
            t for t in filtered_tasks
            if t["priority"].lower() == priority.lower()
        ]

    return filtered_tasks