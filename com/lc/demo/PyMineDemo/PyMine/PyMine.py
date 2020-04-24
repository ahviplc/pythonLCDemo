# This program is written by
# the technology of wxPython GUI and the OO design
# author: Jerry Shen
# email: jerry_shen_sjf@qq.com
# release date: 2015.8.24
# released under GPLv3
# all rights reserved.

import wx
import threading as thread
import threading
import time
from MineAlgo import MineAlgo
from AboutFrame import AboutFrame
from WinFrame import WinFrame
from PyCounter import PyCounter
from MineButton import MineButton
#from dummy_threading import Thread

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class PyMine(wx.Frame):

    # Constructor of the game
    def __init__(self,parent) :
        wx.Frame.__init__(self,parent,size=(250,341))

        #total mine number
        self.numMine = 12
        #mine amount left
        self.numFlaged = 0

        self.mineCount = self.numMine
        #the seconds passed
        self.timePassed = 0
        #mine map
        self.mine = MineAlgo(self.numMine,4,4)
        # content panel
        # self.pane = wx.Panel(self,-1,name="Content")
        # the counter and restarter panel, the control panel
        self.controlPane = wx.Panel(self,-1,name="Control Panel",size=(210, 30))
        # the about frame for this application
        self.about = AboutFrame(None)

        # mine amount digitals
        self.mineNumIcon = [ wx.Bitmap("0.gif"), wx.Bitmap("1.gif"),
            wx.Bitmap("2.gif"), wx.Bitmap("3.gif"),
            wx.Bitmap("4.gif"), wx.Bitmap("5.gif"),
            wx.Bitmap("6.gif"), wx.Bitmap("7.gif"),
            wx.Bitmap("8.gif") ]

        # the mine status, default, flaged and canceled
        self.mineStatus = [ wx.Bitmap("0.gif"), wx.Bitmap("flag.gif"),
                   wx.Bitmap("question.gif") ]

        # the bomb status
        self.mineBombStatus = [ wx.Bitmap("0.gif"), wx.Bitmap("mine.gif"),
                   wx.Bitmap("wrongmine.gif"), wx.Bitmap("bomb.gif") ]

        # the upper button status
        self.faceIcon = [ wx.Bitmap("smile.gif"), wx.Bitmap("Ooo.gif")]
        # blank image
        self.myIcon = wx.Bitmap("0.gif")

        # mine counter
        self.mineCounter = PyCounter(self.controlPane, self.numMine)
        # time counter
        self.timeCounter = PyCounter(self.controlPane, 0)
        # system timer
        self.timer = PyTimer.getInst(self.timeCounter)

        #self.__panelock = threading.RLock() # used to synchronize code

        # the upper button
        self.bTest = wx.BitmapButton(self.controlPane,-1,self.faceIcon[0])
        self.bTest.Size = (30, 30)
        self.bTest.Bind(wx.EVT_BUTTON, self.OnBTestClicked)

        # the sizer for control panel
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)

        # the content panel
        self.hbox.Add(self.mineCounter,3,flag=wx.ALL|wx.ALIGN_LEFT)
        self.hbox.Add(self.bTest,1)
        self.hbox.Add(self.timeCounter,3,flag=wx.ALL|wx.ALIGN_RIGHT)
        self.controlPane.SetSizerAndFit(self.hbox)

        # the sizer for whole content panel
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.sizer = wx.GridBagSizer()

        # Begin Menu Set
        mb = wx.MenuBar()
        mGame = wx.Menu()
        mEasy = mGame.Append(wx.ID_ADD,'&Easy')
        mMiddle = mGame.Append(wx.ID_ANY,'&Middle')
        mHard = mGame.Append(wx.ID_ABORT,'&Hard')
        mGame.AppendSeparator()
        mExit = mGame.Append(wx.ID_EXIT,'E&xit')
        mb.Append(mGame,'&Game')

        mHelp = wx.Menu()
        mAbout = mHelp.Append(wx.ID_ABOUT,"&About...")
        mb.Append(mHelp,'&Help')
        # the win frame for winners
        self.winFrame = WinFrame(self,title='You win')

        self.SetMenuBar(mb)

        self.Bind(wx.EVT_MENU, self.OnEasy, mEasy)
        self.Bind(wx.EVT_MENU, self.OnMiddle, mMiddle)
        self.Bind(wx.EVT_MENU, self.OnHard, mHard)
        self.Bind(wx.EVT_MENU, self.OnExit, mExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, mAbout)

        # Buttons panel
        self.pane0 = wx.Panel(self,-1,size=(250,250))
        # Buttons
        self.mineButton = [[MineButton for col in range(10)] for row in range(10)]
        self.restartRunner = RestartRunner(self,self.winFrame,False)

        for  i in range(0,10):
            for j in range(0,10):
                self.mineButton[i][j] = MineButton(self.pane0,i,j, self.myIcon)
                self.mineButton[i][j].Bind(wx.EVT_LEFT_DOWN, self.OnMineButtonLeftClicked,id = self.mineButton[i][j].GetId())
                self.mineButton[i][j].Bind(wx.EVT_RIGHT_DOWN, self.OnMineButtonRightClicked,id = self.mineButton[i][j].GetId())
                self.mineButton[i][j].Bind(wx.EVT_LEFT_DCLICK, self.OnMineButtonLeftDoubleClicked,id = self.mineButton[i][j].GetId())
                self.sizer.Add(self.mineButton[i][j],wx.GBPosition(i,j))

        self.pane0.SetSizer(self.sizer)
        self.vbox.Add(self.controlPane)
        self.vbox.Add(self.pane0)
        self.SetSizer(self.vbox)
        self.Center()
        self.Show()

    def OnEasy(self, event):
        self.timer.Stop()
        self.numMine = 1
        self.setNewGame(self.numMine)

    def OnMiddle(self,event):
        self.timer.Stop()
        self.numMine = 24
        self.setNewGame(self.numMine)

    def OnHard(self,event):
        self.timer.Stop()
        self.numMine = 36
        self.setNewGame(self.numMine)

    def OnExit(self,event):
        self.Close()

    def OnAbout(self,event):
        self.about.Show()

    def OnBTestClicked(self, e):
        self.setNewGame(self.numMine)
        e.Skip()

    def OnMineButtonLeftClicked(self, e):
        #self.__panelock.acquire()
        print("LeftButton down")
        btId = e.GetId()
        print("id: %d" % btId)

        button = self.pane0.FindWindowById(btId)
        #print "%s", type(button)
        row = button.getRow()
        col = button.getCol()
        print("row:%d, col:%d" % (row, col))

        if PyTimer.getRunFlag() == False :
            self.startNewGame(self.numMine, row, col)
            e.Skip()
        else :
            self.checkMine(row, col)
            e.Skip()
        #self.__panelock.release()

    def OnMineButtonRightClicked(self, e):
        print("RightButton down")
        btId = e.GetId()
        print("id: %d" % btId)

        button = self.pane0.FindWindowById(btId)
        print("%s", type(button))
        row = button.getRow()
        col = button.getCol()
        print("row: %d col: %d" % (row,col))
        self.flagMine(row, col)
        e.Skip()

    def OnMineButtonLeftDoubleClicked(self, e):
        print("Left double clicked")
        btId = e.GetId()
        print("id: %d" % btId)

        button = self.pane0.FindWindowById(btId)
        print("%s", type(button))
        row = button.getRow()
        col = button.getCol()

        self.clearAll(row, col)
        e.Skip()

    def close(self, event=None):
        """Exit application."""
        self.Close(event=None)

    # if mine bomb
    def bomb(self,row, col):
        #print("Bomb!")
        self.timer.Stop()

        for i in range(0,10) :
            for  j in range(0,10):
                self.mineButton[i][j].setIcon(self.mineBombStatus[0])
                toShow = 0
                if self.mine.mine[i][j] !=9 :
                    toShow = 0
                else :
                    toShow = 1
                self.mineButton[i][j].setClickFlag(True)
                if (toShow == 1 and (i != row or j != col)):
                    self.mineButton[i][j].setIcon(self.mineBombStatus[toShow])
                    self.mineButton[i][j].setClickFlag(True)
                elif (toShow == 1 and (i == row and j== col)):
                    self.mineButton[i][j].setIcon(self.mineBombStatus[3])
                    self.mineButton[i][j].setClickFlag(True)
                elif (toShow == 0 and self.mineButton[i][j].getFlag() != 1) :
                    self.mineButton[i][j].Disable()
                elif ( toShow == 0 and self.mineButton[i][j].getFlag() == 1) :
                    self.mineButton[i][j].setIcon(self.mineBombStatus[2])
                    self.mineButton[i][j].setClickFlag(True)

    # check if you win
    def isWin(self) :
        returnVal = False
        if self.mineCount == 0 and self.mineCounter.getCounterNum() == 0:
            for i in range (0,10):
                for j in range (0,10):
                    if(self.mine.mine[i][j]==9 and self.mineButton[i][j].getFlag() != 1) :
                        returnVal = False
                    if(self.mine.mine[i][j]!=9 and self.mineButton[i][j].getFlag() == 1) :
                        returnVal = False
                    if(self.mine.mine[i][j]!=9 and self.mineButton[i][j].getClickFlag() == True) :
                        returnVal = False
                returnVal = True
        else :
            returnVal = False
        print("returnVal:" ,)
        print(returnVal)
        return returnVal

    # You Win
    def win(self):
        self.timer.Stop()
        self.restartRunner = RestartRunner(self,self.winFrame,False)
        if self.winFrame : self.winFrame.CenterOnParent()
        self.winFrame.Show()
        self.restartRunner.start()

    # the methods to check if there were mines, to be nested
    def checkMine(self, row, col) :
        # check border
        i= 0 if row<0 else row
        i= 9 if i>9 else i
        j= 0 if col<0 else col
        j= 9 if j>9 else j
        print("Check Mine row: %d: %d" %(i,j))

        # 9 stand for the mine
        if self.mine.mine[i][j] == 9:
            self.bomb(i,j)
        elif (self.mine.mine[i][j] == 0 and self.mineButton[i][j].getClickFlag() == False) :
            self.mineButton[i][j].setClickFlag(True)
            self.showLabel(i,j)
            for ii in range(i-1, i+2):
                for jj in range (j-1, j+2):
                    self.checkMine(ii,jj)
        else :
            self.showLabel(i,j)
            self.mineButton[i][j].setClickFlag(True)
            if (self.isWin()) :
                self.win()

    def clearAll(self, row, col) :
        top = 0
        bottom = 0
        left = 0
        right = 0
        count=0
        top = row-1 if row-1>0 else 0
        bottom = row+1 if row+1<10 else 9
        left = col -1 if col-1>0 else 0
        right = col +1 if col+1<10 else 9
        for i in range(top, bottom +1):
            for j in range(left, right + 1):
                if (self.mineButton[i][j].getFlag()!=1):
                    self.checkMine(i,j)

    def resetAll(self) :
        #self.timer.Stop()
        for i in range(0, 10):
            for j in range(0, 10):
                print("%d : %d" % (i,j))
                self.mineButton[i][j].setFlag(0)
                self.mineButton[i][j].setClickFlag(False)
                self.mineButton[i][j].setIcon(self.mineStatus[0])
                self.mineButton[i][j].Enable()
                self.mineButton[i][j].Refresh()

    # to flag the mine you want to flag out
    def flagMine(self,row,col) :
        i = 0 if row<0 else row
        i = 9 if i>9 else i
        j = 0 if col<0 else col
        j = 9 if j>9 else j
        if(self.mineButton[i][j].getFlag() == 0) :
            self.numFlaged = self.numFlaged + 1
        elif (self.mineButton[i][j].getFlag() == 1) :
            self.numFlaged = self.numFlaged -1

        self.mineCount = self.numMine - self.numFlaged
        if self.mineCount < 0:
            self.mineCount = 0

        self.mineCounter.resetCounter(self.mineCount)

        self.mineButton[i][j].setFlag((self.mineButton[i][j].getFlag() + 1) %3)
        self.showFlag(i,j)
        if (self.isWin()) :
            self.win()

    # show the numbers of the nearby mines
    def showLabel(self,row,col) :
        print("ShowLabel row:%d , col:%d" %(row,col))
        toShow = self.mine.mine[row][col]
        if (toShow != 0) :
            self.mineButton[row][col].setIcon(self.mineNumIcon[toShow])
            self.mineButton[row][col].setClickFlag(True)
            self.mineButton[row][col].Enabled = True
        else :
            self.mineButton[row][col].setIcon(self.mineNumIcon[0])
            self.mineButton[row][col].setClickFlag(True)
            self.mineButton[row][col].Enabled = False

    #circle the flag with blank, flaged, questioned
    def showFlag(self,row,col) :
        self.mineButton[row][col].setIcon(self.mineStatus[self.mineButton[row][col].getFlag()])
        self.mineButton[row][col].Refresh()

    # method to start the game
    def startNewGame(self,num,row,col) :
        self.mine = MineAlgo(num, row, col)
        self.mineCount = num
        self.mine.printMine()
        PyTimer.Start()
        self.checkMine(row,col)

    def setNewGame(self, num):
        PyTimer.Stop()
        self.resetAll()
        self.numMine = num
        self.numFlaged = 0
        self.mineCounter.resetCounter(num)
        self.timeCounter.resetCounter(0)

