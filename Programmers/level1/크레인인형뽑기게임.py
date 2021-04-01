def solution(board, moves):
    answer = 0
    basket = []
    for j in moves:
        for i in range(len(board)):
            if board[i][j-1] != 0:
                if basket and basket[-1] == board[i][j-1]:
                    answer += 2
                    board[i][j-1] = 0
                    basket.pop()
                elif not basket or basket[-1] != board[i][j-1]:
                    basket.append(board[i][j-1])
                    board[i][j-1] = 0
                break
    return answer
