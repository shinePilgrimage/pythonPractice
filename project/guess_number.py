import random
import time
# random_number = random.randint(1, 10000)  # 通过random模块randint方法获取一个随机值，通过input函数获取用户的输入。
# guess_number = int(input("请输入数字: "))


def get_random_number(start=0, end=10**3):
    return random.randint(start, end)


def count_down(seconds=3, message=""):
    """
    : param seconds: 倒数的秒数
    : param message:  倒计时结束后输出的提示信息
    : return:
    """
    for _ in range(seconds, 0, -1):
        print(_)
        time.sleep(1)
        if _ == 1:
            print(message)


def serve_forever():
    random_number = get_random_number()
    print(random_number)
    count_down(message="猜数字游戏开始！！！")
    while True:
        try:
            guess_number = int(input("请输入你猜的数字: " + "_"*4 + "\b"*4))
        except ValueError:
            print("请输入合法的数字")
        if guess_number != random_number:
            if guess_number > random_number:
                print("你输入的数字大了")
                continue
            else:
                print("你输入的数字小了")
                continue
        print("你猜对了！！！")

        if input("按键盘任意键继续玩猜数字游戏或输入quit退出游戏:____\b\b\b\b").lower() == "quit":
            break
        else:
            random_number = get_random_number()
            print(random_number)
    print("游戏结束！！！")


if __name__ == "__main__":
    serve_forever()