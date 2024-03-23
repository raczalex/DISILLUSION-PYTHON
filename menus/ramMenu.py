
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.ram import RAM

class RamMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [RAM]')

    def _displayMenu(self):
        
        options = [
            "Do All",
            "Disable Memory Compression",
            "Disable Page Combining",
            "Set SVC Split Host",
            "Disable Super Fetch",
            "Disable Prefetch",
            "RAM Tweaks"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [RAM]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    RAM()._doAll()
                    sleep(2)
                elif choice == 2:
                    print('')
                    RAM()._disableMemoryCompression()
                    sleep(2)    
                elif choice == 3:
                    print('')
                    RAM()._disablePageCombining()
                    sleep(2)  
                elif choice == 4:
                    print('')
                    RAM()._setSvcSplitHost()
                    sleep(2)  
                elif choice == 5:
                    print('')
                    RAM()._disableSuperfetch()
                    sleep(2)  
                elif choice == 6:
                    print('')
                    RAM()._disablePrefetch()
                    sleep(2)  
                elif choice == 7:
                    print('')
                    RAM()._ramTweaks()
                    sleep(2)  
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   