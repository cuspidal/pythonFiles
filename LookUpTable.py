#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    File name: LookUpTable.py
    Author: Kartik Gandhi
    Purpose: To import DS_LUT.c into the build environment from X:
    Date created: 08/11/2016
    Date last modified: 09/11/2016
    Python Version: 2.7

'''
import os, re, fileinput, sys
 
allFuncs = []
reqFuncs = []
specialChars = ['*','#','/']

# function FilterFiles
# Scans a folder for filenames and 
# passes all the EDS_xx1.c files for further scan
def FilterFiles(baseDirectory):
	fNames = os.listdir(baseDirectory)
	for fName in fNames:
		if (fName[-1:] == 'c') and (fName[0:3] == 'EDS'):
			ScanFile(os.path.join(baseDirectory,fName));

# function ScanFile
# Scans a passed file for functions call starting with ds_si or ds_gkl
# Stores all the found functions as per the pattern string in the list - "allFuncs"
def ScanFile(fileNameWithPath):
	global allFuncs
	edsFile = fileinput.input(fileNameWithPath)
	dsFuncPattern = re.compile('ds_[a-z]{2,3}_(sst_|)[S|U|F][0-9]{1,2}')
	for line in edsFile:
		patFound = dsFuncPattern.search(line)
		if patFound : 
			name = patFound.group()
			allFuncs.append(str(name))
	edsFile.close()
			
# function CommentDS_LUT_c
# Scans a passed file for functions call 
# starting with ds_si or ds_gkl
# Stores all the found functions as per 
# the pattern string in the list - "allFuncs"
def CommentDS_LUT_c(requiredFunctions,baseDirectory):
	ds_lut_c = fileinput.input('X:\\Matlab\\Ressourcen\\include\\TL34\\DS_LUT.c')
	comment = False
	tempFile = open(os.path.join(baseDirectory,'DS_LUT.c'),'w')
	dsFuncPattern = re.compile('ds_[a-z]{2,3}_(sst_|)[S|U|F][0-9]{1,2}')
	for line in ds_lut_c:
		
		# every line  in DS_LUT.c that starts with
		# '/'' or '*' or '#'' will be left unchanged 
		if line[0] in specialChars:
			tempFile.write(line);
		else:
			## remaining files will be searched for function definition
			patFound = dsFuncPattern.search(line)
			if patFound:
				## if the function found in the line
				## is required function then commenting
				## will be turned off
				## else commenting will be turned on
				if patFound.group() in requiredFunctions :
					comment = False
				else:
					comment = True
			
			## if commenting for the line is on
			## then the line gets '//' at the start
			## which indicates a commented line in .c
			## the remaining contents of the line are
			## unchanged
			## if the commenting is off then
			## line is inserted unchanged
			if comment == True :
				tempFile.write('//' + line)
				if line == '}':
					comment = False
			else:
				tempFile.write(line)

	ds_lut_c.close()
	tempFile.close()

## Execution Order of functions
try:
	if sys.argv[1] == '' :
		baseDirectory = os.getcwd()
	else :
		baseDirectory = os.path.abspath(sys.argv[1])
except :
	baseDirectory = os.getcwd()

## Working Directory is scanned for EDS Files
## all ds_si or ds_gkl functions are stored in list
FilterFiles(baseDirectory)

## list is sorted to remove duplicates
reqFuncs = list(set(allFuncs))

## DS_LUT.c is pulled from X: and any function 
## not present in the list is commented
## Commented DS_LUT.c is placed in the build environment
CommentDS_LUT_c(reqFuncs,baseDirectory)