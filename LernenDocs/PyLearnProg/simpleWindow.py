__author__ = 'Fabian'

from PyQt4 import QtGui, QtCore
from question_import import *

class SimpleWindow(QtGui.QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

        self.question_importer = QuestionImporter()


    def initUI(self):

        self.centerWidget = LearnToolMainWidget()
        self.setCentralWidget(self.centerWidget)

        exitAction = QtGui.QAction(QtGui.QIcon('exit24.jpg'), 'LadeFragen', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Lade Fragen')
        exitAction.triggered.connect(self.load_questions)

        self.toggle_random_question = QtGui.QAction(QtGui.QIcon('exit24.jpg'), 'Zufaellig', self)
        self.toggle_random_question.setShortcut('Ctrl+R')
        self.toggle_random_question.triggered.connect(self.toggle_random)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(self.toggle_random_question)

        #toolbar = self.addToolBar('Exit')
        #toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 700, 350)
        self.setWindowTitle('Main window')
        self.show()

    def closeEvent(self, event):
        event.accept()

    def load_questions(self):
        self.centerWidget.question_pack = self.question_importer.read_questions_from_file()
        self.centerWidget.question_pack_loaded()

    def toggle_random(self):
        self.centerWidget.toggle_random = not self.centerWidget.toggle_random
        if self.centerWidget.toggle_random:
            self.toggle_random_question.setText("Geordnet")
        else:
            self.toggle_random_question.setText("Zufaellig")
            self.centerWidget.question_pack.reset_question_index()


class LearnToolMainWidget(QtGui.QWidget):

    def __init__(self):

        super().__init__()

        self.answer_shown = False
        self.current_answer = "ANTWORT"
        self.current_question = "QUESTION"
        self.toggle_random = False

        self.question_pack = 0

        self.init_ui()


    def init_ui(self):

        self.btn_answer = QtGui.QPushButton("Antwort zeigen")
        self.btn_next_question = QtGui.QPushButton("Nächste Frage")
        self.btn_answer.clicked.connect(self.display_answer)
        self.btn_next_question.clicked.connect(self.fetch_next_question)
        self.btn_answer.setEnabled(False)
        self.btn_next_question.setEnabled(False)



        self.textbox_question = QtGui.QLabel(self.current_question)
        self.textbox_answer = QtGui.QLabel(self.current_answer)
        self.textbox_question.setAlignment(QtCore.Qt.AlignCenter)
        self.textbox_answer.setAlignment(QtCore.Qt.AlignCenter)
        self.textbox_question.setWordWrap(True)

        vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()

        hbox.addWidget(self.btn_answer)
        hbox.addWidget(self.btn_next_question)

        vbox.addWidget(self.textbox_question)
        vbox.addWidget(self.textbox_answer)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def display_answer(self):
        if not self.answer_shown:
            self.textbox_answer.setText(self.current_answer)
            self.btn_answer.setText("Antwort verstecken")
            self.answer_shown = True
        else:
            self.textbox_answer.setText("")
            self.btn_answer.setText("Antwort zeigen")
            self.answer_shown = False

    def fetch_next_question(self):
        if self.toggle_random:
            qa_tuple = self.question_pack.get_random_question()
        else:
            qa_tuple = self.question_pack.get_next_question()
        self.current_answer = qa_tuple.answer
        self.current_question = qa_tuple.question
        self.textbox_answer.setText("")
        self.textbox_question.setText(self.current_question)
        self.btn_answer.setText("Antwort zeigen")
        self.answer_shown = False

    def question_pack_loaded(self):
        self.btn_answer.setEnabled(True)
        self.btn_next_question.setEnabled(True)
        self.fetch_next_question()