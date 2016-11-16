import os, sys, shutil

def Clean_Directory(directory):
	out = 'Not Done'
	if os.path.isdir(directory):
		files = os.listdir(directory)
		for file in files:
			filePath = os.path.join(directory,file)
			if os.path.isfile(filePath):
				os.unlink(filePath)
				out = 'Done'
	return out

try:
	delStatus = Clean_Directory(os.path.abspath(sys.argv[1]))
except:
	print "whatever"