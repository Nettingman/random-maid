"""
Widget for the help dock.
"""
import os.path

from PyQt5 import QtWidgets, QtGui, QtCore

class CHelpWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.parent = parent
        self.loVLayoutMain = QtWidgets.QVBoxLayout()
        self.loHLayoutMain = QtWidgets.QHBoxLayout()
        self.loVLayoutMain.setAlignment(QtCore.Qt.AlignTop)
        self.helpText = QtWidgets.QLabel("To fully generate a maid press the 'GENERATE MAID' button. In a case of identical stat values " + 'you have to choose which stat to use when rolling for maid power. You can do this with ' + "the 'MP' button. To generate a second maid power (if available) hold down the 'Shift' key " + "then press the 'MP' button of your choosing (from the available options).\n\n" + "To reroll a singe value press the corresponding 'R' button.\n" + 'To roll a Special quality from a specific secondary table (for example: Magic) choose that primary table from the popuplist ' + "then press the corresponding 'R' button while holding down the 'Shift' key.\n\n" + 'Hover your cursor over a choosen trait to see its description.\n\n' + "To save your maid in a txt file press the 'SAVE' button.\n\n\n" + "PS.: There are no easter eggs in this program. Do not try out famous cheat codes.")
        self.helpText.setWordWrap(True)
        self.loVLayoutMain.addWidget(self.helpText)
        hlayout = QtWidgets.QHBoxLayout()
        hlayout.setAlignment(QtCore.Qt.AlignCenter)
        self.picture = QtWidgets.QLabel()
        maid_picture_path = os.path.join(os.path.dirname(__file__), "..", "..", "resources", "ram.png")
        self.picture.setPixmap(QtGui.QPixmap(maid_picture_path).scaled(360, 360))
        self.picture.setGeometry(0, 0, 360, 360)
        hlayout.addWidget(self.picture)
        self.loVLayoutMain.addLayout(hlayout)
        self.loHLayoutMain.addLayout(self.loVLayoutMain)
        self.setLayout(self.loHLayoutMain)

    def easterEgg(self):
        self.parent.parent.statusbarMessage.setText('ALL YOUR MAID ARE BELONG TO US')
