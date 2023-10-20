def rotate(array, x1,y1, x2,y2, rotateCnt):
    length = x2 - x1 + 1
    b = [[0 for _ in range(length)] for _ in range(length)]
    c = [[0 for _ in range(length)] for _ in range(length)]

    for i in range(length):
        for j in range(length):
            b[i][j] = array[x1+i][y1+j]

    while rotateCnt > 0:
        for i in range(length):
            for j in range(length):
                c[i][j] = b[j][length-i-1]

        for i in range(length):
            for j in range(length):
                b[i][j] = c[i][j]

        for i in range(length):
            for j in range(length):
                array[x1+i][y1+j] = b[i][j]

        rotateCnt -= 1
    return array