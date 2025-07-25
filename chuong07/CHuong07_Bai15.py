"""
nguyen thanh hau
24-0-00627
chuong 7 bai 15
ve mathploit bieu do khi hang tuan
"""
import matplotlib.pyplot as plt
def veBieuDo(tempt_content):
    plt.title("Bieu do tieu thu Gas hang tuan")
    plt.ylim(0, 2)
    plt.grid(True)
    plt.xticks(list(tempt_content.keys())[::5])
    plt.yticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5])
    plt.xlabel("Tuan")
    plt.ylabel("muc do tieu thu ")
    plt.bar(tempt_content.keys(),tempt_content.values())
    plt.show()
    return

def main():
    content = {}
    with open("Chương 07/1994_Weekly_Gas_Averages.txt","r") as file:
        for week,val in enumerate(file,start=1):
            content[week] = float(val)
        print(content)
    veBieuDo(content)

main()