class XsOsGame:
    # crating our game's class with private attributes
    __game_field = [["-", "-", "-"],
                    ["-", "-", "-"],
                    ["-", "-", "-"]]
    __current_player = "X"
    __moves_count = 0

    def view(self):
        # this method to see game's progress
        for column in self.__game_field:
            for cell in column:
                print(f" {cell}", end="")
            print("")

    def change_player(self):
        # changing a player every move
        if self.__current_player == "O":
            self.__current_player = "X"
        else:
            self.__current_player = "O"

    def lets_play(self):
        # our game's sequence
        while True:
            self.view()
            print(f"Player {self.__current_player}, your move!")
            row = int(input("Enter the row (1, 2, 3): "))
            column = int(input("Enter the column (1, 2, 3): "))
            if self.__game_field[row - 1][column - 1] not in "XO":
                self.__game_field[row - 1][column - 1] = self.__current_player
                self.__moves_count += 1  # for a tie's check up
                self.winner_columns()
                self.winner_rows()
                self.winner_diag()
                self.tie()
                self.change_player()

    def repeat(self):
        # if we want to take another round
        self.__game_field = []
        self.__moves_count = 0
        for row in range(3):
            self.__game_field.append(["-", "-", "-"])

    def winner_columns(self):
        # looking for a winner through columns
        for col in self.__game_field:
            res = 0
            for cell in col:
                if cell == self.__current_player:
                    res += 1
            if res == 3:
                print(f"Player {self.__current_player} has won!")
                self.view()
                self.exitt()

    def winner_rows(self):
        # looking for a winner through rows
        start = 0
        while start < 3:
            res = 0
            for col in self.__game_field:
                for cell in col[start:]:
                    if cell == self.__current_player:
                        res += 1
                    break
            start += 1
            if res == 3:
                print(f"Player {self.__current_player} has won!")
                self.view()
                self.exitt()

    def winner_diag(self):
        # looking for a winner through diagonals
        if self.__game_field[0][0] == self.__game_field[1][1] == self.__game_field[2][2] == self.__current_player:
            print(f"Player {self.__current_player} has won!")
            self.view()
            self.exitt()
        elif self.__game_field[0][2] == self.__game_field[1][1] == self.__game_field[2][0] == self.__current_player:
            print(f"Player {self.__current_player} has won!")
            self.view()
            self.exitt()

    def tie(self):
        # in case of a tie
        if self.__moves_count == 9:
            print("It's a TIE!")
            self.view()
            self.exitt()

    def exitt(self):
        # to exit the program or repeat
        q = input("Do you want to finish? ")
        if q == "yes":
            exit()
        else:
            self.repeat()


if __name__ == "__main__":
    new_game = XsOsGame()
    new_game.lets_play()
