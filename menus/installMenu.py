
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.install import Install

class InstallMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [INSTALL]')

    def _displayMenu(self):
        
        options = [
            "Do All",
            "Disillusion",
            "Firefox",
            "Chrome",
            "Opera",
            "Brave",
            "Discord",
            "Messenger",
            "TeamSpeak",
            "AnyDesk",
            "VLC",
            "MPV",
            "Spotify",
            "Steam",
            "Epic Games Launcher",
            "7-Zip",
            "WinRar",
            "Visual Studio Code",
            "Notepad++",
            "Git",
            "GitHub Desktop",
            "HWInfo",
            "GPU-Z",
            "CPU-Z",
            "MSI Afterburner",
            "YT-DLP",
            "GALLERY-DL"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [INSTALL]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    Install()._doAll()
                    sleep(2)
                elif choice == 2:
                    print('')
                    Install()._DISILLUSION()
                    sleep(2)    
                elif choice == 3:
                    print('')
                    Install()._installFirefox()
                    sleep(2)   
                elif choice == 4:
                    print('')
                    Install()._installChrome()
                    sleep(2)   
                elif choice == 5:
                    print('')
                    Install()._installOpera()
                    sleep(2)   
                elif choice == 6:
                    print('')
                    Install()._installBrave()
                    sleep(2)   
                elif choice == 7:
                    print('')
                    Install()._installDiscord()
                    sleep(2)   
                elif choice == 8:
                    print('')
                    Install()._installMessenger()
                    sleep(2)   
                elif choice == 9:
                    print('')
                    Install()._installTeamSpeak()
                    sleep(2)   
                elif choice == 10:
                    print('')
                    Install()._installAnyDesk()
                    sleep(2)   
                elif choice == 11:
                    print('')
                    Install()._installVLC()
                    sleep(2)   
                elif choice == 12:
                    print('')
                    Install()._installMPV()
                    sleep(2)   
                elif choice == 13:
                    print('')
                    Install()._installSpotify()
                    sleep(2)   
                elif choice == 14:
                    print('')
                    Install()._installSteam()
                    sleep(2)   
                elif choice == 15:
                    print('')
                    Install()._installEpicGames()
                    sleep(2)   
                elif choice == 16:
                    print('')
                    Install()._install7Zip()
                    sleep(2)   
                elif choice == 17:
                    print('')
                    Install()._installWinRar()
                    sleep(2)   
                elif choice == 18:
                    print('')
                    Install()._installVSCode()
                    sleep(2)   
                elif choice == 19:
                    print('')
                    Install()._installNotepadPlusPlus()
                    sleep(2)   
                elif choice == 20:
                    print('')
                    Install()._installGit()
                    sleep(2)   
                elif choice == 21:
                    print('')
                    Install()._installGitHubDesktop()
                    sleep(2)   
                elif choice == 22:
                    print('')
                    Install()._installHwInfo()
                    sleep(2)   
                elif choice == 23:
                    print('')
                    Install()._installGpuZ()
                    sleep(2)  
                elif choice == 24:
                    print('')
                    Install()._installCPUZ()
                    sleep(2)  
                elif choice == 25:
                    print('')
                    Install()._installMSIAfterburner()
                    sleep(2)  
                elif choice == 26:
                    print('')
                    Install()._installYTDLP()
                    sleep(2)  
                elif choice == 27:
                    print('')
                    Install()._installGalleryDL()
                    sleep(2)  
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   