import os
import sys
import shutil
import datetime 

def list_dir(path):
    """Показать содержымое папки"""
    if os.path.isdir(path):
        print("Содержимое папки:")
        for item in os.listdir(path):
            print(f"- {item}")
    else:
        print(f"Папка '{path}' не найдена.")

def delete_file(filename):
    """Удалить файл"""
    if os.path.isfile(filename):
        os.remove(filename)
        print(f"Файл '{filename}' успешно удалён.")
    else:
        print(f"Файл '{filename}' не найден.")

def delete_path(path):
    """Удалить папку"""
    if os.path.isdir(path):
        try:
            shutil.rmtree(path)
            print(f"Папка '{path}' успешно удалена.")
        except Exception as e:
            print(f"Ошибка: не удалось удалить папку '{path}': {e}")
    else:
        print(f"Папка '{path}' не найдена.")

def file_info(filename):
    """Показать инф. о папке"""
    if os.path.isfile(filename):
        abs_path = os.path.abspath(filename)
        size = os.path.getsize(filename)
        modified = os.path.getatime(filename)
        modified_time = datetime.datetime.fromtimestamp(modified)
        print(f"Путь: {abs_path}")
        print(f"Размер: {size} байт")
        print(f"Последнее изменение: {modified_time.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print(f"Файл '{filename}' не найден.")

def show_help():
    """Показать меню помощи"""
    print("""=== Меню помощи ===
list         — показать содержимое папки
delete       — удалить файл или папку
delete_file  — удалить только файл
delete_path  — удалить только директорию
info         — показать информацию о файле
help         — показать это меню
*void        — обязательная приписка(если не использовать файл) пример: help void
""")

# Посчитать количество аргументов и если менеше 3 показать это меню.
if len(sys.argv) < 3:
    print("Использование: python3 file_tool.py <команда> <файл или папка>\nДля справки используйте команду: help void")
    sys.exit(1)# Завершение программы после выполнения этого кода.

# Аргументы.
command = sys.argv[1]
target  = sys.argv[2]

# Основное тело программы.
if command == "list":
    list_dir(target)
elif command == "delete":
    if os.path.isfile(target):
        delete_file(target)
    elif os.path.isdir(target):
        confirm = input("Вы уверены, что хотите удалить папку? (y/yes): ")
        if confirm.lower() in ('y', 'yes'):
            delete_path(target)
    else:
        print("Указанный путь не является ни файлом, ни папкой.")
elif command == "delete_file":
    delete_file(target)
elif command == "delete_path":
    confirm = input("Вы уверены, что хотите удалить папку? (y/yes): ")
    if confirm.lower() in ('y', 'yes'):
        delete_path(target)
elif command == "info":
    file_info(target)
elif command == "help":
    show_help()
else:
    print(f"Неизвестная команда '{command}'. Для справки используйте 'help'.")
