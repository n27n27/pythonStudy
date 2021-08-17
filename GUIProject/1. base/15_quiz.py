from tkinter import *
import os

root = Tk()
root.title("제목 없음 - Windows 메모장")
# 가로 x 세로 + 위치(x좌표) + 위치(y좌표)
root.geometry("640x480+300+100")
menu = Menu(root)
menu_file = Menu(menu, tearoff = 0)

# 열기, 저장 파일 이름
filename = "mynote.txt"

def openFile():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())

def saveFile():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))

menu_file.add_command(label="열기", command = openFile)
menu_file.add_command(label="저장", command = saveFile)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command = root.quit)
menu.add_cascade(label="파일", menu = menu_file)

menu_edit = Menu(menu, tearoff = 0)
menu.add_cascade(label="편집", menu = menu_edit)

menu_set = Menu(menu, tearoff = 0)
menu.add_cascade(label="서식", menu = menu_set)

menu_view = Menu(menu, tearoff = 0)
menu.add_cascade(label="보기", menu = menu_view)

menu_help = Menu(menu, tearoff = 0)
menu.add_cascade(label="도움말", menu = menu_help)

# 스크롤 바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")


# 본문 영역
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=txt.yview)

root.config(menu = menu)
root.mainloop()
