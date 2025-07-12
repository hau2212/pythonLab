"""
nguyen thanh hau
24-0-00627
chuong 6 bai 8
"""

def tinhToan(fileName):
    wordInFile = 0
    temp = 0
    longestInFile = 0
    avegareInFile = 0
    i = 1
    with open(fileName,"r") as file:
        for line in file:
            wordInFile += int(line)
            i+=1
            if longestInFile <= int(line):
                longestInFile = int(line)
        avegareInFile = wordInFile / i

        print(wordInFile , longestInFile , avegareInFile)

tinhToan("Ch6/steps.txt")
