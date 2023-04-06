import os


def create_project():
    os.system("git init")
    os.system("git submodule add -b 4.0 https://github.com/godotengine/godot-cpp")
    os.system("cd godot-cpp && git submodule update --init && cd ..")
    os.system(
        "/Applications/Godot.app/Contents/MacOS/Godot --dump-extension-api extension_api.json")
    os.system("python3 -m venv scons")
    os.system("source ./scons/bin/activate")
    os.system("pip install scons")
    os.system(
        "cd godot-cpp && scons platform=macos -j4 custom_api_file=../extension_api.json && cd ..")
    os.system("mkdir src")
    os.system(
        "curl https://docs.godotengine.org/en/stable/_downloads/45a3f5e351266601b5e7663dc077fe12/SConstruct >> SConstruct")


def remove_project_files():
    os.system("cd " + os.getcwd())
    os.system("rm -rf .git")
    os.system("rm -rf scons")
    os.system("rm -rf godot-cpp")
    os.system("rm .gitmodules")
    os.system("rm extension_api.json")
    os.system("rm SConstruct")
    os.system("rm -rf src")


def menu():
    print("""
        1) Create Project
        2) Remove project files
        3) Close
          """)

    value = int(input("< "))

    if value == 1:
        create_project()
    elif value == 2:
        remove_project_files()
    elif value == 3:
        exit()
    else:
        menu()


if __name__ == "__main__":
    menu()
