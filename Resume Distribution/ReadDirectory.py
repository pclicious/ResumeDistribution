import os,sys
path=r'C:\Users\pochaudh\Desktop\bat-t-exe converter in batch mode v-1'
print(path)
files = (file for file in os.listdir(path) 
         if os.path.isfile(os.path.join(path, file)))
for file in files:
	print(file)
