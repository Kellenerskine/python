class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0, 0]
        self.holes = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]



    def hole_picked(self, hole_number):
        marbles = self.holes[hole_number]
        next_hole = hole_number + 1

        while marbles > 0:
            if (next_hole == 6):
                if (True):  # goal is not mine
                    next_hole += 1  # incrementing next hole index
            else:
                self.holes[next_hole] += 1  # adding marble to next hole
                next_hole += 1  # incrementing next hold index
                marbles -= 1

        self.holes[hole_number] = 0

        return self.holes

    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went


    def winner(self):
        winner_is_p1 = False
        winner_is_p2 = False
        game_is_ongoing = True

        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        while game_is_ongoing:
            for i in range(6):  # checks if bottom row is empty
                if self.holes[i] == 0:
                    game_is_ongoing = False
                else:
                    game_is_ongoing = True

            for i in range(7, 13):  # checks if top row is empty
                if self.holes[i] == 0:
                    game_is_ongoing = False
                else:
                    game_is_ongoing = True




        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False
