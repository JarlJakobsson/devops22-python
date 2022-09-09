
firstlist=[1,9,7,4,5]
secondlist=[5,7,9,4,1]
#tupplelist=[]
newlist = [(i, firstlist.index(i)) for i in secondlist]
print(newlist)

#for i in secondlist:
#    tupplelist.append(f"{i, firstlist.index(i)}")
#print(tupplelist)