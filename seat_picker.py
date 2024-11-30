import random
import time

def generate_seats(rows, cols):
    total_seats = rows * cols
    numbers = list(range(1, total_seats + 1))
    random.shuffle(numbers)

    seat_grid = []
    for i in range(rows):
        row = numbers[i * cols: (i + 1) * cols]
        seat_grid.append(row)

    return seat_grid

def display_seats(seat_grid):
    print("\n자리 배치 결과:")
    for row in seat_grid:
        print(" ".join(f"{num:2}" for num in row))

def main():
    print("자리 뽑기 프로그램에 오신 걸 환영합니다!")
    rows = 5  # 행 고정
    cols = 5  # 열 고정
    
    print("\n자리 번호를 무작위로 뽑고 있습니다...\n")
    seat_grid = generate_seats(rows, cols)
    
    for i in range(rows * cols):
        print(f"번호 뽑기: {i + 1}번 자리가 선택됨...")
        time.sleep(0.2)  # 긴장감 추가
    display_seats(seat_grid)

if __name__ == "__main__":
    main()