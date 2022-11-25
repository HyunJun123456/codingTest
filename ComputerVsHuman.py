import random

computer, user = 0, 0

for i in range(1, 11, 1):
    computer = random.randint(1, 5)
    print("게임", i, "회:", end="")
    user = int(input("컴퓨터가 생각한 숫자는 ? "))

    if computer == user:
        print("맞혔네요. 축하합니다!!")
        break
    else:
        print("아까워요.", computer, "였는데요. 다시 해보세요. ㅠㅠ")
        continue
print("게임을 마칩니다.")