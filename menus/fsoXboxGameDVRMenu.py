
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.fsoXboxGameDVR import FsoXboxGameDVR

class FsoXboxGameDVRMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [FSO & XBOX GAMEDVR]')

    def _displayMenu(self):
        
        options = [
            "Disable",
            "Revert"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [FSO & XBOX GAMEDVR]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                
                if choice == 1:
                    print('')
                    FsoXboxGameDVR()._disable()
                    sleep(2)
                elif choice == 2:
                    print('')
                    FsoXboxGameDVR()._revert()
                    sleep(2)    
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   