from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
from wordle import Wordle


class WordleController:
    def __init__(self, game, ui):
        self.game = game
        self.ui = ui
        self.set_connections()

    def set_connections(self):
        self.ui.newGameButton.clicked.connect(self.new_game_button_clicked)
        self.ui.menuButton.clicked.connect(self.menu_button_clicked)
        self.ui.recordsButton.clicked.connect(self.records_button_clicked)
        self.ui.pushButton.clicked.connect(self.push_button_clicked)

    def new_game_button_clicked(self):
        self.ui.menuButton.setVisible(True)
        self.ui.recordsButton.setVisible(True)
        self.ui.textBrowser.setVisible(True)
        self.ui.show_line_edit()

        log = self.game.new_game()
        self.ui.textBrowser.setText(log)

    def menu_button_clicked(self):
        self.ui.show_line_edit()
        self.ui.textBrowser.setText(self.game.get_log())

    def records_button_clicked(self):
        self.ui.hide_line_edit()
        self.ui.textBrowser.setText(self.game.get_records())

    def push_button_clicked(self):
        word = self.ui.lineEdit.text()
        self.ui.lineEdit.clear()
        log = self.game.make_attempt(word.lower())
        self.ui.textBrowser.setText(log)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    game = Wordle()
    
    controller = WordleController(game, ui)
    

    MainWindow.show()
    sys.exit(app.exec_())
