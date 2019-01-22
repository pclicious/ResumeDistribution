import sys,os
try:
	if(len(sys.argv)<2):
		print("first argument not passed")
	else:
		path=sys.argv[1].replace('\\','\\\\')
		print(path)
		files = (file for file in os.listdir(path) 
				if os.path.isfile(os.path.join(path, file)))
		for file in files:
			if file.endswith('.docx'):
				print(file,"is a word")
			elif file.endswith('.pdf'):
				print(file,"is a pdf")
except:
	print("An error occured")