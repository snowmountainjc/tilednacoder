class tile(object):
	def __init__(self):
		#Neighbor Pointers
		self.neighbor={'top':None,'left':None,'right':None,'bottom':None}

		self.rules=[]

		#side state
		self.stLeft=None
		self.stRight=None
		self.stTop=None
		self.stBottom=None

		self.activationRules=[]

def placeTile(tileObject,tileList):
	#To DO: need to consider how to match all sides of an available location
	for each in tileLIst:
		#check for each orientation
		#normal
		if tileObject.stRight == each.stLeft or tileObject.stLeft == each.stRight or tileObject.stTop == each.stBottom or tileobject.stBottom == each.stTop:
			print 'match'
		#90 deg.
		#180 deg.
		#270 deg.

def matchingRule(tileRule,neighbor):
	matches = []
	for each in neighbor.rules:
		if tilerule[0] == each[0] and tilerule[3] == neighbor:
			matches.append(each)
	return matches

def activate(tileObject):
	for tilerule in tileObject.rules:
		if tilerule[1] == 1: #checks if it is an initation rule
			for eachNeighbor in tileObject.neighbor:
				#print neighboreachNeighbor
				print 'hi'
				#if eachNeighbor != None :
				#	for matchrule in eachNeighbor.rules:
				#		if tilerule[0] == matchrule[0]:
				#			print 'matching rule:', tilerule, matchrule
				
#add tiles to be activated next
#activate tiles

def main():
	tilelist=[]
	tileA = tile()
	tileA.rules.append(['a',0,None,None])
	tileA.rules.append(['a',0,None,None])
	tileA.rules.append(['a',0,None,None])
	tileA.rules.append(['a',0,None,None])
	tileA.rules.append(['a',0,None,None])
	tilelist.append(tileA)

	tileB = tile()
	tileB.rules.append(['a', 1, None, None])
	tileB.rules.append(['a', 1, None, 'None'])
	tileB.rules.append(['a', 1, None, None])
	tileB.rules.append(['a', 1, None, 4])
	tilelist.append(tileB)

	tileA.neighbor['left']=tileB
	tileB.neighbor['right']=tileA
	print tileA.rules , tilelist
	print tileA.neighbor
	print tileB.neighbor

	activate(tileB)

main()