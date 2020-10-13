board = list(range(1, 10))

def draw_board(board):

	print("-" * 13)

	for i in range(3):
		print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
		print("-" * 13)

def user_input(board):
	counter = 0

	while True:

		draw_board(board)

		number = int(input())

		for i in range(10):
			counter = i

			if number in board:
				if counter % 2 == 0:
					board[number-1] = 'X'
				else:
					board[number-1] = 'O'



def main(board):
	while True:
		draw_board(board)
		user_input()

user_input(board)