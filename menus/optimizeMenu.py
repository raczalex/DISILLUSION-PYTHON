
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.optimize import Optimize

class OptimizeMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [OPTIMIZE]')

    def _displayMenu(self):
        
        options = [
            "Do All Except Enable / Disable Game Mode",
            "Optimize Capability Access Manager",
            "Disable Office Telemetry",
            "Disable Fault Tolerant Heap",
            "Disable Smart Screen",
            "Optimize Windows Privacy Settings",
            "Disable Diagnostic Services",
            "Stop Reinstalling Preinstalled Apps",
            "Disable Background Apps",
            "Disable Printing Map Services",
            "Deny Apps Access Account Info",
            "Deny Apps Access To Diagnostic",
            "Deny Apps Access To Contacts",
            "Disable Call History",
            'Disable Email',
            'Disable Tasks',
            'Disable Bluetooth Services',
            "Track Only Important Failure Events",
            "Disable Windows Customer Experience Index",
            "Disable Sync",
            "Disable Application Diagnostics Telemetry",
            "Disable Telemetry Through Task Scheduler",
            "Disable Telemetry Through Registry",
            "Enable Game Mode",
            "Disable Game Mode",
            "Disable Feedback",
            "Disable Error Reporting",
            "Disable Telemetry Optimize Windows Settings",
            "Disable Ads And Pop Ups",
            "Windows Tweaks",
            "Menu Kill Time",
            "Explorer Tweaks",
            "Additional Tweaks"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [OPTIMIZE]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    Optimize()._doAll()
                    sleep(2)
                elif choice == 2:
                    print('')
                    Optimize()._optimizeCapabilityAccessManager()
                    sleep(2)    
                elif choice == 3:
                    print('')
                    Optimize()._disableOfficeTelemetry()
                    sleep(2)    
                elif choice == 4:
                    print('')
                    Optimize()._disableFaultTolerantHeap()
                    sleep(2)    
                elif choice == 5:
                    print('')
                    Optimize()._disableSmartScreen()
                    sleep(2)    
                elif choice == 6:
                    print('')
                    Optimize()._OptimizeWindowsPrivacySettings()
                    sleep(2)    
                elif choice == 7:
                    print('')
                    Optimize()._disableDiagnosticServices()
                    sleep(2)    
                elif choice == 8:
                    print('')
                    Optimize()._stopReinstallingPreinstalledApps()
                    sleep(2)    
                elif choice == 9:
                    print('')
                    Optimize()._disableBackgroundApps()
                    sleep(2)    
                elif choice == 10:
                    print('')
                    Optimize()._disablePrintingMapServices()
                    sleep(2)    
                elif choice == 11:
                    print('')
                    Optimize()._noAppsAccessAccountInfo()
                    sleep(2)    
                elif choice == 12:
                    print('')
                    Optimize()._denyAppsAccessToDiagnostic()
                    sleep(2)    
                elif choice == 13:
                    print('')
                    Optimize()._denyAppsAccessToContacts()
                    sleep(2)    
                elif choice == 14:
                    print('')
                    Optimize()._disableCallHistory()
                    sleep(2)    
                elif choice == 15:
                    print('')
                    Optimize()._disableEmail()
                    sleep(2)    
                elif choice == 16:
                    print('')
                    Optimize()._disableTasks()
                    sleep(2)    
                elif choice == 17:
                    print('')
                    Optimize()._disableBluetoothServices()
                    sleep(2)    
                elif choice == 18:
                    print('')
                    Optimize()._trackOnlyImportantFailureEvents()
                    sleep(2)
                elif choice == 19:
                    print('')
                    Optimize()._disableWindowsCustomerExperienceIndex()
                    sleep(2)   
                elif choice == 20:
                    print('')
                    Optimize()._disableSync()
                    sleep(2)   
                elif choice == 21:
                    print('')
                    Optimize()._disableApplicationDiagnosticsTelemetry()
                    sleep(2)   
                elif choice == 22:
                    print('')
                    Optimize()._disableTelemetryThroughTaskScheduler()
                    sleep(2)   
                elif choice == 23:
                    print('')
                    Optimize()._disableTelemetryThroughRegistry()
                    sleep(2)   
                elif choice == 24:
                    print('')
                    Optimize()._enableGameMode()
                    sleep(2)   
                elif choice == 25:
                    print('')
                    Optimize()._disableGameMode()
                    sleep(2)   
                elif choice == 26:
                    print('')
                    Optimize()._disableFeedBack()
                    sleep(2)   
                elif choice == 27:
                    print('')
                    Optimize()._disableErrorReporting()
                    sleep(2)   
                elif choice == 28:
                    print('')
                    Optimize()._disableTelemetryOptimizeWindowsSettings()
                    sleep(2)   
                elif choice == 29:
                    print('')
                    Optimize()._disableAdsAndPopUps()
                    sleep(2) 
                elif choice == 30:
                    print('')
                    Optimize()._windowsTweaks()
                    sleep(2)
                elif choice == 31:
                    print('')
                    Optimize()._menuKillTime()
                    sleep(2)
                elif choice == 32:
                    print('')
                    Optimize()._explorerTweaks()
                    sleep(2)
                elif choice == 33:
                    print('')
                    Optimize()._additionalTweaks()
                    sleep(2)                     
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   