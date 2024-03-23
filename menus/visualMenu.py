
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.visual import Visual

class VisualMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [VISUAL]')

    def _displayMenu(self):
        
        options = [
            "Do All",
            "Disable Transparency",
            "Disable Animations On Taskbar",
            "Show Translucent Selection Rectangle",
            "Disable Balloon Tips",
            "Disable Windows Aero Shake",
            "Disable People Button",
            "Disable Activity Feed",
            "Disable Task View Button",
            "Restore Network Folder Connection",
            "Disable Meet Now",
            "Disable News And Weather",
            "Disable Windows Tips",
            "Allow File Path More Than 260 Chars",
            "Disable File Explorer Ads",
            "Enable Dark Theme",
            "Open Windows Visual Tweaks"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [VISUAL]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                elif choice == 2:
                    print('')
                    Visual()._disableTransparency()
                    sleep(2)    
                elif choice == 3:
                    print('')
                    Visual()._disableAnimationsInTaskbar()
                    sleep(2) 
                elif choice == 4:
                    print('')
                    Visual()._showTranslucentSelectionRectangle()
                    sleep(2) 
                elif choice == 5:
                    print('')
                    Visual()._disableBalloonTips()
                    sleep(2) 
                elif choice == 6:
                    print('')
                    Visual()._disableWindowsAeroShake()
                    sleep(2) 
                elif choice == 7:
                    print('')
                    Visual()._removePeopleButton()
                    sleep(2) 
                elif choice == 8:
                    print('')
                    Visual()._disableActivityFeed()
                    sleep(2) 
                elif choice == 9:
                    print('')
                    Visual()._disableTaskViewButton()
                    sleep(2) 
                elif choice == 10:
                    print('')
                    Visual()._restoreNetworkFolderConnection()
                    sleep(2) 
                elif choice == 11:
                    print('')
                    Visual()._disableMeetNow()
                    sleep(2) 
                elif choice == 12:
                    print('')
                    Visual()._disableNewsAndWeather()
                    sleep(2) 
                elif choice == 13:
                    print('')
                    Visual()._disableWindowsTips()
                    sleep(2) 
                elif choice == 14:
                    print('')
                    Visual()._allowFilePathMoreThan260Chars()
                    sleep(2) 
                elif choice == 15:
                    print('')
                    Visual()._disableFileExplorerAds()
                    sleep(2) 
                elif choice == 16:
                    print('')
                    Visual()._enableDarkTheme()
                    sleep(2)
                elif choice == 17:
                    print('')
                    Visual()._openWindowsVisualTweaks()
                    sleep(2) 
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   