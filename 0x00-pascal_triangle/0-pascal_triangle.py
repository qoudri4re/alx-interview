def pascal_triangle(n):
    triangle = []
    for row in range(n):
        if row == 0:
            triangle.append([1])
        else:
            current_row = [1]
            for i in range(row - 1):
                current_row.append(triangle[row - 1][i] + triangle[row - 1][i + 1])
            current_row.append(1)
            triangle.append(current_row)
    return triangle
