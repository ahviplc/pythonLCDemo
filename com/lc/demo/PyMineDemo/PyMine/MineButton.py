import wx

class MineButton(wx.BitmapButton):
    col = 0
    row = 0
    flag = 0
    clickFlag = False

    def __init__(self,parent,row, col, ticon):
        wx.BitmapButton.__init__(self,parent,size=(23,23),bitmap=ticon)
        self.icon = ticon
        self.row = row
        self.col = col

    def getClickFlag (self) :
        return(self.clickFlag)

    def setClickFlag(self, toSet) :
        self.clickFlag = toSet

    def getCol(self) :
        return(self.col)

    def getRow(self):
        return(self.row)

    def setFlag(self,flag) :
        self.flag = flag

    def getFlag(self):
        return(self.flag)

    def setIcon(self, ticon):
        self.icon = ticon
        self.SetBitmapLabel(ticon)

def main():
    app = wx.App()
    frame = wx.Frame(None)
    pane = wx.Panel(frame)
    button = MineButton(pane,3,3,wx.Bitmap("3.gif"))
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
