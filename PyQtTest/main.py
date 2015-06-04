__author__ = 'Fabian'

import sys
from pyqtmwT import *
from PyQt4 import QtGui
from geturl import *
from simpleWindow import *
from cascade import *


def main():

    casc = Cascade()
    casc.doCascades()
    #urlSnatch = GetImgs()
    #urlSnatch.getthread()


if __name__ == '__main__':
    main()
    app = QtGui.QApplication(sys.argv)
    window = SimpleWindow()
    sys.exit(app.exec_())
