def rock(n, m):
    table = [['L' for x in range(n+1)] for y in range(m+1)]
    for i in range(1, n+1):
        if table[i - 1][0] == 'W':
            table[i][0] = 'L'
        else:
            table[i][0] = 'W'
    for j in range(1, m+1):
        if table[0][j - 1] == 'W':
            table[0][j] = 'L'
        else:
            table[0][j] = 'W'
    for i in range(1, n+1):
        for j in range(1, m+1):
            if table[i-1][j-1] == 'W' and table[i][j-1] == 'W' and table[i-1][j] == 'W':
                table[i][j] = 'L'
            else:
                table[i][j] = 'W'
    table[0][0] = ' '
    return table


while True:
    n = int(input("enter number of rows: "))
    m = int(input("enter number of columns: "))
    if n == 0 and m == 0:
        print("try other than two zeros")
    else:
        break

row, col = n, m
if row > col:
    col = row
else:
    row = col
t = rock(row, col)

for i in range(n+1):
    print(i, end=' ')
    for j in range(m+1):
        print(t[i][j], end='  ')
    print('\n')

if t[n][m] == 'L':
    print("you'll lose")
else:
    print("you'll win")
# 10*10
# 0    W  L  W  L  W  L  W  L  W  L
#
# 1 W  W  W  W  W  W  W  W  W  W  W
#
# 2 L  W  L  W  L  W  L  W  L  W  L
#
# 3 W  W  W  W  W  W  W  W  W  W  W
#
# 4 L  W  L  W  L  W  L  W  L  W  L
#
# 5 W  W  W  W  W  W  W  W  W  W  W
#
# 6 L  W  L  W  L  W  L  W  L  W  L
#
# 7 W  W  W  W  W  W  W  W  W  W  W
#
# 8 L  W  L  W  L  W  L  W  L  W  L
#
# 9 W  W  W  W  W  W  W  W  W  W  W
#
# 10 L  W  L  W  L  W  L  W  L  W  L
