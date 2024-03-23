
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.fix import Fix

class FixMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [FIX]')

    def _displayMenu(self):
        
        options = [
            "Do All",
            "SFC /SCANNOW",
            "DISM RESTORE HEALTH"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [FIX]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    Fix()._doAll()
                    sleep(2)
                elif choice == 2:
                    print('')
                    Fix()._scanNow()    
                elif choice == 3:
                    print('')
                    Fix()._dismRestoreHealth()  
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   