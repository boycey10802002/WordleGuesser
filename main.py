import sys
from importlib import reload
import argparse
import utils
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
import WordleWindow

utils = reload(utils)
UI_FILE_NAME = "guesser_main_window.ui"
UI_PYTHON_FILE_NAME = "guesser_main_window.py"



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="A Wordle support program"
    )
    parser.add_argument('--build_ui',
                        '-u',
                        default=False,
                        action="store_true"
                        )

    args = parser.parse_args()
    print(args)
    if args.build_ui:
        utils.build_ui(UI_PYTHON_FILE_NAME, UI_FILE_NAME)

    app = QApplication(sys.argv)
    reload(WordleWindow)
    main_windows = WordleWindow.WordleWindow()
    sys.exit(app.exec())
