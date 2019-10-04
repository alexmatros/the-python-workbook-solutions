## Exercise 45: What Color is that Square?

gridPos = input("Please enter a chess board position: ")

col = gridPos[0].lower()
row = int(gridPos[1])

if col in "aceg":
	colStartsWithBlack = True
else:
	colStartsWithBlack = False
	
if colStartsWithBlack:
	if row % 2 == 0:
		white = True
	else:
		white = False
else:
	if row % 2 == 0:
		white = False
	else:
		white = True
		
if white:
	print("The position is coloured white.")
else:
	print("The position is coloured black.")