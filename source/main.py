import random
from ot import *

print("欢迎使用GPA比较器")
print("本项目的Github地址为: https://github.com/Oyyko/GPA-Compare")
print("用法简介: 两人一人为Alice,一人为Bob,听从程序的命令发送相关的json文件给对方即可,可以使用QQ或者email发送文件。最终只有Bob会知道结果，请Bob将结果告知Alice。")

name = input("请输入姓名(Alice or Bob):")

if name == "Alice":

    ll = list(range(1, 1001))
    random.shuffle(ll)
    b = input('请输入Alice的GPA乘以100(例如3.7输入370)： ')
    b = int(b)

    y = list(range(1, 1001))

    for i in range(0, 1000):
        if i == b:
            y[i] = ll[i]
        elif i > b:
            y[i] = ll[i]+1000
        else:
            y[i] = ll[i]+2000

    for i in range(0, 1000):
        y[i] = (str(y[i]).rjust(4, '0').encode())

    alice = Alice(y, 1, len(y[0]))

    alice.setup()

    print('请将生成的json文件 alice_setup.json 发送给对方(比如通过QQ发送)，然后等待对方发送json文件 \n 请将收到的文件与本文件放在同一个文件夹下')

    input('在确认收到bob_setup.json后按下回车键继续')

    alice.transmit()

    print('请将生成的json文件 alice_dec.json 发送给对方')
    print('请等待Bob告知你结果')

elif name == "Bob":
    print("请接受alice_setup.json\n请将收到的文件与本文件放在同一个文件夹下")
    b = input('\n在接受完毕之后，请输入Bob的GPA乘以100(例如3.7输入370)： ')
    b = int(b)
    bob = Bob([b])
    bob.setup()

    print('请将生成的json文件发送到对方的终端，然后等待对方发送json文件')

    input('在确认收到alice_dec.json后按下回车键继续')

    x = bob.receive()

    if int(x[0].decode()) > 1999:
        print('Alice更大')
    elif int(x[0].decode()) < 1000:
        print('一样大')
    else:
        print('Bob更大')

else:
    print("名字必须是Alice或者Bob")

input()
input()