__author__ = 'Fabian'


from simpleWindow import *
import sys


def main():
    pass


if __name__ == '__main__':
    main()
    app = QtGui.QApplication(sys.argv)
    window = SimpleWindow()
    sys.exit(app.exec_())

