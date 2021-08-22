from tkinter import *
from makefolder import MakeFolder

mk = MakeFolder()


root = Tk()
root.title("테스트")
root.geometry("360x360")
btn1 = Button(root, text="포토샵", command=mk.makeRoot)
btn2 = Button(root, text="메모장")
btn1.pack()
btn2.pack()
root.mainloop()
