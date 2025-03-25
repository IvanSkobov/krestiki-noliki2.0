<<<<<<< HEAD
<<<<<<< HEAD
from view import TicTacToeView
from model import TicTacToeModel
from controller import TicTacToeController

if __name__ == "__main__":
    model = TicTacToeModel()
    view = TicTacToeView()
    controller = TicTacToeController(model, view)
    view.run()

import tkinter as tk
from tkinter import messagebox, font as tkfont


class TicTacToeView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Крестики-нолики")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.big_font = tkfont.Font(family='Arial', size=20, weight='bold')
        self.small_font = tkfont.Font(family='Arial', size=12)

        self.create_widgets()

    def create_widgets(self):
        # Control Frame
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(pady=10)

        # Reset Button
        self.reset_btn = tk.Button(
            self.control_frame,
            text="Новая игра",
            font=self.small_font
        )
        self.reset_btn.grid(row=0, column=0, padx=5)

        # Player Choice
        self.choice_var = tk.StringVar(value="X")
        tk.Radiobutton(
            self.control_frame,
            text="Играть за X",
            variable=self.choice_var,
            value="X",
            font=self.small_font
        ).grid(row=0, column=1, padx=5)
        tk.Radiobutton(
            self.control_frame,
            text="Играть за O",
            variable=self.choice_var,
            value="O",
            font=self.small_font
        ).grid(row=0, column=2, padx=5)

        # Stats Frame
        self.stats_frame = tk.Frame(self.root)
        self.stats_frame.pack(pady=10)

        tk.Label(
            self.stats_frame,
            text="Статистика:",
            font=self.small_font
        ).grid(row=0, column=0, columnspan=3)

        tk.Label(
            self.stats_frame,
            text="X:",
            font=self.small_font
        ).grid(row=1, column=0)
        self.x_score = tk.Label(
            self.stats_frame,
            text="0",
            font=self.small_font
        )
        self.x_score.grid(row=1, column=1)

        tk.Label(
            self.stats_frame,
            text="Ничьи:",
            font=self.small_font
        ).grid(row=1, column=2, padx=10)
        self.ties_score = tk.Label(
            self.stats_frame,
            text="0",
            font=self.small_font
        )
        self.ties_score.grid(row=1, column=3)

        tk.Label(
            self.stats_frame,
            text="O:",
            font=self.small_font
        ).grid(row=1, column=4)
        self.o_score = tk.Label(
            self.stats_frame,
            text="0",
            font=self.small_font
        )
        self.o_score.grid(row=1, column=5)

        # Status Label
        self.status_label = tk.Label(
            self.root,
            text="Сейчас ходит: X",
            font=self.small_font
        )
        self.status_label.pack(pady=5)

        # Game Board
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(
                    self.board_frame,
                    text="",
                    font=self.big_font,
                    width=5,
                    height=2,
                    bg="#f0f0f0",
                    activebackground="#e0e0e0"
                )
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def run(self):
        self.root.mainloop()

    def update_board(self, board):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = board[i][j]

    def update_status(self, player):
        self.status_label.config(text=f"Сейчас ходит: {player}")

    def update_stats(self, x_wins, o_wins, ties):
        self.x_score.config(text=str(x_wins))
        self.o_score.config(text=str(o_wins))
        self.ties_score.config(text=str(ties))

    def show_winner(self, winner):
        messagebox.showinfo("Победа!", f"Игрок {winner} победил!")

    def show_tie(self):
        messagebox.showinfo("Ничья!", "Игра закончилась вничью!")

    def show_series_winner(self, winner):
        messagebox.showinfo("Конец игры!", f"Игрок {winner} выиграл серию до 3 побед!")

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
>>>>>>> logica
