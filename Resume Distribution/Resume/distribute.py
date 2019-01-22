import sys,os,shutil
import win32com.client
import ReadPDF

word = win32com.client.Dispatch('Word.Application')
wdFormatPDF = 17
word.Visible = False
def checkPath():
	try:
		if os.path.exists(os.path.dirname(sys.argv[1])):
			return True
		else:
			return False
	except:
		print("some error occured")
def checkArgument():
	global path
	try:
		if(len(sys.argv)<2):
			print("first argument not passed")
		elif(checkPath()):	
			path=sys.argv[1]
			#print(path)
	except:
			print("An error occured")
def convertWordToPDF():
	try:
			files = (file for file in os.listdir(path) 
				if os.path.isfile(os.path.join(path, file)))
			for file in files:
				if file.endswith('.docx'):
					print(str(file)+" is a word, Converting it to a pdf")
					docfile=path+'\\\\'+file
					#print(docfile)
					doc = word.Documents.Open(docfile)
					newPdf=path+'\\\\'+os.path.splitext(file)[0]
					doc.SaveAs(newPdf,FileFormat=wdFormatPDF)
					doc.Close()
	except:
		print("an error occured")
def moveDocuments():
		global dirname
		dirname = os.path.dirname(__file__)
		files = (file for file in os.listdir(path) 
				if os.path.isfile(os.path.join(path, file)))
		for file in files:
			if file.endswith('.pdf'):
				moveFrom=path+"\\\\"+file
				moveTo=os.path.join(dirname, 'temp\\\\'+file)
				shutil.move(moveFrom,moveTo)
def extractWordList():
		files = (file for file in os.listdir(dirname+'temp') 
				if os.path.isfile(os.path.join(dirname+'temp', file)))
		for file in files:
			wordstring = ReadPDF.extract_text_from_pdf(dirname+'temp\\\\'+file).encode("utf-8",errors="ignore").strip().decode('utf-8')
			print(wordstring)
checkArgument()
convertWordToPDF()
moveDocuments()
extractWordList()
