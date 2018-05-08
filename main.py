import wx
import get_time
import datetime

# print(time.time())
#
# nowTime = time.localtime(time.time())
# print(nowTime)
def get_dead_line():
    nowTime = datetime.datetime.now()

    workTime = datetime.datetime(2019, 7, 1, 0, 00, 00,)

    deadLine = workTime - nowTime
    #print(deadLine)
    return str(deadLine)


# class Frame(wx.Frame):
#     def __init__(self, image, parent=None, id=-1):
#         pos = wx.DefaultPosition
#         title = 'Countdown of finding work'
#

class MyFrame(wx.Frame):
    def __init__(self,parent=None,id=-1,
                 title='',pos=wx.DefaultPosition,
                 size=wx.DefaultSize,style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self,parent,id,title,pos,size,style)
        self.InitUI()
        pass
    def InitUI(self):
        countdown = get_dead_line()
        self.SetBackgroundColour('#ffffff')

        content = wx.StaticText(self,-1,'离找工作还有  ' + countdown,pos=(20,20))
        content.SetForegroundColour('#000000')
        content1 = wx.StaticText(self,-1,'作者：烤肉',pos=(50,50))
        pass


class App(wx.App):
    def OnInit(self):
        self.frame = MyFrame(id=-1,title='Countdown of finding work',pos=(10,10),size=(230,230))
        self.frame.Show()

        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()