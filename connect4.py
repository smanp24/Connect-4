import random
import os

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def print_rules():
	print("================= Rules =================")
	print("Connect 4 is a two-player game where the")
	print("objective is to get four of your pieces")
	print("in a row either horizontally, vertically")
	print("or diagonally. The game is played on a")
	print("6x7 grid. The first player to get four")
	print("pieces in a row wins the game. If the")
	print("grid is filled and no player has won,")
	print("the game is a draw.")
	print("=========================================")

def validate_input(prompt, valid_inputs):
	while True:
		user_input = input(prompt)

		if user_input in valid_inputs:
			return user_input
		else:
			print("Invalid input, please try again.")

def create_board():
	board = []
	row = 6
	column = 7

	for i in range(row):
		board.append([0] * column)

	return board
def print_board(board):
	rows = len(board)
	columns = len(board[0])

	print('========== Connect4 =========')
	print('Player 1: X       Player 2: O\n')
	print('  1   2   3   4   5   6   7')

	for i in range(rows):
		print(' ---' * columns)

		for j in range(columns):
			if board[i][j] == 0:
				print('|   ', end='')
			elif board[i][j] == 1:
				print('| X ', end='')
			elif board[i][j] == 2:
				print('| O ', end='')

		print('|')

	print(' ---' * columns)
	print('=============================')

def drop_piece(board, player, column):
	i = len(board) - 1

	while i >= 0:
		if board[i][column - 1] == 0:
			board[i][column - 1] = player
			return True
		else:
			i -= 1

	return False

def execute_player_turn(player, board):
	while True:
		column = int(input(f'Player {player}, please enter the column you would like to drop your piece into: '))

		if str(column) in ["1", "2", "3", "4", "5", "6", "7"]:
			if drop_piece(board, player, column):
				return column
			else:
				print("That column is full, please try again.")
		else:
			print("Invalid input, please try again.")

def end_of_game(board):
	rows = len(board)
	columns = len(board[0])

	for i in range(rows - 3):
		for j in range(columns):
			if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] != 0:
				return board[i][j]

	for i in range(rows):
		for j in range(columns - 3):
			if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] != 0:
				return board[i][j]

	for i in range(rows - 3):
		for j in range(columns - 3):
			if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] != 0:
				return board[i][j]

	for i in range(rows - 3):
		for j in range(3, columns):
			if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] != 0:
				return board[i][j]

	for i in range(rows):
		for j in range(columns):
			if board[i][j] == 0:
				return 0

	return 3

def local_2_player_game():
	clear_screen()
	board = create_board()
	print_board(board)

	stop = 0
	while stop < 1:
		for i in range(1, 3):
			column = execute_player_turn(i, board)

			clear_screen()
			print_board(board)

			print(f'Player {i} dropped a piece into column {column}')

			result = end_of_game(board)
			if result == 1 or result == 2:
				print(f'Player {result} has won!')
				stop = 2
				break
			elif result == 3:
				print(f'This game is a draw!')
				stop = 2
				break

def main():
	print('=============== Main Menu ===============')
	print('Welcome to Connect 4!')
	print('1. View Rules')
	print('2. Play a local 2 player game')
	print('3. Play a game against the computer')
	print('4. Exit')
	print('=========================================')

	option = input('Please select an option (1/2/3/4): ')

	if option == '1':
		clear_screen()
		print_rules()
		return1 = input('Press 1 to return: ')
		if return1 == '1':
			clear_screen()
			main()
		else:
			return 1

	elif option == '2':
		clear_screen()
		local_2_player_game()
		return1 = input('Press 1 to return: ')
		if return1 == '1':
			clear_screen()
			main()
		else:
			return 1

	elif option == '3':
		clear_screen()
		game_against_cpu()

	elif option == '4':
		return 1

def cpu_player_easy(board, player):
	while True:
		column = random.randint(1, 7)

		if drop_piece(board, player, column):
			return column

