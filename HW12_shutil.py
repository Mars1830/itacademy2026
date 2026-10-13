import os.path
import shutil


def task1():
    shutil.copy("settings.ini", "settings_backup.ini")


def task2():
    backup_folder = "logs_backup"
    if not os.path.isdir(backup_folder):
        os.makedirs(backup_folder)
    shutil.copy("app.log", f"{backup_folder}/app.log")


def task3():
    project_folder = "."
    backup_folder = "../project_backup"
    try:
        shutil.copytree(project_folder, backup_folder, dirs_exist_ok=False)
    except FileExistsError:
        shutil.rmtree(backup_folder)
        shutil.copytree(project_folder, backup_folder)


def task4():
    try:
        shutil.move("report.txt", "report_old.txt")
    except FileNotFoundError:
        print("File not found")


def task5():
    logs = "logs"
    logs_archive = "logs/archive"
    if not os.path.isdir(logs_archive):
        os.mkdir(logs_archive)
    for file in os.listdir(logs):
        if file != "archive":
            shutil.move(f"{logs}/{file}", f"{logs_archive}/{file}")


# task 6
def clean_build():
    try:
        shutil.rmtree("build")
    except:
        print("Error")
    else:
        print("Build deleted successfully")


def task7():
    shutil.make_archive("project_backup", "zip", ".")


def task8():
    restored = "restored_project"
    if os.path.isdir(restored):
        shutil.rmtree(restored)
    shutil.unpack_archive("project_backup.zip", restored)


def task9():
    bytes_per_mb = 1024 * 1024
    disk_info = shutil.disk_usage(".")
    for data in disk_info:
        print(round(data / bytes_per_mb, 2))


def task10():
    python_path = shutil.which("python")
    if python_path is None:
        python_path = shutil.which("python3")
    if python_path is None:
        print("Path not found")
    else:
        print(f"Python path: {python_path}")


if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    # task4()
    task5()
    clean_build()
    task7()
    task8()
    task9()
    task10()