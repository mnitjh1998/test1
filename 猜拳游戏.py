"""
1.电脑随机出拳-random
2.人的话采用input函数手动输入；
3.石头剪刀布，分别用什么来表示；
4.if-elif 语句判断
"""
import random
computer = random.randint(0, 2)
player = int(input("请输入您的拳头，石头为1，剪刀为2，布为0:"))
if ((player == 1) and (computer == 2)) or ((player == 0) and (computer == 1)) or ((player == 2) and (computer == 0)):
    print("恭喜玩家获胜")
elif computer == player:
    print("您和电脑是平局，再来一局")
else:
    print("恭喜电脑获胜")
