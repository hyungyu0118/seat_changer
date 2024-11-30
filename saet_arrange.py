import random
import time
import os

def generate_new_grid(previous_grid, corner_numbers):
    numbers = list(range(1, 26))
    for num in corner_numbers:
        numbers.remove(num)
    random.shuffle(numbers)
    
    new_grid = [[0 for _ in range(5)] for _ in range(5)]
    
    # 떠드는놈들 배치
    corners = [(0, 0), (0, 4), (4, 0), (4, 4)]
    random.shuffle(corners)
    for i, (x, y) in enumerate(corners[:len(corner_numbers)]):
        new_grid[x][y] = corner_numbers[i]
    
    # 조용한 범생이 친구들
    idx = 0
    for i in range(5):
        for j in range(5):
            if new_grid[i][j] == 0:
                new_grid[i][j] = numbers[idx]
                idx += 1

    return new_grid

def display_grid(grid, delay=False):
    if delay:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("새로운 자리배치 결과:")
        for i in range(5):
            for j in range(5):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("새로운 자리배치 결과:")
                for k in range(5):
                    row = grid[k]
                    if k < i:
                        print(' '.join(f'{num:2d}' for num in row))
                    elif k == i:
                        row_display = row[:j] + [grid[i][j]] + ['  ']*(5-j-1)
                        print(' '.join(f'{num:2d}' if isinstance(num, int) else f'{num:2s}' for num in row_display))
                    else:
                        print(' '.join(f'  ' for _ in range(5)))
                time.sleep(1)
    else:
        for row in grid:
            print(' '.join(f'{num:2d}' for num in row))

# 현재 자리
previous_grid = [
    [17, 10, 1, 23, 8],
    [20, 5, 9, 16, 18],
    [24,19, 25, 12, 7],
    [2, 21, 11, 15, 6],
    [13, 4, 22, 14, 3]
]

# 수업의 볼륨을 채워주는 아름다운 친구들을 위한 꼭짓점 배치
corner_numbers = [3, 8, 13, 17]

# 자리뽑기
new_grid = generate_new_grid(previous_grid, corner_numbers)

print("이전 자리배치:")
display_grid(previous_grid)

input("새로운 자리배치를 확인하려면 엔터를 누르세요.")

display_grid(new_grid, delay=True)

input("프로그램을 종료하려면 엔터를 누르세요.")
input("이 자리배치가 마음에 안든다구요???")
input("어쩔팁이")