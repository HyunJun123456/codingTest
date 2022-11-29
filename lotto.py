
import wx
import random


class Mainframe(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(300, 450))
        panel = wx.Panel(self)
        self.count = wx.TextCtrl(panel, id=1, pos=(5, 5))
        self.count.SetHint("시행 횟수 입력")
        self.generate_button = wx.Button(panel, id=2, label='생성', pos=(5, 50))
        self.output = wx.ListBox(panel, id=3, choices=[], pos=(120, 5), size=(150, 400))

        fixed_number_box = wx.StaticBox(panel, id=5, label="고정수", pos=(5, 100), size=(80, 50))
        self.fixed_number_1 = wx.TextCtrl(fixed_number_box, id=6, size=(30, 20), pos=(5, 20))
        self.fixed_number_2 = wx.TextCtrl(fixed_number_box, id=7, size=(30, 20), pos=(40, 20))
        self.fixed_number_check = wx.CheckBox(panel, id=8, pos=(100, 120))

        self.Bind(wx.EVT_BUTTON, self.lotto, id=2)

    def lotto(self, event):
        for i in range(int(self.count.GetValue())):
            number = set()
            if self.fixed_number_check.GetValue():
                try:
                    fixed_number_1 = int(self.fixed_number_1.GetValue())
                    number.add(fixed_number_1)
                except:
                    pass
                try:
                    fixed_number_2 = int(self.fixed_number_2.GetValue())
                    number.add(fixed_number_2)
                except:
                    pass
            while len(number) < 6:
                number.add(random.randint(1, 45))
            number = list(number)
            number.sort()
            self.output.Append(str(number))


def run():
    app = wx.App()
    frame = Mainframe(None, -1, 'Lotto Number Generator')
    frame.Show()
    app.MainLoop()


run()