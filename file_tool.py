import os
import sys
import shutil
import datetime 

def list_dir(path):
    """Show folder contents"""
    if os.path.isdir(path):
        print("Folder contents:")
        for item in os.listdir(path):
            print(f"- {item}")
    else:
        print(f"Folder '{path}' not found.")

def delete_file(filename):
    """delete file"""
    if os.path.isfile(filename):
        os.remove(filename)
        print(f"File '{filename}' successfully removed.")
    else:
        print(f"File '{filename}' not found.")

def delete_path(path):
    """Delete folder"""
    if os.path.isdir(path):
        try:
            shutil.rmtree(path)
            print(f"Folder '{path}' successfully removed.")
        except Exception as e:
            print(f"Error: Could not delete folder '{path}': {e}")
    else:
        print(f"Folder '{path}' not found.")

def file_info(filename):
    """show file information"""
    if os.path.isfile(filename):
        abs_path = os.path.abspath(filename)
        size = os.path.getsize(filename)
        modified = os.path.getatime(filename)
        modified_time = datetime.datetime.fromtimestamp(modified)
        print(f"Way: {abs_path}")
        print(f"Size: {size} байт")
        print(f"Last modified: {modified_time.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print(f"File '{filename}' not found.")

def show_help():
    """Show help menu"""
    print("""=== Help Menu ===
list         — show folder contest
delete       — delete file of folder
delete_file  — delete file
delete_path  — delete folder
info         — show file info
help         — show help menu
*void        — Mandatory postscript(if don't use a file) example: help void
""")

# Count the number of arguments and if there are less than 3, show this menu.
if len(sys.argv) < 3:
    print("Use: python3 file_tool.py <command> <file of folder>\nFor reference enter: help void")
    sys.exit(1)

# Arguments.
command = sys.argv[1]
target  = sys.argv[2]

# Main.
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
        print("The specified path is neither a file nor a folder.")
elif command == "delete_file":
    delete_file(target)
elif command == "delete_path":
    confirm = input("Are you sure? (y/yes): ")
    if confirm.lower() in ('y', 'yes'):
        delete_path(target)
elif command == "info":
    file_info(target)
elif command == "help":
    show_help()
else:
    print(f"Unknow command '{command}'. For reference use 'help void'.")
