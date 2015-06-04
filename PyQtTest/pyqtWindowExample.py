__author__ = 'Fabian'

from PyQt4 import QtGui
from PyQt4 import QtCore


class standardWindow(QtGui.QWidget):

    def __init__(self):
        super(standardWindow, self).__init__()
        self.initUI()

    def createButton(self):

        btn = QtGui.QPushButton('Quit',self)
        btn.setToolTip('This is a <i> BUTTON </i>')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)  # QtCore.QCoreApplication.instance().quit

    def initUI(self):

        self.statusBar().showMessage('Read')

        self.center()
        self.setWindowTitle('tooltips')
        self.show()

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',"Are you sure to quit?", QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
