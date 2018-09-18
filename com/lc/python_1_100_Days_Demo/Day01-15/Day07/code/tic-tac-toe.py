"""

井字棋游戏

Version: 0.1
Author: LC
DateTime:2018年9月18日11:46:05
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

import os



def print_board(board):
	print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
	print('-+-+-')
	print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
	print('-+-+-')
	print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main():
	init_board = {
		'TL': ' ', 'TM': ' ', 'TR': ' ',
		'ML': ' ', 'MM': ' ', 'MR': ' ',
		'BL': ' ', 'BM': ' ', 'BR': ' '
	}
	begin = True
	while begin:
		curr_board = init_board.copy()
		begin = False
		turn = 'x'
		counter = 0
		os.system('clear')
		print_board(curr_board)
		while counter < 9:
			move = input('轮到%s走棋, 请输入位置: ' % turn)
			if curr_board[move] == ' ':
				counter += 1
				curr_board[move] = turn
				if turn == 'x':
					turn = 'o'
				else:
					turn = 'x'
			os.system('clear')
			print_board(curr_board)
		choice = input('再玩一局?(yes|no)')
		begin = choice == 'yes'


if __name__ == '__main__':
	main()
