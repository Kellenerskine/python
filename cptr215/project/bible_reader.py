import requests
from PySide6.QtWidgets import *
from bs4 import BeautifulSoup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.book_chosen = ""
        self.chapter_chosen = ""
        self.version_chosen = ""
        self.num_times = 0

        # sets a window of fixed size for the app
        self.setWindowTitle("Bible Statistics")
        self.setFixedSize(500, 200)

        # creates a textbox that can be typed in
        self.input = QLineEdit()

        # creates button that calls the addListItem function when clicked
        search = QPushButton("Search")
        search.clicked.connect(self.search_bible)

        # this section of code creates a title for the app and makes the app visible

        self.version_selector = QLabel(text="Versions: ")
        self.book_selector = QLabel(text="Books: ")
        self.chapter_selector = QLabel(text="Chapters: ")
        self.search_word = QLabel(text="Search word here: ")
        self.filler = QLabel(text="Number of times the word appears: ")

        # adds the version selector dropdown
        self.version = QComboBox()
        self.version.addItems(["NIV", "KJV", "NKJV", "MSG", "MEV", "NLV", "TLB"])

        # adds the book selector drop down
        self.book_dict = {
            "N/A": 0,
            "Genesis": 50,
            "Exodus": 40,
            "Leviticus": 27,
            "Numbers": 36,
            "Deuteronomy": 34,
            "Joshua": 24,
            "Judges": 21,
            "Ruth": 4,
            "1 Samuel": 31,
            "2 Samuel": 24,
            "1 Kings": 22,
            "2 Kings": 25,
            "1 Chronicles": 29,
            "2 Chronicles": 36,
            "Ezra": 10,
            "Nehemiah": 13,
            "Esther": 10,
            "Job": 42,
            "Psalm": 150,
            "Proverbs": 31,
            "Ecclesiastes": 12,
            "Song of Songs": 8,
            "Isaiah": 66,
            "Jeremiah": 52,
            "Lamentations": 5,
            "Ezekiel": 48,
            "Daniel": 12,
            "Hosea": 14,
            "Joel": 3,
            "Amos": 9,
            "Obadiah": 1,
            "Jonah": 4,
            "Micah": 7,
            "Nahum": 3,
            "Habakkuk": 3,
            "Zephaniah": 3,
            "Haggai": 2,
            "Zechariah": 14,
            "Malachi": 4,
            "Matthew": 28,
            "Mark": 16,
            "Luke": 24,
            "John": 21,
            "Acts": 28,
            "Romans": 28,
            "1 Corinthians": 16,
            "2 Corinthians": 13,
            "Galatians": 6,
            "Ephesians": 6,
            "Philippians": 4,
            "Colossians": 4,
            "1 Thessalonians": 5,
            "2 Thessalonians": 3,
            "1 Timothy": 6,
            "2 Timothy": 4,
            "Titus": 3,
            "Philemon": 1,
            "Hebrews": 13,
            "James": 5,
            "1 Peter": 5,
            "2 Peter": 3,
            "1 John": 5,
            "2 John": 1,
            "3 John": 1,
            "Jude": 1,
            "Revelation": 22
        }
        self.book = QComboBox()

        for i in self.book_dict:
            self.book.addItem(i)
        self.book.currentIndexChanged.connect(self.book_changed)

        # adds the chapter selector drop down
        self.chapter = QComboBox()

        # creates an instance of QGridLayout which can be used to position widgets within a window
        layout = QGridLayout()
        # adding widgets with specific positions
        layout.addWidget(self.version_selector, 1, 0)
        layout.addWidget(self.version, 1, 1)
        layout.addWidget(self.book_selector, 2, 0)
        layout.addWidget(self.book, 2, 1)
        layout.addWidget(self.chapter, 3, 1)
        layout.addWidget(self.chapter_selector, 3, 0)

        layout.addWidget(self.input, 5, 1)
        layout.addWidget(self.search_word, 5, 0)
        layout.addWidget(search, 6, 1)
        layout.addWidget(self.filler, 8, 0)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def book_changed(self, i):
        self.chapter.clear()
        self.dict_values_list = list(self.book_dict.values())
        self.num_chapters = self.dict_values_list[i]
        self.chapter.addItem("N/A")
        for i in range(1, self.num_chapters + 1):
            self.chapter.addItem(str(i))

    def search_bible(self):
        x = requests.get(
            f"https://www.biblegateway.com/passage/?search={self.book.currentText()}+{self.chapter.currentText()}&version={self.version.currentText()}")
        soup = BeautifulSoup(x.content, "html.parser")
        text = ""
        for i in soup.find_all("p"):
            text += i.get_text()

        # counts the number of occurrences of given search word
        self.num_times = text.upper().count(" " + self.input.text().upper() + " ", 0,
                                            (text.find("Holy Bible", 0, len(text))))
        self.filler.setText(f"Number of times the word appears: {self.num_times}")


app = QApplication()

window = MainWindow()
window.show()

app.exec()
