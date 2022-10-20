def spiralPath(matrix):

    rows = len(matrix)  # indexul lui i de final
    columns = len(matrix[0])  # indexul lui j de final

    left = 0  # indexul lui i de inceput
    right = 0  # indexul lui j de inceput

    while left < rows and right < columns:

        for i in range(right, columns):
            print(matrix[left][i], end="")
        left += 1

        for i in range(left, rows):
            print(matrix[i][rows - 1], end="")
        columns -= 1

        if left < rows:
            for i in range(columns - 1, right - 1, -1):
                print(matrix[rows - 1][i], end="")

            rows -= 1

        if right < columns:
            for i in range(rows - 1, left - 1, -1):
                print(matrix[i][right], end="")
            right += 1


matrix = [['f', 'i', 'r', 's'],
          ['n', '_', 'l', 't'],
          ['o', 'b', 'a', '_'],
          ['h', 't', 'y', 'p']]

print("The word formed is: ", end="")

spiralPath(matrix)

print("")