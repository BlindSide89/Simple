__author__ = 'Fabian'

import sys
from pyqtmwT import *
from PyQt4 import QtGui
from geturl import *
from simpleWindow import *


def main():

    urlSnatch = GetImgs()
    urlSnatch.getthread()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = SimpleWindow()
    sys.exit(app.exec_())
#    main()