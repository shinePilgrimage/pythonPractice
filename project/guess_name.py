import time


def count_down(seconds=3, message=""):
    for _ in range(seconds, 0, -1):
        print(_)
        time.sleep(1)
    else:
        print(message)


def build_find_table(data):
    find_table = {}
    for name in data:
        find_table_ = find_table
        for char in name:
            if char not in find_table_:
                find_table_[char] = {}
            find_table_ = find_table_[char]
    print(find_table)
    return find_table


def guess_name():
    stars = ("成龙", "刘德华", "刘诗诗", "王李丹妮", "迪丽热巴", "邓超", "王一博")
    # 构造一个查找表
    find_table = build_find_table(stars)  # 对象实例化
    count_down(3, "猜姓名游戏开始！！！")
    message = {0: "请不要瞎猜！", 1: "不错，有点接近了", 2: "厉害，比较接近了", 3: "哇塞，你是个猜姓名天才，请收下我的膝盖"}
    end = 2

    while True:
        name = input("请输入你要猜的姓名:____\b\b\b\b")  # ‘\b’:主要功能是将光标倒退指定长度的字符
        if name == "quit":
            print("游戏结束!!!")
            break
        if name in stars:
            print(message[3])
            if input("按键盘任意键继续玩猜数字游戏或输入quit退出游戏:____\b\b\b\b").lower() == "quit":
                break
        else:
            find_table_ = find_table
            index = 0
            for word in name:
                if word in find_table_:
                    find_table_ = find_table_[word]
                    index = index + 1 if index < end else index
                else:
                    break
            print(message[index])


if __name__ == "__main__":

    guess_name()

