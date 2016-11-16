import os, re, sys
from shutil import copy2

def Copy_Code_Files(src,dest):
	mNames = os.listdir(src)
	out = 'Not Done'
	for mName in mNames:
		if (os.path.isdir(os.path.join(src,mName))) and (mName[0:4].upper() == 'eds_'.upper()) and (len(mName) == len('EDS_XX')):
			codePath = os.path.join(src,mName,'matlab','tlcode')
			fNames = os.listdir(codePath)
			for fName in fNames:
				if os.path.isfile(os.path.join(codePath,fName)):
					fileNamePattern = re.compile('(^e_EDS_[a-zA-Z]{2,}[0-9]{1,}.h|^EDS_[a-zA-Z]{2,}[0-9]{1,}.[c|h])')
					patFound = fileNamePattern.search(fName)
					if patFound :
						copy2(os.path.join(codePath,fName),dest)
						out = 'Done'
	return out

try:
	copyStatus = Copy_Code_Files(os.path.abspath(sys.argv[1]),os.path.abspath(sys.argv[2]))
except:
	print "whatever"