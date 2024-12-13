import os
import yaml
import subprocess
from graphviz import Digraph

# Чтение конфигурации
def read_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

# Проверка существования git-репозитория
def validate_git_repo(repo_path):
    if not os.path.isdir(os.path.join(repo_path, ".git")):
        raise ValueError(f"Путь {repo_path} не является git-репозиторием.")

# Получение всех коммитов, связанных с файлом
def get_commits_for_file(repo_path, target_file):
    command = ["git", "-C", repo_path, "log", "--pretty=format:%H", "--", target_file]
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True, shell=True)
    if result.returncode != 0:
        raise RuntimeError(f"Не удалось получить историю коммитов для файла {target_file}")
    return result.stdout.splitlines()

# Построение графа зависимостей
def build_dependency_graph(commits, target_file):
    graph = Digraph(format="png")
    graph.attr(rankdir="TB")
    graph.attr('node', shape='box')

    # Узел для файла
    file_node_id = f"file_{target_file.replace('.', '_')}"  # Уникальный идентификатор узла файла
    graph.node(file_node_id, label=f"Файл: {target_file}", shape="ellipse", style="filled", color="lightblue")

    # Узлы для коммитов и их связи с файлом
    for i, commit in enumerate(commits):
        graph.node(commit, label=f"Commit {commit[:7]}", shape="box", color="black")
        graph.edge(file_node_id, commit)  # Связываем файл с коммитами
        if i > 0:
            graph.edge(commits[i-1], commit)  # Связываем коммиты между собой

    return graph

# Основная функция
def main():
    # Загрузка конфигурации
    config = read_config("config.yaml")
    repo_path = config["repository_path"]
    target_file = config["target_file"]

    # Проверка репозитория
    validate_git_repo(repo_path)

    # Получение истории коммитов
    commits = get_commits_for_file(repo_path, target_file)
    if not commits:
        print(f"Не найдено коммитов для файла {target_file}.")
        return

    # Построение графа зависимостей
    graph = build_dependency_graph(commits, target_file)
    output_path = "dependency_graph"
    graph.render(output_path, cleanup=True)
    print(f"Граф зависимостей сохранён в {output_path}.png")

if __name__ == "__main__":
    main()