from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.index = QLabel(txt_index)
        self.result = QLabel(txt_workheart)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index,
        alignment = Qt.AlignCenter)
        self.layout.addWidget(self.result,
        alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

app = QApplication([])
main_win = FinalWin()
app.exec_()