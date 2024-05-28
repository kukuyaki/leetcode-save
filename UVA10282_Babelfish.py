from collections import defaultdict
dictt=defaultdict(list)
while(x:=input()):
	li=x.split()
	dictt[li[1]].append(li[0])
while(y:=input()):
	if dictt[y]==[]:
		print("eh")
	else:
		print(dictt[y][0])