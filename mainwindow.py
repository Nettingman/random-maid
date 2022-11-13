"""
Maid RPG character generator
'maid' by Wazul

2017.06.08.
"""
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from maidWidget import CMaidWidget
from helpWidget import CHelpWidget
from masterWidget import CMasterWidget
from butlerWidget import CButlerWidget

class ApplicationWindow(QtWidgets.QMainWindow):
    """ Main window for the application. """
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle('RMG - MaidRPG random generator')

        self.icon = QtGui.QIcon('icon.ico')
        self.setWindowIcon(self.icon)

        self.setTabPosition(QtCore.Qt.TopDockWidgetArea, QtWidgets.QTabWidget.North)

       # self.setFixedWidth(550)
       # self.setFixedHeight(650)

        self.statusbarMessage = QtWidgets.QLabel("Version number 1.1 - 'maid' by Wazul (2017)")
        self.statusBar().addWidget(self.statusbarMessage)


        self.maidDock = QtWidgets.QDockWidget('Random maid')
        self.maidDock.parent = self

        self.maidDock.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        titleWidget = QtWidgets.QWidget()
        self.maidDock.setTitleBarWidget(titleWidget)

        self.maidWidget = CMaidWidget(self.maidDock)
        self.maidDock.setWidget(self.maidWidget)
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.maidDock)


        self.butlerDock = QtWidgets.QDockWidget('Random butler')
        self.butlerDock.parent = self

        self.butlerDock.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        titleWidget = QtWidgets.QWidget()
        self.butlerDock.setTitleBarWidget(titleWidget)

        self.butlerWidget = CButlerWidget(self.butlerDock)
        self.butlerDock.setWidget(self.butlerWidget)
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.butlerDock)


        self.masterDock = QtWidgets.QDockWidget('Random master')
        self.masterDock.parent = self

        self.masterDock.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        titleWidgetMaster = QtWidgets.QWidget()
        self.masterDock.setTitleBarWidget(titleWidgetMaster)

        self.masterWidget = CMasterWidget(self.masterDock)
        self.masterDock.setWidget(self.masterWidget)
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.masterDock)


        self.helpDock = QtWidgets.QDockWidget('Help')
        self.helpDock.parent = self

        self.helpDock.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        titleWidgetHelp = QtWidgets.QWidget()
        self.helpDock.setTitleBarWidget(titleWidgetHelp)

        self.helpWidget = CHelpWidget(self.helpDock)
        self.helpDock.setWidget(self.helpWidget)
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.helpDock)


        self.tabifyDockWidget(self.maidDock, self.butlerDock)
        self.tabifyDockWidget(self.butlerDock, self.masterDock)
        self.tabifyDockWidget(self.masterDock, self.helpDock)
        self.maidDock.raise_()
        self.seq = 0

    def keyPressEvent(self, event):
        if self.seq == 0 and event.key() == QtCore.Qt.Key_Up:
            self.seq += 1
        elif self.seq == 1 and event.key() == QtCore.Qt.Key_Up:
            self.seq += 1
            self.helpDock.setFocus()
        elif self.seq == 2 and event.key() == QtCore.Qt.Key_Down:
            self.seq += 1
        elif self.seq == 3 and event.key() == QtCore.Qt.Key_Down:
            self.seq += 1
        elif self.seq == 4 and event.key() == QtCore.Qt.Key_Left:
            self.seq += 1
        elif self.seq == 5 and event.key() == QtCore.Qt.Key_Right:
            self.seq += 1
        elif self.seq == 6 and event.key() == QtCore.Qt.Key_Left:
            self.seq += 1
        elif self.seq == 7 and event.key() == QtCore.Qt.Key_Right:
            self.seq += 1
        elif self.seq == 8 and event.key() == QtCore.Qt.Key_B:
            self.seq += 1
        elif self.seq == 9 and event.key() == QtCore.Qt.Key_A:
            self.helpWidget.easterEgg()
        else:
            self.seq = 0


def main(argv):
    app = QtWidgets.QApplication(sys.argv)
    maidProgram = ApplicationWindow()
    maidProgram.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
