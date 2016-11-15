import os, re, time

class ModuleFile:
	def __init__(self):
		self.name = ""
		self.ver = ""
		self.date = ""

class Module:
	def __init__(self):
		self.name = ""
		self.path = ""
		self.model = ModuleFile()
		self.params = ModuleFile()
		self.scaling = ModuleFile()
		self.code = ModuleFile()
		self.header = ModuleFile()

allModules = []

def Get_File_Version(path):
	version = 'Not Found'
	versionPattern = re.compile('[0-9]{1,}_[0-9]{2}[a|b]_[0-9]{1,}.[0-9]{1,}')
	f = open(path,'r')
	verFound = versionPattern.search(f.read())
	if verFound :
		version = verFound.group()
	f.close()
	return version

def Process_Module_Folders(baseDirectory):
	global allModules
	mNames = os.listdir(baseDirectory)
	for mName in mNames:
		if (os.path.isdir(mName)) and (mName[0:4] == 'eds_') and (len(mName) == len('EDS_XX')):
			mPath = baseDirectory + os.sep + mName
			module = Find_Module_Details(mName, mPath)
			allModules.append(module)

def Find_Module_Details(mName, mPath):
	module = Module()
	module.name = mName
	module.path = mPath
	matlabFolder = module.path + os.sep + 'matlab'
	fNames = os.listdir(matlabFolder)
	for fName in fNames:
		if (fName[-3:] == 'mdl') and (fName[0:len('EDS_xxy')].upper() == module.name.upper() + '1'):
			module.model.name = fName
			module.model.ver = Get_File_Version(matlabFolder + os.sep + fName)
			module.model.date = time.ctime(os.stat(matlabFolder + os.sep + fName).st_mtime)

		if (fName[-5:] == 'par.m') and (fName[0:len('EDS_xxy')].upper() == module.name.upper() + '1'):
			module.params.name = fName
			module.params.ver = Get_File_Version(matlabFolder + os.sep + fName)
			module.params.date = time.ctime(os.stat(matlabFolder + os.sep + fName).st_mtime)

		if (fName[-9:] == 'scaling.m') and (fName[0:len('EDS_xxy')].upper() == module.name.upper() + '1'):
			module.scaling.name = fName
			module.scaling.ver = Get_File_Version(matlabFolder + os.sep + fName)
			module.scaling.date = time.ctime(os.stat(matlabFolder + os.sep + fName).st_mtime)

	codeFolder = matlabFolder + os.sep + 'tlcode'
	fNames = os.listdir(codeFolder)
	for fName in fNames:
		if (fName[-1:] == 'c') and (fName[0:len('EDS_xxy')].upper() == module.name.upper() + '1'):
			module.code.name = fName
			module.code.ver = Get_File_Version(codeFolder + os.sep + fName)
			module.code.date = time.ctime(os.stat(codeFolder + os.sep + fName).st_mtime)

		if (fName[-1:] == 'h') and (fName[0:len('EDS_xxy')].upper() == module.name.upper() + '1'):
			module.header.name = fName
			module.header.ver = Get_File_Version(codeFolder + os.sep + fName)
			module.header.date = time.ctime(os.stat(codeFolder + os.sep + fName).st_mtime)

	return module

def Print_Module_Information(listModule):
	global allModules
	f = open('Module Details.txt','w')
	f.write('Script run by : ' + os.environ.get('USERNAME').upper() + ' on ' + time.strftime("%Y-%m-%d %H:%M:%S") + '\n\n')
	for i in range(len(listModule)):
		f.write(listModule[i].name + '\n')
		f.write('\tModel : \t' + listModule[i].model.name + '\n')
		f.write('\t version : \t' + listModule[i].model.ver + '\n')
		f.write('\t date : \t' + listModule[i].model.date + '\n\n')
		f.write('\tParams : \t' + listModule[i].params.name + '\n')
		f.write('\t version : \t' + listModule[i].params.ver + '\n')
		f.write('\t date : \t' + listModule[i].params.date + '\n\n')
		f.write('\tScaling : \t' + listModule[i].scaling.name + '\n')
		f.write('\t version : \t' + listModule[i].scaling.ver + '\n')
		f.write('\t date : \t' + listModule[i].scaling.date + '\n\n')
		f.write('\tCode : \t\t' + listModule[i].code.name + '\n')
		f.write('\t version : \t' + listModule[i].code.ver + '\n')
		f.write('\t date : \t' + listModule[i].code.date + '\n\n')
		f.write('\tHeader : \t' + listModule[i].header.name + '\n')
		f.write('\t version : \t' + listModule[i].header.ver + '\n')
		f.write('\t date : \t' + listModule[i].header.date + '\n\n\n')
	f.close()

def Print_Module_Information_On_Screen(listModule):
	global allModules
	print('Script run by : ' + os.environ.get('USERNAME').upper() + ' on ' + time.strftime("%Y-%m-%d %H:%M:%S") + '\n\n')
	for i in range(len(listModule)):
		print(listModule[i].name)
		print('\tModel : \t' + listModule[i].model.name)
		print('\t version : \t' + listModule[i].model.ver)
		print('\t date : \t' + listModule[i].model.date + '\n')
		print('\tParams : \t' + listModule[i].params.name)
		print('\t version : \t' + listModule[i].params.ver)
		print('\t date : \t' + listModule[i].params.date + '\n')
		print('\tScaling : \t' + listModule[i].scaling.name)
		print('\t version : \t' + listModule[i].scaling.ver)
		print('\t date : \t' + listModule[i].scaling.date + '\n')
		print('\tCode : \t\t' + listModule[i].code.name)
		print('\t version : \t' + listModule[i].code.ver)
		print('\t date : \t' + listModule[i].code.date + '\n')
		print('\tHeader : \t' + listModule[i].header.name)
		print('\t version : \t' + listModule[i].header.ver)
		print('\t date : \t' + listModule[i].header.date)


Process_Module_Folders(os.getcwd())
Print_Module_Information(allModules)
Print_Module_Information_On_Screen(allModules)