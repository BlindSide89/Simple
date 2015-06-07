__author__ = 'Fabian'


from simpleWindow import *
from cascade import *


def main():

    casc = Cascade()
    casc.doCascades()
    casc.createRandomGraph(vnum=16)


if __name__ == '__main__':
    #main()
    app = QtGui.QApplication(sys.argv)
    window = SimpleWindow()
    sys.exit(app.exec_())
