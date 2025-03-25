class TicTacToeModel:
    def __init__(self):
        self.reset_game()
        self.reset_stats()

    def reset_game(self):
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.current_player = "X"
        self.game_active = True

    def reset_stats(self):
        self.x_wins = 0
        self.o_wins = 0
        self.ties = 0
        self.game_count = 0

    def make_move(self, row, col):
        if not self.game_active or self.board[row][col] != "":
            return False

        self.board[row][col] = self.current_player
        return True

    def check_winner(self):
        # Проверка строк
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return self.board[i][0]

        # Проверка столбцов
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != "":
                return self.board[0][j]

        # Проверка диагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]

        return None

    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def update_stats(self, winner):
        if winner == "X":
            self.x_wins += 1
        elif winner == "O":
            self.o_wins += 1
        else:
            self.ties += 1
        self.game_count += 1