from PyQt5 import QtWidgets
from ui import WordleUI
from wordle import Wordle


class WordleController:
    def __init__(self, game, ui):
        self.game = game
        self.ui = ui
        self.set_connections()
        self.ui.show()

    def set_connections(self):
        self.ui.newGameButton.clicked.connect(self.new_game_button_clicked)
        self.ui.menuButton.clicked.connect(self.menu_button_clicked)
        self.ui.recordsButton.clicked.connect(self.records_button_clicked)
        self.ui.pushButton.clicked.connect(self.push_button_clicked)
        self.ui.clearButton.clicked.connect(self.clear_button_clicked)

    def new_game_button_clicked(self):
        self.ui.change_checked_button()
        self.ui.show_line_edit()

        log = self.game.new_game()
        self.ui.textBrowser.setText(log)

    def menu_button_clicked(self):
        self.ui.show_line_edit()
        self.ui.textBrowser.setText(self.game.get_log())
        self.ui.change_checked_button()

    def records_button_clicked(self):
        self.ui.hide_line_edit()
        self.ui.textBrowser.setText(self.game.get_records())
        self.ui.change_checked_button("records")

    def push_button_clicked(self):
        word = self.ui.lineEdit.text()
        self.ui.lineEdit.clear()
        log = self.game.make_attempt(word.lower())
        self.ui.textBrowser.setText(log)

    def clear_button_clicked(self):
        self.game.clear_records()
        self.ui.textBrowser.setText(self.game.get_records())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = WordleUI()
    game = Wordle()

    controller = WordleController(game, ui)

    sys.exit(app.exec_())
