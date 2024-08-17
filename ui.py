import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget


class WordleUI(QWidget):

    def __init__(self):
        super().__init__()
        self.center()
        self.setupUI()

    def center(self):
        """
        Центрирование окна
        """
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),
                  int((screen.height() - size.height()) / 2))

    def setupUI(self):
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(100, 100, 100, 100)
        self.gridLayout.setObjectName("gridLayout")

        self.newGameButton = QtWidgets.QPushButton(self)
        self.newGameButton.setObjectName("newGameButton")
        self.gridLayout.addWidget(self.newGameButton, 0, 0, 1, 1)

        self.menuButton = QtWidgets.QPushButton(self)
        self.menuButton.setCheckable(True)
        self.menuButton.setObjectName("menuButton")
        self.gridLayout.addWidget(self.menuButton, 0, 1, 1, 1)

        self.recordsButton = QtWidgets.QPushButton(self)
        self.recordsButton.setCheckable(True)
        self.recordsButton.setObjectName("recordsButton")
        self.gridLayout.addWidget(self.recordsButton, 0, 2, 1, 1)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)

        self.clearButton = QtWidgets.QPushButton(self)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 1, 1, 1, 1)
        self.clearButton.setVisible(False)

        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 2, 0, 1, 3)

        self.hide_line_edit()

        self.nameButtons()

    def nameButtons(self):
        self.newGameButton.setText("Новая игра")
        self.menuButton.setText("Меню игры")
        self.recordsButton.setText("Меню Рекордов")
        self.pushButton.setText("Отправить")
        self.clearButton.setText("Очистить")

    def hide_line_edit(self):
        self.pushButton.setVisible(False)
        self.lineEdit.setVisible(False)

    def show_line_edit(self):
        self.pushButton.setVisible(True)
        self.lineEdit.setVisible(True)

    def change_checked_button(self, btn="menu"):
        self.menuButton.setChecked(btn == "menu")
        self.recordsButton.setChecked(btn == "records")


if __name__ == '__main__':
    app = QApplication([])
    game_window = WordleUI()
    game_window.show()
    sys.exit(app.exec_())
