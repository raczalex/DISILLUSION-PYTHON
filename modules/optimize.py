from utilities import regedit
from winreg import HKEY_LOCAL_MACHINE
from utilities import print
import subprocess

class Optimize():
    def __init__(self) -> None:
        pass

    def _optimizeCapabilityAccessManager(self):
        regedit._setHKLMregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appDiagnostics","Value","Deny")
        regedit._setHKLMregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appointments","Value","Deny")
        regedit._setHKLMregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\email","Value","Deny")
        regedit._setHKLMregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\phoneCall","Value","Deny")
        regedit._setHKLMregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\userDataTasks","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{C1D23ACC-752B-43E5-8448-8D0E519CD6D6}","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{2297E4E2-5DBE-466D-A12B-0F8286F0D9CA}","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{E5323777-F976-4f5b-9B55-B94699C46E44}","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{2EEF81BE-33FA-4800-9670-1CD474972C3F}","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{52079E78-A92B-413F-B213-E8FE35712E72}","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{7D7E8402-7C54-4821-A34E-AEEFD62DED93}","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{D89823BA-7180-4B81-B50C-7E471E6121A3}","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{8BC668CF-7728-45BD-93F8-CF2B3B41D7AB}","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{9231CB4C-BF57-4AF3-8C55-FDA7BFCC04C5}","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{E390DF20-07DF-446D-B962-F5C953062741}","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{992AFA70-6F47-4148-B3E9-3003349C1548}","Value","Deny")
        regedit._setHKLMregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\chat","Value","Deny")
        regedit._setHKLMregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\contacts","Value","Deny")
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\Messaging","AllowMessageSync",0)

    def _disableOfficeTelemetry(self):
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\Common\ClientTelemetry","DisableTelemetry",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\Common","sendcustomerdata",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\Common\Feedback","enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\Common\Feedback","includescreenshot",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\Outlook\Options\Mail","EnableLogging",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\Word\Options","EnableLogging",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\Common\ClientTelemetry","SendTelemetry",3)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\Common","qmenable",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\Common","updatereliabilitydata",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\Common\General","shownfirstrunoptin",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\Common\General","skydrivesigninoption",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\Common\ptwatson","ptwoptin",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\Firstrun","disablemovie",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\OSM","Enablelogging",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\OSM","EnableUpload",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\OSM","EnableFileObfuscation",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\OSM\preventedapplications","accesssolution",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\OSM\preventedapplications","olksolution",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\OSM\preventedapplications","onenotesolution",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\OSM\preventedapplications","pptsolution",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\OSM\preventedapplications","projectsolution",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\OSM\preventedapplications","publishersolution",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\OSM\preventedapplications","visiosolution",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\OSM\preventedapplications","wdsolution",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\OSM\preventedapplications","xlsolution",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\OSM\preventedsolutiontypes","agave",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\OSM\preventedsolutiontypes","appaddins",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\OSM\preventedsolutiontypes","comaddins",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\OSM\preventedsolutiontypes","documentfiles",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Office\16.0\OSM\preventedsolutiontypes","templatefiles",1)

    def _disableFaultTolerantHeap(self):
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\FTH","Enabled",0)

    def _disableSmartScreen(self):
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\System","EnableSmartScreen",0)
        regedit._setHKLMregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer","SmartScreenEnabled","Off")
        regedit._setHKUdwordREG('OPTIMIZE',f"{regedit._getSID()}\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\AppHost","EnableWebContentEvaluation",0)

    def _OptimizeWindowsPrivacySettings(self):
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\activity","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appDiagnostics","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appointments","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\bluetoothSync","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\broadFileSystemAccess","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\chat","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\contacts","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\documentsLibrary","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\gazeInput","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\microphone","Value","Allow")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\microphone\Microsoft.Win32WebViewHost_cw5n1h2txyewy","Value","Prompt")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\phoneCall","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\phoneCallHistory","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\picturesLibrary","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\radios","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\userNotificationListener","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\videosLibrary","Value","Deny")        

    def _stopReinstallingPreinstalledApps(self):
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SystemPaneSuggestionsEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-338388Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-314559Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-280815Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-314563Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-338393Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-353694Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-353696Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-310093Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-202914Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-338387Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-338389Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-353698Enabled",0)

    def _disableBackgroundApps(self):
        regedit._setHKUdwordREG('OPTIMIZE',f"{regedit._getSID()}\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications","GlobalUserDisabled",1)
        regedit._setHKUdwordREG('OPTIMIZE',f"{regedit._getSID()}\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Search","BackgroundAppGlobalToggle",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SYSTEM\CurrentControlSet\Services\bam","Start",4)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SYSTEM\CurrentControlSet\Services\dam","Start",4)

    def _disablePrintingMapServices(self):
        regedit._setHKLMdwordREG('OPTIMIZE',r"SYSTEM\CurrentControlSet\Services\Spooler","Start",4)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SYSTEM\CurrentControlSet\Services\PrintNotify","Start",4)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SYSTEM\CurrentControlSet\Services\MapsBroker","Start",4)

    def _disableDiagnosticServices(self):
        commands = [r"sc stop DiagTrack",
                    r"sc config DiagTrack start= disabled",
                    r"sc stop dmwappushservice",
                    r"sc config dmwappushservice start= disabled",
                    r"sc stop diagnosticshub.standardcollector.service",
                    r"sc config diagnosticshub.standardcollector.service start= disabled",
                    r'schtasks /change /tn "\Microsoft\Windows\Application Experience\StartupAppTask" /disable',
                    r'schtasks /end /tn "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector"', 
                    r'schtasks /change /tn "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector" /disable',
                    r'schtasks /end /tn "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver"', 
                    r'schtasks /change /tn "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver" /disable',
                    r'schtasks /end /tn "\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem"',
                    r'schtasks /change /tn "\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem" /disable'
                    ]
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('OPTIMIZE',cmd)

        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","PreInstalledAppsEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SilentInstalledAppsEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","OemPreInstalledAppsEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","ContentDeliveryAllowed",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContentEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","PreInstalledAppsEverEnabled",0)

    def _noAppsAccessAccountInfo(self):
        regedit._setHKCUregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{C1D23ACC-752B-43E5-8448-8D0E519CD6D6}","Value","Deny")

    def _denyAppsAccessToDiagnostic(self):
        regedit._setHKCUregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{2297E4E2-5DBE-466D-A12B-0F8286F0D9CA}","Value","Deny")
    
    def _denyAppsAccessToContacts(self):
        regedit._setHKCUregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{7D7E8402-7C54-4821-A34E-AEEFD62DED93}","Value","Deny")
    
    def _disableCallHistory(self):
        regedit._setHKCUregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{8BC668CF-7728-45BD-93F8-CF2B3B41D7AB}","Value","Deny")

    def _disableEmail(self):
        regedit._setHKCUregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{9231CB4C-BF57-4AF3-8C55-FDA7BFCC04C5}","Value","Deny")

    def _disableTasks(self):
        regedit._setHKCUregszREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{E390DF20-07DF-446D-B962-F5C953062741}","Value","Deny")

    def _disableBluetoothServices(self):
        regedit._setHKLMdwordREG('OPTIMIZE',r"SYSTEM\ControlSet001\Services\BTAGService","Start",4)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SYSTEM\ControlSet001\Services\bthserv","Start",4)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SYSTEM\ControlSet001\Services\BthAvctpSvc","Start",4)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SYSTEM\ControlSet001\Services\BluetoothUserService","Start",4)

    def _trackOnlyImportantFailureEvents(self):
        commands = [r'Auditpol /set /subcategory:"Process Termination" /success:disable /failure:enable',
                    r'Auditpol /set /subcategory:"RPC Events" /success:disable /failure:enable',
                    r'Auditpol /set /subcategory:"Filtering Platform Connection" /success:disable /failure:enable',
                    r'Auditpol /set /subcategory:"DPAPI Activity" /success:disable /failure:disable',
                    r'Auditpol /set /subcategory:"IPsec Driver" /success:disable /failure:enable',
                    r'Auditpol /set /subcategory:"Other System Events" /success:disable /failure:enable',
                    r'Auditpol /set /subcategory:"Security State Change" /success:disable /failure:enable',
                    r'Auditpol /set /subcategory:"Security System Extension" /success:disable /failure:enable',
                    r'Auditpol /set /subcategory:"System Integrity" /success:disable /failure:enable'
                    ]

        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('OPTIMIZE',cmd)

        regedit._setHKLMdwordREG('OPTIMIZE',r"System\CurrentControlSet\Control\WMI\Autologger\AutoLogger-Diagtrack-Listener","Start",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"System\CurrentControlSet\Control\WMI\Autologger\DiagLog","Start",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"System\CurrentControlSet\Control\WMI\Autologger\Diagtrack-Listener","Start",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"System\CurrentControlSet\Control\WMI\Autologger\WiFiSession","Start",0)

    def _disableWindowsCustomerExperienceIndex(self):
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\SQMClient\IE","CEIPEnable",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\SQMClient\IE","SqmLoggerRunning",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\SQMClient\Reliability","CEIPEnable",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\SQMClient\Reliability","SqmLoggerRunning",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\SQMClient\Windows","CEIPEnable",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\SQMClient\Windows","DisableOptinExperience",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\SQMClient\Windows","SqmLoggerRunning",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\AppV\CEIP","CEIPEnable",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Messenger\Client","CEIP",2)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\SQMClient\Windows","CEIPEnable",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Policies\Microsoft\Internet Explorer\SQM","DisableCustomerImprovementProgram",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Policies\Microsoft\Windows\AppCompat","DisablePCA",1)

    def _disableSync(self):
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Accessibility","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\AppSync","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\BrowserSettings","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Credentials","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\DesktopTheme","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Language","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\PackageState","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Personalization","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\StartLayout","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Windows","Enabled",0)

    def _disableApplicationDiagnosticsTelemetry(self):
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\AppCompat","DisableInventory",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\AppCompat","AITEnable",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\AppCompat","DisableUAR",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\AppCompat","VDMDisallowed",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\AppCompat","DisableEngine",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\AppCompat","DisableWizard",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\AppCompat","DisablePCA",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\AppCompat","SbEnable",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-Application-Experience/Steps-Recorder","Enabled",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Policies\Microsoft\DeviceHealthAttestationService","DisableSendGenericDriverNotFoundToWER",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\DeviceInstall\Settings","DisableSendGenericDriverNotFoundToWER",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SYSTEM\DriverDatabase\Policies\Settings","DisableSendGenericDriverNotFoundToWER",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Policies\Microsoft\Windows\CloudContent","ConfigureWindowsSpotlight",2)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Policies\Microsoft\Windows\CloudContent","DisableThirdPartySuggestions",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Policies\Microsoft\Windows\CloudContent","DisableWindowsSpotlightFeatures",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\CloudContent","DisableWindowsConsumerFeatures",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","ContentDeliveryAllowed",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","FeatureManagementEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","OemPreInstalledAppsEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","PreInstalledAppsEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","PreInstalledAppsEverEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","RemediationRequired",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SilentInstalledAppsEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SoftLandingEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\UserProfileEngagement","ScoobeSystemSettingEnabled",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer","AllowOnlineTips",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Policies\Microsoft\PushToInstall","DisablePushToInstall",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SystemPaneSuggestionsEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-310093Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-338388Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-338389Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-353698Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-338387Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-338393Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-353694Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-353696Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-314563Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-314559Enabled",0)

    def _disableTelemetryThroughTaskScheduler(self):
        commands = [r'schtasks /end /tn "\Microsoft\Windows\Customer Experience Improvement Program\Consolidator"',
                    r'schtasks /change /tn "\Microsoft\Windows\Customer Experience Improvement Program\Consolidator" /disable',
                    r'schtasks /end /tn "\Microsoft\Windows\Customer Experience Improvement Program\BthSQM"',
                    r'schtasks /change /tn "\Microsoft\Windows\Customer Experience Improvement Program\BthSQM" /disable',
                    r'schtasks /end /tn "\Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask"',
                    r'schtasks /change /tn "\Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask" /disable',
                    r'schtasks /end /tn "\Microsoft\Windows\Customer Experience Improvement Program\UsbCeip"',
                    r'schtasks /change /tn "\Microsoft\Windows\Customer Experience Improvement Program\UsbCeip" /disable',
                    r'schtasks /end /tn "\Microsoft\Windows\Customer Experience Improvement Program\Uploader"',
                    r'schtasks /change /tn "\Microsoft\Windows\Customer Experience Improvement Program\Uploader" /disable',
                    r'schtasks /end /tn "\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser"',
                    r'schtasks /change /tn "\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser" /disable',
                    r'schtasks /end /tn "\Microsoft\Windows\Application Experience\ProgramDataUpdater"',
                    r'schtasks /change /tn "\Microsoft\Windows\Application Experience\ProgramDataUpdater" /disable',
                    r'schtasks /end /tn "\Microsoft\Windows\Application Experience\StartupAppTask"',
                    r'schtasks /end /tn "\Microsoft\Windows\Shell\FamilySafetyMonitor"',
                    r'schtasks /change /tn "\Microsoft\Windows\Shell\FamilySafetyMonitor" /disable',
                    r'schtasks /end /tn "\Microsoft\Windows\Shell\FamilySafetyRefresh"',
                    r'schtasks /change /tn "\Microsoft\Windows\Shell\FamilySafetyRefresh" /disable',
                    r'schtasks /end /tn "\Microsoft\Windows\Shell\FamilySafetyUpload"',
                    r'schtasks /change /tn "\Microsoft\Windows\Shell\FamilySafetyUpload" /disable',
                    r'schtasks /end /tn "\Microsoft\Windows\Maintenance\WinSAT"']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('OPTIMIZE',cmd)

    def _disableTelemetryThroughRegistry(self):
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Device Metadata","PreventDeviceMetadataFromNetwork",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection","AllowTelemetry",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\InputPersonalization","RestrictImplicitInkCollection",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\InputPersonalization","RestrictImplicitTextCollection",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Sensor\Permissions\{BFA794E4-F964-4FDB-90F6-51056BFE4B44}","SensorPermissionState",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Sensor\Overrides\{BFA794E4-F964-4FDB-90F6-51056BFE4B44}","SensorPermissionState",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\WUDF","LogEnable",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\WUDF","LogLevel",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\DataCollection","AllowTelemetry",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\DataCollection","DoNotShowFeedbackNotifications",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\DataCollection","AllowCommercialDataPipeline",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\DataCollection","AllowDeviceNameInTelemetry",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\DataCollection","LimitEnhancedDiagnosticDataWindowsAnalytics",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\DataCollection","MicrosoftEdgeDataOptIn",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Siuf\Rules","NumberOfSIUFInPeriod",0)
        regedit._setHKCUdwordREG('OPTIMIZE', r"SOFTWARE\Microsoft\Siuf\Rules","PeriodInNanoSeconds",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Assistance\Client\1.0","NoExplicitFeedback",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Assistance\Client\1.0","NoActiveHelp",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\AppCompat","DisableInventory",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\AppCompat","AITEnable",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\AppCompat","DisableUAR",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\TabletPC","PreventHandwritingDataSharing",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\TabletPC","DoSvc",3)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors","DisableLocation",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors","DisableLocationScripting",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors","DisableSensors",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors","DisableWindowsLocationProvider",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\DeviceHealthAttestationServices","DisableSendGenericDriverNotFoundToWER",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\DeviceInstall\Settings","DisableSendGenericDriverNotFoundToWER",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SYSTEM\DriverDatabase\Policies\Settings","DisableSendGenericDriverNotFoundToWER",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\System","PublishUserActivities",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\System","EnableActivityFeed",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\System","UploadUserActivities",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\SQMClient\Windows","CEIPEnable",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\SQMClient\Reliability","CEIPEnable",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\SQMClient\Reliability","SqmLoggerRunning",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\SQMClient\Windows","CEIPEnable",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\SQMClient\Windows","DisableOptinExperience",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\SQMClient\Windows","SqmLoggerRunning",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\SQMClient\IE","SqmLoggerRunning",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\HandwritingErrorReports","PreventHandwritingErrorReports",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\MediaPlayer\Preferences","UsageTracking",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\CloudContent","DisableSoftLanding",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Peernet","Disabled",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\DeliveryOptimization\Config","DODownloadMode",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\PolicyManager\default\WiFi\AllowWiFiHotSpotReporting","value",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\InputPersonalization\TrainedDataStore","HarvestContacts",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo","Enabled",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\AdvertisingInfo","DisabledByGroupPolicy",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\MRT","DontOfferThroughWUAU",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Biometrics","Enabled",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SYSTEM\CurrentControlSet\Services\dmwappushservice","Start",4)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SYSTEM\DriverDatabase\Policies\Settings","DisableSendGenericDriverNotFoundToWER",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Control Panel\International\User Profile","HttpAcceptLanguageOptOut",1)

    def _enableGameMode(self):
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\GameBar","AllowAutoGameMode",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\GameBar","AutoGameModeEnabled",1)

    def _disableGameMode(self):
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\GameBar","AllowAutoGameMode",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\GameBar","AutoGameModeEnabled",0)
        
    def _disableFeedBack(self):
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Policies\Microsoft\Windows\DataCollection","DoNotShowFeedbackNotifications",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Siuf\Rules","NumberOfSIUFInPeriod",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Siuf\Rules","PeriodInNanoSeconds",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Policies\Microsoft\Assistance\Client\1.0","NoExplicitFeedback",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Assistance\Client\1.0\Settings","ImplicitFeedback",0)

    def _disableErrorReporting(self):
        commands = [r'sc stop WerSvc',r'sc config WerSvc start= disabled']
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('OPTIMIZE',cmd)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Control Panel\International\User Profile","HttpAcceptLanguageOptOut",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\AppHost","EnableWebContentEvaluation",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\Windows Error Reporting","DontShowUI",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\Windows Error Reporting","Disabled",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\Windows Error Reporting","DontSendAdditionalData",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\Windows Error Reporting","LoggingDisabled",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\Windows Error Reporting\Consent","DefaultConsent",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\Windows Error Reporting\Consent","DefaultOverrideBehavior",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\Windows Error Reporting","DontShowUI",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\PCHealth\ErrorReporting","DoReport",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\AdvertisingInfo","DisabledByGroupPolicy",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\HandwritingErrorReports","PreventHandwritingErrorReports",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\TabletPC","PreventHandwritingDataSharing",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting","AutoApproveOSDumps",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting","Disabled",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting","DontSendAdditionalData",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Microsoft\PCHealth\ErrorReporting","ShowUI",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Control Panel\International\User Profile","HttpAcceptLanguageOptOut",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\AppHost","EnableWebContentEvaluation",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\Windows Error Reporting","DontShowUI",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\Windows Error Reporting","Disabled",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\Windows Error Reporting","DontSendAdditionalData",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\Windows Error Reporting","LoggingDisabled",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\Windows Error Reporting\Consent","DefaultConsent",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\Windows Error Reporting\Consent","DefaultOverrideBehavior",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\Windows Error Reporting","DontShowUI",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\PCHealth\ErrorReporting","DoReport",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\AdvertisingInfo","DisabledByGroupPolicy",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\HandwritingErrorReports","PreventHandwritingErrorReports",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\TabletPC","PreventHandwritingDataSharing",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting","AutoApproveOSDumps",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting","Disabled",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting","DontSendAdditionalData",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SYSTEM\CurrentControlSet\Services\W3SVC","Start",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Microsoft\PCHealth\ErrorReporting","ShowUI",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\Windows Error Reporting","Disabled",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\Windows Error Reporting","DontSendAdditionalData",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\Windows Error Reporting","DontShowUI",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\Windows Error Reporting","LoggingDisabled",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\Windows Error Reporting\Consent","DefaultConsent",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\Windows Error Reporting\Consent","DefaultOverrideBehavior",1)

    def _disableTelemetryOptimizeWindowsSettings(self):
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\FTH","Enabled",0)
        regedit._deleteSubKey(HKEY_LOCAL_MACHINE,r'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Schedule\\TaskCache\\Tree\\MicrosoftEdgeUpdateTaskMachineCore')
        regedit._deleteSubKey(HKEY_LOCAL_MACHINE,r'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Schedule\\TaskCache\\Tree\\MicrosoftEdgeUpdateTaskMachineUA')
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Google\Chrome","StartupBoostEnabled",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Google\Chrome","BackgroundModeEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\DWM","UseDpiScaling",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Multimedia\Audio","UserDuckingPreference",3)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\BootAnimation","DisableStartupSound",1)
        regedit._setHKCUregszREG('OPTIMIZE',r"Control Panel\Mouse","MouseSpeed","0")
        regedit._setHKCUregszREG('OPTIMIZE',r"Control Panel\Mouse","MouseThreshold1","0")
        regedit._setHKCUregszREG('OPTIMIZE',r"Control Panel\Mouse","MouseThreshold2","0")
        regedit._setHKLMregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run","ctfmon",r"C:\Windows\System32\ctfmon.exe")
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\VideoSettings","VideoQualityOnBattery",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced","IconsOnly",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced","ListviewShadow",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Policies\Microsoft\Windows\DataCollection","AllowTelemetry",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\Policies\DataCollection","AllowTelemetry",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\DataCollection","AllowDeviceNameInTelemetry",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Policies\Microsoft\Windows\safer\codeidentifiers","authenticodeenabled",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Policies\Microsoft\Windows\Windows Error Reporting","DontSendAdditionalData",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Policies\DataCollection","AllowTelemetry",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Speech_OneCore\Settings\OnlineSpeechPrivacy","HasAccepted",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Personalization\Settings","AcceptedPrivacyPolicy",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\InputPersonalization","RestrictImplicitInkCollection",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\InputPersonalization","RestrictImplicitTextCollection",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\InputPersonalization\TrainedDataStore","HarvestContacts",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\DataCollection","AllowTelemetry",0)
        regedit._setHKUdwordREG('OPTIMIZE',r"S-1-5-20\Software\Microsoft\Windows\CurrentVersion\DeliveryOptimization\Settings","DownloadMode",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Control Panel\International\User Profile","HttpAcceptLanguageOptOut",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\DriverSearching","SearchOrderConfig",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Device Metadata","PreventDeviceMetadataFromNetwork",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU","NoAutoUpdate",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\DWM","EnableAeroPeek",0)
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\location","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appDiagnostics","Value","Deny")
        regedit._setHKCUregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\userAccountInformation","Value","Deny")
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SilentInstalledAppsEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SystemPaneSuggestionsEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SoftLandingEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","RotatingLockScreenEnabled",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\System","PublishUserActivities",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\System","UploadUserActivities",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications","GlobalUserDisabled",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\Search","BackgroundAppGlobalToggle",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\DeliveryOptimization\Config","DownloadMode",0)

    def _disableAdsAndPopUps(self):
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\PushNotifications","ToastEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Notifications\Settings","NOC_GLOBAL_SETTING_ALLOW_NOTIFICATION_SOUND",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Notifications\Settings","NOC_GLOBAL_SETTING_ALLOW_CRITICAL_TOASTS_ABOVE_LOCK",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Notifications\Settings\QuietHours","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Notifications\Settings\windows.immersivecontrolpanel_cw5n1h2txyewy!microsoft.windows.immersivecontrolpanel","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Notifications\Settings\Windows.SystemToast.AutoPlay","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Notifications\Settings\Windows.SystemToast.LowDisk","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Notifications\Settings\Windows.SystemToast.Print.Notification","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Notifications\Settings\Windows.SystemToast.SecurityAndMaintenance","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Notifications\Settings\Windows.SystemToast.WiFiNetworkManager","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\Explorer","DisableNotificationCenter",1)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\Windows Feeds","EnableFeeds",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft","AllowNewsAndInterests",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Windows\System","EnableActivityFeed",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Control Panel\International\User Profile","HttpAcceptLanguageOptOut",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\AdvertisingInfo","Enabled",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Policies\Microsoft\Windows\System","EnableActivityFeed",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced","DisallowShaking",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced","EnableBalloonTips",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced","ShowSyncProviderNotifications",0)
        regedit._setHKLMregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\userNotificationListener","Value","Deny")
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Policies\Microsoft\Windows\AdvertisingInfo","DisabledByGroupPolicy",1)

    def _windowsTweaks(self):
        regedit._setHKLMdwordREG('OPTIMIZE',r"SYSTEM\CurrentControlSet\Control\Remote Assistance","fAllowToGetHelp",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Edge","StartupBoostEnabled",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Policies\Microsoft\Edge","BackgroundModeEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\SearchSettings","IsDeviceSearchHistoryEnabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-338393Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-353694Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-353696Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Personalization","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\BrowserSettings","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Credentials","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Accessibility","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Windows","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync","SyncPolicy",5)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-338393Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-353694Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager","SubscribedContent-353696Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MultitaskingView\AllUpView","AllUpView",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MultitaskingView\AllUpView","Remove TaskView",1)

    def _menuKillTime(self):
        regedit._setHKCUregszREG('OPTIMIZE',r"Control Panel\Desktop","AutoEndTasks","1")
        regedit._setHKCUregszREG('OPTIMIZE',r"Control Panel\Desktop","HungAppTimeout","1000")
        regedit._setHKCUregszREG('OPTIMIZE',r"Control Panel\Desktop","WaitToKillAppTimeout","2000")
        regedit._setHKCUregszREG('OPTIMIZE',r"Control Panel\Desktop","LowLevelHooksTimeout","1000")
        regedit._setHKCUregszREG('OPTIMIZE',r"Control Panel\Desktop","MenuShowDelay","0")
        regedit._setHKLMregszREG('OPTIMIZE',r"SYSTEM\CurrentControlSet\Control","WaitToKillServiceTimeout","2000")

    def _explorerTweaks(self):
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced","Start_TrackProgs",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer","HideSCAHealth",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced","ExtendedUIHoverTime",196608)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced","DontPrettyPath",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced","ListviewShadow",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced","TaskbarAnimations",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer","HideSCAHealth",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer","NoLowDiskSpaceChecks",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer","LinkResolveIgnoreLinkInfo",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer","NoResolveSearch",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer","NoResolveTrack",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer","NoInternetOpenWith",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer","NoInstrumentation",1)

    def _additionalTweaks(self):
        regedit._setHKLMregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows Photo Viewer\Capabilities\FileAssociations",".tif","PhotoViewer.FileAssoc.Tiff")
        regedit._setHKLMregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows Photo Viewer\Capabilities\FileAssociations",".tiff","PhotoViewer.FileAssoc.Tiff")
        regedit._setHKLMregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows Photo Viewer\Capabilities\FileAssociations",".bmp","PhotoViewer.FileAssoc.Tiff")
        regedit._setHKLMregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows Photo Viewer\Capabilities\FileAssociations",".dib","PhotoViewer.FileAssoc.Tiff")
        regedit._setHKLMregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows Photo Viewer\Capabilities\FileAssociations",".gif","PhotoViewer.FileAssoc.Tiff")
        regedit._setHKLMregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows Photo Viewer\Capabilities\FileAssociations",".jfif","PhotoViewer.FileAssoc.Tiff")
        regedit._setHKLMregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows Photo Viewer\Capabilities\FileAssociations",".jpe","PhotoViewer.FileAssoc.Tiff")
        regedit._setHKLMregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows Photo Viewer\Capabilities\FileAssociations",".jpeg","PhotoViewer.FileAssoc.Tiff")
        regedit._setHKLMregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows Photo Viewer\Capabilities\FileAssociations",".jpg","PhotoViewer.FileAssoc.Tiff")
        regedit._setHKLMregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows Photo Viewer\Capabilities\FileAssociations",".jxr","PhotoViewer.FileAssoc.Tiff")
        regedit._setHKLMregszREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows Photo Viewer\Capabilities\FileAssociations",".png","PhotoViewer.FileAssoc.Tiff")
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\AppHost","ContentEvaluation",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Siuf\Rules","NumberOfSIUFInPeriod",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System","DisableAutomaticRestartSignOn",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"SYSTEM\GameConfigStore\Children\fefe78e0-cf54-411d-9154-04b8f488bea2","Flags",529)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Control Panel\International\User Profile","HttpAcceptLanguageOptOut",1)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\AdvertisingInfo","Enabled",0)
        regedit._setHKCUdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\AppHost","EnableWebContentEvaluation",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Microsoft\PolicyManager\default\WiFi\AllowAutoConnectToWiFiSenseHotspots","value",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Microsoft\PolicyManager\default\WiFi\AllowWiFiHotSpotReporting","value",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Microsoft\Windows\CurrentVersion\ImmersiveShell","UseActionCenterExperience",0)
        regedit._setHKLMdwordREG('OPTIMIZE',r"Software\Policies\Microsoft\Windows\EnhancedStorageDevices","TCGSecurityActivationDisabled",0)

    def _doAll(self):
        self._optimizeCapabilityAccessManager()
        self._disableOfficeTelemetry()
        self._disableFaultTolerantHeap()
        self._disableSmartScreen()
        self._OptimizeWindowsPrivacySettings()
        self._disableDiagnosticServices()
        self._stopReinstallingPreinstalledApps()
        self._disableBackgroundApps()
        self._disablePrintingMapServices()
        self._noAppsAccessAccountInfo()
        self._denyAppsAccessToDiagnostic()
        self._denyAppsAccessToContacts()
        self._disableCallHistory()
        self._disableEmail()
        self._disableTasks()
        self._disableBluetoothServices()
        self._trackOnlyImportantFailureEvents()
        self._disableWindowsCustomerExperienceIndex()
        self._disableSync()
        self._disableApplicationDiagnosticsTelemetry()
        self._disableTelemetryThroughTaskScheduler()
        self._disableTelemetryThroughRegistry()
        self._disableFeedBack()
        self._disableErrorReporting()
        self._disableTelemetryOptimizeWindowsSettings()
        self._disableAdsAndPopUps()
        self._windowsTweaks()
        self._menuKillTime()
        self._explorerTweaks()
        self._additionalTweaks()