def analyse_medium(board, player):
	rows = len(board)
	columns = len(board[0])

	for i in range(rows - 3):
		for j in range(columns):
			if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == player:
				return True

	for i in range(rows):
		for j in range(columns - 3):
			if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == player:
				return True

	for i in range(rows - 3):
		for j in range(columns - 3):
			if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == player:
				return True

	for i in range(rows - 3):
		for j in range(3, columns):
			if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] == player:
				return True

	return False

def cpu_player_medium(board, player):

	row = len(board)
	column = len(board[0])

	count = 0

	for col in range(1, column + 1):

		temp = [row[:] for row in board]

		if drop_piece(temp, player, col) == False:
			count += 1

	if count == column - 1:
		for col in range(1, column + 1):
			if drop_piece(board, player, col):
				return col

	for col in range(1, column + 1):

		temp = [row[:] for row in board]
		if drop_piece(temp, player, col):
			if analyse_medium(temp, player):
				drop_piece(board, player, col)
				return col

	for col in range(1, column + 1):

		temp = [row[:] for row in board]
		if drop_piece(temp, player % 2 + 1, col):
			if analyse_medium(temp, player % 2 + 1):
				drop_piece(board, player, col)
				return col

	i = random.randint(1, 7)
	if drop_piece(board, player, i):
		return i

def analyse_three(board, player):

	rows = len(board)
	columns = len(board[0])

	for row in range(rows - 3):
		for col in range(columns):
			if board[row][col] == board[row+1][col] == board[row+2][col] == player and row > 0:
				return True

	for row in range(rows):
		for col in range(columns - 3):
			if board[row][col] == board[row][col+1] == board[row][col+2] == player:
				return True

	for row in range(rows - 3):
		for col in range(columns - 3):
			if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == player:
				return True

	for row in range(rows - 3):
		for col in range(3, columns):
			if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == player:
				return True

	return False

def analyse_hard(board, player):
	rows = len(board)
	columns = len(board[0])

	weight = {
		(player, player, player, player): 150,
		(player, player, player, 0): 100,
		(0, player, player, player): 100,
		(player, player, 0, player): 50,
		(player, 0, player, player): 50,
		(player, player, 0, 0): 10,
		(player, 0, player, 0): 10,
		(0, player, player, 0): 10,
		(player, 0, 0, player): 10,
		(0, 0, player, player): 10,
	}

	for row in range(rows - 3):
		for col in range(columns):
			key = (board[row][col], board[row+1][col], board[row+2][col], board[row+3][col])
			if key in weight:
				if weight[key] > 50:
					return True
				elif key.count(player) == 3:
					if weight[key] > 10:
						return True
					elif key.count(player) == 2:
						return True

	for row in range(rows):
		for col in range(columns - 3):
			key = (board[row][col], board[row][col+1], board[row][col+2], board[row][col+3])
			if key in weight:
				if weight[key] > 50:
					return True
				elif key.count(player) == 3:
					if weight[key] > 10:
						return True
					elif key.count(player) == 2:
						return True

	for row in range(rows - 3):
		for col in range(columns - 3):
			key =(board[row][col], board[row+1][col+1], board[row+2][col+2], board[row+3][col+3])
			if key in weight:
				if weight[key] > 50:
					return True
				elif key.count(player) == 3:
					if weight[key] > 10:
						return True
					elif key.count(player) == 2:
						return True

	for row in range(rows - 3):
		for col in range(3, columns):
			key = (board[row][col], board[row+1][col-1], board[row+2][col-2], board[row+3][col-3])
			if key in weight:
				if weight[key] > 50:
					return True
				elif key.count(player) == 3:
					if weight[key] > 10:
						return True
					elif key.count(player) == 2:
						return True

	return False



def block_horizontal(board):
	weight = {
		(0, 0, 0, 1, 0, 0, 0): 100,
		(0, 0, 1, 0, 0, 0, 0): 80,
		(0, 1, 0, 0, 0, 0, 0): 80,
		(0, 0, 0, 0, 1, 0, 0): 80,
		(0, 0, 0, 0, 0, 1, 0): 80,
		(0, 0, 0, 0, 0, 0, 1): 80,
		(1, 0, 0, 0, 0, 0, 0): 80
	}

	key = (board[5][0], board[5][1], board[5][2], board[5][3], board[5][4], board[5][5], board[5][6])
	if key in weight:
		if weight[key] > 90:
			return 5
		elif weight[key] > 70:
			return 4

	return False

