from libs.filerm import filerm
from libs.color import *

def fetcherm():
    printlnWithBold(TGRN, "\nWelcome to Fetcherm")
    
    printWithBold(TYLW, f"OS:  {TWHT}{filerm.getOS('os-name')}")
    printWithBold(TYLW, f"Kernel: {TWHT}{filerm.getOS('kernel')}")
    printWithBold(TYLW, f"Shell: {TWHT}{filerm.getOS('shell')}")
    printWithBold(TYLW, f"DE: {TWHT}{filerm.getOS('desktop-env')}")
    printWithBold(TYLW, f"WM: {TWHT}{filerm.getOS('window-mngr').capitalize()}")
    printWithBold(TYLW, f"Theme: {TWHT}{filerm.getOS('gnome-theme')}")

    printWithBold(TYLW, f"CPU: {TWHT}{filerm.ReadCPU()}")
    printWithBold(TYLW, f"GPU: {TWHT}{filerm.ReadGPU()}")
    printWithBold(TYLW, f"Memory: {TWHT}{filerm.CurrentRam() + ' / ' + filerm.ReadMemory('mb')}\n")

fetcherm()