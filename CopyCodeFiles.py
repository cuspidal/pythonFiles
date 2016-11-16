import os, re, sys
from shutil import copy2

def Copy_Code_Files(src,dest):
	mNames = os.listdir(src)
	for mName in mNames:
		if (os.path.isdir(mName)) and (mName[0:4].upper() == 'eds_'.upper()) and (len(mName) == len('EDS_XX')):
			codePath = os.path.join(src,mName,'matlab','tlcode')
			fNames = os.listdir(codePath)
			for fName in fNames:
				if os.path.isfile(os.path.join(codePath,fName)):
					print "hje"
					fileNamePattern = re.compile('(^e_EDS_[a-zA-Z]{2,}[0-9]{1,}.h|^EDS_[a-zA-Z]{2,}[0-9]{1,}.[c|h])')
					patFound = fileNamePattern.search(fName)
					if patFound :
						copy2(os.path.join(codePath,fName),dest)

Copy_Code_Files(sys.argv[1],sys.argv[2])