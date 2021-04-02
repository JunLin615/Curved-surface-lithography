# -*- coding: utf-8 -*-
"""
@Time:2021/3/2 14:16
@Auth"JunLin615
@File:P2AStepperMotor.py
@IDE:PyCharm
@Motto:With the wind light cloud light mentality, do insatiable things
@email:ljjjun123@gmail.com 
"""
import serial
class central_control(object):
    def __init__(self):
        """
        中控程序
        """
        self.Serial_port_number = "COM3"
        self.Baud_rate = 9600


        pass
    def arduino_on(self):
        #self.ser = serial.Serial(self.Serial_port_number, self.Baud_rate, timeout=60)
        self.ser.open()
    def arduino_initialization(self):
        self.ser = serial.Serial(self.Serial_port_number, self.Baud_rate, timeout=60)
        # self.ser.open()

    def arduino_off(self):

        self.ser.close()