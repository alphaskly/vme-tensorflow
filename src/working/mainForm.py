# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created: Sun Aug 13 10:18:41 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import src.common.fileutil as FileMD5
import time
import threading

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainForm(QtWidgets.QDialog):

    def __init__(self):
        super(Ui_MainForm, self).__init__()
        self.setupUi(self)
        shadow = QtGui.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10);
        shadow.setColor(QtCore.Qt.black);
        shadow.setOffset(2);
        self.setGraphicsEffect(shadow);
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground);
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(770, 500)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 768, 482))
        self.widget.setStyleSheet(_fromUtf8(""))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.widget_2 = QtGui.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 771, 71))
        self.widget_2.setStyleSheet(_fromUtf8("background-image: url(:/img/banner.jpg);"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.logo = QtGui.QLabel(self.widget_2)
        self.logo.setGeometry(QtCore.QRect(20, 0, 111, 71))
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet(_fromUtf8("background-image: url(:/img/logo.png);"))
        self.logo.setText(_fromUtf8(""))
        self.logo.setObjectName(_fromUtf8("logo"))
        self.label_5 = QtGui.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(630, 10, 71, 51))
        self.label_5.setStyleSheet(_fromUtf8("background-image: url(:/img/head.png);"))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton = QtGui.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(140, 0, 121, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("color: rgb(211, 211, 211);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 0, 121, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("color: rgb(211, 211, 211);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 0, 121, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_fromUtf8("color: rgb(211, 211, 211);"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 0, 121, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(_fromUtf8("color: rgb(211, 211, 211);"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.widget_2)
        self.pushButton_5.setGeometry(QtCore.QRect(700, 20, 51, 31))
        self.pushButton_5.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);\n"
"font: 75 14pt \"Agency FB\";\n"
"text-decoration: underline;"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.widget_3 = QtGui.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(0, 459, 771, 21))
        self.widget_3.setStyleSheet(_fromUtf8("background-image: url(:/img/font.jpg);"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.label_7 = QtGui.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(330, 0, 51, 21))
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 0);\n"
"font: 75 10pt \"Agency FB\";"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.progressBar = QtGui.QProgressBar(self.widget_3)
        self.progressBar.setGeometry(QtCore.QRect(380, 0, 181, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_8 = QtGui.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(20, 0, 54, 21))
        self.label_8.setStyleSheet(_fromUtf8("font: 75 10pt \"Agency FB\";\n"
"color: rgb(255, 170, 0);"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.tip = QtGui.QLabel(self.widget_3)
        self.tip.setGeometry(QtCore.QRect(80, 1, 241, 20))
        self.tip.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.tip.setObjectName(_fromUtf8("tip"))
        self.label = QtGui.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(570, 0, 31, 21))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 170, 0);\n"
"font: 75 10pt \"Agency FB\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(600, 0, 161, 21))
        self.label_2.setStyleSheet(_fromUtf8("font: 75 12pt \"Microsoft YaHei UI\";\n"
""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.operArea = QtGui.QWidget(self.widget)
        self.operArea.setGeometry(QtCore.QRect(0, 70, 771, 391))
        self.operArea.setObjectName(_fromUtf8("operArea"))
        self.fileWidget = QtGui.QWidget(self.operArea)
        self.fileWidget.setGeometry(QtCore.QRect(0, 0, 771, 391))
        self.fileWidget.setStyleSheet(_fromUtf8("#fileWidget {\n"
"\n"
"    background-image: url(:/img/timg.jpg);\n"
"\n"
"}"))
        self.fileWidget.setObjectName(_fromUtf8("fileWidget"))
        self.lineEdit = QtGui.QLineEdit(self.fileWidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 461, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(_fromUtf8("LineEdit{background-image: url(:/img/banner.jpg)}"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.selectBtn = QtGui.QPushButton(self.fileWidget)
        self.selectBtn.setGeometry(QtCore.QRect(570, 20, 91, 42))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selectBtn.setFont(font)
        self.selectBtn.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
""))
        self.selectBtn.setIconSize(QtCore.QSize(42, 42))
        self.selectBtn.setObjectName(_fromUtf8("selectBtn"))
        self.listWidget = QtGui.QListWidget(self.fileWidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 150, 291, 231))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget_2 = QtGui.QListWidget(self.fileWidget)
        self.listWidget_2.setGeometry(QtCore.QRect(400, 150, 311, 231))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.label_3 = QtGui.QLabel(self.fileWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.fileWidget)
        self.label_4.setGeometry(QtCore.QRect(370, 120, 51, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_6 = QtGui.QPushButton(self.fileWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 80, 201, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.fileWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(426, 78, 201, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))

        self.pushButton_5.clicked.connect(self.exit_clicked)
        self.selectBtn.clicked.connect(self.select_clicked)
        self.pushButton_6.clicked.connect(self.checkdup_clicked)
        self.listWidget.connect(self.listWidget,
                                QtCore.SIGNAL("currentItemChanged (QListWidgetItem*,QListWidgetItem*)"),
                                self.selectedChanged)

        self.fileMd5 = FileMD5.FileUtil()
        self.fileMd5.process.connect(self.flashProcess)

        self.timer = QtCore.QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.flashTime)  # 计时结束调用operate()方法
        self.timer.start(1000)  # 设置计时间隔并启动

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "文件操作", None))
        self.pushButton_2.setText(_translate("Form", " 聊天室", None))
        self.pushButton_3.setText(_translate("Form", "爬虫", None))
        self.pushButton_4.setText(_translate("Form", "小工具", None))
        self.pushButton_5.setText(_translate("Form", "[退出]", None))
        self.label_7.setText(_translate("Form", "进度条:", None))
        self.label_8.setText(_translate("Form", "信息提示:", None))
        self.tip.setText(_translate("Form", "系统维护中...", None))
        self.label.setText(_translate("Form", "时间:", None))
        self.label_2.setText(_translate("Form", "2017-8-13 09:30:38", None))
        self.selectBtn.setText(_translate("Form", "选择文件", None))
        self.label_3.setText(_translate("Form", "MD5:", None))
        self.label_4.setText(_translate("Form", "文件:", None))
        self.pushButton_6.setText(_translate("Form", "文件查重", None))
        self.pushButton_7.setText(_translate("Form", "清理垃圾", None))

    def mouseMoveEvent(self, QMouseEvent):
        if self.z == QtCore.QPoint(): return
        y = QMouseEvent.globalPos()
        x = y - self.z
        self.move(x)

    def mousePressEvent(self, QMouseEvent):
        #鼠标相对于桌面左上角的位置
        y = QMouseEvent.globalPos()
        #窗口左上角相对于桌面左上角的位置
        x = self.geometry().topLeft()
        #z为定值
        self.z = y - x

    def mouseReleaseEvent(self, QMouseEvent):
        self.z = QtCore.QPoint()

    def exit_clicked(self):
        self.close()

    def select_clicked(self):
        path = QtGui.QFileDialog.getExistingDirectory(self, 'Select Directory', '.')
        self.lineEdit.setText(path)

    def checkdup_clicked(self):
        threading.Thread(target=self.checkdup_thread).start()

    def checkdup_thread(self):
        self.listWidget.clear()
        path = self.lineEdit.text()
        if path:
            self.md5Map = self.fileMd5.ListFilesMD5(path)
            for key in self.md5Map:
                self.listWidget.addItem(key)

    def selectedChanged(self, Item):
        if Item:
            self.listWidget_2.clear()
            md5 = Item.text()
            if md5:
                files = self.md5Map[str(md5)]
                for file in files:
                    self.listWidget_2.addItem(file)

    def flashTime(self):
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.label_2.setText(t)

    def flashProcess(self, cur, total):
        n = float(cur) / float(total) * 100
        p = int(str(n).split('.')[0])
        self.progressBar.setProperty("value", p)


import src.working.res as res
