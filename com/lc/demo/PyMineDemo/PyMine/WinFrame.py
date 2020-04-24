import wx
import threading
import threading as thread

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class WinFrame(wx.Frame,Singleton):
    def __init__(self, parent,style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)|wx.STAY_ON_TOP, *args, **kw):
        """Create the WinPanel."""
        wx.Frame.__init__(self, parent, style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)|wx.STAY_ON_TOP, *args, **kw)

        self.parent = parent  # Sometimes one can use inline Comments

        self.mineCount = 0

        self.winTimer = WinTimer()

        msg = wx.StaticText(self, 1, "  Congratulation!  ", wx.Point(15, 30))
        msg1 = wx.StaticText(self, 2, "   You win.   ", wx.Point(15, 30))
        msg2 = wx.StaticText(self, 3, "  Click to restart!  ", wx.Point(15, 30))
        easy = wx.Button(self, label="Easy")
        easy.Bind(wx.EVT_BUTTON,self.OnEasyButtonClicked)
        middle = wx.Button(self, label="Middle")
        middle.Bind(wx.EVT_BUTTON, self.OnMiddleButtonClicked)
        hard = wx.Button(self, label="Hard")
        hard.Bind(wx.EVT_BUTTON, self.OnHardButtonClicked)

        self.closeBtn = wx.Button(self, label="Close")
        self.closeBtn.Bind(wx.EVT_BUTTON, self.OnCloseButtonClicked)
        self.Bind(wx.EVT_CLOSE,self.close)

        Sizer = wx.BoxSizer(wx.VERTICAL)

        Sizer.Add(msg)
        Sizer.Add(msg1)
        Sizer.Add(msg2)
        Sizer.Add(easy)
        Sizer.Add(middle)
        Sizer.Add(hard)
        Sizer.Add(self.closeBtn)

        self.SetSizerAndFit(Sizer)
        self.level = 0
        self.isOk = False;

    def getMineNum(self) :
        return (self.level*12)

    def getWinOk(self) :
        return (self.isOk)

    def setWinOk(self, flag):
        self.isOk = flag;

    def close(self, event=None):
        """Exit application."""
        self.parent.Close()


    def Stop(self):
        if self.getWinOk() == True:
            self.setWinOk(False)

    def Start(self):
        if self.getWinOk() == False:
            self.setWinOk(True)


    def Ready(self):
        self.setWinOk(False)

    def OnEasyButtonClicked(self, e):
        self.Stop()
        self.mineCount = 12
        self.parent.setNewGame(self.mineCount)
        self.setWinOk(True)
        self.parent.timer.Stop()
        self.Hide()
        e.Skip()

    def OnMiddleButtonClicked(self, e):
        self.Stop()
        self.mineCount = 24
        self.parent.setNewGame(self.mineCount)
        self.setWinOk(True)
        self.parent.timer.Stop()
        self.Hide()
        e.Skip()

    def OnHardButtonClicked(self, e):
        self.Stop()
        self.mineCount = 36
        self.parent.setNewGame(self.mineCount)
        self.setWinOk(True)
        self.parent.timer.Stop()
        self.Hide()
        e.Skip()

    def OnCloseButtonClicked(self, e):
        self.close()

    def getMineNum(self):
        return self.mineCount

class WinTimer(threading.Thread,Singleton) :
    def __init__(self):
        "disable the __init__ method"
        threading.Thread.__init__(self,group=None)
        self.start()

    def run(self):
    	try:
            while (self.getWinOk() == True):
                self.acquire()
                time.sleep(1)
                print("zbzbzb")
                self.release()
    	except :
    	    print("error")

if __name__ == '__main__':
    app = wx.App()
    frame = WinFrame(None, title="You win")
    frame.Size = (300, 200)
    frame.Show()
    app.MainLoop()
