while True:
	print("Enter 'x' for exit.")
	name = input("Enter your name: ")
	ntime = int(input("How many time you want to print your name ? "))
	if name == 'x':
		break
	else:
		for i in range(0, ntime):
			print(name)
	print()
