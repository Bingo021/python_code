"""开发画图软件的菜单"""

from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import *

# 窗口的高度和宽度
win_width = 900
win_height = 450


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.bgcolor = "#FFFFFF"
        self.x = 0
        self.y = 0
        self.fgcolor = "#000000"
        self.startDrawFlag = False
        self.lastDraw = 0
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建绘图区
        self.drawpad = Canvas(root, width=win_width, height=win_height * 0.9, bg=self.bgcolor)
        self.drawpad.pack()

        # 创建按钮
        btn_start = Button(root, text="开始", name="satrt")
        btn_start.pack(side="left", padx="10")
        btn_pen = Button(root, text="画笔", name="pen")
        btn_pen.pack(side="left", padx="10")
        btn_rect = Button(root, text="矩形", name="rect")
        btn_rect.pack(side="left", padx="10")
        btn_clear = Button(root, text="清屏", name="clear")
        btn_clear.pack(side="left", padx="10")
        btn_erasor = Button(root, text="橡皮擦", name="erasor")
        btn_erasor.pack(side="left", padx="10")
        btn_line = Button(root, text="直线", name="line")
        btn_line.pack(side="left", padx="10")
        btn_lineArrow = Button(root, text="箭头直线", name="lineArrow")
        btn_lineArrow.pack(side="left", padx="10")
        btn_color = Button(root, text="颜色", name="color")
        btn_color.pack(side="left", padx="10")

        # 事件处理
        btn_pen.bind_class("Button", "<1>", self.eventManager)
        self.drawpad.bind("<ButtonRelease-1>", self.stopDraw)

        #增加颜色处理快捷键
        root.bind("<KeyPress-r>",self.kuaijiejian)
        root.bind("<KeyPress-g>", self.kuaijiejian)
        root.bind("<KeyPress-y>", self.kuaijiejian)

    def eventManager(self, event):
        name = event.widget.winfo_name()
        print(name)
        if name == "line":
            self.drawpad.bind("<B1-Motion>", self.myline)
        elif name == "lineArrow":
            self.drawpad.bind("<B1-Motion>", self.mylineArrow)
        elif name == "rect":
            self.drawpad.bind("<B1-Motion>",self.myRect)
        elif name == "pen":
            self.drawpad.bind("<B1-Motion>",self.myPen)
        elif name == "erasor":
            self.drawpad.bind("<B1-Motion>",self.myErasor)
        elif name == "clear":
            self.drawpad.delete("all")
        elif name == "color":
            c = askcolor(color=self.fgcolor,title="选择画笔颜色")
            #[(255,0,0),"#000000"]
            self.fgcolor = c[1]

    def startDraw(self, event):
        self.drawpad.delete(self.lastDraw)

        if not self.startDrawFlag:
            self.startDrawFlag = True
            self.x = event.x
            self.y = event.y

    def stopDraw(self, event):
        self.startDrawFlag = False
        self.lastDraw = 0

    def myline(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)

    def mylineArrow(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, arrow=LAST, fill=self.fgcolor)

    def myRect(self,event):
        self.startDraw(event)
        self.lastDraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fgcolor)

    def myPen(self, event):
        self.startDraw(event)
        self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)
        self.x = event.x
        self.y = event.y

    def myErasor(self,event):
        self.startDraw(event)
        self.drawpad.create_rectangle(event.x-5, event.y-45, event.x+5, event.y+5, outline=self.bgcolor,fill=self.bgcolor)
        self.x = event.x
        self.y = event.y

    def kuaijiejian(self,event):
        if event.char =="r":
            self.fgcolor = "#ff0000"
        elif event.char =="g":
            self.fgcolor = "#00ff00"
        elif event.char =="y":
            self.fgcolor = "#ffff00"

if __name__ == '__main__':
    root = Tk()
    root.geometry(str(win_width) + "x" + str(win_height) + "+200+300")
    root.title("张嘉灏的画图软件")
    app = Application(master=root)
    root.mainloop()
