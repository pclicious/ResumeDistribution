import sys,os
import win32com.client

word = win32com.client.Dispatch('Word.Application')
wdFormatPDF = 17
word.Visible = False
if(len(sys.argv)<2):
		print("first argument not passed")
else:
		path=sys.argv[1].replace('\\','\\\\')
		print(path)
		files = (file for file in os.listdir(path) 
				if os.path.isfile(os.path.join(path, file)))
		for file in files:
			if file.endswith('.docx'):
				print(file,"is a word, Converting it to a pdf")
				docfile=path+'\\\\'+file
				print(docfile)
				doc = word.Documents.Open(docfile)
				newPdf=path+'\\\\'+os.path.splitext(file)[0]
				doc.SaveAs(newPdf,FileFormat=wdFormatPDF)
				doc.Close()
			elif file.endswith('.pdf'):
				print(file,"is a pdf")
		word.Quit()

