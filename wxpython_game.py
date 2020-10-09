#!/bin/user/python
import wx, random


class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        self.num1 =random.randint(0,25)
        self.num2 = random.randint(75,100)
        self.SetNum = random.randint(self.num1,self.num2)
        # self.UserMin = wx.StaticText(self, label= '你想要的最小值',pos=(20,20))
        # self.SetMin = wx.TextCtrl(self, value = '', pos= (135,20), size=(140,-1))
        # self.UserMax = wx.StaticText(self, label = '你想要的最大值', pos=(20,40))
        # self.SetMax = wx.TextCtrl(self, label = '', pos = (135,40),size = (140,-1))
        # self.num1 = int(self.SetMin.GetValue())
        # self.num2 = int(self.SetMax.GetValue())
        # self.SetNum = random.randint(self.num1,self.num2)
        wx.Panel.__init__(self, parent)
        self.Cycle = wx.StaticText(self, label="范围是{0}--{1}".format(self.num1,self.num2), pos=(20, 30))

        # 这个多行的文本框只是用来记录并显示结果
        self.Result = wx.TextCtrl(self, pos=(20, 100), size=(300, 200), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # 仅有1行的编辑控件
        self.UserNum = wx.StaticText(self, label="你猜的数字", pos=(20, 60))
        self.GuessNum = wx.TextCtrl(self, value="", pos=(150, 60), size=(140, -1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.GuessNum)

    def EvtText(self, event):
        if int(self.GuessNum.GetValue()) > self.SetNum:
            self.Result.AppendText('太大了\n')
        elif int(self.GuessNum.GetValue()) < self.SetNum:
            self.Result.AppendText('太小了\n')
        else:
            self.Result.AppendText('答对了\n')


app = wx.App(False)
frame = wx.Frame(None)
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()
