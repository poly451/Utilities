# This program walks the directory structure underneath the current working directory.
# It includes the current working directory
import os, sys
from datetime import datetime

def findDirectory(startingDirectory, targetdir):
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

def main(targetdir):
    # startingDirectory = os.getcwd()
    # ----------
    startingDirectory = "/Users/BigBlue/Documents/Programming/Python"
    startingDirectory = "/Users/BigBlue/Documents"
    targetFound, dirpath = findDirectory(startingDirectory, targetdir)

    print("target directory: {}".format(targetdir))
    print("starting directory: {}".format(startingDirectory))
    if targetFound == True:
        print("DIRECTORY FOUND!!! :-)")
        print("path to directory: {}".format(dirpath))
    else:
        print("target directory ({}) was not found.".format(targetdir))

if __name__=="__main__":
    mystring = """
    This program walks the directory structure, starting from the given
    directory, and finds the given directory name {} if it exists.
    NOTE: If no starting directory is given, the program will begin in
    "/Users/BigBlue/Documents"
    >python find_directory.py <directory name> <starting directory>
    For example:
    python find_directory.py '/Users/BigBlue' 'flask'
    """
    print("---- begin ----")
    try:
        directory_to_find = sys.argv[1]
    except:
        print("ERROR: I need a directory to find, but none was given! :-()")
        sys.exit("Exiting ...")
    if directory_to_find == "-h" or directory_to_find=='--help':
        print(mystring)
    else:
        main(directory_to_find)
    print("---- end ----")
