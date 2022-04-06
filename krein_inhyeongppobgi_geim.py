def solution(board, moves):
    board_size = len(board)
    board_column_stack =  [[] for i in range(board_size)]
    
    for floor in reversed(board):
        for j in range(board_size):
            if (floor[j] != 0):
                board_column_stack[j].append(floor[j])
                
    basket_stack = []
    answer = 0
    for move in moves:
        column = board_column_stack[move - 1]
        if (column != []):
            doll = column.pop()
            if (basket_stack != [] and doll == basket_stack[-1]):
                basket_stack.pop()
                answer += 2
            else:
                basket_stack.append(doll)
    return answer
