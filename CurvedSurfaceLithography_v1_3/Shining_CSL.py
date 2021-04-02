# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Shining_CSL.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(977, 536)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 250, 71, 21))
        self.label_10.setObjectName("label_10")
        self.Capillary_length_box = QtWidgets.QSpinBox(self.centralwidget)
        self.Capillary_length_box.setGeometry(QtCore.QRect(120, 250, 91, 22))
        self.Capillary_length_box.setMinimum(-150)
        self.Capillary_length_box.setMaximum(150)
        self.Capillary_length_box.setProperty("value", 10)
        self.Capillary_length_box.setObjectName("Capillary_length_box")
        self.Velocity_box = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Velocity_box.setGeometry(QtCore.QRect(320, 250, 91, 22))
        self.Velocity_box.setMinimum(0.01)
        self.Velocity_box.setMaximum(10.0)
        self.Velocity_box.setProperty("value", 1.0)
        self.Velocity_box.setObjectName("Velocity_box")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(240, 250, 71, 21))
        self.label_11.setObjectName("label_11")
        self.translation_step = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.translation_step.setGeometry(QtCore.QRect(130, 150, 91, 22))
        self.translation_step.setPrefix("")
        self.translation_step.setDecimals(2)
        self.translation_step.setMinimum(0.0)
        self.translation_step.setMaximum(10.0)
        self.translation_step.setProperty("value", 5.0)
        self.translation_step.setObjectName("translation_step")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(130, 120, 71, 21))
        self.label_13.setObjectName("label_13")
        self.RtranslationButton = QtWidgets.QPushButton(self.centralwidget)
        self.RtranslationButton.setGeometry(QtCore.QRect(230, 150, 75, 23))
        self.RtranslationButton.setObjectName("RtranslationButton")
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(40, 100, 75, 23))
        self.reset_button.setObjectName("reset_button")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(40, 290, 75, 23))
        self.start_button.setObjectName("start_button")
        self.on_button = QtWidgets.QPushButton(self.centralwidget)
        self.on_button.setGeometry(QtCore.QRect(40, 10, 75, 23))
        self.on_button.setObjectName("on_button")
        self.off_button = QtWidgets.QPushButton(self.centralwidget)
        self.off_button.setGeometry(QtCore.QRect(240, 330, 75, 23))
        self.off_button.setCheckable(False)
        self.off_button.setAutoDefault(False)
        self.off_button.setObjectName("off_button")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 410, 541, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(650, 80, 271, 41))
        self.textEdit.setObjectName("textEdit")
        self.suspend = QtWidgets.QCheckBox(self.centralwidget)
        self.suspend.setGeometry(QtCore.QRect(250, 300, 71, 16))
        self.suspend.setCheckable(True)
        self.suspend.setChecked(False)
        self.suspend.setObjectName("suspend")
        self.LtranslationButton = QtWidgets.QPushButton(self.centralwidget)
        self.LtranslationButton.setGeometry(QtCore.QRect(40, 150, 75, 23))
        self.LtranslationButton.setObjectName("LtranslationButton")
        self.textEdit2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit2.setGeometry(QtCore.QRect(650, 200, 271, 81))
        self.textEdit2.setObjectName("textEdit2")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(650, 160, 71, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(650, 60, 71, 21))
        self.label_15.setObjectName("label_15")
        self.rotate_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.rotate_spinBox.setGeometry(QtCore.QRect(360, 150, 91, 22))
        self.rotate_spinBox.setPrefix("")
        self.rotate_spinBox.setMaximum(4)
        self.rotate_spinBox.setProperty("value", 1)
        self.rotate_spinBox.setObjectName("rotate_spinBox")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(360, 120, 71, 21))
        self.label_16.setObjectName("label_16")
        self.rotate_state = QtWidgets.QCheckBox(self.centralwidget)
        self.rotate_state.setGeometry(QtCore.QRect(470, 150, 71, 16))
        self.rotate_state.setCheckable(True)
        self.rotate_state.setChecked(False)
        self.rotate_state.setObjectName("rotate_state")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 40, 551, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(40, 180, 551, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(590, 0, 20, 501))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 60, 71, 21))
        self.label_12.setObjectName("label_12")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(40, 200, 71, 21))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(610, 10, 71, 21))
        self.label_18.setObjectName("label_18")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(40, 310, 181, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.Tstart_button = QtWidgets.QPushButton(self.centralwidget)
        self.Tstart_button.setGeometry(QtCore.QRect(40, 360, 75, 23))
        self.Tstart_button.setObjectName("Tstart_button")
        self.readT_button = QtWidgets.QPushButton(self.centralwidget)
        self.readT_button.setGeometry(QtCore.QRect(40, 330, 75, 23))
        self.readT_button.setCheckable(False)
        self.readT_button.setAutoDefault(False)
        self.readT_button.setObjectName("readT_button")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(220, 280, 20, 101))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 977, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "加工长度："))
        self.Capillary_length_box.setToolTip(_translate("MainWindow", "<html><head/><body><p>要加工的毛细管的长度，单位mm</p></body></html>"))
        self.Capillary_length_box.setSuffix(_translate("MainWindow", " mm"))
        self.Velocity_box.setToolTip(_translate("MainWindow", "<html><head/><body><p>水平移动速度，单位mm/s</p></body></html>"))
        self.Velocity_box.setSuffix(_translate("MainWindow", " mm/s"))
        self.label_11.setText(_translate("MainWindow", "平移速度："))
        self.translation_step.setToolTip(_translate("MainWindow", "<html><head/><body><p>指定一个位移，按《移动键》完成移动</p></body></html>"))
        self.translation_step.setSuffix(_translate("MainWindow", " mm"))
        self.label_13.setText(_translate("MainWindow", "移动步长"))
        self.RtranslationButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>点击此按键，向右移动，移动距离为“移动步长”设置距离。</p><p><br/></p></body></html>"))
        self.RtranslationButton.setText(_translate("MainWindow", "右移"))
        self.reset_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>点击此按键，校准并回归零点。</p></body></html>"))
        self.reset_button.setText(_translate("MainWindow", "复位"))
        self.start_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>点击此按键，进行经典加工：按已设定的加工长度、平移速度、旋转速度进行单次连续遍历加工。</p></body></html>"))
        self.start_button.setText(_translate("MainWindow", "开始"))
        self.on_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>点击此按键，启动设备。</p></body></html>"))
        self.on_button.setText(_translate("MainWindow", "启动"))
        self.off_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>点击此按键，结束当前正在执行的加工。</p></body></html>"))
        self.off_button.setText(_translate("MainWindow", "关闭"))
        self.progressBar.setToolTip(_translate("MainWindow", "<html><head/><body><p>加工进度条</p></body></html>"))
        self.suspend.setToolTip(_translate("MainWindow", "<html><head/><body><p>勾选此选项，暂停当前的加工，取消勾选则继续执行加工 。</p></body></html>"))
        self.suspend.setText(_translate("MainWindow", "暂停"))
        self.LtranslationButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>点击此按键，向左移动，移动距离为“移动步长”设置距离。</p><p><br/></p></body></html>"))
        self.LtranslationButton.setText(_translate("MainWindow", "左移"))
        self.label_14.setText(_translate("MainWindow", "串口信号："))
        self.label_15.setText(_translate("MainWindow", "操作反馈："))
        self.rotate_spinBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>旋转速度，单位赫兹，即每秒转动圈数。</p></body></html>"))
        self.rotate_spinBox.setSuffix(_translate("MainWindow", " Hz"))
        self.label_16.setText(_translate("MainWindow", "旋转速度："))
        self.rotate_state.setToolTip(_translate("MainWindow", "<html><head/><body><p>勾选后，旋转电机会按设定速度旋转，案例加工时，请勿勾选。</p></body></html>"))
        self.rotate_state.setText(_translate("MainWindow", "旋转"))
        self.label_12.setText(_translate("MainWindow", "调整区"))
        self.label_17.setText(_translate("MainWindow", "加工区"))
        self.label_18.setText(_translate("MainWindow", "反馈区"))
        self.Tstart_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>点击此按键，按轨迹文件进行加工。</p></body></html>"))
        self.Tstart_button.setText(_translate("MainWindow", "轨迹加工"))
        self.readT_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>点击此按键，读取轨迹文件，轨迹文件格式为csv，文件内数据为3列，无表头。前两列分别为控制旋转与移动的信号，信号有三种：1、2、3，1为左移动或逆时针，2为不动，3为右移或者顺时针转动</p><p><br/></p></body></html>"))
        self.readT_button.setText(_translate("MainWindow", "读取轨迹"))
