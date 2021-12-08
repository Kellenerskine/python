import sys
import requests
from PySide6.QtGui import QFont
from PySide6.QtWidgets import *
from bs4 import BeautifulSoup


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
        search = QPushButton("Search")
        search.clicked.connect(self.search_bible)

        stats = "random stuff"

        # this section of code creates a title for the app and makes the app visible
        self.text = QLabel(text="Bible Statistics")
        self.text.setIndent(150)
        self.text.setFont(QFont("Times", weight=QFont.Bold))
        self.text.show()

        self.version_selector = QLabel(text="Versions: ")
        self.book_selector = QLabel(text="Books: ")
        self.chapter_selector = QLabel(text="Chapters: ")
        self.search_word = QLabel(text="Search word here: ")
        self.filler = QLabel(text="")
        self.stats = QLabel(text=stats)
        # adds the version selector dropdown
        self.version = QComboBox()
        self.version.addItems(["NIV", "KJV", "NKJV", "MSG"])
        self.version.currentIndexChanged.connect(self.version_select)

        # adds the book selector drop down
        self.book = QComboBox()
        self.book.addItems([
            "Genesis",
            "Exodus",
            "Leviticus",
            "Numbers",
            "Deuteronomy",
            "Joshua",
            "Judges",
            "Ruth",
            "1 Samuel",
            "2 Samuel",
            "1 Kings",
            "2 Kings",
            "1 Chronicles",
            "2 Chronicles",
            "Ezra",
            "Nehemiah",
            "Esther",
            "Job",
            "Psalms",
            "Proverbs",
            "Ecclesiastes",
            "Song of Songs",
            "Isaiah",
            "Jeremiah",
            "Lamentations",
            "Ezekiel",
            "Daniel",
            "Hosea",
            "Joel",
            "Amos",
            "Obadiah",
            "Jonah",
            "Micah",
            "Nahum",
            "Habakkuk",
            "Zephaniah",
            "Haggai",
            "Zechariah",
            "Malachi",
            "Matthew",
            "Mark",
            "Luke",
            "John",
            "Acts",
            "Romans",
            "1 Corinthians",
            "2 Corinthians",
            "Galatians",
            "Ephesians",
            "Philippians",
            "Colossians",
            "1 Thessalonians",
            "2 Thessalonians",
            "1 Timothy",
            "2 Timothy",
            "Titus",
            "Philemon",
            "Hebrews",
            "James",
            "1 Peter",
            "2 Peter",
            "1 John",
            "2 John",
            "3 John",
            "Jude",
            "Revelation"
        ])
        self.book.currentIndexChanged.connect(self.book_select)

        # adds the chapter selector drop down
        self.chapter = QComboBox()
        # TODO: add a loop to populate the dropdown with proper amount of chapters
        self.chapter.addItems(["1", "2", "3", "4", "5"])
        self.book.currentIndexChanged.connect(self.chapter_select)

        # creates an instance of QGridLayout which can be used to position widgets within a window
        layout = QGridLayout()
        # adding widgets with specific positions
        layout.addWidget(self.text, 0, 0)
        layout.addWidget(self.version_selector, 1, 0)
        layout.addWidget(self.version, 1, 1)
        layout.addWidget(self.book_selector, 2, 0)
        layout.addWidget(self.book, 2, 1)
        layout.addWidget(self.chapter, 3, 1)
        layout.addWidget(self.chapter_selector, 3, 0)

        layout.addWidget(self.input, 5, 1)
        layout.addWidget(self.search_word, 5, 0)
        layout.addWidget(search, 6, 1)
        layout.addWidget(self.filler, 6, 0)
        layout.addWidget(self.stats, 7, 0)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def version_select(self, i):
        print("Items in the list are: ")

        for count in range(self.version.count()):
            print(self.version.itemText(count))
        print(f"Current index {i} selection changed {self.version.currentText()}")

    def book_select(self, i):
        print("Items in the list are: ")

        for count in range(self.book.count()):
            print(self.book.itemText(count))
        print(f"Current index {i} selection changed {self.book.currentText()}")

    def chapter_select(self, i):
        print("Items in the list are: ")

        for count in range(self.chapter.count()):
            print(self.chapter.itemText(count))
        print(f"Current index {i} selection changed {self.chapter.currentText()}")

    def search_bible(self):
        # this function should scrape the bible.com website for the specified text
        x = requests.get('https://www.bible.com/bible/111/GEN.1.NIV')
        num_times = 0
        soup = BeautifulSoup(x.content, "html.parser")
        print(soup)
        for i in soup:
            if self.input.text() == i:
                num_times += 1
        print(num_times)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
