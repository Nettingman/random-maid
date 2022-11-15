"""
Widget for the random maid dock.
"""

from random import randint
from math import floor
from PyQt5 import QtWidgets, QtGui, QtCore
from .data import butlerPowers, butlerRoots

butlerPowerList = butlerPowers.returnButlerPowerList()
butlerRootList = butlerRoots.returnButlerRootList()

class CButlerWidget(QtWidgets.QWidget):

    def __init__(self, data_reader, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.data_reader = data_reader
        self.parent = parent

        self.stats = [0, 0, 0, 0, 0, 0]

        self.loVLayoutMain = QtWidgets.QVBoxLayout()
        self.loHLayoutMain = QtWidgets.QHBoxLayout()

        self.gbBasic = QtWidgets.QGroupBox('Basics', self)
        self.loGbBasic = QtWidgets.QVBoxLayout()

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Name: ')
        hLayout.addWidget(textLabel)
        self.liName = QtWidgets.QLineEdit()
        self.liName.setFixedWidth(200)
        hLayout.addWidget(self.liName)
        hLayout.addStretch(1)
        self.loGbBasic.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Age:   ')
        hLayout.addWidget(textLabel)
        self.liAge = QtWidgets.QSpinBox()
        self.liAge.setFixedWidth(50)
        self.liAge.setMaximum(9999)
        hLayout.addWidget(self.liAge)
        self.bAge = QtWidgets.QPushButton('R')
        self.bAge.parent = self.liAge
        self.bAge.setFixedWidth(50)
        hLayout.addWidget(self.bAge)
        self.loGbBasic.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Suit color: ')
        hLayout.addWidget(textLabel)
        self.liUniColor = QtWidgets.QLineEdit()
        self.liUniColor.setFixedWidth(150)
        hLayout.addWidget(self.liUniColor)
        self.bUniColor = QtWidgets.QPushButton('R')
        self.bUniColor.parent = self.liUniColor
        self.bUniColor.setFixedWidth(50)
        hLayout.addWidget(self.bUniColor)
        self.loGbBasic.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Hair color: ')
        hLayout.addWidget(textLabel)
        self.liHairColor = QtWidgets.QLineEdit()
        self.liHairColor.setFixedWidth(150)
        hLayout.addWidget(self.liHairColor)
        self.bHairColor = QtWidgets.QPushButton('R')
        self.bHairColor.setFixedWidth(50)
        self.bHairColor.parent = self.liHairColor
        hLayout.addWidget(self.bHairColor)
        self.loGbBasic.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Eye color: ')
        hLayout.addWidget(textLabel)
        self.liEyeColor = QtWidgets.QLineEdit()
        self.liEyeColor.setFixedWidth(150)
        hLayout.addWidget(self.liEyeColor)
        self.bEyeColor = QtWidgets.QPushButton('R')
        self.bEyeColor.setFixedWidth(50)
        self.bEyeColor.parent = self.liEyeColor
        hLayout.addWidget(self.bEyeColor)
        self.loGbBasic.addLayout(hLayout)
        self.gbBasic.setLayout(self.loGbBasic)
        self.loH1 = QtWidgets.QHBoxLayout()
        self.loH1.addWidget(self.gbBasic)
        self.gbMaidType = QtWidgets.QGroupBox('Butler Type', self)
        self.loGbMaidType = QtWidgets.QVBoxLayout()

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('First: ')
        hLayout.addWidget(textLabel)
        self.liFirstType = QtWidgets.QComboBox()
        self.setButlerTypeComboBox(self.liFirstType)
        self.liFirstType.setFixedWidth(100)
        hLayout.addWidget(self.liFirstType)
        self.bFirstType = QtWidgets.QPushButton('R')
        self.bFirstType.setFixedWidth(50)
        self.bFirstType.parent = self.liFirstType
        hLayout.addWidget(self.bFirstType)
        self.loGbMaidType.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        self.descFirst = QtWidgets.QLabel('')
        self.descFirst.setWordWrap(True)
        self.liFirstType.desc = self.descFirst
        self.liFirstType.changeList = [0, 0, 0, 0, 0, 0]
        hLayout.addWidget(self.descFirst)
        self.loGbMaidType.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Second: ')
        hLayout.addWidget(textLabel)
        self.liSecondType = QtWidgets.QComboBox()
        self.setButlerTypeComboBox(self.liSecondType)
        self.liSecondType.setFixedWidth(100)
        hLayout.addWidget(self.liSecondType)
        self.bSecondType = QtWidgets.QPushButton('R')
        self.bSecondType.setFixedWidth(50)
        self.bSecondType.parent = self.liSecondType
        hLayout.addWidget(self.bSecondType)
        self.loGbMaidType.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        self.descSecond = QtWidgets.QLabel('')
        self.descSecond.setWordWrap(True)
        self.liSecondType.desc = self.descSecond
        self.liSecondType.changeList = [0, 0, 0, 0, 0, 0]
        hLayout.addWidget(self.descSecond)
        self.loGbMaidType.addLayout(hLayout)
        self.gbMaidType.setLayout(self.loGbMaidType)
        self.gbMaidType.setFixedWidth(220)
        self.loH1.addWidget(self.gbMaidType)
        self.gbAttri = QtWidgets.QGroupBox('Attributes', self)
        self.loGbAttri = QtWidgets.QVBoxLayout()

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('ATH:')
        textLabel.setToolTip('Athletics: Physical ability, combat ability.')
        hLayout.addWidget(textLabel, 1, QtCore.Qt.AlignRight)
        self.liATH = QtWidgets.QSpinBox()
        self.liATH.setFixedWidth(35)
        hLayout.addWidget(self.liATH, 1, QtCore.Qt.AlignRight)
        self.textATH = QtWidgets.QLabel('(0)')
        self.liATH.sumVal = self.textATH
        hLayout.addWidget(self.textATH, 1, QtCore.Qt.AlignRight)
        self.bATH = QtWidgets.QPushButton('R')
        self.bATH.setFixedWidth(50)
        self.bATH.parent = self.liATH
        hLayout.addWidget(self.bATH, 1, QtCore.Qt.AlignRight)
        self.loGbAttri.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('AFF:')
        textLabel.setToolTip('Affection: How good are you at forming bonds with your master and the other maids?')
        hLayout.addWidget(textLabel, 1, QtCore.Qt.AlignRight)
        self.liAFF = QtWidgets.QSpinBox()
        self.liAFF.setFixedWidth(35)
        hLayout.addWidget(self.liAFF, 1, QtCore.Qt.AlignRight)
        self.textAFF = QtWidgets.QLabel('(0)')
        self.liAFF.sumVal = self.textAFF
        hLayout.addWidget(self.textAFF, 1, QtCore.Qt.AlignRight)
        self.bAFF = QtWidgets.QPushButton('R')
        self.bAFF.setFixedWidth(50)
        self.bAFF.parent = self.liAFF
        hLayout.addWidget(self.bAFF, 1, QtCore.Qt.AlignRight)
        self.loGbAttri.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('SKI:')
        textLabel.setToolTip('Skill: How good are you at your maid duties?')
        hLayout.addWidget(textLabel, 1, QtCore.Qt.AlignRight)
        self.liSKI = QtWidgets.QSpinBox()
        self.liSKI.setFixedWidth(35)
        hLayout.addWidget(self.liSKI, 1, QtCore.Qt.AlignRight)
        self.textSKI = QtWidgets.QLabel('(0)')
        self.liSKI.sumVal = self.textSKI
        hLayout.addWidget(self.textSKI, 1, QtCore.Qt.AlignRight)
        self.bSKI = QtWidgets.QPushButton('R')
        self.bSKI.setFixedWidth(50)
        self.bSKI.parent = self.liSKI
        hLayout.addWidget(self.bSKI, 1, QtCore.Qt.AlignRight)
        self.loGbAttri.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('CNN:')
        textLabel.setToolTip('Cunning: How capable are you at tricking enemies and other maids, and deceiving the master?')
        hLayout.addWidget(textLabel, 1, QtCore.Qt.AlignRight)
        self.liCNN = QtWidgets.QSpinBox()
        self.liCNN.setFixedWidth(35)
        hLayout.addWidget(self.liCNN, 1, QtCore.Qt.AlignRight)
        self.textCNN = QtWidgets.QLabel('(0)')
        self.liCNN.sumVal = self.textCNN
        hLayout.addWidget(self.textCNN, 1, QtCore.Qt.AlignRight)
        self.bCNN = QtWidgets.QPushButton('R')
        self.bCNN.setFixedWidth(50)
        self.bCNN.parent = self.liCNN
        hLayout.addWidget(self.bCNN, 1, QtCore.Qt.AlignRight)
        self.loGbAttri.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('LCK:')
        textLabel.setToolTip('Luck: Just how lucky are you?')
        hLayout.addWidget(textLabel, 1, QtCore.Qt.AlignRight)
        self.liLCK = QtWidgets.QSpinBox()
        self.liLCK.setFixedWidth(35)
        hLayout.addWidget(self.liLCK, 1, QtCore.Qt.AlignRight)
        self.textLCK = QtWidgets.QLabel('(0)')
        self.liLCK.sumVal = self.textLCK
        hLayout.addWidget(self.textLCK, 1, QtCore.Qt.AlignRight)
        self.bLCK = QtWidgets.QPushButton('R')
        self.bLCK.setFixedWidth(50)
        self.bLCK.parent = self.liLCK
        hLayout.addWidget(self.bLCK, 1, QtCore.Qt.AlignRight)
        self.loGbAttri.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('WIL:')
        textLabel.setToolTip('Will: How positive and constructive is your thinking?')
        hLayout.addWidget(textLabel, 1, QtCore.Qt.AlignRight)
        self.liWIL = QtWidgets.QSpinBox()
        self.liWIL.setFixedWidth(35)
        hLayout.addWidget(self.liWIL, 1, QtCore.Qt.AlignRight)
        self.textWIL = QtWidgets.QLabel('(0)')
        self.liWIL.sumVal = self.textWIL
        hLayout.addWidget(self.textWIL, 1, QtCore.Qt.AlignRight)
        self.bWIL = QtWidgets.QPushButton('R')
        self.bWIL.setFixedWidth(50)
        self.bWIL.parent = self.liWIL
        hLayout.addWidget(self.bWIL, 1, QtCore.Qt.AlignRight)
        self.loGbAttri.addLayout(hLayout)
        self.gbAttri.setLayout(self.loGbAttri)
        self.loH2 = QtWidgets.QHBoxLayout()
        self.loH2.addWidget(self.gbAttri)
        self.gbEtc = QtWidgets.QGroupBox('Etcetera', self)
        self.loGbEtc = QtWidgets.QVBoxLayout()

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Butler root: ')
        hLayout.addWidget(textLabel)
        self.liMaidRoot = QtWidgets.QComboBox()
        self.setButlerRootComboBox()
        self.liMaidRoot.setFixedWidth(150)
        hLayout.addWidget(self.liMaidRoot)
        self.bMaidRoot = QtWidgets.QPushButton('R')
        self.bMaidRoot.parent = self.liMaidRoot
        self.bMaidRoot.setFixedWidth(50)
        hLayout.addWidget(self.bMaidRoot)
        self.loGbEtc.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Butler power: ')
        hLayout.addWidget(textLabel)
        self.liMP = QtWidgets.QComboBox()
        self.liMP.setFixedWidth(150)
        self.liFirstType.powerBox = self.liMP
        self.liMP.parent = self.liFirstType
        hLayout.addWidget(self.liMP)
        self.bButlerPower = QtWidgets.QPushButton('R')
        self.bButlerPower.parent = self.liMP
        self.liMP.rollButton = self.bButlerPower
        self.bButlerPower.setFixedWidth(50)
        hLayout.addWidget(self.bButlerPower)
        self.loGbEtc.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Butler power 2: ')
        hLayout.addWidget(textLabel)
        self.liMP2 = QtWidgets.QComboBox()
        self.liMP2.setFixedWidth(150)
        self.liSecondType.powerBox = self.liMP2
        self.liMP2.parent = self.liSecondType
        hLayout.addWidget(self.liMP2)
        self.bButlerPower2 = QtWidgets.QPushButton('R')
        self.bButlerPower2.parent = self.liMP2
        self.liMP2.rollButton = self.bButlerPower2
        self.bButlerPower2.setFixedWidth(50)
        hLayout.addWidget(self.bButlerPower2)
        self.loGbEtc.addLayout(hLayout)
        self.liMP.otherMP = self.liMP2
        self.liMP2.otherMP = self.liMP
        self.favor = QtWidgets.QLabel('Favor: 0')
        self.spirit = QtWidgets.QLabel('Spirit: 0')
        self.loGbEtc.addWidget(self.favor)
        self.loGbEtc.addWidget(self.spirit)
        self.gbEtc.setLayout(self.loGbEtc)
        self.loH2.addWidget(self.gbEtc)
        self.gbSpec = QtWidgets.QGroupBox('Special Qualities', self)
        self.loGbSpec = QtWidgets.QVBoxLayout()

        hLayout = QtWidgets.QHBoxLayout()
        self.liSpec1 = QtWidgets.QComboBox()
        self.setButlerQualityComboBox(self.liSpec1)
        self.liSpec1.setFixedWidth(150)
        hLayout.addWidget(self.liSpec1, 10, QtCore.Qt.AlignRight)
        self.bSpec1 = QtWidgets.QPushButton('R')
        self.bSpec1.setFixedWidth(50)
        self.bSpec1.parent = self.liSpec1
        hLayout.addWidget(self.bSpec1, 0, QtCore.Qt.AlignRight)
        self.loGbSpec.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        self.liSpec2 = QtWidgets.QComboBox()
        self.setButlerQualityComboBox(self.liSpec2)
        self.liSpec2.setFixedWidth(150)
        hLayout.addWidget(self.liSpec2, 10, QtCore.Qt.AlignRight)
        self.bSpec2 = QtWidgets.QPushButton('R')
        self.bSpec2.setFixedWidth(50)
        self.bSpec2.parent = self.liSpec2
        hLayout.addWidget(self.bSpec2, 1, QtCore.Qt.AlignRight)
        self.loGbSpec.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        self.cbSpec3 = QtWidgets.QCheckBox()
        hLayout.addWidget(self.cbSpec3, 1, QtCore.Qt.AlignRight)
        self.liSpec3 = QtWidgets.QComboBox()
        self.setButlerQualityComboBox(self.liSpec3)
        self.liSpec3.setFixedWidth(150)
        hLayout.addWidget(self.liSpec3, 1, QtCore.Qt.AlignRight)
        self.bSpec3 = QtWidgets.QPushButton('R')
        self.bSpec3.setFixedWidth(50)
        self.bSpec3.parent = self.liSpec3
        self.cbSpec3.button = self.bSpec3
        self.cbSpec3.box = self.liSpec3
        hLayout.addWidget(self.bSpec3, 1, QtCore.Qt.AlignRight)
        self.loGbSpec.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        self.cbSpec4 = QtWidgets.QCheckBox()
        hLayout.addWidget(self.cbSpec4, 1, QtCore.Qt.AlignRight)
        self.liSpec4 = QtWidgets.QComboBox()
        self.setButlerQualityComboBox(self.liSpec4)
        self.liSpec4.setFixedWidth(150)
        hLayout.addWidget(self.liSpec4, 1, QtCore.Qt.AlignRight)
        self.bSpec4 = QtWidgets.QPushButton('R')
        self.bSpec4.setFixedWidth(50)
        self.bSpec4.parent = self.liSpec4
        self.cbSpec4.button = self.bSpec4
        self.cbSpec4.box = self.liSpec4
        hLayout.addWidget(self.bSpec4, 1, QtCore.Qt.AlignRight)
        self.loGbSpec.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        self.cbSpec5 = QtWidgets.QCheckBox()
        hLayout.addWidget(self.cbSpec5, 1, QtCore.Qt.AlignRight)
        self.liSpec5 = QtWidgets.QComboBox()
        self.setButlerQualityComboBox(self.liSpec5)
        self.liSpec5.setFixedWidth(150)
        hLayout.addWidget(self.liSpec5, 1, QtCore.Qt.AlignRight)
        self.bSpec5 = QtWidgets.QPushButton('R')
        self.bSpec5.setFixedWidth(50)
        self.bSpec5.parent = self.liSpec5
        self.cbSpec5.button = self.bSpec5
        self.cbSpec5.box = self.liSpec5
        hLayout.addWidget(self.bSpec5, 1, QtCore.Qt.AlignRight)
        self.loGbSpec.addLayout(hLayout)

        self.gbSpec.setLayout(self.loGbSpec)
        self.gbSpec.setFixedWidth(250)
        self.loH3 = QtWidgets.QHBoxLayout()
        self.loH3.addWidget(self.gbSpec)
        self.gbWeap = QtWidgets.QGroupBox('Weapons', self)
        self.loGbWeap = QtWidgets.QVBoxLayout()
        self.liWeapon = QtWidgets.QComboBox()
        self.setButlerWeaponComboBox(self.liWeapon)
        self.loGbWeap.addWidget(self.liWeapon)
        self.bWeap = QtWidgets.QPushButton('R')
        self.bWeap.parent = self.liWeapon
        self.loGbWeap.addWidget(self.bWeap)
        self.loGbWeap.addWidget(QtWidgets.QLabel('\n\n'))
        self.liWeapon2 = QtWidgets.QComboBox()
        self.setButlerWeaponComboBox(self.liWeapon2)
        self.loGbWeap.addWidget(self.liWeapon2)
        self.bWeap2 = QtWidgets.QPushButton('R')
        self.bWeap2.parent = self.liWeapon2
        self.loGbWeap.addWidget(self.bWeap2)
        self.liWeapon.otherWeapon = self.liWeapon2
        self.liWeapon2.otherWeapon = self.liWeapon
        self.gbWeap.setLayout(self.loGbWeap)
        self.loH3.addWidget(self.gbWeap)

        self.gbSave = QtWidgets.QGroupBox('Generate and save', self)
        self.loGbSave = QtWidgets.QVBoxLayout()
        self.bRollAll = QtWidgets.QPushButton('GENERATE\nBUTLER', self)
        self.loGbSave.addWidget(self.bRollAll)
        self.bSave = QtWidgets.QPushButton('SAVE', self)
        self.loGbSave.addWidget(self.bSave)
        self.gbSave.setLayout(self.loGbSave)
        self.gbSave.setFixedWidth(120)
        self.loH3.addWidget(self.gbSave)

        self.loVLayoutMain.addLayout(self.loH1)
        self.loVLayoutMain.addLayout(self.loH2)
        self.loVLayoutMain.addLayout(self.loH3)
        self.loHLayoutMain.addLayout(self.loVLayoutMain)
        self.setLayout(self.loHLayoutMain)

        self.setEnabilities()
        self.cbSpec3.clicked.connect(self.setEnabilities)
        self.cbSpec4.clicked.connect(self.setEnabilities)
        self.cbSpec5.clicked.connect(self.setEnabilities)
        self.liATH.valueChanged.connect(self.calculateStats)
        self.liAFF.valueChanged.connect(self.calculateStats)
        self.liSKI.valueChanged.connect(self.calculateStats)
        self.liCNN.valueChanged.connect(self.calculateStats)
        self.liLCK.valueChanged.connect(self.calculateStats)
        self.liWIL.valueChanged.connect(self.calculateStats)
        self.bAge.clicked.connect(self.generateAge)
        self.bUniColor.clicked.connect(self.generateSuitColor)
        self.bHairColor.clicked.connect(self.generateHairColor)
        self.bEyeColor.clicked.connect(self.generateEyeColor)
        self.bATH.clicked.connect(self.generateAttribute)
        self.bAFF.clicked.connect(self.generateAttribute)
        self.bSKI.clicked.connect(self.generateAttribute)
        self.bCNN.clicked.connect(self.generateAttribute)
        self.bLCK.clicked.connect(self.generateLuckAttribute)
        self.bWIL.clicked.connect(self.generateWilAttribute)
        self.bFirstType.clicked.connect(self.generateButlerType)
        self.bSecondType.clicked.connect(self.generateButlerType)
        self.bButlerPower.clicked.connect(self.generateButlerPower)
        self.bButlerPower2.clicked.connect(self.generateButlerPower)
        self.bMaidRoot.clicked.connect(self.generateButlerRoot)
        self.bSpec1.clicked.connect(self.generateButlerQuality)
        self.bSpec2.clicked.connect(self.generateButlerQuality)
        self.bSpec3.clicked.connect(self.generateButlerQuality)
        self.bSpec4.clicked.connect(self.generateButlerQuality)
        self.bSpec5.clicked.connect(self.generateButlerQuality)
        self.bWeap.clicked.connect(self.generateButlerWeapon)
        self.bWeap2.clicked.connect(self.generateButlerWeapon)
        self.liFirstType.currentIndexChanged.connect(self.changedButlerType)
        self.liSecondType.currentIndexChanged.connect(self.changedButlerType)
        self.liMP.currentIndexChanged.connect(self.changedButlerPower)
        self.liMP2.currentIndexChanged.connect(self.changedButlerPower)
        self.liMaidRoot.currentIndexChanged.connect(self.changedButlerRoot)
        self.liSpec1.currentIndexChanged.connect(self.changedButlerQuality)
        self.liSpec2.currentIndexChanged.connect(self.changedButlerQuality)
        self.liSpec3.currentIndexChanged.connect(self.changedButlerQuality)
        self.liSpec4.currentIndexChanged.connect(self.changedButlerQuality)
        self.liSpec5.currentIndexChanged.connect(self.changedButlerQuality)
        self.liWeapon.currentIndexChanged.connect(self.changedButlerWeapon)
        self.liWeapon2.currentIndexChanged.connect(self.changedButlerWeapon)
        self.bRollAll.clicked.connect(self.generateButler)
        self.bSave.clicked.connect(self.saveButler)

    def setEnabilities(self):
        for checkb in [self.cbSpec3, self.cbSpec4, self.cbSpec5]:
            if not checkb.isChecked():
                checkb.button.setEnabled(False)
                checkb.box.setEnabled(False)
                checkb.box.setCurrentIndex(-1)
            else:
                checkb.button.setEnabled(True)
                checkb.box.setEnabled(True)

    def generateAge(self, hideMessage=False):
        if not hideMessage:
            self.parent.parent.statusBar().showMessage('Rolled age...', 1500)
        i = int(str(randint(1, 6)) + str(randint(1, 6)))
        self.liAge.setValue(i)

    def generateSuitColor(self, hideMessage=False):
        if not hideMessage:
            self.parent.parent.statusBar().showMessage('Rolled color...', 1500)
        self.liUniColor.setText(self.data_reader.get_butler_random_suit_color())

    def generateHairColor(self, hideMessage=False):
        if not hideMessage:
            self.parent.parent.statusBar().showMessage('Rolled color...', 1500)
        self.liHairColor.setText(self.data_reader.get_butler_random_hair_color())

    def generateEyeColor(self, hideMessage=False):
        if not hideMessage:
            self.parent.parent.statusBar().showMessage('Rolled color...', 1500)
        self.liEyeColor.setText(self.data_reader.get_random_color())

    def generateAttribute(self, caller=False):
        if caller == False:
            caller = self.sender()
            self.parent.parent.statusBar().showMessage('Rolled attribute...', 1500)
        x = randint(1, 6)
        y = randint(1, 6)
        retVal = int(floor((x + y) / 2))
        caller.parent.setValue(retVal)

    def generateLuckAttribute(self, hideMessage=False):
        if hideMessage == False:
            self.parent.parent.statusBar().showMessage('Rolled attribute...', 1500)
        x = randint(1, 6)
        y = randint(1, 6)
        retVal = int(floor((x + y) / 3))
        self.liLCK.setValue(retVal)

    def generateWilAttribute(self, hideMessage=False):
        if hideMessage == False:
            self.parent.parent.statusBar().showMessage('Rolled attribute...', 1500)
        x = randint(1, 6)
        y = randint(1, 6)
        retVal = x + y
        self.liWIL.setValue(retVal)

    def generateButlerType(self, caller=False):
        if caller == False:
            caller = self.sender()
            self.parent.parent.statusBar().showMessage('Rolled butler type...', 1500)
        i = randint(0, 5)
        caller.parent.setCurrentIndex(i)

    def generateButlerPower(self, caller=False):
        if caller == False:
            caller = self.sender()
            if caller.parent.count() != 0:
                self.parent.parent.statusBar().showMessage('Rolled butler power...', 1500)
        if caller.parent.count() != 0:
            while True:
                i = randint(0, 5)
                caller.parent.setCurrentIndex(i)
                if caller.parent.otherMP.currentText() == '' or caller.parent.otherMP.currentText() != caller.parent.currentText():
                    break

    def generateButlerRoot(self, hideMessage=False):
        if not hideMessage:
            self.parent.parent.statusBar().showMessage('Rolled butler root...', 1500)
        i = randint(0, 5)
        self.liMaidRoot.setCurrentIndex(i)

    def generateButlerQuality(self, caller=False):
        if caller == False:
            caller = self.sender()
            self.parent.parent.statusBar().showMessage('Rolled butler special quality...', 1500)
        i = randint(0, 35)
        caller.parent.setCurrentIndex(i)

    def generateButlerWeapon(self, caller):
        if caller == False:
            caller = self.sender()
            self.parent.parent.statusBar().showMessage('Rolled weapon...', 1500)
        while True:
            i = randint(0, 35)
            caller.parent.setCurrentIndex(i)
            if caller.parent.otherWeapon.currentText() == '' or caller.parent.otherWeapon.currentText() != caller.parent.currentText():
                break

    def calculateStats(self):
        stat0 = self.liATH.value() + self.liFirstType.changeList[0] + self.liSecondType.changeList[0]
        stat1 = self.liAFF.value() + self.liFirstType.changeList[1] + self.liSecondType.changeList[1]
        stat2 = self.liSKI.value() + self.liFirstType.changeList[2] + self.liSecondType.changeList[2]
        stat3 = self.liCNN.value() + self.liFirstType.changeList[3] + self.liSecondType.changeList[3]
        stat4 = self.liLCK.value() + self.liFirstType.changeList[4] + self.liSecondType.changeList[4]
        stat5 = self.liWIL.value() + self.liFirstType.changeList[5] + self.liSecondType.changeList[5]
        self.stats = [stat0, stat1, stat2, stat3, stat4, stat5]
        for i in range(len(self.stats)):
            if self.stats[i] < 0:
                self.stats[i] = 0

        self.liATH.sumVal.setText('(' + str(self.stats[0]) + ')')
        self.liAFF.sumVal.setText('(' + str(self.stats[1]) + ')')
        self.liSKI.sumVal.setText('(' + str(self.stats[2]) + ')')
        self.liCNN.sumVal.setText('(' + str(self.stats[3]) + ')')
        self.liLCK.sumVal.setText('(' + str(self.stats[4]) + ')')
        self.liWIL.sumVal.setText('(' + str(self.stats[5]) + ')')
        self.favor.setText('Favor: ' + str(self.stats[1] * 2))
        self.spirit.setText('Spirit: ' + str(self.stats[5] * 10))

    def changedButlerType(self):
        comboBox = self.sender()
        ii = comboBox.currentIndex()
        elem = self.data_reader.data["butler"]["types"][ii]
        comboBox.desc.setText(elem[1])
        comboBox.changeList = elem[2]
        comboBox.setToolTip(elem[3])
        self.calculateStats()
        comboBox.powerBox.setCurrentIndex(-1)
        for j in range(6):
            comboBox.powerBox.removeItem(0)

        for item in butlerPowerList[ii]:
            comboBox.powerBox.insertItem(100, item.name)

        comboBox.powerBox.setCurrentIndex(-1)
        self.generateButlerPower(comboBox.powerBox.rollButton)

    def changedButlerPower(self):
        comboBox = self.sender()
        i = comboBox.currentIndex()
        j = comboBox.parent.currentIndex()
        if not comboBox.currentIndex() == -1:
            comboBox.setToolTip(butlerPowerList[j][i].descript)
        else:
            comboBox.setToolTip('')

    def changedButlerRoot(self):
        i = self.liMaidRoot.currentIndex()
        self.liMaidRoot.setToolTip(butlerRootList[i].descript)

    def changedButlerQuality(self):
        comboBox = self.sender()
        i = comboBox.currentIndex()
        if not i == -1:
            comboBox.setToolTip(self.data_reader.data["butler"]["qualities"][i][1])
        else:
            comboBox.setToolTip('')

    def changedButlerWeapon(self):
        comboBox = self.sender()
        i = comboBox.currentIndex()
        if not i == -1:
            comboBox.setToolTip(self.data_reader.data["butler"]["weapons"][i][1])
        else:
            comboBox.setToolTip('')

    def setButlerRootComboBox(self):
        for obj in butlerRootList:
            self.liMaidRoot.insertItem(100, obj.name)

        self.liMaidRoot.setCurrentIndex(-1)

    def setButlerTypeComboBox(self, comboBox):
        for elem in self.data_reader.data["butler"]["types"]:
            comboBox.insertItem(100, elem[0])

        comboBox.setCurrentIndex(-1)

    def setButlerQualityComboBox(self, comboBox):
        for elem in self.data_reader.data["butler"]["qualities"]:
            comboBox.insertItem(100, elem[0])

        comboBox.setCurrentIndex(-1)

    def setButlerWeaponComboBox(self, comboBox):
        for elem in self.data_reader.data["butler"]["weapons"]:
            comboBox.insertItem(100, elem[0])

        comboBox.setCurrentIndex(-1)

    def generateButler(self):
        self.generateAge(True)
        self.generateSuitColor(True)
        self.generateHairColor(True)
        self.generateEyeColor(True)
        self.generateAttribute(self.bATH)
        self.generateAttribute(self.bAFF)
        self.generateAttribute(self.bSKI)
        self.generateAttribute(self.bCNN)
        self.generateLuckAttribute(True)
        self.generateWilAttribute(True)
        self.generateButlerType(self.bFirstType)
        self.generateButlerType(self.bSecondType)
        self.generateButlerRoot(True)
        self.generateButlerQuality(self.bSpec1)
        self.generateButlerQuality(self.bSpec2)
        if self.bSpec3.isEnabled():
            self.generateButlerQuality(self.bSpec3)
        if self.bSpec4.isEnabled():
            self.generateButlerQuality(self.bSpec4)
        if self.bSpec5.isEnabled():
            self.generateButlerQuality(self.bSpec5)
        self.generateButlerWeapon(self.bWeap)
        self.generateButlerWeapon(self.bWeap2)

    def saveButler(self):
        savePath = QtWidgets.QFileDialog.getSaveFileName(None, 'Save your butler as...', '', 'Text Documents (*.txt);;All files (*.*)')
        if not savePath[0] == '':
            starSeparator = '-----------------------------------------------------------------------------------------\n'
            printList = []
            printList.append(starSeparator)
            printList.append('Name: ' + self.liName.text() + '\n')
            printList.append('Age: ' + str(self.liAge.value()) + '\n')
            printList.append('Suit color: ' + self.liUniColor.text() + '\n')
            printList.append('Eye color: ' + self.liEyeColor.text() + '\n')
            printList.append('Hair color: ' + self.liHairColor.text() + '\n')
            printList.append(starSeparator)
            printList.append('Stats:\n')
            printList.append('Athletics: ' + str(self.stats[0]) + '\n')
            printList.append('Affection: ' + str(self.stats[1]) + '\n')
            printList.append('Skill: ' + str(self.stats[2]) + '\n')
            printList.append('Cunning: ' + str(self.stats[3]) + '\n')
            printList.append('Luck: ' + str(self.stats[4]) + '\n')
            printList.append('Will: ' + str(self.stats[5]) + '\n')
            printList.append(self.favor.text() + '\n')
            printList.append(self.spirit.text() + '\n')
            printList.append(starSeparator)
            printList.append('Butler types:\n')
            printList.append(self.liFirstType.currentText() + ': ' + self.liFirstType.toolTip() + '\n')
            printList.append(self.liSecondType.currentText() + ': ' + self.liSecondType.toolTip() + '\n')
            printList.append('\n')
            printList.append('Butler powers:\n')
            printList.append(self.liMP.currentText() + ': ' + self.liMP.toolTip() + '\n')
            if self.liMP2.isEnabled():
                printList.append(self.liMP2.currentText() + ': ' + self.liMP2.toolTip() + '\n')
            printList.append('\n')
            printList.append('Butler root: ' + self.liMaidRoot.currentText() + '\n')
            printList.append(self.liMaidRoot.toolTip() + '\n')
            printList.append('\n')
            printList.append(starSeparator)
            printList.append('Special quailities:\n')
            printList.append(self.liSpec1.currentText() + ': ' + self.liSpec1.toolTip() + '\n')
            printList.append(self.liSpec2.currentText() + ': ' + self.liSpec2.toolTip() + '\n')
            if self.liSpec3.isEnabled():
                printList.append(self.liSpec3.currentText() + ': ' + self.liSpec3.toolTip() + '\n')
            if self.liSpec4.isEnabled():
                printList.append(self.liSpec4.currentText() + ': ' + self.liSpec4.toolTip() + '\n')
            if self.liSpec5.isEnabled():
                printList.append(self.liSpec5.currentText() + ': ' + self.liSpec5.toolTip() + '\n')
            printList.append(starSeparator)
            printList.append('Weapon: ' + self.liWeapon.currentText() + '\n')
            printList.append(self.liWeapon.toolTip() + '\n')
            printList.append('\n')
            printList.append('Weapon 2: ' + self.liWeapon2.currentText() + '\n')
            printList.append(self.liWeapon2.toolTip() + '\n')
            f = open(savePath[0], 'w+')
            for line in printList:
                f.write(line)

            f.close()
        return
