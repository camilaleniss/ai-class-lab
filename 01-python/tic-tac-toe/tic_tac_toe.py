import re
import random

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

_WINNER_POSSIBILITIES = {
  0: [[1,2], [4,8], [3, 6]],
  1: [[4, 7]],
  2: [[5,8], [4,6]],
  3: [[4,6]],
  6: [[7,8]],
}

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): 
    # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    for i in _WINNER_POSSIBILITIES:
      pivot_game = _WINNER_POSSIBILITIES[i]
      pivot_turn = self.board[i]

      for item in pivot_game:
        if pivot_turn == None:
          break

        if (self.board[item[0]] is not None and self.board[item[0]]==pivot_turn) and (self.board[item[1]] is not None and self.board[item[1]]==pivot_turn):
          self.winner = _PLAYER if pivot_turn == _PLAYER_SYMBOL else _MACHINE
          self.is_game_over = True

          return True

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
    # The result of this function should be that self.board now has one more random cell occupied
    random_cell = random.choice([x for x in range(len(self.board)) if self.board[x] is None])
    self.board[random_cell] = _MACHINE_SYMBOL

  def format_board(self):
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
    if self.winner is None:
      print("It was a draw, better luck next time")
    else:
      print("%s is the winner" %self.winner)
