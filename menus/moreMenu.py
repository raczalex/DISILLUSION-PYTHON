
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.more import More

class MoreMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [MORE]')

    def _displayMenu(self):
        
        options = [
            "Do All",
            "Change Sound Settings",
            "Show File Extensions",
            "Reset Ip Address",
            "Pin Important Folders To Start",
            "Arrange Desktop Icons",
            "Sync Time",
            "Better Wallpaper Quality",
            "Better Alt Tab",
            "Disable UAC",
            "Revert Alt Tab"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [MORE]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                elif choice == 2:
                    print('')
                    More()._changeSoundSettings()
                    sleep(2)    
                elif choice == 3:
                    print('')
                    More()._showFileExtensions()
                    sleep(2)  
                elif choice == 4:
                    print('')
                    More()._resetIpAddress()
                    sleep(2)  
                elif choice == 5:
                    print('')
                    More()._pinImportantFoldersToStart()
                    sleep(2)  
                elif choice == 6:
                    print('')
                    More()._arrangeDesktopIcons()
                    sleep(2)  
                elif choice == 7:
                    print('')
                    More()._syncTime()
                    sleep(2)  
                elif choice == 8:
                    print('')
                    More()._betterWallpaperQuality()
                    sleep(2)  
                elif choice == 9:
                    print('')
                    More()._betterAltTab()
                    sleep(2)  
                elif choice == 10:
                    print('')
                    More()._disableUAC()
                    sleep(2)  
                elif choice == 11:
                    print('')
                    More()._revertAltTab()
                    sleep(2)  
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   