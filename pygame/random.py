import random
import time
x = 0
y = 1
while True:
    print(f"나무를 {x} 번 찍었다.")
    x += 1
    time.sleep(0.01)
    if x == 10:
        a = random.uniform(0, 10)
        if a >= 5:
            print("넘어간다아ㅏㅏ")
            total = 100 * (1 / y)
            print(f"당신의 확률은 {total}% 입니다.")
            break
        else:
            print("나무는 '텟카이'를 썼다! 데미지를 주지 못했다!")
            x = 0
            print(f"{y} 번째 실패입니다")
            y += 1
            time.sleep(0.5)
            print("기력 회복중 .", end="")
            time.sleep(0.5)
            print(".", end="")
            time.sleep(0.4)
            print(".", end="")
            time.sleep(1)
