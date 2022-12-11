from calc import myEval
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import *
import sys
import functions

class MainWindow(QWidget):
    MainWindowTitle = "Калькулятор"

    def __init__(self):
        self.formula = ''
        self.visibleFormula = ''
        super().__init__()
        self.setWindowTitle(self.MainWindowTitle)
        #self.resize(500,500)
        self.setup_ui()
        self.setup_f()

    def setup_ui(self):
        self.main_layout = QGridLayout()
        self.line = QLineEdit('')
        self.main_layout.addWidget(self.line, 0, 0, 1, 4)
        self.btn1 = QPushButton('1')
        self.main_layout.addWidget(self.btn1, 3, 0)
        self.btn2 = QPushButton('2')
        self.main_layout.addWidget(self.btn2, 3, 1)
        self.btn3 = QPushButton('3')
        self.main_layout.addWidget(self.btn3, 3, 2)
        self.btn4 = QPushButton('4')
        self.main_layout.addWidget(self.btn4, 2, 0)
        self.btn5 = QPushButton('5')
        self.main_layout.addWidget(self.btn5, 2, 1)
        self.btn6 = QPushButton('6')
        self.main_layout.addWidget(self.btn6, 2, 2)
        self.btn7 = QPushButton('7')
        self.main_layout.addWidget(self.btn7, 1, 0)
        self.btn8 = QPushButton('8')
        self.main_layout.addWidget(self.btn8, 1, 1)
        self.btn9 = QPushButton('9')
        self.main_layout.addWidget(self.btn9, 1, 2)
        self.btn0 = QPushButton('0')
        self.main_layout.addWidget(self.btn0, 4, 1)
        self.btn_rav = QPushButton('=')
        self.main_layout.addWidget(self.btn_rav, 5, 1)
        self.btn_sin = QPushButton('sin')
        self.main_layout.addWidget(self.btn_sin, 4, 0)
        self.btn_cos = QPushButton('cos')
        self.main_layout.addWidget(self.btn_cos, 4, 2)
        self.btn_tg = QPushButton('tg')
        self.main_layout.addWidget(self.btn_tg, 5, 0)
        self.btn_ctg = QPushButton('ctg')
        self.main_layout.addWidget(self.btn_ctg, 5, 2)
        self.btn_plus = QPushButton('+')
        self.main_layout.addWidget(self.btn_plus, 1, 3)
        self.btn_minus = QPushButton('-')
        self.main_layout.addWidget(self.btn_minus, 2, 3)
        self.btn_mult = QPushButton('*')
        self.main_layout.addWidget(self.btn_mult, 3, 3)
        self.btn_div = QPushButton('/')
        self.main_layout.addWidget(self.btn_div, 4, 3)
        self.btn_left = QPushButton('(')
        self.main_layout.addWidget(self.btn_left, 6, 0)
        self.btn_right = QPushButton(')')
        self.main_layout.addWidget(self.btn_right, 6, 1)
        self.btn_pi = QPushButton('p')
        self.main_layout.addWidget(self.btn_pi, 5, 3)
        self.btn_del = QPushButton("<-")
        self.main_layout.addWidget(self.btn_del, 6, 3)
        self.btn_C = QPushButton("C")
        self.main_layout.addWidget(self.btn_C, 6, 2)
        self.setLayout(self.main_layout)

    def setup_f(self):
        self.btn1.clicked.connect(self.n1)
        self.btn2.clicked.connect(self.n2)
        self.btn3.clicked.connect(self.n3)
        self.btn4.clicked.connect(self.n4)
        self.btn5.clicked.connect(self.n5)
        self.btn6.clicked.connect(self.n6)
        self.btn7.clicked.connect(self.n7)
        self.btn8.clicked.connect(self.n8)
        self.btn9.clicked.connect(self.n9)
        self.btn0.clicked.connect(self.n0)
        self.btn_rav.clicked.connect(self.rav)
        self.btn_mult.clicked.connect(self.mult)
        self.btn_minus.clicked.connect(self.minus)
        self.btn_plus.clicked.connect(self.plus)
        self.btn_div.clicked.connect(self.div)
        self.btn_ctg.clicked.connect(self.ctg)
        self.btn_tg.clicked.connect(self.tg)
        self.btn_sin.clicked.connect(self.sin)
        self.btn_cos.clicked.connect(self.cos)
        self.btn_left.clicked.connect(self.left)
        self.btn_right.clicked.connect(self.right)
        self.btn_pi.clicked.connect(self.pi)
        self.btn_del.clicked.connect(self.remove)
        self.btn_C.clicked.connect(self.clear)
    def n1(self):
        self.formula += '1'
        self.visibleFormula += '1'
        self.line.setText(self.visibleFormula)
    def n2(self):
        self.formula += '2'
        self.visibleFormula += '2'
        self.line.setText(self.visibleFormula)
    def n3(self):
        self.formula += '3'
        self.visibleFormula += '3'
        self.line.setText(self.visibleFormula)
    def n4(self):
        self.formula += '4'
        self.visibleFormula += '4'
        self.line.setText(self.visibleFormula)
    def n5(self):
        self.formula += '5'
        self.visibleFormula += '5'
        self.line.setText(self.visibleFormula)
    def n6(self):
        self.formula += '6'
        self.visibleFormula += '6'
        self.line.setText(self.visibleFormula)
    def n7(self):
        self.formula += '7'
        self.visibleFormula += '7'
        self.line.setText(self.visibleFormula)
    def n8(self):
        self.formula += '8'
        self.visibleFormula += '8'
        self.line.setText(self.visibleFormula)
    def n9(self):
        self.formula += '9'
        self.visibleFormula += '9'
        self.line.setText(self.visibleFormula)
    def n0(self):
        self.formula += '0'
        self.visibleFormula += '0'
        self.line.setText(self.visibleFormula)
    def rav(self):
        self.visibleFormula += '=' + str(myEval(self.formula))
        print(self.formula)
        self.formula += '=' + str(myEval(self.formula))
        self.line.setText(self.visibleFormula)
    def minus(self):
        self.formula += '-'
        self.visibleFormula += '-'
        self.line.setText(self.visibleFormula)
    def plus(self):
        self.formula += '+'
        self.visibleFormula += '+'
        self.line.setText(self.visibleFormula)
    def div(self):
        self.formula += '/'
        self.visibleFormula += '/'
        self.line.setText(self.visibleFormula)
    def mult(self):
        self.formula += '*'
        self.visibleFormula += '*'
        self.line.setText(self.visibleFormula)
    def sin(self):
        self.formula += 's'
        self.visibleFormula += 'sin'
        self.line.setText(self.visibleFormula)
    def cos(self):
        self.formula += 'c'
        self.visibleFormula += 'cos'
        self.line.setText(self.visibleFormula)
    def tg(self):
        self.formula += 't'
        self.visibleFormula += 'tg'
        self.line.setText(self.visibleFormula)
    def ctg(self):
        self.formula += 'C'
        self.visibleFormula += 'ctg'
        self.line.setText(self.visibleFormula)
    def left(self):
        self.formula += '('
        self.visibleFormula += '('
        self.line.setText(self.visibleFormula)
    def right(self):
        self.formula += ')'
        self.visibleFormula += ')'
        self.line.setText(self.visibleFormula)
    def pi(self):
        self.formula += 'p'
        self.visibleFormula += 'p'
    def remove(self):
        self.formula = self.formula[:-1]
        self.visibleFormula = self.visibleFormula[:-1]
        self.line.setText(self.visibleFormula)
    def clear(self):
        self.line.clear()
        self.formula = ''
        self.visibleFormula = ''
        self.line.setText(self.visibleFormula)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())