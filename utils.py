from pathlib import *
import subprocess

def Project_Path():
    return Path(__file__).parent

def UI_Path():
    return Project_Path().joinpath("ui")

def Dictionary_Path():
    return Project_Path().joinpath("dictionaries")

def build_ui(pyfile, ui_file):
    subprocess.call("pyuic6 -o {0} {1}".format(
        UI_Path().joinpath(pyfile),
        UI_Path().joinpath(ui_file)))




