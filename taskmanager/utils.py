# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def format_task(task):
    status = "✅" if task.get("done") else "⏳"
    
    priority = task['priority'].upper()
    
    # Reordenando os elementos para o terceiro commit
    return f"#{task['id']} | {status} [{priority}] {task['title']}"

"""
    Formata uma tarefa para exibição.

    Exibe o ID, status, prioridade e título da tarefa
    em uma string formatada.
    """

def filter_tasks(tasks, show_done=True):
    if show_done:
        return tasks
    return [t for t in tasks if not t["done"]]


"""
    Filtra tarefas com base no status de conclusão.

    Args:
        tasks (list): Lista de tarefas.
        show_done (bool): Se True, retorna todas as tarefas.
                          Se False, retorna apenas as pendentes.

    Returns:
        list: Lista de tarefas filtradas.
    """