import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QListWidget, QListWidgetItem, QListView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shopping list")
        self.input = QLineEdit()
        self.input.setFixedWidth(200)
        self.setFixedSize(400, 600)

        layout = QVBoxLayout()
        layout.addWidget(self.input)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def addListItem(self):
        items = [4, 5, 7]
        listWidget = QListWidget(self)
        listWidget.show()
        listWidget.addItem(items)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
