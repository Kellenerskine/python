#doesnt work, website has changed formatting (tracker.gg)

import requests
import math
from PySide6.QtWidgets import *
from bs4 import BeautifulSoup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # sets a window of fixed size for the app
        self.setWindowTitle("Valorant hour checker")
        self.setFixedSize(400, 200)

        # creates a textbox that can be typed in
        self.input_username = QLineEdit()
        self.input_tag = QLineEdit()

        # creates button that calls the addListItem function when clicked
        search = QPushButton("Search")
        search.clicked.connect(self.count_hours)

        # this section of code creates a title for the app and makes the app visible
        self.search_word = QLabel(text="Username: ")
        self.tag = QLabel(text="Tag: ")
        self.filler = QLabel(text="Number of hours played: ")

        # creates an instance of QGridLayout which can be used to position widgets within a window
        layout = QGridLayout()
        layout.addWidget(self.search_word, 5, 0)
        layout.addWidget(self.input_username, 5, 1)
        layout.addWidget(self.tag, 6, 0)
        layout.addWidget(self.input_tag, 6, 1)
        layout.addWidget(search, 7, 1)
        layout.addWidget(self.filler, 9, 0)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def count_hours(self):
        game_modes = ["playlist=competitive&", "playlist=deathmatch&", "playlist=escalation&", "playlist=spikerush&",
                      "playlist=replication&", "playlist=snowball&", ""]

        tot_hours = 0

        for i in game_modes:
            doc = f"https://tracker.gg/valorant/profile/riot/{str(self.input_username.text())}%23{str(self.input_tag.text())}/overview?season=all"
            # https://tracker.gg/valorant/profile/riot/Relzwit%2324601/overview?season=all
            res = requests.get(doc)

            soup = BeautifulSoup(res.content, "html.parser")

            tag = soup.body

            rand = ""

            for string in tag.strings:
                if "Play Time" in string:
                    rand += string

            rand = ''.join(ch for ch in rand if ch.isalnum())

            if "h" in rand:
                pos_h = rand.find("h")
                hours = int(rand[0:pos_h])
                rand = rand.removeprefix((str(hours) + "h"))
                pos_m = rand.find("m")
                minutes = int(rand[0:pos_m])
                rand = rand.removeprefix((str(minutes) + "m"))
                tot_hours += ((hours * 60) + minutes) / 60
            else:
                pos_m = rand.find("m")
                print(rand[0:pos_m])
                minutes = int(rand[0:pos_m])
                rand = rand.removeprefix((str(minutes) + "m"))
                pos_s = rand.find("s")
                seconds = int(rand[0:pos_s])
                tot_hours += (minutes + seconds / 60) / 60
            rand = ""

        frac, whole = math.modf(tot_hours)
        tot_mins = frac * 60

        self.filler.setText(f"Time played: {round(tot_hours)} Hours {round(tot_mins)} Minutes")
        print("done")


app = QApplication()

window = MainWindow()
window.show()

app.exec()
