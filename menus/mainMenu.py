
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from menus.bcdeditMenu import BCDEdit
from menus.cpuMenu import CPUMenu
from menus.debloatMenu import DebloatMenu
from menus.fixMenu import FixMenu
from menus.fortniteMenu import FortniteMenu
from menus.fsoXboxGameDVRMenu import FsoXboxGameDVRMenu
from menus.gamePriorityMenu import GamePriorityMenu
from menus.gpuMenu import GPUMenu
from menus.installMenu import InstallMenu
from menus.keyboardMenu import KeyboardMenu
from menus.mouseMenu import MouseMenu
from menus.networkMenu import NetworkMenu
from menus.optimizeMenu import OptimizeMenu
from menus.powerMenu import PowerMenu
from menus.priorityMenu import PriorityMenu
from menus.ramMenu import RamMenu
from menus.serialCheckerMenu import SerialCheckerMenu
from menus.startupsMenu import StartupsMenu
from menus.storageMenu import StorageMenu
from menus.systemInfoMenu import SystemInfoMenu
from menus.tweaksMenu import TweaksMenu
from menus.uninstallMenu import UninstallMenu
from menus.usbMenu import USBMenu
from menus.visualMenu import VisualMenu
from menus.wubMenu import WUBMenu
from menus.legacyBiosTweaksMenu import LegacyBiosTweaksMenu
from menus.moreMenu import MoreMenu

class MainMenu():
    def __init__(self) -> None:
        _initTitle(f'DISILLUSION - [MAIN]')

    def _displayMenu(self):

        options = [
            "BCDEDIT",
            "CPU",
            "DEBLOAT",
            "FIX",
            "FORTNITE",
            "FSO & XBOX & GAMEDVR",
            "GAME PRIORITY",
            "GPU",
            "INSTALL",
            "KEYBOARD",
            "MOUSE",
            "NETWORK",
            "OPTIMIZE",
            "POWER",
            "PRIORITY",
            "RAM",
            "SERIAL CHECKER",
            "STARTUPS",
            "STORAGE",
            "SYSTEM INFO",
            "TWEAKS",
            "UNINSTALL",
            "USB",
            "VISUAL",
            "WUB",
            "LEGACY BIOS TWEAKS",
            "MORE"
        ]

        while True:
            _clear()
            _initTitle(f'DISILLUSION - [MAIN]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    BCDEdit()._displayMenu()
                elif choice == 2:
                    CPUMenu()._displayMenu()    
                elif choice == 3:
                    DebloatMenu()._displayMenu()  
                elif choice == 4:
                    FixMenu()._displayMenu()  
                elif choice == 5:
                    FortniteMenu()._displayMenu()  
                elif choice == 6:
                    FsoXboxGameDVRMenu()._displayMenu()  
                elif choice == 7:
                    GamePriorityMenu()._displayMenu()  
                elif choice == 8:
                    GPUMenu()._displayMenu()  
                elif choice == 9:
                    InstallMenu()._displayMenu()  
                elif choice == 10:
                    KeyboardMenu()._displayMenu()  
                elif choice == 11:
                    MouseMenu()._displayMenu()  
                elif choice == 12:
                    NetworkMenu()._displayMenu()  
                elif choice == 13:
                    OptimizeMenu()._displayMenu()  
                elif choice == 14:
                    PowerMenu()._displayMenu()  
                elif choice == 15:
                    PriorityMenu()._displayMenu()  
                elif choice == 16:
                    RamMenu()._displayMenu()  
                elif choice == 17:
                    SerialCheckerMenu()._displayMenu()  
                elif choice == 18:
                    StartupsMenu()._displayMenu()
                elif choice == 19:
                    StorageMenu()._displayMenu()
                elif choice == 20:
                    SystemInfoMenu()._displayMenu()
                elif choice == 21:
                    TweaksMenu()._displayMenu()
                elif choice == 22:
                    UninstallMenu()._displayMenu()
                elif choice == 23:
                    USBMenu()._displayMenu()
                elif choice == 24:
                    VisualMenu()._displayMenu()
                elif choice == 25:
                    WUBMenu()._displayMenu()
                elif choice == 26:
                    LegacyBiosTweaksMenu()._displayMenu()
                elif choice == 27:
                    MoreMenu()._displayMenu()
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   