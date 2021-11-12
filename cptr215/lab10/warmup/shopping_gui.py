import sys
from PySide6.QtWidgets import QApplication, QListWidgetItem, QMainWindow, QLineEdit, QVBoxLayout, QGroupBox, \
    QHBoxLayout, QWidget, \
    QListWidget, QListWidgetItem, QListView, QGridLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shopping list")
        self.setFixedSize(400, 600)

        self.input = QLineEdit()
        self.input.setFixedWidth(300)

        self.my_list = QListWidget()

        add_item = QPushButton("Add")
        add_item.clicked.connect(self.addListItem())

        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        layout.addWidget(self.input, 0, 0)
        layout.addWidget(add_item, 0, 3)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def addListItem(self):
        # takes content of box
        item = self.input.text()
        self.my_list.addItem(item)
        self.input.setText("")
        print("clicked")

    def removeListItem(self):
        pass


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
