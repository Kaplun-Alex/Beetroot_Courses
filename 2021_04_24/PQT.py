from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize
import random
from functools import partial

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_windows()
        self.cpu_box = QLabel(self)
        self.cpu_box.setGeometry(100, 100, 150, 150)
        self.user_box = QLabel(self)
        self.user_box.setGeometry(400, 100, 150, 150)
        self.int_part = QLabel('0', self)
        self.int_part.setGeometry(100, 1, 65, 20)


    def setup_windows(self):
        int_part = QLabel('0', self)
        int_part.setGeometry(100, 1, 65, 20)
        int_wins = QLabel('0', self)
        int_wins.setGeometry(100, 16, 65, 20)
        int_loose = QLabel('0', self)
        int_loose.setGeometry(100, 31, 65, 20)
        button_list = []
        label_list = []
        b_exit = QPushButton('EXIT', self)
        b_exit.setGeometry(460, 330, 100, 50)
        b_exit.clicked.connect(self.close)
        b_stone = QPushButton(self)
        b_stone.clicked.connect(partial(self.cpu_chooser, 1, int_part, int_wins, int_loose))
        b_scissors = QPushButton(self)
        b_scissors.clicked.connect(partial(self.cpu_chooser, 2,  int_part, int_wins, int_loose))
        b_paper = QPushButton(self)
        b_paper.clicked.connect(partial(self.cpu_chooser, 3,  int_part, int_wins, int_loose))
        b_lizard = QPushButton(self)
        b_lizard.clicked.connect(partial(self.cpu_chooser, 4,  int_part, int_wins, int_loose))
        b_spoke = QPushButton(self)
        b_spoke.clicked.connect(partial(self.cpu_chooser, 5,  int_part, int_wins, int_loose))
        button_list.append(b_exit)
        button_list.append(b_stone)
        button_list.append(b_scissors)
        button_list.append(b_paper)
        button_list.append(b_lizard)
        button_list.append(b_spoke)
        for i in button_list:
            i.setStyleSheet('QPushButton {background-color: #ffffff; color: red;}')
            i.setIconSize(QSize(100, 48))
        b_stone.setGeometry(20, 250, 90, 60)
        b_stone.setIcon(QIcon('stone.jpg'))
        b_scissors.setGeometry(130, 250, 90, 60)
        b_scissors.setIcon(QIcon('sc.jpg'))
        b_paper.setGeometry(240, 250, 90, 60)
        b_paper.setIcon(QIcon('paper.jpg'))
        b_lizard.setGeometry(350, 250, 90, 60)
        b_lizard.setIcon(QIcon('lizard.jpg'))
        b_spoke.setGeometry(460, 250, 90, 60)
        b_spoke.setIcon(QIcon('spok.jpg'))

        l_part = QLabel('Партий:', self)
        l_part.setGeometry(1, 1, 65, 20)
        l_wins = QLabel('Побед:', self)
        l_wins.setGeometry(1, 16, 65, 20)
        l_loose = QLabel('Поражений:', self)
        l_loose.setGeometry(1, 31, 65, 20)

        int_cpu = QLabel('CPU', self)
        int_cpu.setGeometry(140, 110, 65, 20)
        int_user = QLabel('USER', self)
        int_user.setGeometry(440, 110, 65, 20)

        self.setGeometry(200, 200, 600, 400)
        self.setWindowTitle('Играем на репаны!')
        self.show()

    def cpu_chooser(self, obj, int_part, int_wins, int_loose):
        cpu_dict = {1: 'stone.jpg', 2: 'sc.jpg', 3: 'paper.jpg', 4: 'lizard.jpg', 5: 'spok.jpg'}
        cc = random.randint(1, 5)
        self.cpu_box.clear()
        self.user_box.clear()
        self.cpu_box.setPixmap(QPixmap(cpu_dict[cc]))
        self.user_box.setPixmap(QPixmap(cpu_dict[obj]))
        self.cpu_box.show()
        self.user_box.show()
        count_part = int(int_part.text())
        count_wins = int(int_wins.text())
        count_loose = int(int_loose.text())
        int_part.setText(str(count_part + 1))

        playerwins = []
        cpuwinsins = []
        if obj == 1 and (cc == 3 or cc == 5):
            print("Player loose.")
            int_loose.setText(str(count_loose + 1))
            playerwins.append(1)
        elif obj == 2 and (cc == 1 or cc == 5):
            print("Player loose.")
            int_loose.setText(str(count_loose + 1))
            playerwins.append(1)
        elif obj == 3 and (cc == 2 or cc == 4):
            print("Player loose.")
            int_loose.setText(str(count_loose  + 1))
            playerwins.append(1)
        elif obj == 4 and (cc == 2 or cc == 1):
            print("Player loose.")
            int_loose.setText(str(count_loose + 1))
            playerwins.append(1)
        elif obj == 5 and (cc == 4 or cc == 3):
            print("Player loose.")
            int_loose.setText(str(count_loose + 1))
            playerwins.append(1)
        elif obj == cc:
            print("==========")
        else:
            print("WIN")
            int_wins.setText(str(count_wins + 1))
            cpuwinsins.append(1)
        f = open('game.txt', 'a',)
        f.write('Win: ' + str(count_wins) + '///' +'Loose: ' + str(count_loose) + '\n')
        f.close()
        return cc, obj

def run():
    app = QApplication([])
    mw = MyWindow()
    app.exec_()


if __name__ == '__main__':
    run()
