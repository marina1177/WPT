


def loop():
	arr = {}
	for i in range(0, 5):
		for p in range(-i, i):
			for h in range(-i, i):
				print("i= " + str(i) + "\n[" + str(p) + ',' + str(h) + '] ')

if __name__ == '__main__':
	loop()
