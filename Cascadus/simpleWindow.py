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

        self.setGeometry(300,300,700,700)
        self.setWindowTitle('Main window')
        self.show()

    def closeEvent(self, event):
        self.centralWidget().deleteOldPics()
        event.accept()




class CascadusMainWidget(QtGui.QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.cascade = Cascade()
        self.graph = 0
        self.name_index = 0
        self.current_pic_index = 0

        self.anzKnoten  = QtGui.QLineEdit()
        self.entropie = QtGui.QLineEdit()
        self.threshold = QtGui.QLineEdit()
        self.seeds = QtGui.QLineEdit()

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
        self.setGraphPicture()



        hboxside = QtGui.QHBoxLayout()
        hboxside.addWidget(self.label)

        sidegrid = QtGui.QGridLayout()
        sidegrid.addWidget(QtGui.QLabel("Anzahl Knoten:"), 1, 1, alignment=QtCore.Qt.AlignTop)
        sidegrid.addWidget(QtGui.QLabel("Entropie:"), 2, 1, alignment=QtCore.Qt.AlignTop)
        sidegrid.addWidget(QtGui.QLabel("Threshold:"), 3, 1, alignment=QtCore.Qt.AlignTop)
        sidegrid.addWidget(QtGui.QLabel("Seeds:"), 4, 1, alignment=QtCore.Qt.AlignTop)
        sidegrid.addWidget(QtGui.QLabel(), 5, 1, alignment=QtCore.Qt.AlignTop)
        sidegrid.addWidget(QtGui.QLabel(""), 6, 1, alignment=QtCore.Qt.AlignTop)
        sidegrid.addWidget(QtGui.QLabel(""), 7, 1, alignment=QtCore.Qt.AlignTop)
        sidegrid.addWidget(QtGui.QLabel(""), 8, 1, alignment=QtCore.Qt.AlignTop)
        sidegrid.addWidget(QtGui.QLabel(""), 9, 1, alignment=QtCore.Qt.AlignTop)

        sidegrid.addWidget(self.anzKnoten, 1, 2, alignment=QtCore.Qt.AlignTop)
        sidegrid.addWidget(self.entropie, 2, 2, alignment=QtCore.Qt.AlignTop)
        sidegrid.addWidget(self.threshold, 3, 2, alignment=QtCore.Qt.AlignTop)
        sidegrid.addWidget(self.seeds, 4, 2, alignment=QtCore.Qt.AlignTop)

        vsidebox = QtGui.QVBoxLayout()
        vsidebox.addLayout(sidegrid)
        vsidebox.addWidget(QtGui.QLabel())
        hboxside.addLayout(vsidebox)

        vbox.addLayout(hboxside)

        hbox = QtGui.QHBoxLayout()
        hbox.setSpacing(100)
        hbox.addWidget(btnGenerate)
        hbox.addWidget(btnRunCascade)
        hbox.addWidget(btnNext)
        hbox.addWidget(QtGui.QLabel())
        hbox.addWidget(QtGui.QLabel())
        hbox.addWidget(QtGui.QLabel())
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def Generate(self):
        i_knoten = self.anzKnoten.displayText()
        if not i_knoten.isdigit():
            i_knoten = 10
        if int(i_knoten) > 100:
            i_knoten = 100
        self.graph = self.cascade.createRandomGraph(int(i_knoten))
        self.setGraphPicture()

    def runCascade(self):
        if self.graph != 0:
            self.deleteOldPics()
            self.name_index = self.cascade.doCascades(self.graph, seedNum=int(self.seeds.displayText()),
                                                      threshold=float(self.threshold.displayText()))
            self.setGraphPicture(path="cascade.png")
            self.current_pic_index = 0

    def nextPic(self):

        if self.current_pic_index < self.name_index:
            path = "cascade" + self.current_pic_index.__str__() + ".png"
            self.setGraphPicture(path)
            print(self.name_index.__str__() + "  " + self.current_pic_index.__str__())
            self.current_pic_index += 1

    def prevPic(self):
        pass

    def setGraphPicture(self, path="current.png"):
        self.pic = QtGui.QPixmap(path)
        self.label.setPixmap(self.pic)

    def deleteOldPics(self):
        if self.name_index == 0:
            return
        os.remove('./cascade.png')
        for i in range(0, self.name_index):
            os.remove('./cascade' + i.__str__() + '.png')



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