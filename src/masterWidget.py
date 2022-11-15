"""
Widget for the random master dock.
"""
from random import randint
from math import floor
from PyQt5 import QtWidgets, QtGui, QtCore
from .data import masterPowers, stressExplosions

masterPowerList = masterPowers.returnMasterPowerList()
stressExplosionList = stressExplosions.returnStressExplosionList()

traumaList = [
 'Former delinquent', 'Former juvenile vagrant', 'Former prostitute', 'Social stigma', 'Knows no love',
 'In love with brother/cousin', 'Broken by training', 'Miscarriage', 'History of suicide attempts',
 'Horrible accident (car, fall, etc)', 'Kidnapped', 'Assaulted', 'Mistreated by parents', 'Arrested on false charges',
 'Targeted by a stalker', 'Betrayed by close friend', 'Killed a close friend', 'Betrayed a close friend',
 'Parents disappeared', "Witnessed parents' death", 'Parents tried to kill you', 'Attacked by parents',
 'Ran away from home', 'Killed your parents', 'Bad unrequited love', 'Lover died', 'Lover tried to kill you',
 'Betrayed by lover', 'Killed your lover', 'Major failure', 'Family breakup', 'Took part in something bad',
 'Wanted by the police', 'Burdened by strong regret', 'Destroyed your homeland', 'Killed many people']

