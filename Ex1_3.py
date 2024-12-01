
def merge_files(file_names, output_file):
    # Словарь для хранения количества строк в каждом файле
    file_line_counts = {}

    # Читаем файлы и подсчитываем количество строк в каждом
    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file_line_counts[file_name] = len(lines)

    # Сортируем файлы по количеству строк
    sorted_files = sorted(file_names, key=lambda x: file_line_counts[x])

    # Записываем содержимое файлов в результирующий файл
    with open(output_file, 'w', encoding='utf-8') as output:
        for file_name in sorted_files:
            with open(file_name, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                output.write(f"{file_name}\n")
                output.write(f"{len(lines)}\n")
                output.write("".join(lines))
                output.write("\n")  # Добавляем пустую строку между файлами

# Пример использования
file_names = ['recipes.txt', 'recipes_2p.txt']
output_file = 'result.txt'
merge_files(file_names, output_file)