block_count = 0

def cpu_player_hard(board, player):
	row = len(board)
	column = len(board[0])

	count = 0
	for col in range(1, column + 1):
		temp = [row[:] for row in board]
		if drop_piece(temp, player, col) == False:
			count += 1

	if count == column - 1:
		for col in range(1, column + 1):
			if drop_piece(board, player, col):
				return col

	for col in range(1, column + 1):
		temp = [row[:] for row in board]
		if drop_piece(temp, player, col):
			if analyse_medium(temp, player):
				drop_piece(board, player, col)
				return col

	for col in range(1, column + 1):
		temp = [row[:] for row in board]
		if drop_piece(temp, player % 2 + 1, col):
			if analyse_medium(temp, player % 2 + 1):
				drop_piece(board, player, col)
				return col

	global block_count
	if block_count == 0:
		block = block_horizontal(board)
		if block_horizontal(board) != False:
			drop_piece(board, player, block)
			block_count += 1
			return block

	for col in range(1, column + 1):
		temp = [row[:] for row in board]
		if drop_piece(temp, player, col):
			if analyse_hard(temp, player):
				drop_piece(board, player, col)
				return col

	for col in range(1, column + 1):
		temp = [row[:] for row in board]
		if drop_piece(temp, player, col):
			if analyse_three(temp, player):
				drop_piece(board, player, col)
				return col

	temp = [row[:] for row in board]
	if drop_piece(temp, player, 4) and board[3][4] == 0:
		drop_piece(board, player, 4)
		return 4
	elif drop_piece(temp, player, 3) and board[3][3] == 0:
		drop_piece(board, player, 3)
		return 3
	elif drop_piece(temp, player, 5) and board[3][5] == 0:
		drop_piece(board, player, 5)
		return 5
	elif drop_piece(temp, player, 2) and board[3][2] == 0:
		drop_piece(board, player, 2)
		return 2
	elif drop_piece(temp, player, 6) and board[3][6] == 0:
		drop_piece(board, player, 6)
		return 6

	i = random.randint(1, 7)
	if drop_piece(board, player, i):
		return i


def cpu_selection(cpu_difficulty):
	clear_screen()
	board = create_board()
	print_board(board)

	while True:
		column = execute_player_turn(1, board)

		clear_screen()
		print_board(board)

		print(f'Player 1 dropped a piece into column {column} ')

		result = end_of_game(board)
		if result == 1 or result == 2:
			print(f'Player {result} has won!')
			play_again = input('Press 1 to exit: ')
			if play_again == '1':
				break
			else:
				break

		elif result == 3:
			print(f'This game is a draw!')
			play_again = input('Press 1 to exit: ')
			if play_again == '1':
				break
			else:
				break

		column = cpu_difficulty(board, 2)

		clear_screen()
		print_board(board)
		print(f'Player 2 dropped a piece into column {column} ')
		result = end_of_game(board)

		if result == 1 or result == 2:
			print(f'Player {result} has won!')
			play_again = input('Press 1 to exit: ')
			if play_again == '1':
				break
			else:
				break

		elif result == 3:
			print(f'This game is a draw!')
			play_again = input('Press 1 to exit: ')
			if play_again == '1':
				break
			else:
				break

def game_against_cpu():
	clear_screen()
	print('=============== Difficulty ===============')
	print('Please select a difficulty!')
	print('1. Easy')
	print('2. Medium')
	print('3. Hard')
	print('=========================================')

	option = input('Please select an option (1/2/3): ')

	if option == '1':
		cpu_selection(cpu_player_easy)

	elif option == '2':
		cpu_selection(cpu_player_medium)

	elif option == '3':
		cpu_selection(cpu_player_hard)


if __name__ == "__main__":
	main()