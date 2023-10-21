TNRM = "\x1B[0m"    # normal 
TBLK = "\x1B[0;30m" # black 
TRED = "\x1B[0;31m" # red 
TGRN = "\x1B[0;32m" # green 
TBRN = "\x1B[0;33m" # brown 
TBLU = "\x1B[0;34m" # blue 
TPUR = "\x1B[0;35m" # purple 
TCYN = "\x1B[0;36m" # cyan 
TLGY = "\x1B[0;37m" # light gray 
TDGY = "\x1B[1;30m" # dark gray 
TLRD = "\x1B[1;31m" # light red 
TLGN = "\x1B[1;32m" # light green 
TYLW = "\x1B[1;33m" # yellow 
TLBL = "\x1B[1;34m" # light blue 
TLPR = "\x1B[1;35m" # light purple 
TLCY = "\x1B[1;36m" # light cyan 
TWHT = "\x1B[1;37m" # white

BOLD = '\033[1m' # bold


def printlnWithBold(color, text):
    print(color + BOLD + text + TNRM + "\n")

def printlnWithRegular(color, text):
    print(color + text + TNRM + "\n")

def printWithBold(color, text):
    print(color + BOLD + text + TNRM)

def printWithRegular(color, text):
    print(color + text + TNRM)