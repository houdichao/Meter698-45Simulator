# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Meter698_config.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(663, 384)
        Dialog.setMinimumSize(QtCore.QSize(250, 320))
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 621, 321))
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 175, 160))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setAutoRepeat(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setChecked(True)
        self.checkBox.setAutoRepeat(False)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_4.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.checkBox_4.setToolTip("")
        self.checkBox_4.setWhatsThis("")
        self.checkBox_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_4.setCheckable(True)
        self.checkBox_4.setChecked(False)
        self.checkBox_4.setAutoRepeat(False)
        self.checkBox_4.setTristate(False)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.checkBox_5.setToolTip("")
        self.checkBox_5.setWhatsThis("")
        self.checkBox_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setAutoRepeat(False)
        self.checkBox_5.setTristate(False)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_7 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout.addWidget(self.checkBox_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(5, -1, 14, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setEnabled(False)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 17, 421, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 401, 221))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit.setEnabled(False)
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_3.addWidget(self.textEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_4.addWidget(self.radioButton_2)
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setAcceptRichText(False)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_4.addWidget(self.textEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 611, 271))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(224)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(110)
        self.tableWidget.verticalHeader().setVisible(False)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 270, 239, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_3.setToolTip("")
        self.pushButton_3.setStatusTip("")
        self.pushButton_3.setWhatsThis("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 20, 251, 71))
        self.groupBox_4.setObjectName("groupBox_4")
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox_4)
        self.timeEdit.setEnabled(False)
        self.timeEdit.setGeometry(QtCore.QRect(201, 30, 41, 20))
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(True)
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2001, 1, 1), QtCore.QTime(0, 0, 0)))
        self.timeEdit.setDate(QtCore.QDate(2001, 1, 1))
        self.timeEdit.setCurrentSectionIndex(0)
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.groupBox_4)
        self.timeEdit_2.setEnabled(False)
        self.timeEdit_2.setGeometry(QtCore.QRect(140, 30, 41, 20))
        self.timeEdit_2.setWrapping(False)
        self.timeEdit_2.setFrame(True)
        self.timeEdit_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(62, 32, 72, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QtCore.QRect(186, 31, 16, 20))
        self.label_5.setObjectName("label_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 32, 71, 16))
        self.checkBox_6.setObjectName("checkBox_6")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 110, 591, 171))
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_7.setGeometry(QtCore.QRect(20, 20, 561, 81))
        self.groupBox_7.setObjectName("groupBox_7")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_22.setEnabled(False)
        self.lineEdit_22.setGeometry(QtCore.QRect(180, 24, 361, 20))
        self.lineEdit_22.setAccessibleDescription("")
        self.lineEdit_22.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_22.setInputMask("")
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_7)
        self.layoutWidget3.setGeometry(QtCore.QRect(11, 25, 171, 62))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget3)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_4)
        self.radioButton_6 = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radioButton_6.setObjectName("radioButton_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radioButton_6)
        self.radioButton_5 = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radioButton_5.setObjectName("radioButton_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.radioButton_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setGeometry(QtCore.QRect(30, 130, 71, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 128, 461, 20))
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setCursorPosition(0)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 121, 81))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 30, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 120, 161, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 131, 16))
        self.label_3.setObjectName("label_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(210, 20, 371, 161))
        self.groupBox_5.setObjectName("groupBox_5")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 30, 331, 111))
        self.textEdit_3.setAutoFillBackground(True)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setAcceptRichText(False)
        self.textEdit_3.setObjectName("textEdit_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.layoutWidget4 = QtWidgets.QWidget(Dialog)
        self.layoutWidget4.setGeometry(QtCore.QRect(480, 350, 158, 25))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_2.clicked.connect(Dialog.close)
        self.radioButton_5.toggled['bool'].connect(self.lineEdit_22.setEnabled)
        self.radioButton.toggled['bool'].connect(self.textEdit.setEnabled)
        self.radioButton_2.toggled['bool'].connect(self.textEdit_2.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "设置"))
        self.checkBox_3.setText(_translate("Dialog", "实时正向有功自动递增"))
        self.checkBox_2.setText(_translate("Dialog", "曲线时标自动修正"))
        self.checkBox.setText(_translate("Dialog", "日月冻结时标自动修正"))
        self.checkBox_4.setText(_translate("Dialog", "日冻结数据变化"))
        self.checkBox_5.setText(_translate("Dialog", "明文安全响应（回复MAC）"))
        self.checkBox_7.setText(_translate("Dialog", "645时标随抄表次数叠加"))
        self.label.setText(_translate("Dialog", "通配地址数量:"))
        self.groupBox_2.setTitle(_translate("Dialog", "通信地址黑/白名单:(多地址用 / 隔开;地址范围用 - )"))
        self.radioButton_3.setText(_translate("Dialog", "未启用"))
        self.radioButton.setText(_translate("Dialog", "黑名单:"))
        self.radioButton_2.setText(_translate("Dialog", "白名单:"))
        self.textEdit_2.setPlaceholderText(_translate("Dialog", "包含载波搜表回复地址,白名单关闭或搜表帧用全A回复地址为:000000000001"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "功能"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "数据标识"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "值"))
        self.pushButton_3.setText(_translate("Dialog", "+"))
        self.pushButton_4.setText(_translate("Dialog", "-"))
        self.pushButton_6.setText(_translate("Dialog", "刷新"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "698数据标识"))
        self.groupBox_4.setTitle(_translate("Dialog", "曲线漏点"))
        self.timeEdit.setDisplayFormat(_translate("Dialog", "HH:mm"))
        self.timeEdit_2.setDisplayFormat(_translate("Dialog", "HH:mm"))
        self.label_4.setText(_translate("Dialog", "无数据时段:"))
        self.label_5.setText(_translate("Dialog", "-"))
        self.checkBox_6.setText(_translate("Dialog", "启用"))
        self.groupBox_6.setTitle(_translate("Dialog", "特殊事件:"))
        self.groupBox_7.setTitle(_translate("Dialog", "事件返回"))
        self.lineEdit_22.setPlaceholderText(_translate("Dialog", "多个事件用英文分号隔开(;)"))
        self.radioButton_4.setText(_translate("Dialog", "按默认返回"))
        self.radioButton_6.setText(_translate("Dialog", "全回空"))
        self.radioButton_5.setText(_translate("Dialog", "部分回空:"))
        self.label_6.setText(_translate("Dialog", "3320返回值:"))
        self.lineEdit_3.setText(_translate("Dialog", "85 01 00 33 20 02 00 01 01 04 51 30 1b 02 00 51 30 2a 02 00 51 30 13 02 00 51 30 11 02 00 00 00\n"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "698高级"))
        self.groupBox.setTitle(_translate("Dialog", "抄表log导出为:"))
        self.pushButton_5.setText(_translate("Dialog", "txt格式"))
        self.groupBox_3.setTitle(_translate("Dialog", "About："))
        self.label_2.setText(_translate("Dialog", "Version：V1.6"))
        self.label_3.setText(_translate("Dialog", "Frame：200427"))
        self.groupBox_5.setTitle(_translate("Dialog", "645说明:"))
        self.textEdit_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">返回年月日周:@GetDateWeek@                        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">返回当前时间:@GetTime@                        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">返回冻结时标(当前):@FreezeTime@                    </p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "其它"))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))


