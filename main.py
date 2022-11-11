
board = [
  [" "," "," "],
  [" "," "," "],
  [" "," "," "]
]
def showboard(board):
  print (f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
  print ("-"*11)
  print (f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
  print ("-"*11)
  print (f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")

done = False
player = "x"
while not done:
  showboard(board)
  print ("Please choose a row(1-3): ")
  row = input()
  print ("Please choose a column(1-3): ")
  col = input()
  
  if row.isdecimal() and col.isdecimal():
    if (1 <= int(row) <= 3) and (1 <= int(col) <= 3) :
      board[int(row)-1][int(col)-1]= player
      if player =="x":
        player = "o"
      else:
        player = "x"
          