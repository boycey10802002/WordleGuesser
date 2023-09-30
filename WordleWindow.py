from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QComboBox
from PyQt6.QtGui import QValidator
from PyQt6.QtCore import Qt
from ui.guesser_main_window import Ui_MainWindow
import typing
import re
import utils
from functools import partial

class WordleWindow(QMainWindow):
    MAX_LETTERS = 5
    FIRST_GUESS = "STARE"
    LETTERS = [chr(x + ord("A")) for x in range(26)]

    def __init__(self):
        super().__init__()
        self.button_list = []
        #self.combo_list = []
        with open(utils.Dictionary_Path().joinpath("wordle_dictionary.txt"), 'r') as f:
            self.dictionary = f.readlines()

        with open(utils.Dictionary_Path().joinpath("wordle_previous_solutions.txt"), 'r') as f:
            self.previous_solutions = f.readlines()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_ui()

        # self.ui.txt_guess.setText(WordleWindow.FIRST_GUESS)
        for index, entry in enumerate(self.ui_sets):
            self.setComboboxByText(entry['combobox'], WordleWindow.FIRST_GUESS[index])
        self.show()

    def setComboboxByText(self, combobox: QComboBox, char: str):
        # super kludgey
        for index, letter in enumerate(WordleWindow.LETTERS):
            if letter == char:
                combobox.setCurrentIndex(index)


    def setup_ui(self):
        # self.ui.txt_guess.textChanged.connect(self.update_guess_ui)
        # self.ui.txt_guess.setValidator(WordleValidator())
        self.ui_sets = []
        self.ui_sets.append({
            'index': 0,
            'button': self.ui.btn_letter_01,
            'combobox': self.ui.cbx_letter_01})

        self.ui_sets.append({
            'index': 1,
            'button': self.ui.btn_letter_02,
            'combobox': self.ui.cbx_letter_02})

        self.ui_sets.append({
            'index': 2,
            'button': self.ui.btn_letter_03,
            'combobox': self.ui.cbx_letter_03})

        self.ui_sets.append({
            'index': 3,
            'button': self.ui.btn_letter_04,
            'combobox': self.ui.cbx_letter_04})

        self.ui_sets.append({
            'index': 4,
            'button': self.ui.btn_letter_05,
            'combobox': self.ui.cbx_letter_05})

        for entry in self.ui_sets:
            entry['combobox'].addItems(WordleWindow.LETTERS)
            entry['button'].clicked.connect(partial(self.toggle_button, entry['index']))
        self.update_suggestion()

    def toggle_button(self, index: int):
        print(index)
        ui_set = self.ui_sets[index]
        checkbox = ui_set['button']
        combobox = ui_set['combobox']
        state = checkbox.checkState()
        print(checkbox.checkState())
        if state == Qt.CheckState.Checked:
            checkbox.setStyleSheet("background: green;")
            combobox.setStyleSheet("background: green;")

        elif state == Qt.CheckState.PartiallyChecked:
            checkbox.setStyleSheet("background: yellow;")
            combobox.setStyleSheet("background: yellow;")
        else:
            checkbox.setStyleSheet("background: lightgray;")
            combobox.setStyleSheet("background: lightgray;")
        print(checkbox)
        self.update_suggestion()

    def string_from_combos(self):
        guess = [x.currentText() for x in self.combo_list]

    def get_filter_snippet(self, ui_set):
        if ui_set['button'].checkState() == Qt.CheckState.Checked:
            return "[{}]".format(ui_set['combobox'].currentText())
        else:
            return "[A-Z]"

    def filter_suggestions(self):
        filtered_suggestions = []
        pattern = "^({}{}{}{}{})$".format(
            self.get_filter_snippet(self.ui_sets[0]),
            self.get_filter_snippet(self.ui_sets[1]),
            self.get_filter_snippet(self.ui_sets[2]),
            self.get_filter_snippet(self.ui_sets[3]),
            self.get_filter_snippet(self.ui_sets[4]))
        print(pattern)
        for word in self.dictionary:
            if re.match(pattern, word):
                if word in self.previous_solutions:
                    "<b>{}</b>".format(word)
                filtered_suggestions.append(word)
        return filtered_suggestions


    def update_suggestion(self):
        self.ui.txt_Suggestions.clear()
        suggestions = self.filter_suggestions()
        self.ui.txt_Suggestions.setText("".join(suggestions))


    def update_guess_ui(self):
        txt = "|||||"# self.ui.txt_guess.text()
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

        # self.ui.txt_guess.setText(txt)

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

