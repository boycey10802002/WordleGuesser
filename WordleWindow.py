from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox
from PyQt6.QtGui import QValidator
from PyQt6.QtCore import Qt
from ui.guesser_main_window import Ui_MainWindow
import typing
import re
import utils
class WordleWindow(QMainWindow):
    MAX_LETTERS = 5
    FIRST_GUESS = "STARE"
    LETTERS = [chr(x + ord("A")) for x in range(26)]
    print(ord("A") + 26)

    def __init__(self):
        super().__init__()
        self.button_list = []
        self.combo_list = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_ui()
        self.ui.txt_guess.setText(WordleWindow.FIRST_GUESS)
        self.show()
        self.suggestions = None
        with open(utils.Dictionary_Path().joinpath("wordle_dictionary.txt"), 'r') as f:
            self.suggestions = f.readlines()


    def setup_ui(self):
        self.ui.txt_guess.textChanged.connect(self.update_guess_ui)
        self.ui.txt_guess.setValidator(WordleValidator())

        self.ui.btn_letter_01.clicked.connect(lambda: self.toggle_button(self.ui.btn_letter_01))
        self.ui.btn_letter_02.clicked.connect(lambda: self.toggle_button(self.ui.btn_letter_02))
        self.ui.btn_letter_03.clicked.connect(lambda: self.toggle_button(self.ui.btn_letter_03))
        self.ui.btn_letter_04.clicked.connect(lambda: self.toggle_button(self.ui.btn_letter_04))
        self.ui.btn_letter_05.clicked.connect(lambda: self.toggle_button(self.ui.btn_letter_05))
        self.button_list.append(self.ui.btn_letter_01)
        self.button_list.append(self.ui.btn_letter_02)
        self.button_list.append(self.ui.btn_letter_03)
        self.button_list.append(self.ui.btn_letter_04)
        self.button_list.append(self.ui.btn_letter_05)
        for button in self.button_list:
            button.clicked.connect(lambda: self.toggle_button(button))

        self.combo_list.append(self.ui.cbx_letter_01)
        self.combo_list.append(self.ui.cbx_letter_02)
        self.combo_list.append(self.ui.cbx_letter_03)
        self.combo_list.append(self.ui.cbx_letter_04)
        self.combo_list.append(self.ui.cbx_letter_05)
        for combo_box in self.combo_list:
            combo_box.addItems(WordleWindow.LETTERS)



        self.update_suggestion()

    def toggle_button(self, checkbox: QCheckBox):
        # print("index: " + str(index))
        # checkbox = self.button_list[index]
        state = checkbox.checkState()
        print(checkbox.checkState())
        if state == Qt.CheckState.Checked:
            checkbox.setStyleSheet("background: green;")
        elif state == Qt.CheckState.PartiallyChecked:
            checkbox.setStyleSheet("background: yellow;")
        else:
            checkbox.setStyleSheet("background: lightgray;")
        print(checkbox)
        self.update_suggestion()


        #if(b.checkState())

    def update_suggestion(self):
    self.ui.txt_Suggestions.setText("\n".join(self.suggestions)


    def update_guess_ui(self):
        txt = self.ui.txt_guess.text()
        txt = txt.upper()
        for i in range(WordleWindow.MAX_LETTERS):
            try:
                # self.ui.btn_letter_05
                self.button_list[i].setText(txt[i])
                self.button_list[i].setEnabled(True)
            except:
                print("NOPE")
                self.button_list[i].setText("[ ]")
                self.button_list[i].setEnabled(False)
                #self.ui.btn_letter_01.

        self.ui.txt_guess.setText(txt)

class WordleValidator(QValidator):
    def __init__(self):
        super().__init__()
        self.validator_string = r"^[a-zA-Z]+$"

    def validate(self, input: str, pos: int) -> typing.Tuple['QValidator.State', str, int]:
        b = str(re.match(self.validator_string, input))
        print("match: " + b)

        if (len(input) <= 5):
            return (QValidator.State.Intermediate, input, pos)


        if len(input) > 5:
            return (QValidator.State.Invalid, input, pos)

        return (QValidator.State.Acceptable, input, len(input))

