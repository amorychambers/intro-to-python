# Video alternative: https://vimeo.com/954334009/67af9910fc#t=1054

# So far you've spent a lot of time writing new programs.

# This is great for learning the fundamentals of code, but
# actually isn't very realistic. Most software engineers
# spend their time modifying and maintaining existing
# programs, not writing entirely new ones.

# Below is the same program as in the example. Your
# challenge is to implement some improvements:

# 1. Right now users can place their tiles over the other
#    user's tiles. Prevent this.

# 2. Right now if the game reaches a draw with no more free
#    spaces, the game doesn't end. Make it end at that
#    point.

# 3. If you want a real challenge, try to rework this
#    program to support a 5x5 board rather than a 3x3 board.

# 4. If you're still not satisfied, try to rework this
#    program to take a parameter `board_size` and play a
#    game with a board of that size.

# This is getting really challenging now — and is entirely
# optional. Don't forget about your assessment!

def play_game():
  board_size = int(input("Enter a grid size for the board: "))
  board = create_board(board_size)
  player = "X"
  while not is_game_over(board):
    print(print_board(board))
    print("It's " + player + "'s turn.")
    # `input` asks the user to type in a string
    # We then need to convert it to a number using `int`
    i = 0
    while i < 1:
      row = int(input("Enter a row: "))
      column = int(input("Enter a column: "))
      if len(board) >= row:
        if len(board[row]) >= column:
          if board[row][column] == ".":
            i += 1
          else: 
            print("That spot's already taken!")
        else:
          print("That spot doesn't exist!")
      else:
        print("That spot doesn't exist!")
    i = 0
    board = make_move(board, row, column, player)
    if player == "X":
      player = "O"
    else:
      player = "X"
  print(print_board(board))
  print("Game over!")

def print_board(board):
  formatted_rows = []
  for row in board:
    formatted_rows.append(" ".join(row))
  grid = "\n".join(formatted_rows)
  return grid

def make_move(board, row, column, player):
  board[row][column] = player
  return board


# This function will extract three cells from the board
def get_cells(board, coord_1, coord_2, coord_3):
  return [
    board[coord_1[0]][coord_1[1]],
    board[coord_2[0]][coord_2[1]],
    board[coord_3[0]][coord_3[1]]
  ]

# This function will check if the group is fully placed
# with player marks, no empty spaces.
def is_group_complete(board, coord_1, coord_2, coord_3):
  cells = get_cells(board, coord_1, coord_2, coord_3)
  return "." not in cells

# This function will check if the group is all the same
# player mark: X X X or O O O
def are_all_cells_the_same(board, coord_1, coord_2, coord_3):
  cells = get_cells(board, coord_1, coord_2, coord_3)
  return cells[0] == cells[1] and cells[1] == cells[2]

# We'll make a list of groups to check:

groups_to_check_example = [
  # Rows
  [(0, 0), (0, 1), (0, 2)],
  [(1, 0), (1, 1), (1, 2)],
  [(2, 0), (2, 1), (2, 2)],
  # Columns
  [(0, 0), (1, 0), (2, 0)],
  [(0, 1), (1, 1), (2, 1)],
  [(0, 2), (1, 2), (2, 2)],
  # Diagonals
  [(0, 0), (1, 1), (2, 2)],
  [(0, 2), (1, 1), (2, 0)]
]

# This function creates the groups to check for a successful string of three
def create_groups(board_size):
  groups_to_check = []

  # Nested for loops used to calculate groups of three rows and columns based on any board size grid
  # for x in range(board_size):
  #   row = []
  #   column = []
  #   for y in range(board_size):
  #     row.append((x, y))
  #     column.append((y, x))
    # groups_to_check.append(row)
    # groups_to_check.append(column)

  # backslash_diagonals = []
  # for x in range(board_size):
  #   diagonal = []
  #   for y in range(3):
  #     diagonal.append((x + y, x + y))
  #   backslash_diagonals.append(diagonal)
  
  # groups_to_check.extend(backslash_diagonals)
    
  # forwardslash_diagonals = []
  # for x in range(board_size):
  #   diagonal = []
  #   coordinate = ()
  #   for y in range(2, -1, -1):
  #     coordinate += (x, y)
  #   diagonal.append(coordinate)
  #   forwardslash_diagonals.append(diagonal)
  
  # groups_to_check.extend(forwardslash_diagonals)

  my_list = list(range(board_size))
  reverse_list = my_list[::-1]
  new_list = []
  for x in range(board_size):
    new_list.append((my_list[x], reverse_list[x]))
  
  sublists = [new_list[i:i + 3] for i in range(0, len(new_list), 1)] 
  print(new_list)
  print(sublists)


  return groups_to_check

def is_game_over(board):
  # We go through our groups
  for group in groups_to_check:
    # If any of them are empty, they're clearly not a
    # winning row, so we skip them.
    if is_group_complete(board, group[0], group[1], group[2]):
      if are_all_cells_the_same(board, group[0], group[1], group[2]):
        return True # We found a winning row!
        # Note that return also stops the function
  all_spots = "".join(board[0]) + "".join(board[1]) + "".join(board[2])
  if "." not in all_spots:
    return True
  else:
    return False # If we get here, we didn't find a winning row


# This function creates a board based on a grid size taken from the user
def create_board(board_size):
  board = []
  for x in range(0, board_size):
    new_row = []
    board.append(new_row)
    for y in range(0, board_size):
      board[x].append(".")
  return board


print("Game time!")
print(create_groups(5))