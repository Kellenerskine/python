# import sys
# from PySide2.QtWidgets import (
#     QMainWindow, QApplication, QDial,
#     QLabel, QCheckBox, QComboBox, QLineEdit,
#     QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
# )
# from PySide2.QtCore import Qt
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         widget = QDial()
#         widget.setRange(-10, 100)
#         widget.setSingleStep(0.5)
#
#         widget.valueChanged.connect(self.value_changed)
#         widget.sliderMoved.connect(self.slider_position)
#         widget.sliderPressed.connect(self.slider_pressed)
#         widget.sliderReleased.connect(self.slider_released)
#
#         self.setCentralWidget(widget)
#
#     def value_changed(self, i):
#         print(i)
#
#     def slider_position(self, p):
#         print("position", p)
#
#     def slider_pressed(self):
#         print("Pressed!")
#
#     def slider_released(self):
#         print("Released")
#
#
# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec_()

import sys

from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import(
    QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout,
    QPushButton, QWidget, QLabel
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World!")
        text = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(text)
        button = QPushButton("Greet Me!")
        button.clicked.connect(self.greet())
        label = QLabel("message here")

        layout = QVBoxLayout()
        layout.addWidget(text)
        layout.addWidget(button)
        layout.addWidget(label)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def greet(self):
        print("Greetings")

app = QApplication()
window = MainWindow()
window.show()
app.exec_()
