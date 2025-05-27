rows = 10

for i in range(1, rows + 1):
    stars_left = '*' * i
    spaces = ' ' * (rows - i)
    stars_middle = '*' * (rows - i + 1)
    stars_right = '*' * i
    
    print(f"{stars_left}{spaces}{stars_middle}{spaces}{stars_right}")