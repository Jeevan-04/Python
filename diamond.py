# Upper part of the pattern
for i in range(1, 5):
    for k in range(5, i, -1):
        print('  ', end='')
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

# Lower part of the pattern
for i in range(5, 0, -1):
    for k in range(i, 5, +1):
        print('  ', end='')
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
