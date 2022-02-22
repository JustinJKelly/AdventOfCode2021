
def check_board(board):
    for i in range(0,5):
        
        #horizontal
        if board[i] == [1,1,1,1,1]:
            return True
        
        #vertical
        if [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]] == [1,1,1,1,1]:
            return True
        
    return False

def sum_unused_numbers(board_status, best_board):
    sum = 0
    for i in range(0,5):
        for j in range(0,5):
            #print(board_status[i][j], type(board_status[i][j]), "0", type("0"))
            if board_status[i][j] == 0:
                sum += int(best_board[i][j])
                
    return sum
        

#Part 1

f = open('input.txt')
chosen_numbers = []
board = []
boards = []

# O(n), n = # of input lines
for line in f:
    if line == "\n":
        continue
    elif ',' in line:
        chosen_numbers = [n.strip() for n in line.split(',')]
    else:
         board.append(line.split())
         if len(board) == 5:
             boards.append(board)
             board = []
        
min_numbers_so_far = float('inf')
best_board = []
board_status = []
last_number = float('inf')
for b in boards: # m boards
    curr_board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    num_numbers_used = 0
    for i in range(0, len(chosen_numbers)): # n numbers
        for j in range(0,5): # constant
            for k in range(0,5):
                if b[j][k] == chosen_numbers[i]:
                    curr_board[j][k] = 1
                    num_numbers_used += 1
        
        if num_numbers_used >= 5:
            if check_board(curr_board):
                #print(b, min_numbers_so_far, "   ", i)
                if min_numbers_so_far > i:
                    min_numbers_so_far = i
                    best_board = b
                    board_status = curr_board
                    last_number = chosen_numbers[i]
                break
        #print(curr_board)
            
print("Winning Board:", best_board)
print("Numbers called for winner:", min_numbers_so_far)
print("Winning Board Status:", board_status)
print("Part 1")

print("sum:", sum_unused_numbers(board_status, best_board), " last_number:", last_number, " answer:",sum_unused_numbers(board_status, best_board)*int(last_number))

print("====================================")
print("Part 2")

max_numbers_so_far = float('-inf')
board_status = []
last_number = float('inf')
worst_board = []
for b in boards: # m boards
    curr_board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    num_numbers_used = 0
    for i in range(0, len(chosen_numbers)): # n numbers
        for j in range(0,5): # constant
            for k in range(0,5):
                if b[j][k] == chosen_numbers[i]:
                    curr_board[j][k] = 1
                    num_numbers_used += 1
        
        if num_numbers_used >= 5:
            if check_board(curr_board):
                #print(b, max_numbers_so_far, "   ", i)
                if max_numbers_so_far < i:
                    max_numbers_so_far = i
                    worst_board = b
                    board_status = curr_board
                    last_number = chosen_numbers[i]
                break
            
print("Losing Board:", worst_board)
print("Numbers called for loser:", max_numbers_so_far, len(chosen_numbers))
print("Losing Board Status:", board_status)
print("sum:", sum_unused_numbers(board_status, worst_board), " last_number:", last_number, " answer:",sum_unused_numbers(board_status, worst_board)*int(last_number))


