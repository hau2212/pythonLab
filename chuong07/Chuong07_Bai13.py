"""
nguyen thanh hau
24-0-00627
chuong 07 bai 13
"""
import random


def userInput(tempt_content):
    while True:
        temptInput = input("nhap vao cau hoi : ")
        tempt_anser = random.choice(tempt_content)
        print(tempt_anser)
    return

def main():
    content = []
    with open("Chương 07/8_ball_responses.txt","r") as file:
        for line in file:
            content.append(line.strip("\n"))
    userInput(content)


main()