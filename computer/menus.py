from setting import Settings
import tkinter
import math
class menuss():
    def __init__(self):
        #创建主界面
        ai_set = Settings()
        self.root = tkinter.Tk()
        self.root.minsize(280, 450)
        self.root.maxsize(280, 470)
        self.root.title(ai_set.title_1)
        #创建面板上的一些变量
        self.result = tkinter.StringVar() #StringVar()能够自动刷新的字符串变量
        self.result.set(0)
        #设置一个全局变量列表 储存运算数字和符号
        self.lists = []
        self.m_history = []
        #设置一个判断有无运算符号按下的标志
        self.press_sign = False
        self.menus()
        self.layout()
        self.root.mainloop()
    def menus(self):
        #创建一个菜单
        window = tkinter.Menu(self.root)
        #添加子菜单
        filemenus = tkinter.Menu(window, tearoff=0)
        filemenus.add_command(label="标准型(T)          ALT+1", command=self.myfunc)
        window.add_cascade(label="查看(V)", menu=filemenus)
        self.root.config(menu=window)
    def layout(self):
        #计算器主界面的摆放
        result = tkinter.StringVar()
        result.set(0)
        #显示界面
        show_label1 = tkinter.Label(self.root, bd=3, bg='white', font = ('宋体', 30), anchor='e', textvariable=self.result)
        show_label1.place(x = 5, y = 20, width = 270, height = 70)
        #mc功能键
        button_mc = tkinter.Button(self.root, text='MC', command = self.MC)
        button_mc.place(x = 5, y = 95, width = 50, height = 50)
        #mr功能键
        button_mr = tkinter.Button(self.root, text = 'MR', command = self.MR)
        button_mr.place(x = 60, y = 95, width = 50, height = 50)
        #ms功能键
        button_ms = tkinter.Button(self.root, text='MS', command = self.MS)
        button_ms.place(x = 115, y =95, width = 50, height = 50)
        #功能键 左箭头
        button_del_o = tkinter.Button(self.root, text='←', command = self.del_o)
        button_del_o.place(x = 170, y =95, width = 50, height = 50)
        #功能键 C
        button_del_al = tkinter.Button(self.root, text='C', command = self.del_al)
        button_del_al.place(x = 225, y =95, width = 50, height = 50)
        #功能键±
        button_zf = tkinter.Button(self.root, text='±', command = self.zf)
        button_zf.place(x = 5, y =150, width = 50, height = 50)
        #功能键√（开根号
        button_sqrt = tkinter.Button(self.root, text='√', command = self.sqr)
        button_sqrt.place(x = 60, y =150, width = 50, height = 50)
        #数字键7
        button_seven = tkinter.Button(self.root, text='7', command = lambda: self.pressnum('7'))
        button_seven.place(x = 115, y =150, width = 50, height = 50)
        #数字键8
        button_eight = tkinter.Button(self.root, text='8', command = lambda: self.pressnum('8'))
        button_eight.place(x = 170, y =150, width = 50, height = 50)
        #数字键9
        button_nine = tkinter.Button(self.root, text='9', command = lambda: self.pressnum('9'))
        button_nine.place(x = 225, y =150, width = 50, height = 50)
        #功能键 +
        button_add = tkinter.Button(self.root, text='+', command = lambda: self.addition('+'))
        button_add.place(x = 5, y =205, width = 50, height = 50)
        #功能键 =
        button_add = tkinter.Button(self.root, text='=', command = self.equal)
        button_add.place(x = 60, y =205, width = 50, height = 50)
        #数字键4
        button_nine = tkinter.Button(self.root, text='4', command = lambda: self.pressnum('4'))
        button_nine.place(x = 115, y =205, width = 50, height = 50)
        #数字键5
        button_nine = tkinter.Button(self.root, text='5', command = lambda: self.pressnum('5'))
        button_nine.place(x = 170, y =205, width = 50, height = 50)
        #数字键6
        button_nine = tkinter.Button(self.root, text='6', command = lambda: self.pressnum('6'))
        button_nine.place(x = 225, y =205, width = 50, height = 50)
        #功能键 x
        button_add = tkinter.Button(self.root, text='x', command = lambda: self.addition('*'))
        button_add.place(x = 5, y =260, width = 50, height = 50)
        #功能键 ÷
        button_add = tkinter.Button(self.root, text='÷', command = lambda: self.addition('/'))
        button_add.place(x = 60, y =260, width = 50, height = 50)
        #数字键1
        button_nine = tkinter.Button(self.root, text='1', command = lambda: self.pressnum('1'))
        button_nine.place(x = 115, y =260, width = 50, height = 50)
        #数字键2
        button_nine = tkinter.Button(self.root, text='2', command = lambda: self.pressnum('2'))
        button_nine.place(x = 170, y =260, width = 50, height = 50)
        #数字键3
        button_nine = tkinter.Button(self.root, text='3', command = lambda: self.pressnum('3'))
        button_nine.place(x = 225, y =260, width = 50, height = 50)
        #数字键0
        button_nine = tkinter.Button(self.root, text='0', command = lambda: self.pressnum('0'))
        button_nine.place(x = 5, y =315, width = 50, height = 50)
        #小数点键.
        button_nine = tkinter.Button(self.root, text='.', command = lambda: self.pressnum('.'))
        button_nine.place(x = 60, y =315, width = 50, height = 50)
        #1/x按键
        button_nine = tkinter.Button(self.root, text='1/x', command = self.ds)
        button_nine.place(x = 115, y =315, width = 50, height = 50)
        #除号取整键//
        button_nine = tkinter.Button(self.root, text='//', command = lambda: self.pressnum('//'))
        button_nine.place(x = 170, y =315, width = 50, height = 50)
        #取余号%
        button_nine = tkinter.Button(self.root, text='%', command = lambda: self.pressnum('%'))
        button_nine.place(x = 225, y =315, width = 50, height = 50)
    #以下为功能实现函数
    def MC(self):
        self.m_history = []
    def MR(self):
        self.result.set(str(self.m_history[0]))
    def MS(self):
        self.m_history.append(self.result.get())
    def del_o(self):
        if self.result.get() == '' or self.result.get() == '0':
            self.result.set('0')
            return
        else:
            num = len(self.result.get())
            if num > 1:
                strnum = self.result.get()
                strnum = strnum[0:num-1]
                self.result.set(strnum)
            else:
                self.result.set('0')
    def del_al(self):
        self.result.set('0')
    def zf(self):
        strnum = self.result.get()
        if strnum[0] == '-':
            self.result.set(strnum[1:])
        elif strnum[0] != '-' and strnum != '0':
            self.result.set('-' + strnum)
    def sqr(self):
        strnum = self.result.get()
        #self.press_sign
        strnum = float(strnum)
        if strnum > 0:
            endnum = math.sqrt(strnum)
            self.result.set(str(endnum)[:10])
        else:
            self.result.set('erro!')
            return
        if self.lists != 0:
            self.press_sign = True
        '''
        if strnum[0] == '-':
            self.result.set("erro")
            return
        
        else:
            strnum = float(strnum)
            endnum = math.sqrt(strnum)
            self.result.set(str(endnum)[:10])
            self.press_sign = True
        '''
        self.lists.clear()
    def pressnum(self, num):
        #按键程序
        if self.press_sign == False:
            pass
        else:
            self.result.set(0)
            #重置状态
            self.press_sign = False
        old_num = self.result.get()
        if old_num == '0':
            self.result.set(num)
        else:
            new_num = old_num + num
            self.result.set(new_num)
    def addition(self, sign):
        num = self.result.get()
        #保存按下的数字
        self.lists.append(num)
        #保存按下的符号
        self.lists.append(sign)
        self.press_sign = True
    def equal(self):
        #将当前界面上的数字存入列表
        newnum = self.result.get()
        self.lists.append(newnum)
        compute = ''.join(self.lists)
        #Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
        #eval() 函数用来执行一个字符串表达式，并返回表达式的值
        eva = eval(compute)
        self.result.set(str(eva)[:10])  #保留10位小数
        if self.lists != 0:
            self.press_sign = True
        self.lists.clear()
    def ds(self):
        dsnum = 1/float(self.result.get())
        self.result.set(str(dsnum)[:10])
        if self.lists != 0:
            self.press_sign = True
        self.lists.clear()
    def myfunc(self):
        print("1")





