from libs.filerm import filerm, filermWindows
from libs.color import *
import platform

def fetcherm():
    printlnWithBold(TGRN, "\nWelcome to Fetcherm")

    hostUser = f"{TGRN}{BOLD}[{TLGN}{BOLD}{filerm.user}{TRED}{BOLD}@{TLBL}{BOLD}{filerm.host}{TGRN}{BOLD}]{TNRM}"
    print(hostUser)
    for i in range(len(f"[{filerm.user}@{filerm.host}]")):
        print("-", end='')


    if platform.system() == "Linux":
        printWithBold(TYLW, f"\nOS:  {TWHT}{filerm.getOS('os-name')}")
        printWithBold(TYLW, f"Kernel: {TWHT}{filerm.getOS('kernel')}")
        printWithBold(TYLW, f"Shell: {TWHT}{filerm.getOS('shell')}")
        printWithBold(TYLW, f"DE: {TWHT}{filerm.getOS('desktop-env')}")
        printWithBold(TYLW, f"WM: {TWHT}{filerm.getOS('window-mngr').capitalize()}")
        printWithBold(TYLW, f"Theme: {TWHT}{filerm.ReadTheme()}")

        printWithBold(TYLW, f"CPU: {TWHT}{filerm.ReadCPU()}")
        printWithBold(TYLW, f"GPU: {TWHT}{filerm.ReadGPU()}")
        printWithBold(TYLW, f"Memory: {TWHT}{filerm.CurrentRam() + ' / ' + filerm.ReadMemory('mb')}")
        printWithBold(TYLW, f"Disk size: {TWHT}{filerm.ReadDisk()}\n")
    elif platform.system() == "Windows":
        printWithBold(TYLW, f"\nOS: {TWHT} Windows {filermWindows.getOs("os-name")}")
        printWithBold(TYLW, f"Version: {TWHT}{filermWindows.getOs("version")}")

        printWithBold(TYLW, f"CPU: {TWHT}{filermWindows.ReadCPU()}")
        printWithBold(TYLW, f"GPU: {TWHT}{filermWindows.ReadGPU()}")
        printWithBold(TYLW, f"RAM: {TWHT}{filermWindows.ReadMemory("gb") + " GB"}")
        printWithBold(TYLW, f"Disk size: {TWHT}{filerm.ReadDisk()}\n")
    
fetcherm()