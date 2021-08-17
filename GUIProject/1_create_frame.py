from tkinter import *

root = Tk()
root.title("My GUI")
# 가로 x 세로 + 위치(x좌표) + 위치(y좌표)
root.geometry("640x480+300+100")

# x(너비), y(높이) 값 변경 여부
root.resizable(False, True)


root.mainloop()
