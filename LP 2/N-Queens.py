def satisfy_constraints(board, constraints, n, n_queens):
  c1, c2 = constraints
  for col1 in range(n):
    if (isSafe(board, c1, col1, n)):
      board[c1][col1] = "Q"
      # print("?????????",board)
      for col2 in range(n):
        if (isSafe(board, c2, col2, n)):
          board[c2][col2] = "Q"
          # print(board)
          fill_board(board, constraints, 0, n, n_queens-2)
          board[c2][col2] = ""
      board[c1][col1] = ""

def fill_board(board, constraints, row, n, n_queens):
  # print(n_queens)
  if (n_queens == 0):
    print(*board, sep="\n")
    print("=================================")
    return
  if (row == n):
    return
  if row in constraints:
    return fill_board(board, constraints, row+1, n, n_queens)

  for col in range(n):
    if (isSafe(board, row, col, n)):
      board[row][col] = 'Q'
      fill_board(board, constraints, row+1, n, n_queens-1)
      board[row][col] = ''
  fill_board(board, constraints, row+1, n, n_queens)
  

def isSafe(board, row, col, n):
  # return True
  for j in range(n):
    if (board[row][j] == 'Q'):
      return False
  for i in range(n):
    if (board[i][col] == 'Q'):
      return False
  
  i=row+1
  j=col+1
  while (i< n and j < n):
    if (board[i][j] == 'Q'):
      return False
    i+= 1
    j+=1

  i=row-1
  j=col-1
  while (i>=0 and j >= 0):
    if (board[i][j] == 'Q'):
      return False
    i-= 1
    j-=1

  i=row+1
  j=col-1
  while (i < n and j >= 0):
    if (board[i][j] == 'Q'):
      return False
    i+= 1
    j-=1

  i=row-1
  j=col+1
  while (i >= 0  and j < n):
    if (board[i][j] == 'Q'):
      return False
    i-= 1
    j+=1

  return True


n = 5  #board size
n_queens = 3  # number of queens to be placed
c1 = 1        # constraint-1 must be betwwen [0,n-1]
c2 = 2        # constraint-2 must be betwwen [0,n-1]

lst = []
for i in range(n):
  lst.append([""]*n)
satisfy_constraints(lst, (c1, c2), n, n_queens)