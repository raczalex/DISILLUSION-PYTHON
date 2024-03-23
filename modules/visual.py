from utilities import regedit,print
import subprocess
import os

class Visual():
    def __init__(self) -> None:
        pass

    def _disableTransparency(self):
        regedit._setHKCUdwordREG('VISUAL',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize","EnableTransparency",0)

    def _disableAnimationsInTaskbar(self):
        regedit._setHKCUdwordREG('VISUAL',r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced","TaskbarAnimations",0)

    def _showTranslucentSelectionRectangle(self):
        regedit._setHKCUdwordREG('VISUAL',r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced","ListviewAlphaSelect",0)
    
    def _disableBalloonTips(self):
        regedit._setHKCUdwordREG('VISUAL',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced","EnableBalloonTips",0)

    def _disableWindowsAeroShake(self):
        regedit._setHKCUdwordREG('VISUAL',r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced","DisallowShaking",1)
    
    def _removePeopleButton(self):
        regedit._setHKCUdwordREG('VISUAL',r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\People","PeopleBand",0)

    def _disableActivityFeed(self):
        regedit._setHKLMdwordREG('VISUAL',r"Software\Policies\Microsoft\Windows\System","EnableActivityFeed",0)
    
    def _disableTaskViewButton(self):
        regedit._setHKCUdwordREG('VISUAL',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced","ShowTaskViewButton",0)

    def _restoreNetworkFolderConnection(self):
        regedit._setHKLMdwordREG('VISUAL',r"SYSTEM\CurrentControlSet\Control\NetworkProvider","RestoreConnection",0)

    def _disableMeetNow(self):
        regedit._setHKLMdwordREG('VISUAL',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer","HideSCAMeetNow",1)

    def _disableNewsAndWeather(self):
        regedit._setHKCUdwordREG('VISUAL',r"Software\Microsoft\Windows\CurrentVersion\Feeds","ShellFeedsTaskbarViewMode",2)

    def _disableWindowsTips(self):
        regedit._setHKLMdwordREG('VISUAL',r"Software\Policies\Microsoft\Windows\CloudContent","DisableSoftLanding",1)

    def _allowFilePathMoreThan260Chars(self):
        regedit._setHKLMdwordREG('VISUAL',r"SYSTEM\CurrentControlSet\Control\FileSystem","LongPathsEnabled",1)

    def _disableFileExplorerAds(self):
        regedit._setHKCUdwordREG('VISUAL',r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced","ShowSyncProviderNotifications",0)

    def _enableDarkTheme(self):
        regedit._setHKLMdwordREG('VISUAL',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize","AppsUseLightTheme",0)
        regedit._setHKCUdwordREG('VISUAL',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize","AppsUseLightTheme",0)
        regedit._setHKCUdwordREG('VISUAL',r"SOFTWARE\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Storage\microsoft.microsoftedge_8wekyb3d8bbwe\MicrosoftEdge\Main","Theme",1)
    
    def _openWindowsVisualTweaks(self):
        windir = os.environ['windir']
        command = os.path.join(windir, 'system32', 'SystemPropertiesPerformance.exe')

        subprocess.run([command])
        print._printg('VISUAL','System Properties Opened!')

    def _doAll(self):
        self._disableTransparency()
        self._disableAnimationsInTaskbar()
        self._showTranslucentSelectionRectangle()
        self._disableBalloonTips()
        self._disableWindowsAeroShake()
        self._removePeopleButton()
        self._disableActivityFeed()
        self._disableTaskViewButton()
        self._restoreNetworkFolderConnection()
        self._disableMeetNow()
        self._disableNewsAndWeather()
        self._disableWindowsTips()
        self._allowFilePathMoreThan260Chars()
        self._disableFileExplorerAds()
        self._enableDarkTheme()