__author__ = 'Fabian'

from PyQt4 import QtGui, QtCore
from cascade import *

class SimpleWindow(QtGui.QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        centerWidget = CascadusMainWidget()
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

        self.setGeometry(300,300,1000,700)
        self.setWindowTitle('Main window')
        self.show()




class CascadusMainWidget(QtGui.QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.cascade = Cascade()
        self.graph = 0
        self.graphstack = list()

        btnGenerate = QtGui.QPushButton("Generieren")
        btnRunCascade = QtGui.QPushButton("RunCascade")
        btnNext = QtGui.QPushButton("Next")
        btnPrev = QtGui.QPushButton("Vorheriges")

        btnGenerate.clicked.connect(self.Generate)
        btnRunCascade.clicked.connect(self.runCascade)
        btnNext.clicked.connect(self.nextPic)
        btnPrev.clicked.connect(self.prevPic)


        vbox = QtGui.QVBoxLayout()

        self.label = QtGui.QLabel()
        #self.label.setScaledContents(True)
        vbox.addWidget(self.label)
        hbox = QtGui.QHBoxLayout()
        hbox.setSpacing(100)
        hbox.addWidget(btnGenerate)
        hbox.addWidget(btnRunCascade)
        hbox.addWidget(btnNext)
        #hbox.addWidget(btnPrev)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def Generate(self):

        if self.graph != 0:
            self.graphstack.append(self.graph)
        self.graph = self.cascade.createRandomGraph(30)
        self.setGraphPicture()

    def runCascade(self):

        if self.graph != 0:
            self.cascade.doCascades(self.graph)

    def nextPic(self):
        pass

    def prevPic(self):
        if len(self.graphstack) > 0:
            self.graph = self.graphstack.pop()
            self.cascade.printGraph(self.graph)
            self.setGraphPicture()

    def setGraphPicture(self):

        self.pic = QtGui.QPixmap("current.png")
        self.label.setPixmap(self.pic)




class SignalSlotWidget(QtGui.QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        lcd = QtGui.QLCDNumber(self)
        sld = QtGui.QSlider(QtCore.Qt.Horizontal,self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

class signalSlotSender(QtGui.QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        btn1 = QtGui.QPushButton("Button 1",self)
        btn1.move(30,50)

        btn2 = QtGui.QPushButton("Button 2", self)
        btn2.move(150,50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)


    def buttonClicked(self):

        sender = self.sender()
        self.parentWidget().statusBar().showMessage(sender.text() + "  was pressed")

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