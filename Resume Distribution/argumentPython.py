import sys
try:
#print(sys.argv)
	if(len(sys.argv)<2):
		print("first argument not passed")
	else:
		print(sys.argv[1])
except:
	print("An error occured")
	
	
