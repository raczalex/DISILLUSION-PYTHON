
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.fortnite import Fortnite

class FortniteMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [FORTNITE]')

    def _displayMenu(self):
        
        options = [
            "Do All",
            "Europe Ping Test",
            "Na East Ping Test",
            "Na Central Ping Test",
            "Na West Ping Test",
            "Asia Ping Test",
            "OCE / Australia Ping Test",
            "Middle East Ping Test",
            "Brazil Ping Test",
            "Custom Ping Test"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [FORTNITE]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    Fortnite()._doAll()
                    sleep(2)
                elif choice == 2:
                    print('')
                    Fortnite()._europePingTest()
                    sleep(2)    
                elif choice == 3:
                    print('')
                    Fortnite()._naEastPingTest()
                    sleep(2)      
                elif choice == 4:
                    print('')
                    Fortnite()._naCentralPingTest()
                    sleep(2)      
                elif choice == 5:
                    print('')
                    Fortnite()._naWestPingTest()
                    sleep(2)      
                elif choice == 6:
                    print('')
                    Fortnite()._asiaPingTest()
                    sleep(2)      
                elif choice == 7:
                    print('')
                    Fortnite()._oceAustraliaPingTest()
                    sleep(2)      
                elif choice == 8:
                    print('')
                    Fortnite()._middleEastPingTest()
                    sleep(2)      
                elif choice == 9:
                    print('')
                    Fortnite()._brazilPingTest()
                    sleep(2)      
                elif choice == 10:
                    print('')
                    host = str(input(f"   {Colors.white}[FORTNITE]{Colors.light_green} Enter the host to ping (default = google):{Colors.white} "))
                    count = int(input(f"   {Colors.white}[FORTNITE]{Colors.light_green} Enter the number of pings (default = 10):{Colors.white} "))
                    Fortnite()._pingHost(host,count)
                    sleep(2)      
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   