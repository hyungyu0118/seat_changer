import random
import time
import os

def generate_new_grid(previous_grid):
    # 이전 자리배치의 숫자들을 리스트로 변환
    numbers = list(range(1, 26))
    random.shuffle(numbers)
    new_grid = [numbers[i:i+5] for i in range(0, 25, 5)]

    # 같은 행과 같은 열에 같은 숫자가 있는지 확인하고 교환
    for i in range(5):
        for j in range(5):
            if new_grid[i][j] == previous_grid[i][j]:
                # 다른 위치에서 중복되지 않는 숫자 찾기
                for k in range(5):
                    for l in range(5):
                        if (k != i or l != j) and new_grid[k][l] != previous_grid[k][l] and new_grid[k][l] != new_grid[i][j]:
                            new_grid[i][j], new_grid[k][l] = new_grid[k][l], new_grid[i][j]
                            break
                    if new_grid[i][j] != previous_grid[i][j]:
                        break

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

# 사용자가 입력한 이전 자리배치표
previous_grid = [
    [4, 11, 18, 10, 20],
    [1, 3, 12, 14, 22],
    [5, 9, 15, 25, 2],
    [19, 8, 17, 13, 21],
    [24, 7, 16, 6, 23]
]

# 새로운 그리드 생성
new_grid = generate_new_grid(previous_grid)

print("이전 자리배치:")
display_grid(previous_grid)

input("새로운 자리배치를 확인하려면 엔터를 누르세요.")

display_grid(new_grid, delay=True)