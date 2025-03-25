from view import TicTacToeView
from model import TicTacToeModel
from controller import TicTacToeController

if __name__ == "__main__":
    model = TicTacToeModel()
    view = TicTacToeView()
    controller = TicTacToeController(model, view)
    view.run()