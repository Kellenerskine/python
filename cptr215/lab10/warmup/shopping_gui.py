import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QStyle, QLabel, QListWidgetItem, QMainWindow, QLineEdit, QVBoxLayout, \
    QGroupBox, \
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
        self.my_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.my_list.setSortingEnabled(True)

        add_item = QPushButton("Add")
        add_item.clicked.connect(self.addListItem)

        remove_item = QPushButton("Remove Selected Items")
        remove_item.clicked.connect(self.removeListItem)

        self.text = QLabel(text="Shopping List")
        self.text.setIndent(150)
        self.text.setFont(QFont("Times", weight=QFont.Bold))
        self.text.show()

        #TODO: TEST
        app.aboutToQuit.connect(self.closeEvent)

        layout = QGridLayout()
        layout.addWidget(self.text, 0, 0)
        layout.addWidget(self.input, 1, 0)
        layout.addWidget(remove_item, 5, 0)
        layout.addWidget(add_item, 1, 1)

        layout.addWidget(self.my_list, 3, 0)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def addListItem(self):
        # takes content of box
        item = self.input.text()
        self.my_list.addItem(item)
        self.input.setText("")

    def removeListItem(self):
        list_items = self.my_list.selectedItems()
        if not list_items: return
        for item in list_items:
            self.my_list.takeItem(self.my_list.row(item))

    # def closeEvent(self):
    #     #Your desired functionality here
    #     print('Close button pressed')
    #     import sys
    #     sys.exit(0)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# TODO: focus cursor on text box for next item
# TODO: sort the items by alph - done
# TODO: enable multiselect - done
# TODO: remove items that are selected with button
# TODO: require a popup confirmation to exit app
# TODO: save all changes to a file
