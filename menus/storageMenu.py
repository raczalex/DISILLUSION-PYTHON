
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.storage import Storage

class StorageMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [STORAGE]')

    def _displayMenu(self):
        
        options = [
            "Boot Drive SSD Optimization",
            "Boot Drive HDD Optimization",
            "Boot Drive Defrag",
            "Tweak User Write Cache"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [STORAGE]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    Storage()._bootDriveSSDOptimization()
                    sleep(2)    
                elif choice == 2:
                    print('')
                    Storage()._bootDriveHDDOptimization()
                    sleep(2)   
                elif choice == 3:
                    print('')
                    Storage()._bootDriveDefrag()
                    sleep(2)  
                elif choice == 4:
                    print('')
                    Storage()._tweakUserWriteCache()
                    sleep(2)  
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   