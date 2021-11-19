import sys
from PySide6 import QtWidgets
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMessageBox, QLabel, QMainWindow, QLineEdit, QWidget, QListWidget, \
    QGridLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # sets a window of fixed size for the app
        self.setWindowTitle("Shopping list")
        self.setFixedSize(400, 600)

        # creates a textbox that can be typed in
        self.input = QLineEdit()
        self.input.setFixedWidth(300)

        # create an instance of the QListWidget with multiselect enabled as well as sorting
        self.my_list = QListWidget()
        self.my_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.my_list.setSortingEnabled(True)

        # read the contents of the file and writes them to the todolist
        file = open("file.txt", "r")
        for i in file:
            string = i.strip()
            self.my_list.addItem(string)

        file.close()

        # creates button that calls the addListItem function when clicked
        add_item = QPushButton("Add")
        add_item.clicked.connect(self.addListItem)

        # creates button that calls the removeListItem function when clicked
        remove_item = QPushButton("Remove Selected Items")
        remove_item.clicked.connect(self.removeListItem)

        # this section of code creates a title for the app and makes the app visible
        self.text = QLabel(text="Shopping List")
        self.text.setIndent(150)
        self.text.setFont(QFont("Times", weight=QFont.Bold))
        self.text.show()

        # creates an instance of QGridLayout which can be used to position widgets within a window
        layout = QGridLayout()
        # adding widgets with specific positions
        layout.addWidget(self.text, 0, 0)
        layout.addWidget(self.input, 1, 0)
        layout.addWidget(remove_item, 5, 0)
        layout.addWidget(add_item, 1, 1)
        layout.addWidget(self.my_list, 3, 0)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # creating the buttons for the destructive action alert
        self.yes_button = QPushButton("Yes")
        self.no_button = QPushButton("No")

    def addListItem(self):
        # takes content of box and adds it to the list widget
        item = self.input.text()
        self.my_list.addItem(item)
        self.input.setText("")

    def removeListItem(self):
        # removes the selected items from the list widget
        dlg = QMessageBox(self)
        dlg.setFixedWidth(100)
        dlg.setText("Remove selected items?")
        dlg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        button = dlg.exec()
        if button == QMessageBox.Yes:
            list_items = self.my_list.selectedItems()
            if not list_items: return
            for item in list_items:
                self.my_list.takeItem(self.my_list.row(item))

    def closeEvent(self, _):
        # saves the contents of the listwidget to a file to preserve items, is called on exit
        file = open("file.txt", "r+")
        file.truncate(0)
        items = []
        for index in range(self.my_list.count()):
            items.append(self.my_list.item(index))
        for i in items:
            file.write(i.text())
            file.write("\n")

        file.close()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# TODO: enter key should input text
# TODO: change the list widget and remove button to fill entire window
# TODO: add documentation
