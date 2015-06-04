__author__ = 'Fabian'

import sys
from pyFiles.pyqtmwT import *
from PyQt4 import QtGui
from pyFiles.geturl import *
from pyFiles.simpleWindow import *


def main():

    urlSnatch = GetImgs()
    urlSnatch.getthread()


if __name__ == '__main__':
#    app = QtGui.QApplication(sys.argv)
#    window = SimpleWindow()
#    sys.exit(app.exec_())
    main()