from graphviz import Digraph

def create_dependency_graph(commits, target_file):
    """
    Создает граф зависимостей для указанных коммитов и файла.
    :param commits: Список коммитов (результат предыдущего этапа).
    :param target_file: Имя целевого файла.
    :return: Объект Graphviz Digraph.
    """
    graph = Digraph(format='png')
    graph.attr(rankdir='LR')  # Граф будет строиться слева направо

    # Добавляем вершину для целевого файла
    graph.node(target_file, shape='box', color='blue')

    for commit in commits:
        commit_id = commit['commit'][:7]  # Сокращаем SHA-1 коммита для читаемости
        graph.node(commit_id, shape='ellipse', color='green')  # Коммит — эллипс
        graph.edge(commit_id, target_file, label='modifies')  # Ребро от коммита к файлу

    return graph

if __name__ == "__main__":
    # Пример данных коммитов
    commits = [
        {"commit": "abc1234", "author": "Alice", "date": "2024-12-10", "message": "Initial commit"},
        {"commit": "def5678", "author": "Bob", "date": "2024-12-11", "message": "Updated example.py"}
    ]
    target_file = "example.py"

    # Создаем граф
    graph = create_dependency_graph(commits, target_file)

    # Сохраняем и визуализируем
    graph.render('dependency_graph', view=True)  # Сохраняет в файл и открывает граф
