import sys
from PySide6 import QtWidgets
from PySide6.QtGui import QFont
from PySide6.QtWidgets import *


# QApplication, QLabel, QMainWindow, QLineEdit, QWidget, QListWidget, QGridLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # sets a window of fixed size for the app
        self.setWindowTitle("Bible Statistics")
        self.setFixedSize(400, 600)

        # TODO: add dropdown boxes for version, book, and chapter

        # creates a textbox that can be typed in
        self.input = QLineEdit()

        # creates button that calls the addListItem function when clicked
        add_item = QPushButton("Search")
        add_item.clicked.connect(self.search_bible)

        # this section of code creates a title for the app and makes the app visible
        self.text = QLabel(text="Bible Statistics")
        self.text.setIndent(150)
        self.text.setFont(QFont("Times", weight=QFont.Bold))
        self.text.show()

        self.version_selector = QLabel(text="Versions: ")
        self.book_selector = QLabel(text="Books: ")
        self.chapter_selector = QLabel(text="Chapters: ")

        self.version = QComboBox()
        self.version.addItems(["NIV", "KJV", "NKJV", "MSG"])
        self.version.currentIndexChanged.connect(self.version_select)

        # creates an instance of QGridLayout which can be used to position widgets within a window
        layout = QGridLayout()
        # adding widgets with specific positions
        layout.addWidget(self.text, 1, 0)
        layout.addWidget(self.version_selector, 2, 0)
        layout.addWidget(self.version, 2, 1)
        layout.addWidget(self.book_selector, 3, 0)
        # layout.addWidget(self.book, 3, 1)
        # layout.addWidget(self.)

        # TODO: add the rest of the drop downs

        layout.addWidget(self.input, 3, 0)
        layout.addWidget(add_item, 3, 1)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def version_select(self, i):
        print("Items in the list are: ")

        for count in range(self.version.count()):
            print(self.version.itemText(count))
        print(f"Current index {i} selection changed {self.version.currentText()}")

    def search_bible(self):
        # this function should scrape the bible.com website for the specified text
        pass


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
