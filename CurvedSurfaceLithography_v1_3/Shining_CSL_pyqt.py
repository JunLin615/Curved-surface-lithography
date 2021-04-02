# -*- coding: utf-8 -*-
"""
@Time:2021/3/2 13:38
@Auth"JunLin615
@File:Shining_CSL_pyqt.py
@IDE:PyCharm
@Motto:With the wind light cloud light mentality, do insatiable things
@email:ljjjun123@gmail.com 
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QThread,pyqtSignal,QDir,QFile,QIODevice
from PyQt5.QtWidgets import QMainWindow, QApplication,QFileDialog
from Shining_CSL import Ui_MainWindow
from P2AStepperMotor import central_control
import win32con
import ctypes
from win32process import SuspendThread, ResumeThread
#import csv
import time


class Thread_start_button(QThread):  # 线程2
    _signal = pyqtSignal()
    _signal2 = pyqtSignal(int)  # 控制进度条

    def __init__(self):
        super().__init__()

    def setIdentity(self, direction,displacement, time_S, A):

        self.direction = direction
        self.displacement = displacement
        self.time_S = int(time_S)
        self.A = A

    def run(self):
        try:
            # 这个目前我没弄明白这里写法
            self.handle = ctypes.windll.kernel32.OpenThread( win32con.PROCESS_ALL_ACCESS, False, int(QThread.currentThreadId()))
        except Exception as e:
            print('get thread handle failed', e)

        self.mains()
        #self.text()#调试用


    def mains(self):
        demo_s = "52{}".format(self.direction)#2号电机转
        demo = bytes(demo_s, encoding="utf8")
        print(demo)

        for i in range(1,abs(self.displacement)+1):
            self.A.ser.write(demo)
            self._signal2.emit(int(100*i/self.displacement))
            self.msleep(self.time_S)
        self._signal.emit()
    def text(self):


        for i in range(1, abs(self.displacement) + 1):
            print(i)
            i = i + 1
            self._signal2.emit(int(100 * i / self.displacement))
            self.msleep(self.time_S)

        self._signal.emit()


class Thread_Tstart_button(QThread):  # 线程2
    _signal = pyqtSignal()
    _signal2 = pyqtSignal(int)  # 控制进度条

    def __init__(self):
        super().__init__()

    def setIdentity(self,A , data):
        self.A = A
        self.data = data


    def run(self):
        try:
            # 这个目前我没弄明白这里写法
            self.handle = ctypes.windll.kernel32.OpenThread( win32con.PROCESS_ALL_ACCESS, False, int(QThread.currentThreadId()))
        except Exception as e:
            print('get thread handle failed', e)

        self.mains()
        #self.text()#调试用


    def mains(self):
        i = 1
        displacement = len(self.data)
        #print(displacement)
        for row in self.data:

            demo_s1 = "51{}".format(row[0])
            demo_s2 = "52{}".format(row[1])
            demo1 = bytes(demo_s1, encoding="utf8")
            demo2 = bytes(demo_s2, encoding="utf8")
            #print(demo1)
            #print(demo2)
            self.A.ser.write(demo1)
            self.msleep(10)

            #print(5)
            self.A.ser.write(demo2)
            self.msleep(int(row[2])-10)
            #print(6)
            self._signal2.emit(int(100 * i / displacement))
            #print(7)
            i=i+1

        self._signal.emit()
    def text(self):


        for i in range(1, abs(self.displacement) + 1):
            print(i)
            i = i + 1
            self._signal2.emit(int(100 * i / self.displacement))
            self.msleep(self.time_S)

        self._signal.emit()

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        demo格式：
        b'1SVVVVFDDDDDE'：byte格式，第一位1，意思是经典加工；第二位对应speed1，旋转速度，单位Hz；
        3-6：共4位，对应velocity2，单位10um/s；7位：+ or -，displacement的正负；8-12：displacement的绝对值，单位10um
        13：E，意味END，命令结束。
        """
        super(MainWindow, self).__init__(parent)#继承父类的构造函数
        self.setupUi(self)
        self.A=central_control()
        #QMetaObject.connectSlotsByName(self)#别加这句话，会导致触发两次
        #self.matplotlibwidget_dynamic.setVisible(False)
        #self.matplotlibwidget_static.setVisible(False)

    @pyqtSlot()
    def on_on_button_clicked(self):
        """
        点击启动按钮
        """
        #print("触发")
        #self.timer = QTimer(self)
        #self.timer.timeout.connect(self.Serial_port_reading)
        #self.timer.start(5000)
        #self.textEdit2.setText("定时器启动")
        self.Lead = 1000#导程
        self.Subdivision2 = 1000#细分
        try:


            #self.A.arduino_on()
            self.A.arduino_initialization()
            self.textEdit.append("已启动")
            self.on_button.setEnabled(False)#启动后设置启动按钮为不可用
            localtime = time.localtime(time.time())
            time_s = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
            s_r = "时间：{}启动程序\n".format(time_s)
            self.logW(s_r)


        except:
            #print("串口启动失败")
            self.textEdit.append("启动失败")
            time_s = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
            s_r = "时间：{}启动程序失败\n".format(time_s)
            self.logW(s_r)



    @pyqtSlot()
    def on_off_button_clicked(self):
        """
        点击关闭按钮
        """
        try:
            #self.A.arduino_off()
            ctypes.windll.kernel32.TerminateThread(self.thread.handle, 0)
            self.textEdit.setText("已关闭")
            #self.timer.stop()
            self.textEdit2.setText(" ")
            self.on_button.setEnabled(True)#关闭后设置启动按钮为可用。
            self.start_button.setEnabled(True)
            self.progressBar.setValue(0)

            localtime = time.localtime(time.time())
            time_s = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
            s_r = "时间：{}，手动关闭加工\n".format(time_s)
            self.logW(s_r)
            self.start_button.setEnabled(True)
            self.Tstart_button.setEnabled(True)
            self.LtranslationButton.setEnabled(True)
            self.RtranslationButton.setEnabled(True)
            self.reset_button.setEnabled(True)

        except:
            self.textEdit.setText("关闭失败")
            localtime = time.localtime(time.time())
            time_s = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
            s_r = "时间：{}，手动关闭加工失败\n".format(time_s)
            self.logW(s_r)
    @pyqtSlot()
    def on_reset_button_clicked(self):
        """
        点击复位按钮
        """
        try:
            demo =b"0"#0是复位
            self.A.ser.write(demo)
            self.textEdit2.setText(" ")
        except:
            pass

    @pyqtSlot()
    def on_Serial_Edit_editingFinished(self):
        """
        输入串口号并完成
        """
        try:
            self.A.Serial_port_number = self.Serial_Edit.text()

        except:
            pass

    @pyqtSlot()
    def on_start_button_clicked(self):
        """
        点击开始按钮
        """

        try:

            self.start_button.setEnabled(False)
            self.Tstart_button.setEnabled(False)
            self.LtranslationButton.setEnabled(False)
            self.RtranslationButton.setEnabled(False)
            self.reset_button.setEnabled(False)
            self.parameter = "长度：{}mm,平移速度{}mm/s,旋转速度{}Hz".format(self.Capillary_length_box.value(),
                                                                  self.Velocity_box.value(),
                                                                  self.rotate_spinBox.value())

            displacement = self.Capillary_length_box.value() * 100  # displacement平移距离，单位10um,300mm=30000*10um
            if displacement < 0:
                direction = "1"  # 左移
            elif displacement > 0:
                direction = "3"  # 右移
            #demo = bytes(demo_s, encoding="utf8")
            #self.A.ser.write(demo)
            QThread.msleep(500)
            velocity2 = self.Velocity_box.value() * 100  # 平移速度
            time_S = 1000 / velocity2
            #print(displacement)
            #print(time_S)
            self.thread = Thread_start_button()
            self.thread.setIdentity(direction,displacement, int(time_S),self.A)
            self.thread._signal2.connect(self.progress_bar_control)
            self.thread._signal.connect(self.start_button_end)
            self.thread.start()
            self.textEdit2.setText("加工线程开启")
            localtime = time.localtime(time.time())
            time_s = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
            s_r = "时间：{}参数（{}）开始执行\n".format(time_s, self.parameter)
            self.logW(s_r)

        except:

            self.start_button.setEnabled(True)
            self.Tstart_button.setEnabled(True)
            self.LtranslationButton.setEnabled(True)
            self.RtranslationButton.setEnabled(True)
            self.reset_button.setEnabled(True)

            self.textEdit.setText("开始加工失败")
            localtime = time.localtime(time.time())
            time_s = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
            s_r = "时间：{}参数（{}）加工执行失败\n".format(time_s, self.parameter)
            self.logW(s_r)

    @pyqtSlot(int)#stateChanged的信号是int模式，所以这里需要加int，否则不响应，不要删。
    def on_suspend_stateChanged(self):
        """
        暂停控制
        """
        if self.suspend.isChecked():
            try:

                SuspendThread(self.thread.handle)
                self.textEdit2.setText("加工线程暂停")
                print("暂停")
                localtime = time.localtime(time.time())
                time_s = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
                s_r = "时间：{}，加工暂停\n".format(time_s)
                self.logW(s_r)
            except:
                self.textEdit.setText("暂停失败")
                self.suspend.setChecked(False)
        else:
            try:
                ResumeThread(self.thread.handle)
                self.textEdit2.setText("加工线程开启")
                print("取消暂停")
                localtime = time.localtime(time.time())
                time_s = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
                s_r = "时间：{}，取消暂停\n".format(time_s)
                self.logW(s_r)
            except:
                self.textEdit.setText("取消暂停失败")
                self.suspend.setChecked(True)


    @pyqtSlot(int)#stateChanged的信号是int模式，所以这里需要加int，否则不响应，不要删。
    def on_rotate_state_stateChanged(self):
        """
        旋转控制
        """
        if self.rotate_state.isChecked():

            try:
                speed1 = self.rotate_spinBox.value()
                #print(speed1)
                speed1_s = make_up(1, int(speed1))
                #print(speed1_s)
                demo_s = "4{}".format(speed1_s)#0是旋转
                demo = bytes(demo_s, encoding="utf8")
                #print(demo)
                self.A.ser.write(demo)
                self.textEdit.setText("开启旋转")
                self.textEdit2.setText("send out {}".format(demo))
                #print("暂停")
            except:
                self.textEdit.setText("开启旋转失败")
                self.suspend.setChecked(False)
        else:
            try:
                demo_s = "40"#40是取消旋转
                demo = bytes(demo_s, encoding="utf8")
                #print(demo)
                self.A.ser.write(demo)
                self.textEdit.setText("取消旋转")
                self.textEdit2.setText("send out {}".format(demo))
                #print("取消暂停")
            except:
                self.textEdit.setText("取消旋转失败")
                self.suspend.setChecked(True)

    @pyqtSlot()
    def on_LtranslationButton_clicked(self):
        """
        点击左移按钮
        """
        self.LtranslationButton.setEnabled(False)  #锁定
        self.RtranslationButton.setEnabled(False)  # 锁定
        try:

            speed1 = 0  # 旋转速度
            #velocity2 = 10 * 100  # 平移速度
            #delayu = int(1e6/(velocity2/self.Lead*self.Subdivision2*2))
            delayu = int(500)#速度10mm/s
            displacement = self.translation_step.value() * 100*(-1)  # displacement平移距离，单位10um,300mm=30000*10um

            Steps = displacement / self.Lead * self.Subdivision2
            time_s=int(Steps*delayu*2*1e-3+1)


            speed1_s = make_up(1, int(speed1))
            delayu_s = make_up(5, int(delayu))
            displacement_s = make_up_symbol(6, int(displacement))

            demo_s = "1{}{}{}E".format(speed1_s, delayu_s, displacement_s)
            demo = bytes(demo_s, encoding="utf8")
            print(demo)
            self.A.ser.write(demo)
            self.textEdit.setText("开始移动")
            self.textEdit2.setText(" ")
            QThread.msleep(time_s)

        except:
            self.textEdit.setText("移动失败")
            QThread.msleep(1000)

        self.LtranslationButton.setEnabled(True)  # 解除锁定
        self.RtranslationButton.setEnabled(True)  # 解除锁定

    @pyqtSlot()
    def on_RtranslationButton_clicked(self):
        """
        点击右移按钮
        """
        self.LtranslationButton.setEnabled(False)  # 锁定
        self.RtranslationButton.setEnabled(False)  #锁定
        try:

            speed1 = 0  # 旋转速度
            #velocity2 = 10 * 100  # 平移速度
            #delayu = int(1e6/(velocity2/self.Lead*self.Subdivision2*2))
            delayu = int(500)#速度10mm/s
            displacement = self.translation_step.value() * 100  # displacement平移距离，单位10um,300mm=30000*10um

            Steps = displacement / self.Lead * self.Subdivision2
            time_s=int(Steps*delayu*2*1e-3+1)


            speed1_s = make_up(1, int(speed1))
            delayu_s = make_up(5, int(delayu))
            displacement_s = make_up_symbol(6, int(displacement))

            demo_s = "1{}{}{}E".format(speed1_s, delayu_s, displacement_s)
            demo = bytes(demo_s, encoding="utf8")
            print(demo)
            self.A.ser.write(demo)
            self.textEdit.setText("开始移动")
            self.textEdit2.setText(" ")
            QThread.msleep(time_s)

        except:
            self.textEdit.setText("移动失败")
            QThread.msleep(1000)

        self.LtranslationButton.setEnabled(True)  # 解除锁定
        self.RtranslationButton.setEnabled(True)  # 解除锁定

    @pyqtSlot()
    def on_readT_button_clicked(self):
        """
        读取轨迹文件
        """
        print("文件读取")

        self.load_text()


    @pyqtSlot()
    def on_Tstart_button_clicked(self):
        """
        点击轨迹加工按钮
        """

        try:

            self.start_button.setEnabled(False)
            self.Tstart_button.setEnabled(False)
            self.LtranslationButton.setEnabled(False)
            self.RtranslationButton.setEnabled(False)
            self.reset_button.setEnabled(False)


            #print(displacement)
            #print(time_S)

            self.thread = Thread_Tstart_button()
            print(1)
            self.thread.setIdentity(self.A, self.data)
            print(2)
            self.thread._signal2.connect(self.progress_bar_control)
            print(3)
            self.thread._signal.connect(self.Kstart_button_end)
            print(4)
            self.thread.start()
            self.textEdit2.setText("加工线程开启")

            localtime = time.localtime(time.time())
            time_s = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
            s_r = "时间：{}执行文件:{}\n".format(time_s, self.filenames)
            self.logW(s_r)

        except:

            self.start_button.setEnabled(True)
            self.Tstart_button.setEnabled(True)
            self.LtranslationButton.setEnabled(True)
            self.RtranslationButton.setEnabled(True)
            self.reset_button.setEnabled(True)

            self.textEdit.setText("开始加工失败")

            localtime = time.localtime(time.time())
            time_s = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
            s_r = "时间：{}文件:{}执行失败\n".format(time_s, self.filenames)
            self.logW(s_r)

    def Serial_port_reading(self):
        """
        计时器定时读取串口
        """
        try:

            s = self.A.ser.readline()
            self.textEdit2.setText(s)
            self.textEdit.setText("正在读取串口")

        except:
            self.textEdit.setText("读取串口失败")

    def lock_all_buttons(self,state):
        #self.on_button.setEnabled(state)  # 启动后设置启动按钮为不可用
        self.off_button.setEnabled(state)  # 设置关闭按钮状态
        self.reset_button.setEnabled(state)  # 设置复位按钮状态
        self.on_button.setEnabled(state)  # 启动后设置启动按钮为不可用
        self.on_button.setEnabled(state)  # 启动后设置启动按钮为不可用
        self.on_button.setEnabled(state)  # 启动后设置启动按钮为不可用
        self.on_button.setEnabled(state)  # 启动后设置启动按钮为不可用

    def progress_bar_control(self, progress):

        """
        进度条控制
        """
        self.progressBar.setValue(progress)

    def start_button_end(self):
        self.thread.terminate()
        self.start_button.setEnabled(True)
        self.Tstart_button.setEnabled(True)
        self.LtranslationButton.setEnabled(True)
        self.RtranslationButton.setEnabled(True)
        self.reset_button.setEnabled(True)
        self.textEdit2.setText("加工线程结束")
        localtime = time.localtime(time.time())
        time_s  =time.strftime("%Y-%m-%d %H:%M:%S",localtime)
        s_r = "时间：{}参数({})加工结束\n".format(time_s,self.parameter)
        self.logW(s_r)

    def Kstart_button_end(self):
        self.thread.terminate()
        self.start_button.setEnabled(True)
        self.Tstart_button.setEnabled(True)
        self.LtranslationButton.setEnabled(True)
        self.RtranslationButton.setEnabled(True)
        self.reset_button.setEnabled(True)
        self.textEdit2.setText("加工线程结束")

        localtime = time.localtime(time.time())
        time_s  =time.strftime("%Y-%m-%d %H:%M:%S",localtime)
        s_r = "时间：{}文件:{}执行结束\n".format(time_s,self.filenames)
        self.logW(s_r)

    def load_text(self):
        print("load--csv")
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        if dlg.exec_():
          self.filenames = dlg.selectedFiles()
          print(self.filenames)
          fileDevice = QFile(self.filenames[0])

        if not fileDevice.open(QIODevice.ReadOnly | QIODevice.Text):
          return False
        #f = open(filenames[0], 'r')
        data = []
        #try:
        #print(fileDevice.atEnd())
        while not fileDevice.atEnd():
          #print("a")

          qtBytes = fileDevice.readLine()
          pyBytes = bytes(qtBytes.data())  # QByteArray转换为bytes类型
          lineStr = pyBytes.decode("UTF-8-sig")  # bytes转换为str型
          lineStr = lineStr.strip()  # 去除结尾增加的空行
          data.append(lineStr.split(","))  # 返回QByteArray类型
          #print(qtBytes)
        self.data = data
        print(data[0])
        fileDevice.close()

        localtime = time.localtime(time.time())
        time_s  =time.strftime("%Y-%m-%d %H:%M:%S",localtime)
        s_r = "时间：{}读取文件:{}\n".format(time_s,self.filenames)
        self.logW(s_r)
        #finally:
        #    print("b")
            #self.textEdit2.setText(data)
        self.textEdit.setText("读取成功")

    def logW(self,s_r):
        f = open('C:/日志.txt',"a")
        f.write(s_r)
        f.close()



def make_up_symbol(n,s):
    #补齐函数，带符号，将s补齐0至n位
    b = "%+d" % (s)
    other_url = b.zfill(n)
    return other_url
def make_up(n,s):
    # 补齐函数，不带符号，将s补齐0至n位
    b = str(s)
    other_url = b.zfill(n)
    return other_url


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())