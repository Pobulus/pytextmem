import os
#Hint characters:
chars = 10

print("Welcome to PyTextMem: Python Text Memorisation Assistant for learning lyrics, poems, scripts, etc.")
print("Please enter the name of the file you want to learn.")

#Open file
while True:
	try:
		text = input("Name of the file:")
		if text == "":
			print("No file specified.")
			print("Loading default file...")
			text = "default.txt"

		with open(text, 'r') as file:
		    verses = [line.strip() for line in file]
		print("File "+ text +" successfully loaded!")
		input("Press Enter to start")
		break
	except FileNotFoundError:
		print("No such file found. Is the file name correct?")

#Display text line by line.
cnt = 1
out = []
for v in verses:
	out.append(v)
	os.system('clear')
	for o in out:
		if o == out[-1]:
			print(o[:chars])
		else:
			print(o)

	print("")
	prog = round(cnt/len(verses)*100, 1)
	print("Line "+ str(cnt)+ " of " +str(len(verses))+", Progress: " + str(prog) + "%." )
	
#Encouragement ;)

	if prog > 0 and prog < 10:
		print("We all have to start somewhere...")

	if prog >= 10 and prog < 20:
		print("The hardest part is to begin.")

	if prog >= 20 and prog < 30:
		print("Keep it up!")

	if prog >= 30 and prog < 40:
		print("I believe in you")

	if prog >= 40 and prog < 50:
		print("You can do it!")

	if prog >= 50 and prog < 60:
		print("You got the first half!")

	if prog >= 60 and prog < 70:
		print("Keep going!")

	if prog >= 70 and prog < 80:
		print("You've come so far!")

	if prog >= 80 and prog < 90:
		print("You've almost finished")

	if prog >= 90 and prog < 100:
		print("Almost done...")

	if prog == 100:
		print("This is the last line...")
		inp = input("q to quit; Enter to continue. ")
		if inp == "q":
			break
		os.system('clear')
		for o in out:
			print(o)
		print("")
		prog = round(cnt/len(verses)*100, 1)
		print("Line "+ str(cnt)+ " of " +str(len(verses))+", Progress: " + str(prog) + "%." )
		print("All done! Congratulations!")


	inp = input("q to quit; Enter to continue. ")
	if inp == "q":
		break
	cnt += 1