class tile(object):
	def __init__(self):
		self.sideenumerate=enumerate(['top','left','bottom','right'])
		self.coord=[]
		self.sidelabel={'top':None,'left':None,'bottom':None,'right':None}
		self.rules=[] # rules are [label, type, start,end]

	def setside(self,side,label):
		self.sidelabel[side]=label

	def getside(self,side):
		return a.sidelabel[side]

	def testenum(self):
		print self.sideenumerate

	def addRule(self,label,rtype,start,end):
		self.rules.append([label,rtype,start,end])

	def getRules(self):
		return self.rules

	def findNeighborLocations(self):
		return [[self.coord[0],self.coord[1]+1],[self.coord[0],self.coord[1]-1],[self.coord[0]+1,self.coord[1]],[self.coord[0]-1,self.coord[1]]]

	def validRule(self,side):
		valid = []
		for each in self.rules:
			if each[3] == side:
				valid.append(each)
		print 'valid',valid
		return valid


tilelist={}

#propagate determines if there are rules that are valid to activate
def propagate(tileOrigin):
	prpTiles = []
	doneTiles = []
	prpTiles.append(tileOrigin)
	while len(prpTiles)>0:
		for each in tileOrigin.findNeighborLocations():
			print each
			x = each[0]
			y = each[1]
			if tilelist[x,y]!= None:
				print 'tile found'
				#what side is this
				if x>tileOrigin.coord[0] and y==tileOrigin.coord[1]:
					print "to the right"
					activate(tileOrigin,tilelist[x,y],'right')
				if x<tileOrigin.coord[0] and y==tileOrigin.coord[1]:
					print "to the left"
					activate(tileOrigin,tilelist[x,y],'left')
				if y<tileOrigin.coord[1] and x==tileOrigin.coord[0]:
					print "to the bottom"
					activate(tileOrigin,tilelist[x,y],'bottom')
				if y<tileOrigin.coord[1] and x==tileOrigin.coord[0]:
					print 'to the top'
					activate(tileOrigin,tilelist[x,y],'top')
				doneTiles.append(tileOrigin)
				if tilelist[x,y] in doneTiles:
					print 'add to propogation list',tilelist[x,y].coord
					prpTiles.append(tilelist[x,y])
		print 'removing from prop list',tileOrigin.coord
		prpTiles.remove(tileOrigin)	


# Location has been determined to be valid, don't need to test for those things in here
def activate(tileOrigin,tileNeighbor,side):
	validrules = tileOrigin.validRule(side)
	for originrulectr in range(len(validrules)-1, -1, -1):
		originrule = validrules[originrulectr] 
		if originrule[1] == 0:
			for neighborrulectr in range(len(tileNeighbor.rules)-1, -1, -1):
				neighborrule = tileNeighbor.rules[neighborrulectr]
				#print 'compare:', originrule, neighborrule
				if originrule[1]==0 and originrule[0] == neighborrule[0] and neighborrule[1]!=0 and originrule[3]==neighborrule[2]:
					#label matches and initiation rule for origin
					if neighborrule[1] == 1:
						#change to initiation rule
						tileNeighbor.rules[neighborrulectr] = [neighborrule[0],0,None,neighborrule[3]]
					if neighborrule[1] == 2:
						tileNeighbor.rules.remove(tileNeighbor.rules[neighborrulectr])
			tileOrigin.rules.remove(validrules[originrulectr])		

def testmain():
	a = tile()
	#initialize the tilelist
	tilelist[0,0]=a
	#add new empty locations to list
	tilelist[0,1] =None
	tilelist[0,-1] = None
	tilelist[1,0] = None
	tilelist[-1,0] = None

	#print tilelist[0,0]
	a.coord=[0,0]

	b= tile ()
	tilelist[1,0] = b
	#add new empty locations to list
	tilelist[2,0] = None
	tilelist[1,1] = None
	tilelist[1,-1] = None

	b.coord=[1,0]
	#initiation rule
	a.addRule('a',0,None,'right')
	a.addRule('c',0,None, 'right')
	a.addRule('c',1,'left', 'right')
	a.addRule('c',1,'left', 'left')
	#transport rules
	b.addRule('a',1,'right','left')# transport r-l	
	b.addRule('a',1,'right','right')# transport r-r
	b.addRule('a',1,'right','top')# transport r-t
	b.addRule('a',1,'right','bottom')# transport r-b
	b.addRule('b',1,'right','left')# transport with wrong label
	b.addRule('a',1,'left','right')# non-related transport
	b.addRule('a',2,'right','left') # activation


	for each in tilelist:
		print  each,':', tilelist[each] 
	#activate(a,b)
	print '----------------'
	print '>Tile B rules: (',len(b.rules),')' ,b.rules
	print '>Tile A rules(',len(a.rules),')' ,a.rules
	print '----------------\r\n----------------'
	propagate(a)

	print '----------------\r\n----------------'
	print 'Tile B rules: (',len(b.rules),')' ,b.rules
	print 'Tile A rules(',len(a.rules),')'  ,a.rules
	print '----------------'

#debug()
testmain()