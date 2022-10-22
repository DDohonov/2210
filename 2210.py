from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
                    QApplication, 
                    QWidget,
                    QPushButton,
                    QLabel,
                    QVBoxLayout,
                    QHBoxLayout )
app = QApplication([])
window = QWidget()                    
window.resize(360, 500)
window.setWindowTitle("Калькулятор")


main_layout = QVBoxLayout()
h1_layout = QHBoxLayout()
h2_layout = QHBoxLayout()
h3_layout = QHBoxLayout()
h4_layout = QHBoxLayout()
h5_layout = QHBoxLayout()
h6_layout = QHBoxLayout()

total = QLabel('')
h1_layout.addWidget(total, alignment= Qt.AlignCenter)

button_C = QPushButton('C')
button_AC = QPushButton('AC')
button_percent = QPushButton('%')
button_devision = QPushButton('/')
button_multi = QPushButton('*') # 2
button_minus = QPushButton('-') # 3
button_plus = QPushButton('+') # 4
button_dot = QPushButton('.') # 6
button_equals = QPushButton('=') # 6



h2_layout.addWidget(button_C)
h2_layout.addWidget(button_AC)
h2_layout.addWidget(button_percent)
h2_layout.addWidget(button_devision)
numbers = []
for number in range(10):
    numbers.append(QPushButton(str(number)))

k = 1
h6_layout.addWidget(numbers[0])
for  i in range(3):
    h5_layout.addWidget(numbers[k])
    k += 1
for i in range(3):
    h4_layout.addWidget(numbers[k])
    k += 1  
for i in range(3):
    h3_layout.addWidget(numbers[k])
    k += 1

h3_layout.addWidget(button_multi)
h4_layout.addWidget(button_minus)
h5_layout.addWidget(button_plus)
h6_layout.addWidget(button_dot)
h6_layout.addWidget(button_equals)

main_layout.addLayout(h1_layout)
main_layout.addLayout(h2_layout)
main_layout.addLayout(h3_layout)
main_layout.addLayout(h4_layout)
main_layout.addLayout(h5_layout)
main_layout.addLayout(h6_layout)


window.setLayout(main_layout)
window.show()
app.exec_()
