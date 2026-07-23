from FamilyTree import Individual

individuals = {}



print("where is your .sftstores file located (leave blank for normal path)")
installationpath = input("> ")
if installationpath:
	store = open(f"{installationpath}/familytreestore.sftstore")
else:
	store = open("familytreestore.sftstore")
print(f"file successfully opened at {installationpath}/")

while True:
	queryinput = input("> ").lower()
	if queryinput:
		querylist = queryinput.split(".")

		if querylist[0] == "quit" or querylist[0] == "exit":
			quit()

		if querylist[0] == "individual":

			if querylist[1] == "add":
				name = querylist[2]
				individuals[name] = Individual(name)
				print(f"added {name} to individuals as {Individual(name)}")

			if querylist[1] == "display":
				print(individuals)


		if querylist[0] == "stores":
			print(store.read())

	else:
		print("invalid operation")