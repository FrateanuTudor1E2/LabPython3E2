def get_spectators(matrix):

    sol = set()
    for j in range(0, len(matrix[0])):
        for i in range(0, len(matrix)):
            for k in range(0, i):
                if matrix[i][j] <= matrix[k][j]:
                    sol.add((i, j))

    return sol


matrix = [[1, 2, 3, 2, 1, 1],
          [2, 4, 4, 3, 7, 2],
          [5, 5, 2, 5, 6, 4],
          [6, 6, 7, 6, 7, 5]]

print(get_spectators(matrix), end="\n\n")