def solution(board, moves):
    cnt = 0
    idx = 0
    bucket = []
    while idx <= len(moves) - 1:

        for i in range(len(board)):
            if board[i][moves[idx]-1]:
                bucket.append(board[i][moves[idx]-1])
                board[i][moves[idx]-1] = 0
                idx += 1

                if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
                    bucket.pop()
                    bucket.pop()
                    cnt += 1
                break
        else:
            idx += 1
            continue
    return cnt * 2