class PyTimer :
    def __init__(self):
        "disable the __init__ method"

    __inst = None # make it so-called private
    __lock = threading.RLock() # used to synchronize code
    __runFlag = False
    __timetict = 0

    innerTimeCounter = None

    @classmethod
    def getInst(cls,timeCounter):
        if (cls.__inst == None):
            cls.__inst = PyTimer()
        cls.innerTimeCounter = timeCounter
        return cls.__inst

    @classmethod
    def run(cls):
        try:
            while (cls.getRunFlag() == True):
                cls.__lock = thread.allocate()
                time.sleep(0.2)
                cls.__timetict += 1
                cls.innerTimeCounter.resetCounter(cls.__timetict//5)
                print("zzz")
                if cls.__lock.acquire():
                    cls.__lock.release()
        except (BaseException , data):
            print(data)

    @classmethod
    def getRunFlag(cls):
        return cls.__runFlag

    @classmethod
    def Stop(cls):
        if cls.getRunFlag() == True :
            cls.__timetict = 0
            cls.__runFlag = False

    @classmethod
    def Start(cls):
        if cls.getRunFlag() == False :
            cls.__runFlag = True
            cls.__timetict = 0
            thread.start_new(cls.run, ())

@singleton
class RestartRunner(threading.Thread):
    def __init__(self,pyMine,mywin,isMineSet):
        threading.Thread.__init__(self)
        self.win = mywin
        self.isMineSet = False
        self.mine = pyMine

    def run(self):
        self.isMineSet = False
        while (self.win.getWinOk() == False and self.isMineSet == True):
            print("wait...")

            #self.win.CenterOnParent()
            #self.win.Show()
            if (self.win.getWinOk() == True):
                self.mine.setNewGame(self.win.getMineNum())
                self.win.Stop()
                self.win.Hide()

def main():
    app = wx.App()
    mineFrame = PyMine(None)
    app.MainLoop()

if __name__ == '__main__':
    main()
