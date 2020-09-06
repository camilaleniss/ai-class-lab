import re
import random

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    return self.board.count(None) == 0

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self):
    # TODO: Implement this function to make the machine choose a random cell (use random module)
    # The result of this function should be that self.board now has one more random cell occupied
    random_cell = random.choice([x for x in range(len(self.board)) if self.board[x] is None])
    self.board[random_cell] = _MACHINE_SYMBOL

  def format_board(self):
    # TODO: Implement this function, it must be able to print the board in the following format:
    board =""

    for i in range(len(self.board)):
      separator = "|"
      if (i+1)%3 == 0:
        separator = "\n"

      turn = " "
      symbol = self.board[i]
      if symbol in (_PLAYER_SYMBOL, _MACHINE_SYMBOL):
          turn = symbol

      board += (turn+separator)

    return board

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())


  def print_result(self):
    # TODO: Implement this function in order to print the result based on the self.winner
    if self.winner is None:
      print("It was a draw, better luck next time")
    else:
      print("%s is the winner" %self.winner)
