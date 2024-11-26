import pickle
def search():
	f = open("binary3.dat","rb")
	try:
		while True:
			data = pickle.load(f)
			if data[2]>=50:
				print(data[1])

	except:
		f.close()


search()	