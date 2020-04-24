import sys
import random
import string

class MineAlgo:
	mine = [[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0]]

	fMineSet = False

	def setMine(self , mineNum , outRow , outCol):
		row = 0
		col = 0
		i = 0

		self.mine = [[0,0,0,0,0,0,0,0,0,0],
			     [0,0,0,0,0,0,0,0,0,0],
			     [0,0,0,0,0,0,0,0,0,0],
			     [0,0,0,0,0,0,0,0,0,0],
			     [0,0,0,0,0,0,0,0,0,0],
			     [0,0,0,0,0,0,0,0,0,0],
			     [0,0,0,0,0,0,0,0,0,0],
			     [0,0,0,0,0,0,0,0,0,0],
			     [0,0,0,0,0,0,0,0,0,0],
			     [0,0,0,0,0,0,0,0,0,0]]

		random.seed()
		while i < mineNum:
			row = random.randint(0, 9)
			col = random.randint(0, 9)
			#print 'col:%d' % col
			#print 'row:%d' % row
			if (self.mine[row] [col]!= 9 and ( row != outRow or col != outCol)):
				#print 'mineset:%d' %i
				self.mine[row][col] = 9
				i = i + 1

	def setMineNum(self):
		for i in range(0,10):
			for j in range(0,10):
				if (self.mine[i][j] != 9) :
					summ = self.checkMineNum(i,j)
					self.mine[i][j] = summ
					#print "row: %d col: %d count:%d" % (i,j, summ)
		fMineSet = True

	def checkMineNum(self,ii,jj):
		count = 0
		top = 0
		bottom = 0
		left = 0
		right = 0

		if ii-1>0:
			top = ii-1
		else:
			top = 0

		if ii+1<10:
			bottom = ii+1
		else:
			bottom = 9

		if jj-1>0:
			left = jj-1
		else :
			left = 0

		if jj+1<10:
			right = jj+1
		else:
			right = 9

		#print "top%d bottom%d left %d right%d" % (top, bottom, left, right)
		for i in range(top, bottom+1):
			for j in range(left,right+1):
				if self.mine[i][j] == 9:
					count = count + 1
		#print count
		return count

	def printMine(self):
		for i in range(0,10):
			#print "row: %d" %i
			for j in range(0,10):
				print("%d " % self.mine[i][j] ,)
			print('\n')
		#print self.mine

	def __init__ (self,mineNum,outRow, outCol):
		self.setMine(mineNum,outRow,outCol)
		self.setMineNum()

if __name__ == "__main__":
	#print  "argv %s %s %s" % (sys.argv[1],  sys.argv[2] , sys.argv[3])
	mine = MineAlgo(string.atoi(sys.argv[1]),string.atoi(sys.argv[2]),string.atoi(sys.argv[3]))
	mine.printMine()
