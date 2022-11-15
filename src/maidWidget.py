"""
Widget for the random maid dock.
"""
from random import randint
from math import floor
from PyQt5 import QtWidgets, QtGui, QtCore
from .data import maidTypes, specialQualities, maidRoots, stressExplosions, maidPowers

maidTypeList = maidTypes.returnMaidTypeList()
specialQualityList = specialQualities.returnSpecialQualityList()
maidRootList = maidRoots.returnMaidRootList()
stressExplosionList = stressExplosions.returnStressExplosionList()
maidPowerList = maidPowers.returnMaidPowerList()

class CMaidWidget(QtWidgets.QWidget):

    def __init__(self, data_reader, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.data_reader = data_reader
        self.parent = parent

        self.stats = [0, 0, 0, 0, 0, 0]
        self.rebuildingMaidPowers = False

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
        hLayout.addStretch(1)
        self.loGbBasic.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Uniform color: ')
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
        self.gbBasic.setLayout(self.loGbBasic)
        self.loH1 = QtWidgets.QHBoxLayout()
        self.loH1.addWidget(self.gbBasic)
        self.gbMaidType = QtWidgets.QGroupBox('Maid Type', self)
        self.loGbMaidType = QtWidgets.QVBoxLayout()

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('First: ')
        hLayout.addWidget(textLabel)
        self.liFirstType = QtWidgets.QComboBox()
        self.setMaidTypeComboBox(self.liFirstType)
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
        self.setMaidTypeComboBox(self.liSecondType)
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
        self.bMpATH = QtWidgets.QPushButton('MP')
        self.bMpATH.setFixedWidth(50)
        self.bMpATH.statType = 0
        self.liATH.mpButton = self.bMpATH
        hLayout.addWidget(self.bMpATH, 1, QtCore.Qt.AlignRight)
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
        self.bMpAFF = QtWidgets.QPushButton('MP')
        self.bMpAFF.setFixedWidth(50)
        self.bMpAFF.statType = 1
        self.liAFF.mpButton = self.bMpAFF
        hLayout.addWidget(self.bMpAFF, 1, QtCore.Qt.AlignRight)
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
        self.bMpSKI = QtWidgets.QPushButton('MP')
        self.bMpSKI.setFixedWidth(50)
        self.bMpSKI.statType = 2
        self.liSKI.mpButton = self.bMpSKI
        hLayout.addWidget(self.bMpSKI, 1, QtCore.Qt.AlignRight)
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
        self.bMpCNN = QtWidgets.QPushButton('MP')
        self.bMpCNN.setFixedWidth(50)
        self.bMpCNN.statType = 3
        self.liCNN.mpButton = self.bMpCNN
        hLayout.addWidget(self.bMpCNN, 1, QtCore.Qt.AlignRight)
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
        self.bMpLCK = QtWidgets.QPushButton('MP')
        self.bMpLCK.setFixedWidth(50)
        self.bMpLCK.statType = 4
        self.liLCK.mpButton = self.bMpLCK
        hLayout.addWidget(self.bMpLCK, 1, QtCore.Qt.AlignRight)
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
        self.bMpWIL = QtWidgets.QPushButton('MP')
        self.bMpWIL.setFixedWidth(50)
        self.bMpWIL.statType = 5
        self.liWIL.mpButton = self.bMpWIL
        hLayout.addWidget(self.bMpWIL, 1, QtCore.Qt.AlignRight)
        self.loGbAttri.addLayout(hLayout)

        self.gbAttri.setLayout(self.loGbAttri)
        self.loH2 = QtWidgets.QHBoxLayout()
        self.loH2.addWidget(self.gbAttri)
        self.gbEtc = QtWidgets.QGroupBox('Etcetera', self)
        self.loGbEtc = QtWidgets.QVBoxLayout()

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Maid root: ')
        hLayout.addWidget(textLabel)
        self.liMaidRoot = QtWidgets.QComboBox()
        self.setMaidRootComboBox()
        self.liMaidRoot.setFixedWidth(130)
        hLayout.addWidget(self.liMaidRoot)
        self.bMaidRoot = QtWidgets.QPushButton('R')
        self.bMaidRoot.parent = self.liMaidRoot
        self.bMaidRoot.setFixedWidth(50)
        hLayout.addWidget(self.bMaidRoot)
        self.loGbEtc.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Stress explosion: ')
        hLayout.addWidget(textLabel)
        self.liStress = QtWidgets.QComboBox()
        self.setStressExplosionComboBox()
        self.liStress.setFixedWidth(130)
        hLayout.addWidget(self.liStress)
        self.bStress = QtWidgets.QPushButton('R')
        self.bStress.parent = self.liStress
        self.bStress.setFixedWidth(50)
        hLayout.addWidget(self.bStress)
        self.loGbEtc.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Maid power: ')
        hLayout.addWidget(textLabel)
        self.liMP = QtWidgets.QComboBox()
        self.liMP.setFixedWidth(150)
        hLayout.addWidget(self.liMP)
        self.loGbEtc.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Maid power 2: ')
        hLayout.addWidget(textLabel)
        self.liMP2 = QtWidgets.QComboBox()
        self.liMP2.setFixedWidth(150)
        hLayout.addWidget(self.liMP2)
        self.loGbEtc.addLayout(hLayout)

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
        self.setSpecialQualityComboBox(self.liSpec1)
        self.liSpec1.setFixedWidth(150)
        hLayout.addWidget(self.liSpec1, 10, QtCore.Qt.AlignRight)
        self.bSpec1 = QtWidgets.QPushButton('R')
        self.bSpec1.setFixedWidth(50)
        self.bSpec1.parent = self.liSpec1
        hLayout.addWidget(self.bSpec1, 0, QtCore.Qt.AlignRight)
        self.loGbSpec.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        self.liSpec2 = QtWidgets.QComboBox()
        self.setSpecialQualityComboBox(self.liSpec2)
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
        self.setSpecialQualityComboBox(self.liSpec3)
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
        self.setSpecialQualityComboBox(self.liSpec4)
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
        self.setSpecialQualityComboBox(self.liSpec5)
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
        self.gbWeap = QtWidgets.QGroupBox('Weapon', self)
        self.loGbWeap = QtWidgets.QVBoxLayout()
        self.cbEnableWeapon = QtWidgets.QCheckBox('Enable weapon')
        self.cbEnableWeapon.setChecked(True)
        self.loGbWeap.addWidget(self.cbEnableWeapon)
        self.liWeapon = QtWidgets.QComboBox()
        self.setWeaponComboBox()
        self.loGbWeap.addWidget(self.liWeapon)
        self.bWeap = QtWidgets.QPushButton('R')
        self.loGbWeap.addWidget(self.bWeap)
        self.cbEnableWeapon.button = self.bWeap
        self.cbEnableWeapon.box = self.liWeapon
        self.gbWeap.setLayout(self.loGbWeap)
        self.loH3.addWidget(self.gbWeap)

        self.gbSave = QtWidgets.QGroupBox('Generate and save', self)
        self.loGbSave = QtWidgets.QVBoxLayout()
        self.bRollAll = QtWidgets.QPushButton('GENERATE\nMAID', self)
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
        self.setMaidPowerComboBox(self.liMP, [0, 1, 2, 3, 4, 5])
        self.setMaidPowerComboBox(self.liMP2, [0, 1, 2, 3, 4, 5])
        self.bATH.clicked.connect(self.generateAttribute)
        self.bAFF.clicked.connect(self.generateAttribute)
        self.bSKI.clicked.connect(self.generateAttribute)
        self.bCNN.clicked.connect(self.generateAttribute)
        self.bLCK.clicked.connect(self.generateAttribute)
        self.bWIL.clicked.connect(self.generateAttribute)
        self.bFirstType.clicked.connect(self.generateMaidType)
        self.bSecondType.clicked.connect(self.generateMaidType)
        self.bUniColor.clicked.connect(self.generateMaidColor)
        self.bEyeColor.clicked.connect(self.generateMaidColor)
        self.bHairColor.clicked.connect(self.generateMaidColor)
        self.bSpec1.clicked.connect(self.generateSpecialQuality)
        self.bSpec2.clicked.connect(self.generateSpecialQuality)
        self.bSpec3.clicked.connect(self.generateSpecialQuality)
        self.bSpec4.clicked.connect(self.generateSpecialQuality)
        self.bSpec5.clicked.connect(self.generateSpecialQuality)
        self.bWeap.clicked.connect(self.generateWeapon)
        self.bMaidRoot.clicked.connect(self.generateMaidRoot)
        self.bStress.clicked.connect(self.generateStressExplosion)
        self.bMpATH.clicked.connect(self.generateMaidPower)
        self.bMpAFF.clicked.connect(self.generateMaidPower)
        self.bMpSKI.clicked.connect(self.generateMaidPower)
        self.bMpCNN.clicked.connect(self.generateMaidPower)
        self.bMpLCK.clicked.connect(self.generateMaidPower)
        self.bMpWIL.clicked.connect(self.generateMaidPower)
        self.bRollAll.clicked.connect(self.generateFullMaid)
        self.bSave.clicked.connect(self.saveMaid)
        self.cbEnableWeapon.clicked.connect(self.setEnabilities)
        self.cbSpec3.clicked.connect(self.setEnabilities)
        self.cbSpec4.clicked.connect(self.setEnabilities)
        self.cbSpec5.clicked.connect(self.setEnabilities)
        self.liFirstType.currentIndexChanged.connect(self.changedMaidType)
        self.liSecondType.currentIndexChanged.connect(self.changedMaidType)
        self.liSpec1.currentIndexChanged.connect(self.changedSpecialQuailty)
        self.liSpec2.currentIndexChanged.connect(self.changedSpecialQuailty)
        self.liSpec3.currentIndexChanged.connect(self.changedSpecialQuailty)
        self.liSpec4.currentIndexChanged.connect(self.changedSpecialQuailty)
        self.liSpec5.currentIndexChanged.connect(self.changedSpecialQuailty)
        self.liWeapon.currentIndexChanged.connect(self.changedWeapon)
        self.liMaidRoot.currentIndexChanged.connect(self.changedMaidRoot)
        self.liStress.currentIndexChanged.connect(self.changedStressExplosion)
        self.liATH.valueChanged.connect(self.calculateStats)
        self.liAFF.valueChanged.connect(self.calculateStats)
        self.liSKI.valueChanged.connect(self.calculateStats)
        self.liCNN.valueChanged.connect(self.calculateStats)
        self.liLCK.valueChanged.connect(self.calculateStats)
        self.liWIL.valueChanged.connect(self.calculateStats)
        self.liMP.activated.connect(self.changedMaidPower)
        self.liMP2.activated.connect(self.changedMaidPower)

    def setEnabilities(self):
        for checkb in [self.cbEnableWeapon, self.cbSpec3, self.cbSpec4, self.cbSpec5]:
            if not checkb.isChecked():
                checkb.button.setEnabled(False)
                checkb.box.setEnabled(False)
                checkb.box.setCurrentIndex(-1)
            else:
                checkb.button.setEnabled(True)
                checkb.box.setEnabled(True)

    def generateAttribute(self, caller=False):
        if caller == False:
            caller = self.sender()
            self.parent.parent.statusBar().showMessage('Rolled attribute...', 1500)
        x = randint(1, 6)
        y = randint(1, 6)
        retVal = int(floor((x + y) / 3))
        caller.parent.setValue(retVal)

    def generateMaidType(self, caller=False):
        if caller == False:
            caller = self.sender()
            self.parent.parent.statusBar().showMessage('Rolled maid type...', 1500)
        i = randint(0, 5)
        caller.parent.setCurrentIndex(i)

    def generateMaidColor(self, caller=False):
        if caller == False:
            caller = self.sender()
            self.parent.parent.statusBar().showMessage('Rolled color...', 1500)
        caller.parent.setText(self.data_reader.get_random_color())

    def generateWeapon(self, hideMessage=False):
        if not hideMessage:
            self.parent.parent.statusBar().showMessage('Rolled weapon...', 1500)
        i = randint(0, 35)
        self.liWeapon.setCurrentIndex(i)

    def generateMaidRoot(self, hideMessage=False):
        if not hideMessage:
            self.parent.parent.statusBar().showMessage('Rolled maid root...', 1500)
        i = randint(0, 17)
        self.liMaidRoot.setCurrentIndex(i)

    def generateStressExplosion(self, hideMessage=False):
        if not hideMessage:
            self.parent.parent.statusBar().showMessage('Rolled stress explosion...', 1500)
        i = randint(0, 17)
        self.liStress.setCurrentIndex(i)

    def generateMaidPower(self, caller=False, generateSecond=False):
        if caller == False:
            caller = self.sender()
            self.parent.parent.statusBar().showMessage('Rolled maid power...', 1500)
        if not QtWidgets.QApplication.keyboardModifiers() == QtCore.Qt.ShiftModifier and not generateSecond:
            upperLimit = self.liMP.count()
            desiredStat = caller.statType
            while True:
                success = False
                while True:
                    i = randint(0, upperLimit - 1)
                    text = self.liMP.itemText(i)
                    if text != self.liMP2.currentText():
                        break

                for item in maidPowerList[desiredStat]:
                    if item.name == text:
                        success = True
                        self.liMP.setCurrentIndex(i)
                        break

                if success:
                    break

            self.changedMaidPower(self.liMP)
        elif self.liMP2.isEnabled():
            upperLimit = self.liMP2.count()
            desiredStat = caller.statType
            while True:
                success = False
                while True:
                    i = randint(0, upperLimit - 1)
                    text = self.liMP2.itemText(i)
                    if text != self.liMP.currentText():
                        break

                for item in maidPowerList[desiredStat]:
                    if item.name == text:
                        success = True
                        self.liMP2.setCurrentIndex(i)
                        break

                if success:
                    break

            self.changedMaidPower(self.liMP2)

    def generateSpecialQuality(self, caller=False):
        onlySecondary = False
        allowed2Go = True
        if caller == False:
            if QtWidgets.QApplication.keyboardModifiers() == QtCore.Qt.ShiftModifier:
                onlySecondary = True
            caller = self.sender()
            if onlySecondary:
                if caller.parent.currentIndex() < 18:
                    allowed2Go = False
            if allowed2Go:
                self.parent.parent.statusBar().showMessage('Rolled special quality...', 1500)
        if allowed2Go:
            i = -1
            if not onlySecondary:
                i = randint(0, 35)
                caller.parent.setCurrentIndex(i)
            if i > 17 or i == -1:
                i = randint(37, 42)
                caller.parent.setCurrentIndex(i)

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
        highestValue = -1
        for i in range(len(self.stats)):
            if highestValue < self.stats[i]:
                highestValue = self.stats[i]

        highestValueList = []
        buttonList = [
         self.bMpATH, self.bMpAFF, self.bMpSKI, self.bMpCNN, self.bMpLCK, self.bMpWIL]
        for i in range(len(self.stats)):
            if self.stats[i] == highestValue:
                buttonList[i].setEnabled(True)
                highestValueList.append(i)
            else:
                buttonList[i].setEnabled(False)

        if self.stats[0] + self.stats[1] + self.stats[2] + self.stats[3] + self.stats[4] + self.stats[5] < 10:
            self.liMP2.setEnabled(True)
        else:
            self.liMP2.setCurrentIndex(-1)
            self.liMP2.setEnabled(False)
        self.setMaidPowerComboBox(self.liMP, highestValueList)
        self.setMaidPowerComboBox(self.liMP2, highestValueList)

    def changedMaidType(self):
        comboBox = self.sender()
        obj = maidTypeList[comboBox.currentIndex()]
        comboBox.desc.setText(obj.descript)
        comboBox.setToolTip(obj.tooltip)
        comboBox.changeList = obj.changeList
        self.calculateStats()

    def changedMaidPower(self, comboBox=0):
        if not self.rebuildingMaidPowers:
            if type(comboBox) is int:
                comboBox = self.sender()
            text = comboBox.currentText()
            found = False
            for stat in maidPowerList:
                for item in stat:
                    if item.name == text:
                        comboBox.setToolTip(item.descript)
                        found = True

            if comboBox.currentIndex() == -1 or found == False:
                comboBox.setToolTip('')

    def changedSpecialQuailty(self):
        comboBox = self.sender()
        if comboBox.currentIndex() < 36:
            if not comboBox.currentIndex() == -1:
                if comboBox.count() > 36:
                    for i in range(7):
                        comboBox.removeItem(36)

                obj = specialQualityList[comboBox.currentIndex()]
                comboBox.setToolTip(obj.descript)
                if obj.secondaryTable != []:
                    comboBox.setStyleSheet('color: olive')
                    comboBox.insertSeparator(36)
                    for item in reversed(obj.secondaryTable):
                        comboBox.insertItem(37, item.name)

                    comboBox.previousIndex = comboBox.currentIndex()
                else:
                    comboBox.setStyleSheet('color: black')
            else:
                comboBox.setStyleSheet('color: black')
                comboBox.setToolTip('')
        else:
            comboBox.setStyleSheet('color: black')
            item = specialQualityList[comboBox.previousIndex].secondaryTable[(comboBox.currentIndex() - 37)]
            comboBox.setToolTip(item.descript)

    def changedWeapon(self):
        if not self.liWeapon.currentIndex() == -1:
            desc = self.data_reader.data["maid"]["weapons"][self.liWeapon.currentIndex()][1]
            self.liWeapon.setToolTip(desc)
        else:
            self.liWeapon.setToolTip('')

    def changedMaidRoot(self):
        obj = maidRootList[self.liMaidRoot.currentIndex()]
        self.liMaidRoot.setToolTip(obj.descript)

    def changedStressExplosion(self):
        obj = stressExplosionList[self.liStress.currentIndex()]
        self.liStress.setToolTip(obj.descript)

    def setMaidPowerComboBox(self, comboBox, highestStats):
        self.rebuildingMaidPowers = True
        text = comboBox.itemText(comboBox.currentIndex())
        for i in range(comboBox.count()):
            comboBox.removeItem(0)

        for statNumber in highestStats:
            for item in maidPowerList[statNumber]:
                comboBox.insertItem(100, item.name)

            comboBox.insertSeparator(100)

        comboBox.removeItem(comboBox.count() - 1)
        listOfNames = [ comboBox.itemText(i) for i in range(comboBox.count()) ]
        comboBox.setCurrentIndex(-1)
        for i in range(len(listOfNames)):
            if listOfNames[i] == text:
                comboBox.setCurrentIndex(i)

        self.rebuildingMaidPowers = False
        self.changedMaidPower(comboBox)

    def setMaidTypeComboBox(self, comboBox):
        for obj in maidTypeList:
            comboBox.insertItem(100, obj.name)

        comboBox.setCurrentIndex(-1)
        comboBox.previousIndex = -1

    def setSpecialQualityComboBox(self, comboBox):
        for obj in specialQualityList:
            comboBox.insertItem(100, obj.name)

        comboBox.setCurrentIndex(-1)

    def setWeaponComboBox(self):
        for elem in self.data_reader.data["maid"]["weapons"]:
            self.liWeapon.insertItem(100, elem[0])

        self.liWeapon.setCurrentIndex(-1)

    def setMaidRootComboBox(self):
        for obj in maidRootList:
            self.liMaidRoot.insertItem(100, obj.name)

        self.liMaidRoot.setCurrentIndex(-1)

    def setStressExplosionComboBox(self):
        for obj in stressExplosionList:
            self.liStress.insertItem(100, obj.name)

        self.liStress.setCurrentIndex(-1)

    def generateFullMaid(self):
        self.generateMaidColor(self.bUniColor)
        self.generateMaidColor(self.bHairColor)
        self.generateMaidColor(self.bEyeColor)
        self.generateAttribute(self.bATH)
        self.generateAttribute(self.bAFF)
        self.generateAttribute(self.bSKI)
        self.generateAttribute(self.bCNN)
        self.generateAttribute(self.bLCK)
        self.generateAttribute(self.bWIL)
        self.generateMaidType(self.bFirstType)
        self.generateMaidType(self.bSecondType)
        self.liMP.setCurrentIndex(-1)
        self.liMP2.setCurrentIndex(-1)
        onlyButton = None
        for button in [self.bMpATH, self.bMpAFF, self.bMpSKI, self.bMpCNN, self.bMpLCK, self.bMpWIL]:
            if button.isEnabled():
                if onlyButton == None:
                    onlyButton = button
                elif onlyButton == 'MORE':
                    continue
                else:
                    onlyButton = 'MORE'

        if onlyButton != None and onlyButton != 'MORE':
            self.generateMaidPower(onlyButton)
            if self.liMP2.isEnabled():
                self.generateMaidPower(onlyButton, True)
        self.generateMaidRoot(True)
        self.generateStressExplosion(True)
        self.generateSpecialQuality(self.bSpec1)
        self.generateSpecialQuality(self.bSpec2)
        if self.liSpec3.isEnabled():
            self.generateSpecialQuality(self.bSpec3)
        if self.liSpec4.isEnabled():
            self.generateSpecialQuality(self.bSpec4)
        if self.liSpec5.isEnabled():
            self.generateSpecialQuality(self.bSpec5)
        if self.liWeapon.isEnabled():
            self.generateWeapon(True)
        return

    def saveMaid(self):
        savePath = QtWidgets.QFileDialog.getSaveFileName(None, 'Save your maid as...', '', 'Text Documents (*.txt);;All files (*.*)')
        if not savePath[0] == '':
            starSeparator = '-----------------------------------------------------------------------------------------\n'
            printList = []
            printList.append(starSeparator)
            printList.append('Name: ' + self.liName.text() + '\n')
            printList.append('Age: ' + str(self.liAge.value()) + '\n')
            printList.append('Uniform color: ' + self.liUniColor.text() + '\n')
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
            printList.append('Maid types:\n')
            printList.append(self.liFirstType.currentText() + ': ' + self.liFirstType.toolTip() + '\n')
            printList.append(self.liSecondType.currentText() + ': ' + self.liSecondType.toolTip() + '\n')
            printList.append('\n')
            printList.append('Maid powers:\n')
            printList.append(self.liMP.currentText() + ': ' + self.liMP.toolTip() + '\n')
            if self.liMP2.isEnabled():
                printList.append(self.liMP2.currentText() + ': ' + self.liMP2.toolTip() + '\n')
            printList.append('\n')
            printList.append('Maid root: ' + self.liMaidRoot.currentText() + '\n')
            printList.append(self.liMaidRoot.toolTip() + '\n')
            printList.append('\n')
            printList.append('Stress explosion: ' + self.liStress.currentText() + '\n')
            printList.append(self.liStress.toolTip() + '\n')
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
            if self.liWeapon.isEnabled():
                printList.append('Weapon: ' + self.liWeapon.currentText() + '\n')
                printList.append(self.liWeapon.toolTip() + '\n')
            f = open(savePath[0], 'w+')
            for line in printList:
                f.write(line)

            f.close()
        return
