import random

secret = random.randint(1, 100)
temp = input("猜猜我心里想的是哪个数字：")
guess = int(temp)

while guess != secret:
    temp = input("哎呀，你猜错了，请重新输入吧：")
    guess = int(temp)

    if guess == secret:
        print("恭喜，你猜对了！")
    else:
        if guess > secret:
            print("哥，大了大了~~~~")
        else:
            print("哥，小了小了~~~~")
print("游戏结束了，不玩了")