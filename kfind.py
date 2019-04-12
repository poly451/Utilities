# This program lives in:
# /Users/BigBlue/Documents/Programming/Python/utilities
import os, sys
from datetime import datetime
sys.path.append('/Users/BigBlue/Documents/Programming/Python/utilities')

def myadd(a, b):
    return a+b

def findDirectory_helper(startingDirectory, targetdir):
    numberOfDirectories = 0
    #startingDirectory = os.environ.get('HOME')
    os.chdir(startingDirectory)
    #print(dir(os))
    #print(os.listdir())
    for dirpath, dirnames, filenames in os.walk(startingDirectory):
        #print("dirpath: {}".format(dirpath))
        #print("dirnames: {}".format(dirnames))
        #print("filenames: {}".format(filenames))
        numberOfDirectories += 1
        for dirname in dirnames:
            if dirname == targetdir:
                return True, os.path.join(dirpath, dirname)
    return False, ""

def findDirectory(targetdir, startingDirectory):
    # startingDirectory = os.getcwd()
    # ----------
    print("Searching {} for DIRECTORY {}.".format(startingDirectory, targetdir))
    targetFound, dirpath = findDirectory_helper(startingDirectory, targetdir)

    print("target directory: {}".format(targetdir))
    #print("starting directory: {}".format(startingDirectory))
    if targetFound == True:
        print("DIRECTORY FOUND!!! :-)")
        print("path to directory: {}".format(dirpath))
    else:
        print("target directory ({}) was NOT found.".format(targetdir))

def findFile_helper(startingDirectory, targetFile):
    #print("startingDirectory: {}".format(startingDirectory))
    #print("targetFile: ".format(targetFile))
    numberOfFiles = 0
    #startingDirectory = os.environ.get('HOME')
    os.chdir(startingDirectory)
    #print(dir(os))
    #print(os.listdir())
    for dirpath, dirnames, filenames in os.walk(startingDirectory):
        #print("dirpath: {}".format(dirpath))
        #print("dirnames: {}".format(dirnames))
        #print("filenames: {}".format(filenames))
        for afile in filenames:
            if afile == targetFile:
                return True, os.path.join(dirpath, afile)
    return False, ""

def findFile(targetFile, startingDirectory):
    print("Searching {} for FILE {}.".format(startingDirectory, targetFile))
    targetFound, filepath = findFile_helper(startingDirectory, targetFile)

    #print("path to file: {}".format(filepath))
    #print("starting directory: {}".format(startingDirectory))
    if targetFound == True:
        print("FILE FOUND!!! :-)")
        print("path to file: {}".format(filepath))
    else:
        print("target file ({}) was NOT found.".format(targetFile))


if __name__=="__main__":
    mystring = """
    This program walks the directory structure, starting from the given
    directory, and finds either the file name or the given directory name {}
    if it exists.
    NOTE:
    * If -d is used but no starting directory is given, the program will begin in
    "/Users/BigBlue/Documents"
    * If -f is used but no starting directory is given, the program will begin in
    "/Users/BigBlue/Documents"
    * If no switch (-f or -d) is given, the program will interpret the string
    as a file name.
    Examples:
    >python kfind.py -d <directory name> <starting directory>
    >python kfind.py -f <filename> <starting direcctory>
    For example:
    python find_directory.py '/Users/BigBlue' 'flask'
    """
    print("---- begin ----")
    findingAFile = False
    file_to_find = ""
    directory_to_find = ""
    startingDirectory = ""
    startingDirectory = "/Users/BigBlue/Documents/Programming/Python"
    startingDirectory = "/Users/BigBlue/Documents"

    arg1 = ""
    arg2 = ""
    arg3 = ""
    try:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
    except:
        print("Error! Couldn't make sense of the input.")
        sys.stop("Exiting ...")

    if arg1 == "-f" or arg1 == "-d":
        if arg1 == "-f":
            findingAFile = True
            file_to_find = arg2
        else:
            findingAFile = False
            directory_to_find = arg2
    else:
        # We're going to assume a filename was passed through.
        findingAFile = True
        file_to_find = arg1
        startingDirectory = arg2

    try:
        arg3 = sys.argv[3]
    except:
        pass

    if arg3 == "":
        pass
    else: startingDirectory = arg3
    #print("arg3: {}".format(arg3))
    if findingAFile == True:
        print("file name: {}".format(file_to_find))
        findFile(file_to_find, startingDirectory)
    else:
        print("directory name: {}".format(directory_to_find))
        findDirectory(directory_to_find, startingDirectory)
    #print("starting directory : {}".format(startingDirectory))

    print("---- end ----")
