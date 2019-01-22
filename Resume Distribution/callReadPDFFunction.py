import ReadPDFFunction
import xlrd, string
exclude = set(string.punctuation)
wordstring = ReadPDFFunction.extract_text_from_pdf('PoojaCV.pdf').encode("utf-8",errors="ignore").strip()
wordstring = wordstring.decode('utf-8')
wordlist = wordstring.split()
loc = ("skillset.xlsx") 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
rows=int(sheet.nrows)
cols=int(sheet.ncols)
for i in range(1,rows):
	data1=sheet.cell_value(i, 0)
	data1=''.join(ch for ch in data1 if ch not in exclude)
	data1=data1.split()
	print(data1)
	for j in range(1,cols):
		data2=sheet.cell_value(i, j)
		print(data2)
		result=all(elem in wordlist for elem in data1)
		if result:
			print("Yes")
		else:
			print("No")
#print(wordstring)