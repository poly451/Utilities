# This program walks the directory structure underneath the current working directory.
# It includes the current working directory
import os, sys
from datetime import datetime

def fileInfo(filename, filepath):
    fileNotFound = 0
    fileSize = -1
    fileDate = datetime.today()
    fullPath = os.path.join(filepath, filename)
    #print("fullpath: {}".format(fullPath))
    try:
        fileSize = os.path.getsize(fullPath)
    except:
        fileNotFound += 1
        return -1, -1
    try:
        fileDate = os.path.getmtime(fullPath)
        fileDate = datetime.fromtimestamp(fileDate)
    except:
        return -1, -1
    return fileSize, fileDate

def main():
    # startingDirectory = os.getcwd()
    fileTuple = []
    fileTuple_size = []
    numberOfFiles = 0
    sizeOfFiles = 0
    fileNotFound = 0
    oldestFile = datetime.today()
    largestFile = -1
    # ----------
    startingDirectory = "/Users/BigBlue/Documents/Programming/Python"
    startingDirectory = "/Users/BigBlue/Documents/Programming/"
    #startingDirectory = os.environ.get('HOME')
    os.chdir(startingDirectory)
    #print(dir(os))
    #print(os.listdir())
    for dirpath, dirnames, filenames in os.walk(startingDirectory):
        #print("dirpath: {}".format(dirpath))
        #print("dirnames: {}".format(dirnames))
        #print("filenames: {}".format(filenames))
        numberOfFiles += len(filenames)
        for afile in filenames:
            #rint("filename: {}".format(afile))
            fullPath = os.path.join(dirpath, afile)
            #print("fullpath: {}".format(fullPath))
            try:
                fileSize = os.path.getsize(fullPath)
            except:
                fileNotFound += 1
                continue
            sizeOfFiles += fileSize
            numberOfFiles += 1
            # ------------
            fileSize, fileDate = fileInfo(afile, dirpath)
            if fileDate < oldestFile:
                oldestFile = fileDate
                fileTuple=[os.path.join(dirpath, afile), fileSize, fileDate]
            if fileSize > largestFile:
                largestFile = fileSize
                fileTuple_size = [os.path.join(dirpath, afile), fileSize, fileDate]
            #print("fileSize: {}; fileDate: {}".format(fileSize, fileDate))
    mystring = """
    This program walks the directory structure, starting from the given
    directory, and lists a number of statistics, including the oldest file
    and the largest file.
    """
    print(mystring)
    print("starting directory: {}".format(startingDirectory))
    print("number of files: {}".format(numberOfFiles))
    print("Total size of files in kilobytes: {}".format(sizeOfFiles/1000))
    print("Total size of files in megabytes: {}".format((sizeOfFiles/1000)/1000))
    print("Average size of file in kilobytes: {}".format((sizeOfFiles/numberOfFiles)/1000))
    print("Number of files not found: {}".format(fileNotFound))
    print("Oldest file: {} : {}".format(oldestFile, fileTuple))
    print("largestFile file: {} mb : {}".format(largestFile/10000, fileTuple_size))

if __name__=="__main__":
    print("---- begin ----")
    main()
    print("---- end ----")
