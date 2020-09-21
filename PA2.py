def blankmatrix(n, m):
    matrix = []
    for i in range(n):
        z = []
        for j in range(m):
            z.append(0)
        matrix.append(z)
    return matrix

def createAugmentedMatrix(a,b):
    for i in range(len(a)):
        for j in range(len(b)):
            if i == j:
                if isinstance(b[i], int):
                    a[i].append(b[i])
                else:
                    for k in range(len(b[i])):
                        a[i].append(b[i][k])
    c = a
    return c

def gaussJordan(a,b):
    c = createAugmentedMatrix(a,b)  #Create augmented matrix
    p = 0
    solution = []
    for j in range(len(c)): #iterate through columns of matrix
        mag = 0
        absmag = 0
        for i in range(j,len(c)):
            if abs(c[i][j]) > absmag: #find largest magnitude value
                p = i
                absmag = abs(c[i][j])
                mag = c[i][j]
                if mag == 0: #if mag = 0, exit
                    return "No Solution"

        if p > j:
            c[p],c[j] = c[j],c[p] #swap rows

        for i in range(len(c[0])):
            c[j][i] = c[j][i]/mag #divide row by mag

        for i in range(len(c)): #for all remaining rows, zero out
            val = c[i][j]
            if i != j:
                for n in range(len(c[0])):
                    c[i][n] -= c[j][n] * val
    return c

def gaussian(a,b):
    c = createAugmentedMatrix(a,b)  #Create augmented matrix
    p = 0
    for j in range(len(c)): #iterate through columns of matrix
        absmag = 0
        for i in range(j,len(c)):
            if abs(c[i][j]) > absmag: #find largest magnitude value
                p = i
                absmag = abs(c[i][j])
                mag = c[i][j]

                if mag == 0: #if mag = 0, exit
                    return "No Solution"

        if p > j:
            c[p],c[j] = c[j],c[p] #swap rows

        for i in range(len(c)): #for all remaining rows, zero out
            val = c[i][j]
            diag = c[j][j]

            if i > j:
                for n in range(len(c[0])):
                    c[i][n] -= c[j][n] * (val/diag) #zero out
    return c

def gaussJordanInverse(a,b):
    sol = blankmatrix(len(a), len(a[0]))
    c = gaussJordan(a,b)

    for i in range(len(a)):
        for j in range(len(a),len(c[0])):
            sol[i][j-len(a[0])] = c[i][j]

    return sol

def gausDeterminant(c):
    p = 0
    r = 0
    x = 1
    for j in range(len(c)):  # iterate through columns of matrix
        absmag = 0
        for i in range(j, len(c)):
            if abs(c[i][j]) > absmag:  # find largest magnitude value
                p = i
                absmag = abs(c[i][j])
                mag = c[i][j]

                if mag == 0:  # if mag = 0, exit
                    return "No Solution"

        if p > j:
            c[p], c[j] = c[j], c[p]  # swap rows
            r += 1

        for i in range(len(c)):  # for all remaining rows, zero out
            val = c[i][j]
            diag = c[j][j]

            if i > j:
                for n in range(len(c[0])):
                    c[i][n] -= c[j][n] * (val / diag) #zero out

    for i in range(len(c)):
        x *= c[i][i] #Compute the product of the diagonal
    if r%2 == 1: #If r is odd, multiply a -1 to the product
        x *= -1
    return x

def main():
    a = [[1, 0, 2],
         [2, -1, 3],
         [4, 1, 8]]

    b = [[1],[-1],[2]]

    c = [[1, -1, 0],
         [-2, 2, -1],
         [0, 1, -2]]

    identity = [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]]

    # Gauss-Jordan Elimination:
    matrix = gaussJordan(a,b)
    print("Gauss-Jordan Elim:")
    print("matrix: " + str(matrix))

    solution = blankmatrix(len(matrix), 1)
    for k in range(len(matrix)):
        solution[k][0] = matrix[k][len(matrix[0]) - 1]

    print("x = " + str(solution[0]))
    print("y = " + str(solution[1]))
    print("z = " + str(solution[2]))

    print("\n")

    # Gauss-Jordan Inverse
    matrix2 = gaussJordanInverse(c,identity)
    print("Gauss-Jordan Elim Inverse:")
    print("inverse matrix: " + str(matrix2))

    print("\n")

    a = [[1, 0, 2],
         [2, -1, 3],
         [4, 1, 8]]

    b = [[1],[-1],[2]]

    # Gaussian Elimination:
    x = gaussian(a,b)
    print("Gaussian Elim:")
    print("matrix: " + str(x))

    print("\n")

    c = [[1, -1, 0],
         [-2, 2, -1],
         [0, 1, -2]]

    # Gaussian Elimination to Compute Determinant
    print("Guassian Elimination to Compute Determinant:")
    print("Determinant = ",gausDeterminant(c))


main()