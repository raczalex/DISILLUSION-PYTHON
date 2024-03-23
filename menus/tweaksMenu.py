
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.tweaks import Tweaks

class TweaksMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [TWEAKS]')

    def _displayMenu(self):
        
        options = [
            "Do All Except Force Monitor",
            "Monitor Latency Tolerance",
            "Force Monitor Hz (60)",
            "Force Monitor Hz (75)",
            "Force Monitor Hz (120)",
            "Force Monitor Hz (144)",
            "Force Monitor Hz (160)",
            "Force Monitor Hz (165)",
            "Force Monitor Hz (240)",
            "Force Monitor Hz (280)",
            "Force Monitor Hz (360)",
            "Force Monitor Hz (540)",
            "Force Monitor Hz (Custom)",
            "Speed Up Startup Time",
            "Disable DMA Remapping",
            "Microsoft Multimedia Tweaks",
            "Harden SMB",
            "Enable Memory Mapping For PCI-E Devices",
            "Harden Security",
            "Health Monitor",
            "Game DVR Xbox Disable",
            "Latency Tolerance",
            "Optimize Search",
            "NTFS Tweaks",
            "Disable Bing",
            'Disable Hyper-V',
            'Disable Lazy Mode',
            'Disable Maintenance',
            "Disable Auto Loggers",
            "Disable Windows Insider",
            "Disable & Remove OneDrive",
            "Optimize Resource Policy",
            "Disable Mitigations",
            "Disable Sub Mitigations",
            "Disable Sehop",
            "IO Tweaks + Boost",
            "Kernel Tweaks",
            "Latency Cap Tweaks",
            "Additional Tweaks",
            "Optimize MMCSS"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [TWEAKS]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    Tweaks()._doAll()
                    sleep(2)
                elif choice == 2:
                    print('')
                    Tweaks()._monitorLatencyTolerance()
                    sleep(2)
                elif choice == 3:
                    print('')
                    Tweaks()._force60hz()
                    sleep(2)
                elif choice == 4:
                    print('')
                    Tweaks()._force75hz()
                    sleep(2)
                elif choice == 5:
                    print('')
                    Tweaks()._force120hz()
                    sleep(2)
                elif choice == 6:
                    print('')
                    Tweaks()._force144hz()
                    sleep(2)
                elif choice == 7:
                    print('')
                    Tweaks()._force160hz()
                    sleep(2)
                elif choice == 8:
                    print('')
                    Tweaks()._force165hz()
                    sleep(2)
                elif choice == 9:
                    print('')
                    Tweaks()._force240hz()
                    sleep(2)
                elif choice == 10:
                    print('')
                    Tweaks()._force280hz()
                    sleep(2)
                elif choice == 11:
                    print('')
                    Tweaks()._force360hz()
                    sleep(2) 
                elif choice == 12:
                    print('')
                    Tweaks()._force540hz()
                    sleep(2)
                elif choice == 13:
                    print('')
                    monitor_hz = int(input(f"   {Colors.white}[TWEAKS]{Colors.light_green} Enter the number of hz:{Colors.white} "))
                    Tweaks()._forceMonitorHz(monitor_hz)
                    sleep(2)
                elif choice == 14:
                    print('')
                    Tweaks()._speedUpStartupTime()
                    sleep(2) 
                elif choice == 15:
                    print('')
                    Tweaks()._disableDMARemapping()
                    sleep(2) 
                elif choice == 16:
                    print('')
                    Tweaks()._microsoftMultimediaTweaks()
                    sleep(2)  
                elif choice == 17:
                    print('')
                    Tweaks()._hardenSMB()
                    sleep(2)  
                elif choice == 18:
                    print('')
                    Tweaks()._enableMemoryMappingForPcieDevices()
                    sleep(2)  
                elif choice == 19:
                    print('')
                    Tweaks()._hardenSecurity()
                    sleep(2) 
                elif choice == 20:
                    print('')
                    Tweaks()._healthMonitor()
                    sleep(2) 
                elif choice == 21:
                    print('')
                    Tweaks()._gameDVRXboxDisable()
                    sleep(2) 
                elif choice == 22:
                    print('')
                    Tweaks()._latencyTolerance()
                    sleep(2) 
                elif choice == 23:
                    print('')
                    Tweaks()._optimizeSearch()
                    sleep(2) 
                elif choice == 24:
                    print('')
                    Tweaks()._ntfsTweaks()
                    sleep(2) 
                elif choice == 25:
                    print('')
                    Tweaks()._disableBing()
                    sleep(2) 
                elif choice == 26:
                    print('')
                    Tweaks()._disableHyperV()
                    sleep(2) 
                elif choice == 27:
                    print('')
                    Tweaks()._disableLazyMode()
                    sleep(2) 
                elif choice == 28:
                    print('')
                    Tweaks()._disableMaintenance()
                    sleep(2) 
                elif choice == 29:
                    print('')
                    Tweaks()._disableAutoLoggers()
                    sleep(2) 
                elif choice == 30:
                    print('')
                    Tweaks()._disableWindowsInsider()
                    sleep(2) 
                elif choice == 31:
                    print('')
                    Tweaks()._disableRemoveOneDrive()
                    sleep(2) 
                elif choice == 32:
                    print('')
                    Tweaks()._optimizeResourcePolicy()
                    sleep(2) 
                elif choice == 33:
                    print('')
                    Tweaks()._disableMitigations()
                    sleep(2) 
                elif choice == 34:
                    print('')
                    Tweaks()._disableSubMitigations()
                    sleep(2) 
                elif choice == 35:
                    print('')
                    Tweaks()._disableSehop()
                    sleep(2)
                elif choice == 36:
                    print('')
                    Tweaks()._ioTweaksBoost()
                    sleep(2) 
                elif choice == 37:
                    print('')
                    Tweaks()._kernel()
                    sleep(2) 
                elif choice == 38:
                    print('')
                    Tweaks()._latencyCapTweaks()
                    sleep(2) 
                elif choice == 39:
                    print('')
                    Tweaks()._additionalTweaks()
                    sleep(2)  
                elif choice == 40:
                    print('')
                    Tweaks()._optimizeMMCSS()
                    sleep(2)   
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   