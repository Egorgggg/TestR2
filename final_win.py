from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout
from instr import *

class FinalWin(QWidget):
    def __init__(self,age,t1,t2,t3):
        super().__init__()
        self.set_appear()
        self.age = age
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.index2 = 4 * ((int(self.t1) + int(self.t2) + int(self.t3))-200)/10
        self.initUI()
        self.show() 
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)

    def initUI(self):
        self.index = QLabel(txt_index + str(self.index2))
        self.result = QLabel(txt_workheart + str(self.result_r()))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index,
        alignment = Qt.AlignCenter)
        self.layout.addWidget(self.result,
        alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def p_r(self):                              #Pre_result
        k = int(self.age)
        if k >= 15:
            return 0
        if 13 <= k <= 14:
            return 1
        if 11 <= k <= 12:
            return 2
        if 9 <= k <= 10:
            return 3
        if 7 <= k <= 8:
            return 4     

    def result_r(self):
        k = self.index2
        d = self.p_r()
        if k >= 15 + 1.5*d:
            return txt_res1
        elif (11 + 1.5*d) <= k <= (14.9 + 1.5*d):             
            return txt_res2
        elif (6 + 1.5*d) <= k <= (10,9 + 1.5*d):
            return txt_res3
        elif (11 + 1.5*d) <= k <= (15,9 + 1.5*d): 
            return txt_res4
        elif (11 + 1.5*d) <= k <= (14,9 + 1.5 * d):
            return txt_res5

    def print_k(self):
        return self.index2                  
