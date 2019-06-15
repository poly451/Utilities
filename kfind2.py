# This program lives in:
# /Users/BigBlue/Documents/Programming/Python/utilities
import os, sys
from datetime import datetime
sys.path.append('/Users/BigBlue/Documents/Programming/Python/utilities')

def findDirectory_helper(startingDirectory, targetdir):
    numberOfDirectories = 0
    #startingDirectory = os.environ.get('HOME')
    os.chdir(startingDirectory)
    #print(dir(os))
    #print(os.listdir())
    returnList = []
    for dirpath, dirnames, filenames in os.walk(startingDirectory):
        # print("dirpath: {}".format(dirpath))
        #print("dirnames: {}".format(dirnames))
        #print("filenames: {}".format(filenames))
        numberOfDirectories += 1
        for dirname in dirnames:
            if targetdir in dirname:
                returnList.append(os.path.join(dirpath, dirname))
    return returnList

def findDirectory(targetdir, startingDirectory):
    # startingDirectory = os.getcwd()
    # ----------
    print("Searching ({}) for DIRECTORY ({}).".format(startingDirectory, targetdir))
    dirsFound = findDirectory_helper(startingDirectory, targetdir)
    print("{} paths found.".format(len(dirsFound)))

    print("target directory: {}".format(targetdir))
    #print("starting directory: {}".format(startingDirectory))
    if len(dirsFound) > 0:
        print("DIRECTORY FOUND!!! :-)")
        print("path(s) to directory:")
        for mystring in dirsFound:
            print(mystring)
    else:
        print("target directory ({}) was NOT found.".format(targetdir))

# ----------------------------------------------------------------

def findFile_helper(startingDirectory, targetFile):
    #print("startingDirectory: {}".format(startingDirectory))
    #print("targetFile: ".format(targetFile))
    numberOfFiles = 0
    #startingDirectory = os.environ.get('HOME')
    os.chdir(startingDirectory)
    #print(dir(os))
    #print(os.listdir())
    filelist = []
    for dirpath, dirnames, filenames in os.walk(startingDirectory):
        #print("dirpath: {}".format(dirpath))
        #print("dirnames: {}".format(dirnames))
        #print("filenames: {}".format(filenames))
        for afile in filenames:
            if targetFile in afile:
                filelist.append(os.path.join(dirpath, afile))

    if len(filelist) > 0:
        return True, filelist
    return False, ""

def findFile(targetFile, startingDirectory):
    print("Searching ({}) for FILE ({}).".format(startingDirectory, targetFile))
    targetFound, filepaths = findFile_helper(startingDirectory, targetFile)

    #print("path to file: {}".format(filepath))
    #print("starting directory: {}".format(startingDirectory))
    if targetFound == True:
        print("FILE FOUND!!! :-)")
        print("File(s) found:")
        [print(i) for i in filepaths]
    else:
        print("target file ({}) was NOT found.".format(targetFile))

def main(switch, name, starting):
    if switch == "-f":
        findFile(name, starting)
    else:
        if switch == "-d":
            findDirectory(name, starting)
        else:
            sys.stop("Input not recognized. Should have been either -f or -d: {}".format(switch))


if __name__=="__main__":
    startingDirectory = "/Users/BigBlue/Documents/Programming/Python"
    # startingDirectory = "/Users/BigBlue/Documents/Programming/Python/graphics/pygame/hello_world_programs"
    mystring = """
    This program walks the directory structure, starting from the given
    directory, and finds either the file name or the given directory name {}
    if it exists.
    Examples:
    >python kfind.py -d <directory name> <starting directory>
    >python kfind.py -f <filename> <starting direcctory>
    """.format(startingDirectory)

    # if len(sys.argv) == 1:
    #     print(mystring)
    #     print("The default starting directory is: {}".format(startingDirectory))
    #     sys.exit()

    # arg1 = "-f"
    # arg2 = "game"
    # arg3 = startingDirectory

    arg1 = "-d"
    arg2 = "py"
    arg3 = startingDirectory

    main(arg1, arg2, arg3)

    # arg1 = ""
    # arg2 = ""
    # arg3 = ""
    # try:
    #     arg1 = sys.argv[1]
    #     arg2 = sys.argv[2]
    #     arg3 = sys.argv[3]
    # except:
    #     print("Error! Couldn't make sense of the input.")
    #     sys.stop("Exiting ...")
