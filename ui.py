from PyQt5 import QtCore, QtGui, QtWidgets
from wordle import Wordle


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.game = Wordle()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setPointSize(8)

        self.newGameButton = QtWidgets.QPushButton(self.centralwidget)
        self.newGameButton.setGeometry(QtCore.QRect(90, 160, 161, 61))
        self.newGameButton.setFont(font)
        self.newGameButton.setObjectName("newGameButton")

        self.menuButton = QtWidgets.QPushButton(self.centralwidget)
        self.menuButton.setGeometry(QtCore.QRect(290, 160, 161, 61))
        self.menuButton.setFont(font)
        self.menuButton.setObjectName("menuButton")
        self.menuButton.setVisible(False)

        self.recordsButton = QtWidgets.QPushButton(self.centralwidget)
        self.recordsButton.setGeometry(QtCore.QRect(490, 160, 161, 61))
        self.recordsButton.setFont(font)
        self.recordsButton.setObjectName("recordsButton")
        self.recordsButton.setVisible(False)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 240, 75, 23))
        font.setPointSize(5)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setVisible(False)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(182, 240, 381, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMaxLength(4)
        self.lineEdit.setVisible(False)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(90, 270, 561, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setVisible(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.newGameButton.clicked.connect(self.new_game_button_clicked)
        self.menuButton.clicked.connect(self.menu_button_clicked)
        self.recordsButton.clicked.connect(self.records_button_clicked)
        self.pushButton.clicked.connect(self.push_button_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.newGameButton.setText(_translate("MainWindow", "Новая игра"))
        self.menuButton.setText(_translate("MainWindow", "Меню игры"))
        self.recordsButton.setText(_translate("MainWindow", "Меню Рекордов"))
        self.pushButton.setText(_translate("MainWindow", "Отправить"))

    def new_game_button_clicked(self):
        self.menuButton.setVisible(True)
        self.recordsButton.setVisible(True)
        self.textBrowser.setVisible(True)
        self.show_line_edit()
        log = self.game.new_game()
        self.textBrowser.setText(log)

    def menu_button_clicked(self):
        self.show_line_edit()
        self.textBrowser.setText(self.game.get_log())

    def records_button_clicked(self):
        self.hide_line_edit()
        self.textBrowser.setText(self.game.get_records())

    def push_button_clicked(self):
        word = self.lineEdit.text()
        self.lineEdit.clear()
        log = self.game.make_attempt(word.lower())
        self.textBrowser.setText(log)

    def hide_line_edit(self):
        self.pushButton.setVisible(False)
        self.lineEdit.setVisible(False)
    
    def show_line_edit(self):
        self.pushButton.setVisible(True)
        self.lineEdit.setVisible(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
