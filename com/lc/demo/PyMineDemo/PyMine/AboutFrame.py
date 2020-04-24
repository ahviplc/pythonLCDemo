import wx

class AboutPanel(wx.Panel):
    def __init__(self,parent, style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)|wx.STAY_ON_TOP):
        """Create the DemoPanel."""
        wx.Panel.__init__(self, parent,style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)|wx.STAY_ON_TOP)

        msg = wx.StaticText(self, 1, "PyMine written by Jerry Shen.", wx.Point(15, 30));
        msg1 = wx.StaticText(self, 2, "         Enjoy!           ", wx.Point(15, 30));
        msg2 = wx.StaticText(self, 3, "Vision 1.1                ", wx.Point(15, 30));
        msg3 = wx.StaticText(self, 4, "Date August 24th,2015     ", wx.Point(15, 30));

        CloseBtn = wx.Button(self, label="Close")
        CloseBtn.Bind(wx.EVT_BUTTON, parent.close)

        Sizer = wx.BoxSizer(wx.VERTICAL)

        Sizer.Add(msg)
        Sizer.Add(msg1)
        Sizer.Add(msg2)
        Sizer.Add(msg3)
        Sizer.Add(CloseBtn)

        self.SetSizerAndFit(Sizer)

class AboutFrame(wx.Frame):
    def __init__(self,parent, *args, **kwargs):
        wx.Frame.__init__(self,parent,size=(250,200))

        # Add the Widget Panel
        self.Panel = AboutPanel(self)
        self.Fit()
        self.Center()

    def close(self, event=None):
        """Exit application."""
        self.Hide()

if __name__ == '__main__':
    app = wx.App()
    frame = AboutFrame(None,title="About PyMine")
    frame.Size = (300, 200)
    frame.Show()
    app.MainLoop()

