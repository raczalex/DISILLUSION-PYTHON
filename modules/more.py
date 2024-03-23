import subprocess
from utilities import regedit
from utilities import print

class More():
    def __init__(self) -> None:
        pass

    def _changeSoundSettings(self):
        regedit._setHKLMregszREG('MORE',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Audio","Background Only","True")
        regedit._setHKLMdwordREG('MORE',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Audio","Clock Rate",10000)
        regedit._setHKLMdwordREG('MORE',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Audio","GPU Priority",12)
        regedit._setHKLMdwordREG('MORE',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Audio","Priority",6)
        regedit._setHKLMregszREG('MORE',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Audio","Scheduling Category","Medium")
        regedit._setHKLMregszREG('MORE',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Audio","SFIO Priority","Normal")

    def _showFileExtensions(self):
        regedit._setHKCUdwordREG('MORE',r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced','HideFileExt',0)
        regedit._setHKCRregszREG('MORE',r'lnkfile','NeverShowExt','')
        regedit._setHKCRregszREG('MORE',r'IE.AssocFile.URL','NeverShowExt','')
        regedit._setHKCRregszREG('MORE',r'IE.AssocFile.WEBSITE','NeverShowExt','')
        regedit._setHKCRregszREG('MORE',r'InternetShortcut','NeverShowExt','')
        regedit._setHKCRregszREG('MORE',r'Microsoft.Website','NeverShowExt','')
        regedit._setHKCRregszREG('MORE',r'piffile','NeverShowExt','')
        regedit._setHKCRregszREG('MORE',r'SHCmdFile','NeverShowExt','')
        regedit._setHKCRregszREG('MORE',r'LibraryFolder','NeverShowExt','')

    def _resetIpAddress(self):
        commands = [r'ipconfig /release',r'ipconfig /renew']
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('MORE',cmd)

    def _pinImportantFoldersToStart(self):
        regedit._setHKLMdwordREG('MORE',r"SOFTWARE\Microsoft\PolicyManager\current\device\Start","AllowPinnedFolderDocuments",1)
        regedit._setHKLMdwordREG('MORE',r"SOFTWARE\Microsoft\PolicyManager\current\device\Start","AllowPinnedFolderDocuments_ProviderSet",1)
        regedit._setHKLMdwordREG('MORE',r"SOFTWARE\Microsoft\PolicyManager\current\device\Start","AllowPinnedFolderDownloads",1)
        regedit._setHKLMdwordREG('MORE',r"SOFTWARE\Microsoft\PolicyManager\current\device\Start","AllowPinnedFolderDownloads_ProviderSet",1)
        regedit._setHKLMdwordREG('MORE',r"SOFTWARE\Microsoft\PolicyManager\current\device\Start","AllowPinnedFolderPersonalFolder",1)
        regedit._setHKLMdwordREG('MORE',r"SOFTWARE\Microsoft\PolicyManager\current\device\Start","AllowPinnedFolderPersonalFolder_ProviderSet",1)
        regedit._setHKLMdwordREG('MORE',r"SOFTWARE\Microsoft\PolicyManager\current\device\Start","AllowPinnedFolderFileExplorer",1)
        regedit._setHKLMdwordREG('MORE',r"SOFTWARE\Microsoft\PolicyManager\current\device\Start","AllowPinnedFolderFileExplorer_ProviderSet",1)

    def _arrangeDesktopIcons(self):
        regedit._setHKCUdwordREG('MORE',r"Software\Microsoft\Windows\Shell\Bags\1\Desktop","FFlags",1075839525)

    def _syncTime(self):
        commands = [r'net stop w32time',
                    r'w32tm /unregister',
                    r'w32tm /register',
                    r'w32tm /config /syncfromflags:manual /manualpeerlist:"0.pool.ntp.org 1.pool.ntp.org 2.pool.ntp.org 3.pool.ntp.org" /reliable:YES',
                    r'net start w32time',
                    r'w32tm /config /update',
                    r'w32tm /resync /rediscover'
                    ]
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('MORE',cmd)

    def _betterWallpaperQuality(self):
        regedit._setHKCUdwordREG('MORE',r"Control Panel\Desktop","JPEGImportQuality",100)

    def _betterAltTab(self):
        regedit._setHKCUdwordREG('MORE',r"Software\Microsoft\Windows\CurrentVersion\Explorer","AltTabSettings",1)

    def _revertAltTab(self):
        regedit._setHKCUdwordREG('MORE',r"Software\Microsoft\Windows\CurrentVersion\Explorer","AltTabSettings",0)

    def _disableUAC(self):
        regedit._setHKLMdwordREG('MORE',r"Software\Microsoft\Windows\CurrentVersion\Policies\System","EnableVirtualization",0)
        regedit._setHKLMdwordREG('MORE',r"Software\Microsoft\Windows\CurrentVersion\Policies\System","EnableInstallerDetection",0)
        regedit._setHKLMdwordREG('MORE',r"Software\Microsoft\Windows\CurrentVersion\Policies\System","PromptOnSecureDesktop",0)
        regedit._setHKLMdwordREG('MORE',r"Software\Microsoft\Windows\CurrentVersion\Policies\System","EnableLUA",0)
        regedit._setHKLMdwordREG('MORE',r"Software\Microsoft\Windows\CurrentVersion\Policies\System","EnableSecureUIAPaths",0)
        regedit._setHKLMdwordREG('MORE',r"Software\Microsoft\Windows\CurrentVersion\Policies\System","ConsentPromptBehaviorAdmin",0)
        regedit._setHKLMdwordREG('MORE',r"Software\Microsoft\Windows\CurrentVersion\Policies\System","ValidateAdminCodeSignatures",0)
        regedit._setHKLMdwordREG('MORE',r"Software\Microsoft\Windows\CurrentVersion\Policies\System","EnableUIADesktopToggle",0)
        regedit._setHKLMdwordREG('MORE',r"Software\Microsoft\Windows\CurrentVersion\Policies\System","ConsentPromptBehaviorUser",0)
        regedit._setHKLMdwordREG('MORE',r"Software\Microsoft\Windows\CurrentVersion\Policies\System","FilterAdministratorToken",0)