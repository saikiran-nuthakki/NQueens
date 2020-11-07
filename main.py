def num_placements_all(n):
    return math.factorial(n**2) / (math.factorial((n**2) - n) * math.factorial(n))


def num_placements_one_per_row(n):
    return n**n
    

def n_queens_valid(board):
    i = 0
    while i < len(board):
        if board.index(board[i]) != i:
            return False
        j = 0
        while j < i:
            if abs(board[i] - board[j]) == abs(i - j):
                return False
            j += 1
        i += 1
    return True


def n_queens_helper(n, board):
    i = 0
    while i < n:
        board.append(i)
        if n_queens_valid(board):
            for j in n_queens_helper(n, board):
                yield j[:]
            if len(board) == n:
                yield board
        i += 1
        board.pop(len(board) - 1)


def n_queens_solutions(n):
    solution = [i for i in n_queens_helper(n, [])]
    return iter(solution)
