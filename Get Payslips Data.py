import PyPDF2
def hasNumbers(inputString):
return any(char.isdigit() for char in inputString)
directory = "C:\\Users\\venkats4\\Desktop\\Payslips\\2014\\"
file = "10_2014.pdf"
pdf = open(directory+file,'rb')
reader = PyPDF2.PdfFileReader(pdf)
unicode_text = reader.getPage(0).extractText()
normalized = unicode_text.encode('ascii', 'ignore')
text = normalized.decode('utf-8')
pattern = r"([\w,\/\.]+[\w\s])"
_words = re.findall(pattern,text)
_words = [word.strip() for word in _words]
_digits = r"([\d,.]+)"
_test = [re.findall(_digits, word)[0] for word in _words if len(re.findall(_digits, word)) > 0]
_number_pattern = 
keywords = []
