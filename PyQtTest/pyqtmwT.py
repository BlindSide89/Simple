__author__ = 'Fabian'

#python pyqt QMainWindow test

from PyQt4 import QtGui

class mainwindow_t(QtGui.QMainWindow):

    def __init__(self):
        super(mainwindow_t, self).__init__()

        self.initUI()

    def initUI(self):

        exitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), '&Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)


        self.toolbar= self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)



        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(200,200,1024,768)
        self.setWindowTitle('Menubar')
        self.show()
