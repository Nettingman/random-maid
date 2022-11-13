"""
Widget for the help dock.
"""
from PyQt5 import QtWidgets, QtGui, QtCore

class CHelpWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.parent = parent
        self.loVLayoutMain = QtWidgets.QVBoxLayout()
        self.loHLayoutMain = QtWidgets.QHBoxLayout()
        self.loVLayoutMain.setAlignment(QtCore.Qt.AlignTop)
        self.helpText = QtWidgets.QLabel("To generate a complete maid, press the 'GENERATE MAID' button. In a case of equal stats " + 'you may have to choose, for which stat you want to generate a maid power. You can do this, with ' + "the 'MP' button. To generate a second maid power (if available), hold down the 'Shift' button, " + "then press the correct 'MP' button.\n\n" + "To reroll a singe value, press the corresponding 'R' button.\n" + 'To roll a Special quality from a specific secondary table (for example: Magic), choose that table from the popuplist, ' + "then press the corresponding 'R' button while holding down the 'Shift' button.\n\n" + 'Hover your cursor over a choosen trait, to see its description.\n\n' + "To save your maid in a txt file, press the 'SAVE' button.\n\n\n" + "PS.: There's no easter egg in this program. It is useless to try famous cheat code sequences.")
        self.helpText.setWordWrap(True)
        self.loVLayoutMain.addWidget(self.helpText)
        hlayout = QtWidgets.QHBoxLayout()
        hlayout.setAlignment(QtCore.Qt.AlignCenter)
        self.picture = QtWidgets.QLabel()
        self.picture.setPixmap(QtGui.QPixmap('ram.png').scaled(360, 360))
        self.picture.setGeometry(0, 0, 360, 360)
        hlayout.addWidget(self.picture)
        self.loVLayoutMain.addLayout(hlayout)
        self.loHLayoutMain.addLayout(self.loVLayoutMain)
        self.setLayout(self.loHLayoutMain)

    def easterEgg(self):
        self.parent.parent.statusbarMessage.setText('ALL YOUR MAID ARE BELONG TO US')
