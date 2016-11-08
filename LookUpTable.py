import os, re, fileinput, sys
 
allFuncs = []
reqFuncs = []
specialChars = ['*','#','/']

def FilterFiles():
	fNames = os.listdir(os.getcwd())
	for fName in fNames:
		if (fName[len(fName)-1] == 'c') and (fName[0:3] == 'EDS'):
			ScanFile(fName);

def ScanFile(fileName):
	global allFuncs
	edsFile = fileinput.input(fileName)
	dsFuncPattern = re.compile('ds_[a-z]{2,3}_(sst_|)[S|U|F][0-9]{1,2}')
	for line in edsFile:
		patFound = dsFuncPattern.search(line)
		if patFound : 
			name = patFound.group()
			allFuncs.append(str(name))
	edsFile.close()
			
def CommentDS_LUT_c(requiredFunctions):
	ds_lut_c = fileinput.input('X:\\Matlab\\Ressourcen\\include\\TL34\\DS_LUT.c')
	comment = False
	tempFile = open('DS_LUT.c','w')
	dsFuncPattern = re.compile('ds_[a-z]{2,3}_(sst_|)[S|U|F][0-9]{1,2}')
	for line in ds_lut_c:
		if line[0] in specialChars:
			tempFile.write(line);
		else:
			patFound = dsFuncPattern.search(line)
			if patFound:
				if patFound.group() in requiredFunctions :
					comment = False
				else:
					comment = True
		
			if comment == True :
				tempFile.write('//' + line)
				if line == '}':
					comment = False
			else:
				tempFile.write(line)

	ds_lut_c.close()
	tempFile.close()


FilterFiles()
reqFuncs = list(set(allFuncs))
CommentDS_LUT_c(reqFuncs)