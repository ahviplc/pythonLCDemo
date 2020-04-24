#!python 
import wx

class PyCounter(wx.Panel):
    counter = []
    __numSet = []
    counterNum = 0

    def __init__(self,parent, num):
        wx.Panel.__init__(self,parent,size=(90,30),name="PyCounter Test")
        self.numSet =  [ wx.Bitmap("c0.gif"), wx.Bitmap("c1.gif"),
                        wx.Bitmap("c2.gif"), wx.Bitmap("c3.gif"),
                        wx.Bitmap("c4.gif"), wx.Bitmap("c5.gif"),
                        wx.Bitmap("c6.gif"), wx.Bitmap("c7.gif"),
                        wx.Bitmap("c8.gif"), wx.Bitmap("c9.gif")]

        self.counterNum = num

        ones = self.counterNum % 10
        tens = self.counterNum % 100 // 10
        hundreds = self.counterNum % 1000 // 100

        #print "%d : %d : %d" % (hundreds, tens, ones)

        self.counter = [ wx.BitmapButton(self,-1,self.numSet[hundreds],size=(26,30)),
                         wx.BitmapButton(self,-1,self.numSet[tens],size=(26,30)),
                         wx.BitmapButton(self,-1, self.numSet[ones], size=(26,30))]

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        for i in range(0,3):
            hbox.Add(self.counter[i])

        self.SetSizerAndFit(hbox)
        self.Center()
        self.Show()

    def getCounterNum(self):
        return(self.counterNum)

    def setCounterNum(self,num):
        self.counterNum = num

    def resetImage(self, num) :
        ones = num % 10
        tens = num % 100 // 10
        hundreds = num % 1000 // 100

        print("num: %d" % (num))
        print("%d:%d:%d" % (hundreds,tens, ones))

        self.counter[0].SetBitmapLabel(self.numSet[hundreds])
        self.counter[1].SetBitmapLabel(self.numSet[tens])
        self.counter[2].SetBitmapLabel(self.numSet[ones])
        self.counter[0].Refresh()
        self.counter[1].Refresh()
        self.counter[2].Refresh()

    def resetCounter(self,num):
        self.setCounterNum(num)
        self.resetImage(num)
        self.Refresh()

def main():
    app = wx.App()
    pf = wx.Frame(None)
    pc = PyCounter(pf,394)
    pc.resetCounter(12)
    pc.Refresh()
    pf.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
