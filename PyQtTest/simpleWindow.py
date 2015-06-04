__author__ = 'Fabian'

from PyQt4 import QtGui


class SimpleWindow(QtGui.QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

#        textEdit = QtGui.QTextEdit()
        centerWidget = positionWidgetGrid()
        self.setCentralWidget(centerWidget)


        exitAction = QtGui.QAction(QtGui.QIcon('exit24.jpg'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300,300,500,500)
        self.setWindowTitle('Main window')
        self.show()


class positionWidgetBox(QtGui.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        firstButton = QtGui.QPushButton('First')
        secondButton = QtGui.QPushButton('Second')

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(firstButton)
        hbox.addWidget(secondButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)


class positionWidgetGrid(QtGui.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QtGui.QGridLayout()

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(grid)
        self.setLayout(vbox)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']

        positions = [(i,j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QtGui.QPushButton(name)
            grid.addWidget(button,*position)


class positionWidgetGrid2(QtGui.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        author = QtGui.QLabel("Author")
        title = QtGui.QLabel("Title")
        review = QtGui.QLabel("Review")

        aedit = QtGui.QLineEdit()
        tedit = QtGui.QLineEdit()
        redit = QtGui.QTextEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title,1,0)
        grid.addWidget(review,0,0)
        grid.addWidget(author,2,0,5,1)
        #grid.addWidget(redit,1,1)


        self.setLayout(grid)