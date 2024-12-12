Как работает программа

Программа визуализирует граф зависимостей для указанного файла в git-репозитории. Она состоит из трёх основных модулей:
	1.	Чтение конфигурации: загружает пути к инструментам и данным из файла config.yaml.
	2.	Анализ git-репозитория: извлекает коммиты, связанные с указанным файлом.
	3.	Построение графа зависимостей: на основе данных коммитов создает визуализацию графа с помощью Graphviz.

Порядок работы программы
	1.	Подготовка:
	•	Убедитесь, что config.yaml содержит актуальные пути (об этом ниже).
	•	Проверьте, что Graphviz установлен и доступен в системе.
	2.	Запуск программы:
Выполните основной скрипт для запуска анализа и визуализации:

python graph_visualizer.py


	3.	Вывод:
	•	Программа создаёт файл dependency_graph.png с визуализацией.
	•	Открывает сгенерированный граф (если указано view=True).

Где нужно настроить пути
	1.	В config.yaml:
Укажите следующие пути:

graphviz_path: "/usr/local/bin/dot"  # Путь к исполняемому файлу Graphviz (измените, если Graphviz установлен в другом месте)
repo_path: "/path/to/repo"           # Абсолютный путь к анализируемому git-репозиторию
target_file: "example.py"            # Имя файла, для которого строится граф зависимостей

Как проверить путь graphviz_path:
	•	В терминале выполните:

which dot

Вывод покажет путь к исполняемому файлу, например: /usr/local/bin/dot.

	2.	В файле graph_visualizer.py:
Если config.yaml настроен, пути менять не нужно. Скрипт автоматически загружает их из конфигурации:

from config_reader import read_config

config = read_config('config.yaml')
graphviz_path = config['graphviz_path']
repo_path = config['repo_path']
target_file = config['target_file']

Если всё же нужно указать пути вручную:
Можно заменить вызовы из config_reader.py на прямую передачу путей:

graphviz_path = "/usr/local/bin/dot"
repo_path = "/path/to/repo"
target_file = "example.py"


	3.	В тестах (test_project.py):
В тестах можно использовать тестовые пути и файлы:

config = {
    'graphviz_path': '/usr/local/bin/dot',
    'repo_path': '/fake/path/to/repo',
    'target_file': 'test_file.py'
}

Установка зависимостей
	1.	Создайте виртуальное окружение для проекта:

python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate     # Для Windows


	2.	Установите зависимости:

pip install -r requirements.txt


	3.	Убедитесь, что все зависимости установлены:

pip list

Пример запуска
	1.	Настройте config.yaml:

graphviz_path: "/usr/bin/dot"
repo_path: "/Users/username/projects/myrepo"
target_file: "main.py"


	2.	Запустите скрипт:

python graph_visualizer.py


	3.	Результат:
В директории проекта появится файл dependency_graph.png, который можно открыть.

Возможные ошибки и их решение
	1.	Ошибка FileNotFoundError:
	•	Проверьте, существует ли указанный repo_path.
	2.	Ошибка ValueError: The directory is not a valid git repository:
	•	Убедитесь, что указанный путь является git-репозиторием.
	3.	Graphviz не установлен:
	•	Установите Graphviz:
	•	Для macOS:

brew install graphviz


	•	Для Ubuntu:

sudo apt install graphviz


	•	Для Windows:
Скачайте Graphviz с официального сайта и укажите путь к dot.exe в config.yaml.

Если что-то непонятно или требуется помощь с настройкой, напиши!
