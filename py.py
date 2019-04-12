import os, sys
sys.path.append('/Users/BigBlue/Documents/Programming/Python/utilities')
import kfind

def main(switch, name, starting):
    if switch == "-f":
        kfind.findFile(name, starting)
    else:
        if switch == "-d":
            kfind.findDirectory(name, starting)
        else:
            sys.stop("Input not recognized. Should have been either -f or -d: {}".format(switch))
    print(kfind.myadd(1, 2))

if __name__=="__main__":
    arg1=""
    arg2=""
    arg3=""
    try:
        arg1=sys.argv[1]
        arg2=sys.argv[2]
        arg3=sys.argv[3]
    except:
        mystring = """
        Incorrect input.
        1. A switch (-f or -d) must be given.
        2. A directory name or file name.
        3. Either a beginning directory or -default
        """
        print(mystring)
        sys.exit("Exiting ...")

    main(arg1, arg2, arg3)