class CMasterWidget(QtWidgets.QWidget):

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
        textLabel = QtWidgets.QLabel('Gender: ')
        hLayout.addWidget(textLabel)
        self.rbMale = QtWidgets.QRadioButton('Male')
        self.rbFemale = QtWidgets.QRadioButton('Female')
        hLayout.addWidget(self.rbMale)
        hLayout.addWidget(self.rbFemale)
        self.rbMale.setChecked(True)
        self.bgGender = QtWidgets.QButtonGroup()
        self.bgGender.addButton(self.rbMale)
        self.bgGender.addButton(self.rbFemale)
        self.bGender = QtWidgets.QPushButton('R')
        self.bGender.setFixedWidth(50)
        hLayout.addWidget(self.bGender)
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
        self.gbMasterType = QtWidgets.QGroupBox('Master Type', self)
        self.loGbMasterType = QtWidgets.QVBoxLayout()

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Type: ')
        hLayout.addWidget(textLabel)
        self.liMasterType = QtWidgets.QComboBox()
        self.liMasterType.setFixedWidth(100)
        self.setMasterTypeComboBox()
        hLayout.addWidget(self.liMasterType)
        self.bMT = QtWidgets.QPushButton('R')
        self.bMT.setFixedWidth(50)
        hLayout.addWidget(self.bMT)
        self.loGbMasterType.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Age: ')
        hLayout.addWidget(textLabel)
        self.spAge = QtWidgets.QSpinBox()
        self.spAge.setFixedWidth(50)
        self.spAge.setMaximum(9999)
        hLayout.addWidget(self.spAge)
        self.bAge = QtWidgets.QPushButton('R')
        self.bAge.setFixedWidth(50)
        hLayout.addWidget(self.bAge)
        self.loGbMasterType.addLayout(hLayout)
        self.laAge = QtWidgets.QLabel('Age dice: ')
        self.loGbMasterType.addWidget(self.laAge)
        self.gbMasterType.setLayout(self.loGbMasterType)
        self.gbMasterType.setFixedHeight(160)
        self.gbMasterType.setFixedWidth(210)
        self.loH1.addWidget(self.gbMasterType)
        self.gbAttri = QtWidgets.QGroupBox('Attributes', self)
        self.loGbAttri = QtWidgets.QVBoxLayout()

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('ATH:')
        textLabel.setToolTip('Athletics: Physical ability, combat ability.')
        hLayout.addWidget(textLabel, 1, QtCore.Qt.AlignRight)
        self.liATH = QtWidgets.QSpinBox()
        self.liATH.setFixedWidth(35)
        hLayout.addWidget(self.liATH, 1, QtCore.Qt.AlignRight)
        self.bATH = QtWidgets.QPushButton('R')
        self.bATH.setFixedWidth(50)
        self.bATH.parent = self.liATH
        hLayout.addWidget(self.bATH, 1, QtCore.Qt.AlignRight)
        self.loGbAttri.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('AFF:')
        textLabel.setToolTip('Affection: How good are you at forming bonds with the maids?')
        hLayout.addWidget(textLabel, 1, QtCore.Qt.AlignRight)
        self.liAFF = QtWidgets.QSpinBox()
        self.liAFF.setFixedWidth(35)
        hLayout.addWidget(self.liAFF, 1, QtCore.Qt.AlignRight)
        self.bAFF = QtWidgets.QPushButton('R')
        self.bAFF.setFixedWidth(50)
        self.bAFF.parent = self.liAFF
        hLayout.addWidget(self.bAFF, 1, QtCore.Qt.AlignRight)
        self.loGbAttri.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('SKI:')
        textLabel.setToolTip('Skill: How good are you at your duties?')
        hLayout.addWidget(textLabel, 1, QtCore.Qt.AlignRight)
        self.liSKI = QtWidgets.QSpinBox()
        self.liSKI.setFixedWidth(35)
        hLayout.addWidget(self.liSKI, 1, QtCore.Qt.AlignRight)
        self.bSKI = QtWidgets.QPushButton('R')
        self.bSKI.setFixedWidth(50)
        self.bSKI.parent = self.liSKI
        hLayout.addWidget(self.bSKI, 1, QtCore.Qt.AlignRight)
        self.loGbAttri.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('CNN:')
        textLabel.setToolTip('Cunning: How capable are you at tricking enemies and the maids?')
        hLayout.addWidget(textLabel, 1, QtCore.Qt.AlignRight)
        self.liCNN = QtWidgets.QSpinBox()
        self.liCNN.setFixedWidth(35)
        hLayout.addWidget(self.liCNN, 1, QtCore.Qt.AlignRight)
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
        self.bLCK = QtWidgets.QPushButton('R')
        self.bLCK.setFixedWidth(50)
        self.bLCK.parent = self.liLCK
        hLayout.addWidget(self.bLCK, 1, QtCore.Qt.AlignRight)
        self.loGbAttri.addLayout(hLayout)
        textLabel = QtWidgets.QLabel('    WIL:  2')
        textLabel.setToolTip('Luck: Just how lucky are you?')
        self.loGbAttri.addWidget(textLabel)
        textLabel = QtWidgets.QLabel('  Spirit:  20')
        self.loGbAttri.addWidget(textLabel)
        self.gbAttri.setLayout(self.loGbAttri)
        self.gbAttri.setFixedWidth(150)
        self.gbAttri.setFixedHeight(200)
        self.loH2 = QtWidgets.QHBoxLayout()
        self.loH2.addWidget(self.gbAttri)
        self.gbEtc = QtWidgets.QGroupBox('Etcetera', self)
        self.loGbEtc = QtWidgets.QVBoxLayout()

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Master power source: ')
        hLayout.addWidget(textLabel)
        self.liMP = QtWidgets.QComboBox()
        self.liMP.setFixedWidth(130)
        self.setMasterPowerComboBox(self.liMP)
        hLayout.addWidget(self.liMP)
        self.bMP = QtWidgets.QPushButton('R')
        self.bMP.parent = self.liMP
        self.bMP.setFixedWidth(50)
        hLayout.addWidget(self.bMP)
        self.loGbEtc.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Master power source 2: ')
        hLayout.addWidget(textLabel)
        self.liMP2 = QtWidgets.QComboBox()
        self.liMP2.setFixedWidth(130)
        self.setMasterPowerComboBox(self.liMP2)
        hLayout.addWidget(self.liMP2)
        self.bMP2 = QtWidgets.QPushButton('R')
        self.bMP2.parent = self.liMP2
        self.bMP2.setFixedWidth(50)
        hLayout.addWidget(self.bMP2)
        self.loGbEtc.addLayout(hLayout)

        hLayout = QtWidgets.QHBoxLayout()
        textLabel = QtWidgets.QLabel('Favorite maid type: ')
        hLayout.addWidget(textLabel)
        self.liFavorite = QtWidgets.QComboBox()
        self.liFavorite.setFixedWidth(130)
        self.setFavoriteMaidTypeComboBox()
        hLayout.addWidget(self.liFavorite)
        self.bFavorite = QtWidgets.QPushButton('R')
        self.bFavorite.parent = self.liFavorite
        self.bFavorite.setFixedWidth(50)
        hLayout.addWidget(self.bFavorite)
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
        self.gbEtc.setFixedHeight(200)
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
        self.loH3 = QtWidgets.QHBoxLayout()
        self.loH3.addWidget(self.gbSpec)

        self.gbTrauma = QtWidgets.QGroupBox('Trauma', self)
        self.loGbTrauma = QtWidgets.QVBoxLayout()
        self.cbEnableTrauma = QtWidgets.QCheckBox('Enable trauma')
        self.loGbTrauma.addWidget(self.cbEnableTrauma)
        self.liTrauma = QtWidgets.QComboBox()
        self.setTraumaComboBox()
        self.loGbTrauma.addWidget(self.liTrauma)
        self.bTrauma = QtWidgets.QPushButton('R')
        self.loGbTrauma.addWidget(self.bTrauma)
        self.cbEnableTrauma.button = self.bTrauma
        self.cbEnableTrauma.box = self.liTrauma
        self.gbTrauma.setLayout(self.loGbTrauma)
        self.gbTrauma.setFixedWidth(150)
        self.loH3.addWidget(self.gbTrauma)

        self.gbSave = QtWidgets.QGroupBox('Generate and save', self)
        self.loGbSave = QtWidgets.QVBoxLayout()
        self.bRollAll = QtWidgets.QPushButton('GENERATE\nMASTER', self)
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
        self.cbEnableTrauma.clicked.connect(self.setEnabilities)
        self.cbSpec3.clicked.connect(self.setEnabilities)
        self.cbSpec4.clicked.connect(self.setEnabilities)
        self.cbSpec5.clicked.connect(self.setEnabilities)
        self.bHairColor.clicked.connect(self.generateMaidColor)
        self.bEyeColor.clicked.connect(self.generateMaidColor)
        self.bGender.clicked.connect(self.generateGender)
        self.bATH.clicked.connect(self.generateAttribute)
        self.bAFF.clicked.connect(self.generateAttribute)
        self.bSKI.clicked.connect(self.generateAttribute)
        self.bCNN.clicked.connect(self.generateAttribute)
        self.bLCK.clicked.connect(self.generateAttribute)
        self.bMT.clicked.connect(self.generateMasterType)
        self.bAge.clicked.connect(self.generateAge)
        self.bMP.clicked.connect(self.generateMasterPower)
        self.bMP2.clicked.connect(self.generateMasterPower)
        self.bStress.clicked.connect(self.generateStressExplosion)
        self.bFavorite.clicked.connect(self.generateFavoriteMaidType)
        self.bSpec1.clicked.connect(self.generateSpecialQuality)
        self.bSpec2.clicked.connect(self.generateSpecialQuality)
        self.bSpec3.clicked.connect(self.generateSpecialQuality)
        self.bSpec4.clicked.connect(self.generateSpecialQuality)
        self.bSpec5.clicked.connect(self.generateSpecialQuality)
        self.bTrauma.clicked.connect(self.generateTrauma)
        self.liMasterType.currentIndexChanged.connect(self.changedMasterType)
        self.liMP.currentIndexChanged.connect(self.changedMasterPower)
        self.liMP2.currentIndexChanged.connect(self.changedMasterPower)
        self.liStress.currentIndexChanged.connect(self.changedStressExplosion)
        self.liFavorite.currentIndexChanged.connect(self.changedFavoriteMaidType)
        self.liSpec1.currentIndexChanged.connect(self.changedSpecialQuailty)
        self.liSpec2.currentIndexChanged.connect(self.changedSpecialQuailty)
        self.liSpec3.currentIndexChanged.connect(self.changedSpecialQuailty)
        self.liSpec4.currentIndexChanged.connect(self.changedSpecialQuailty)
        self.liSpec5.currentIndexChanged.connect(self.changedSpecialQuailty)
        self.bRollAll.clicked.connect(self.generateMaster)
        self.bSave.clicked.connect(self.saveMaster)

    def setEnabilities(self):
        for checkb in [self.cbEnableTrauma, self.cbSpec3, self.cbSpec4, self.cbSpec5]:
            if not checkb.isChecked():
                checkb.button.setEnabled(False)
                checkb.box.setEnabled(False)
                checkb.box.setCurrentIndex(-1)
            else:
                checkb.button.setEnabled(True)
                checkb.box.setEnabled(True)

    def generateMaidColor(self, caller=False):
        if caller == False:
            caller = self.sender()
            self.parent.parent.statusBar().showMessage('Rolled color...', 1500)
        caller.parent.setText(self.data_reader.get_random_color())

    def generateGender(self, hideMessage=False):
        if not hideMessage:
            self.parent.parent.statusBar().showMessage('Rolled gender...', 1500)
        i = randint(0, 1)
        if i == 0:
            self.rbMale.setChecked(True)
        else:
            self.rbFemale.setChecked(True)

    def generateAttribute(self, caller=False):
        if caller == False:
            caller = self.sender()
            self.parent.parent.statusBar().showMessage('Rolled attribute...', 1500)
        x = randint(1, 6)
        y = randint(1, 6)
        retVal = int(floor((x + y) / 4))
        caller.parent.setValue(retVal)

    def generateMasterType(self, hideMessage=False):
        if not hideMessage:
            self.parent.parent.statusBar().showMessage('Rolled master type...', 1500)
        i = randint(0, 5)
        self.liMasterType.setCurrentIndex(i)

    def generateAge(self, hideMessage=False):
        if not hideMessage:
            self.parent.parent.statusBar().showMessage('Rolled age...', 1500)
        self.spAge.setValue(self.data_reader.generate_master_age(self.liMasterType.currentIndex()))

    def generateMasterPower(self, caller=False):
        if caller == False:
            caller = self.sender()
            self.parent.parent.statusBar().showMessage('Rolled master power...', 1500)
        x = randint(1, 6)
        y = randint(1, 6)
        i = x + y - 2
        caller.parent.setCurrentIndex(i)

    def generateStressExplosion(self, hideMessage=False):
        if not hideMessage:
            self.parent.parent.statusBar().showMessage('Rolled stress explosion...', 1500)
        i = randint(0, 17)
        self.liStress.setCurrentIndex(i)

    def generateFavoriteMaidType(self, hideMessage=False):
        if not hideMessage:
            self.parent.parent.statusBar().showMessage('Rolled favorite maid type...', 1500)
        i = randint(0, 5)
        self.liFavorite.setCurrentIndex(i)

    def generateTrauma(self, hideMessage=False):
        if not hideMessage:
            self.parent.parent.statusBar().showMessage('Rolled trauma...', 1500)
        i = randint(0, 35)
        self.liTrauma.setCurrentIndex(i)

    def generateSpecialQuality(self, caller=False):
        onlySecondary = False
        allowed2Go = True
        inWhichTable = 0
        if caller == False:
            if QtWidgets.QApplication.keyboardModifiers() == QtCore.Qt.ShiftModifier:
                onlySecondary = True
            caller = self.sender()
            if onlySecondary:
                if caller.parent.currentIndex() < 35:
                    allowed2Go = False
            if allowed2Go:
                self.parent.parent.statusBar().showMessage('Rolled special quality...', 1500)
        if caller.parent.currentIndex() < 36:
            inWhichTable = 1
        elif caller.parent.currentIndex() < 55:
            inWhichTable = 2
        else:
            inWhichTable = 3
        if allowed2Go:
            if inWhichTable == 1:
                i = -1
                if not onlySecondary:
                    i = randint(0, 35)
                    caller.parent.setCurrentIndex(i)
                    if i == 35:
                        i = randint(37, 54)
                        caller.parent.setCurrentIndex(i)
                        i = randint(56, 61)
                        caller.parent.setCurrentIndex(i)
                elif caller.parent.currentIndex() == 35:
                    i = randint(37, 54)
                    caller.parent.setCurrentIndex(i)
            elif inWhichTable == 2:
                i = -1
                if not onlySecondary:
                    i = randint(0, 35)
                    caller.parent.setCurrentIndex(i)
                else:
                    i = randint(56, 61)
                    caller.parent.setCurrentIndex(i)
            elif inWhichTable == 3:
                i = -1
                if not onlySecondary:
                    i = randint(0, 35)
                    caller.parent.setCurrentIndex(i)
                else:
                    i = randint(56, 61)
                    caller.parent.setCurrentIndex(i)

    def changedMasterType(self):
        ii = self.liMasterType.currentIndex()
        type_of_master = self.data_reader.data["master"]["types"][ii]
        self.liMasterType.setToolTip(type_of_master[1])
        self.laAge.setText('Age dice: {}'.format(type_of_master[2]))
        self.spAge.setValue(self.data_reader.generate_master_age(ii))

    def changedMasterPower(self, caller=False):
        comboBox = self.sender()
        i = comboBox.currentIndex()
        powerOfMaster = masterPowerList[i]
        comboBox.setToolTip(powerOfMaster.descript)

    def changedStressExplosion(self):
        obj = stressExplosionList[self.liStress.currentIndex()]
        self.liStress.setToolTip(obj.descript)

    def changedFavoriteMaidType(self):
        elem = self.data_reader.data["maid"]["types"][self.liFavorite.currentIndex()]
        self.liFavorite.setToolTip(elem[1])

    def changedSpecialQuailty(self):
        comboBox = self.sender()
        if comboBox.currentIndex() < 36:
            if not comboBox.currentIndex() == -1:
                if comboBox.count() > 36:
                    for i in range(26):
                        comboBox.removeItem(36)

                elem = self.data_reader.data["master"]["qualities"][comboBox.currentIndex()]
                comboBox.setToolTip(elem[1])
                if comboBox.currentIndex() == 35:
                    comboBox.setStyleSheet('color: olive')
                    comboBox.insertSeparator(36)
                    for elem in reversed(self.data_reader.data["maid"]["qualities"][18:]):
                        comboBox.insertItem(37, elem[0])

                else:
                    comboBox.setStyleSheet('color: black')
            else:
                comboBox.setStyleSheet('color: black')
                comboBox.setToolTip('')
        elif comboBox.currentIndex() < 55:
            comboBox.setStyleSheet('color: olive')
            for i in range(7):
                comboBox.removeItem(55)

            comboBox.insertSeparator(55)
            elem = self.data_reader.data["maid"]["qualities"][18:][(comboBox.currentIndex() - 37)]
            comboBox.setToolTip(elem[1])
            comboBox.previousIndex = comboBox.currentIndex()
            for item in reversed(elem[2]):
                comboBox.insertItem(56, item[0])

        else:
            comboBox.setStyleSheet('color: black')
            item = self.data_reader.data["maid"]["qualities"][18:][(comboBox.previousIndex - 37)][2][(comboBox.currentIndex() - 56)]
            comboBox.setToolTip(item[1])

    def setMasterTypeComboBox(self):
        for elem in self.data_reader.data["master"]["types"]:
            self.liMasterType.insertItem(100, elem[0])

        self.liMasterType.setCurrentIndex(-1)

    def setMasterPowerComboBox(self, comboBox):
        for obj in masterPowerList:
            comboBox.insertItem(100, obj.name)

        comboBox.setCurrentIndex(-1)

    def setStressExplosionComboBox(self):
        for obj in stressExplosionList:
            self.liStress.insertItem(100, obj.name)

        self.liStress.setCurrentIndex(-1)

    def setFavoriteMaidTypeComboBox(self):
        for elem in self.data_reader.data["maid"]["types"]:
            self.liFavorite.insertItem(100, elem[0])

        self.liFavorite.setCurrentIndex(-1)

    def setSpecialQualityComboBox(self, comboBox):
        for elem in self.data_reader.data["master"]["qualities"]:
            comboBox.insertItem(100, elem[0])

        comboBox.setCurrentIndex(-1)

    def setTraumaComboBox(self):
        for item in traumaList:
            self.liTrauma.insertItem(100, item)

        self.liTrauma.setCurrentIndex(-1)

    def generateMaster(self):
        self.generateGender(True)
        self.generateMaidColor(self.bEyeColor)
        self.generateMaidColor(self.bHairColor)
        self.generateAttribute(self.bATH)
        self.generateAttribute(self.bAFF)
        self.generateAttribute(self.bSKI)
        self.generateAttribute(self.bCNN)
        self.generateAttribute(self.bLCK)
        self.generateMasterPower(self.bMP)
        self.generateMasterPower(self.bMP2)
        self.generateFavoriteMaidType(True)
        self.generateMasterType(True)
        self.generateStressExplosion(True)
        self.generateSpecialQuality(self.bSpec1)
        self.generateSpecialQuality(self.bSpec2)
        if self.bSpec3.isEnabled():
            self.generateSpecialQuality(self.bSpec3)
        if self.bSpec4.isEnabled():
            self.generateSpecialQuality(self.bSpec4)
        if self.bSpec5.isEnabled():
            self.generateSpecialQuality(self.bSpec5)
        if self.bTrauma.isEnabled():
            self.generateTrauma(True)

    def saveMaster(self):
        savePath = QtWidgets.QFileDialog.getSaveFileName(None, 'Save your master as...', '', 'Text Documents (*.txt);;All files (*.*)')
        if not savePath[0] == '':
            starSeparator = '-----------------------------------------------------------------------------------------\n'
            printList = []
            printList.append(starSeparator)
            printList.append('Name: ' + self.liName.text() + '\n')
            printList.append('Age: ' + str(self.spAge.value()) + '\n')
            genderText = 'male'
            if self.rbFemale.isChecked():
                genderText = 'female'
            printList.append('Gender: ' + genderText + '\n')
            printList.append('Eye color: ' + self.liEyeColor.text() + '\n')
            printList.append('Hair color: ' + self.liHairColor.text() + '\n')
            printList.append(starSeparator)
            printList.append('Stats:\n')
            printList.append('Athletics: ' + str(self.liATH.value()) + '\n')
            printList.append('Affection: ' + str(self.liAFF.value()) + '\n')
            printList.append('Skill: ' + str(self.liSKI.value()) + '\n')
            printList.append('Cunning: ' + str(self.liCNN.value()) + '\n')
            printList.append('Luck: ' + str(self.liLCK.value()) + '\n')
            printList.append('Will: 2\n')
            printList.append('Spirit: 20\n')
            printList.append(starSeparator)
            printList.append('Master type:' + self.liMasterType.currentText() + '\n')
            printList.append(self.liMasterType.toolTip() + '\n')
            printList.append('\n')
            printList.append('Master powers:\n')
            printList.append(self.liMP.currentText() + ': ' + self.liMP.toolTip() + '\n')
            printList.append(self.liMP2.currentText() + ': ' + self.liMP2.toolTip() + '\n')
            printList.append('\n')
            printList.append('Favorite maid type: ' + self.liFavorite.currentText() + '\n')
            printList.append(self.liFavorite.toolTip() + '\n')
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
            if self.liTrauma.isEnabled():
                printList.append('Trauma: ' + self.liTrauma.currentText() + '\n')
                printList.append(self.liTrauma.toolTip() + '\n')
            f = open(savePath[0], 'w+')
            for line in printList:
                f.write(line)

            f.close()
        return
