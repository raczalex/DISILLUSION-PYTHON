import subprocess
from utilities import regedit
from shutil import rmtree
from os import path
from utilities.print import _printg,_printr

class Tweaks():
    def __init__(self) -> None:
        pass

    def _monitorLatencyTolerance(self):
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Services\DXGKrnl","MonitorLatencyTolerance",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Services\DXGKrnl","MonitorRefreshLatencyTolerance",0)

    def _forceMonitorHz(self,hz):
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\DirectDraw","ForceRefreshRate",hz)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\WOW6432Node\Microsoft\DirectDraw","ForceRefreshRate",hz)

    def _force60hz(self):
        self._forceMonitorHz(60)
    
    def _force75hz(self):
        self._forceMonitorHz(75)

    def _force120hz(self):
        self._forceMonitorHz(120)

    def _force144hz(self):
        self._forceMonitorHz(144)

    def _force160hz(self):
        self._forceMonitorHz(160)

    def _force165hz(self):
        self._forceMonitorHz(165)

    def _force240hz(self):
        self._forceMonitorHz(240)

    def _force280hz(self):
        self._forceMonitorHz(280)

    def _force360hz(self):
        self._forceMonitorHz(360)

    def _force540hz(self):
        self._forceMonitorHz(540)

    def _speedUpStartupTime(self):
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System","DelayedDesktopSwitchTimeout",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Serialize","StartupDelayInMSec",0)

    def _disableDMARemapping(self):
        regedit._setHKLMdwordREG('TWEAKS',r'SOFTWARE\Microsoft\PolicyManager\default\DmaGuard\DeviceEnumerationPolicy','value',2)

        services = subprocess.check_output(['reg', 'query', 'HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services', '/s', '/f', 'DmaRemappingCompatible'], text=True)
        for service in services.splitlines():
            if "Services\\" in service:
                subprocess.run(['reg', 'add', service, '/v', 'DmaRemappingCompatible', '/t', 'REG_DWORD', '/d', '0', '/f'],stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
                _printg('TWEAKS','DmaRemappingCompatible 0')

    def _microsoftMultimediaTweaks(self):
        regedit._setHKCUdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Games","FpsAll",1)
        regedit._setHKCUdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Games","FpsStatusGames",10)
        regedit._setHKCUdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Games","FpsStatusGamesAll",4)
        regedit._setHKCUdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Games","GameFluidity",1)

    def _hardenSMB(self):
        commands = [r'POWERSHELL "Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol"',
                    r'POWERSHELL "Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol-Client"',
                    r'POWERSHELL "Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol-Server"',
                    r'POWERSHELL "Set-SmbClientConfiguration -RequireSecuritySignature $True -Force"',
                    r'POWERSHELL "Set-SmbClientConfiguration -EnableSecuritySignature $True -Force"',
                    r'POWERSHELL "Set-SmbServerConfiguration -EncryptData $True -Force"',
                    r'POWERSHELL "Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force"']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            _printg('TWEAKS',cmd)

    def _enableMemoryMappingForPcieDevices(self):
        commands = [r'bcdedit /set configaccesspolicy Default',
                    r'bcdedit /set MSI Default',
                    r'bcdedit /set usephysicaldestination No',
                    r'bcdedit /set usefirmwarepcisettings No'
                ]
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            _printg('TWEAKS',cmd)

    def _hardenSecurity(self):
        regedit._setHKLMdwordREG('TWEAKS',r"System\CurrentControlSet\Control\Lsa","RestrictAnonymous",1)
        regedit._setHKLMdwordREG('TWEAKS',r"System\CurrentControlSet\Control\Lsa","RestrictAnonymousSAM",1)
        commands = [r'sc config lmhosts start=disabled',
                    r'sc stop lmhosts']
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            _printg('TWEAKS',cmd)
        regedit._setHKLMdwordREG('TWEAKS',r"System\CurrentControlSet\Services\NetBT\Parameters","NodeType",2)
        commands.clear()
        commands = [r'sc stop LanmanWorkstation',
                    r'sc config LanmanWorkstation start=disabled']
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            _printg('TWEAKS',cmd)
        regedit._setHKLMdwordREG('TWEAKS',r"System\CurrentControlSet\Services\LanManServer\Parameters","RestrictNullSessAccess",1)
        regedit._setHKLMdwordREG('TWEAKS',r"System\CurrentControlSet\Services\LanManServer\Parameters","DisableCompression",1)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\lsass.exe","AuditLevel",8)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\CredentialsDelegation","AllowProtectedCreds",1)
        regedit._setHKLMdwordREG('TWEAKS',r"System\CurrentControlSet\Control\Lsa","DisableRestrictedAdminOutboundCreds",1)
        regedit._setHKLMdwordREG('TWEAKS',r"System\CurrentControlSet\Control\Lsa","DisableRestrictedAdmin",0)
        regedit._setHKLMdwordREG('TWEAKS',r"System\CurrentControlSet\Control\Lsa","RunAsPPL",1)
        regedit._setHKLMdwordREG('TWEAKS',r"System\CurrentControlSet\Control\SecurityProviders\WDigest","Negotiate",0)
        regedit._setHKLMdwordREG('TWEAKS',r"System\CurrentControlSet\Control\SecurityProviders\WDigest","UseLogonCredential",0)

    def _healthMonitor(self):
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\PCHealth\ErrorReporting\DW","DWNoSecondLevelCollection",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\PCHealth\ErrorReporting\DW","DWNoFileCollection",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\PCHealth\ErrorReporting\DW","DWNoExternalURL",1)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\DeviceHealthAttestationService","EnableDeviceHealthAttestationService",00000000)

    def _gameDVRXboxDisable(self):
        commands = [r'sc config xbgm start= disabled',
                    r'sc config XblAuthManager start= disabled',
                    r'sc config XblGameSave start= disabled',
                    r'sc config XboxGipSvc start= disabled',
                    r'sc config XboxNetApiSvc start= disabled']
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            _printg('TWEAKS',cmd)

        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\GameBar","AllowAutoGameMode",0)
        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\GameBar","ShowStartupPanel",0)
        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\GameBar","UseNexusForGameBarEnabled",0)
        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\GameBar","GameDVR_Enabled",0)
        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\Windows\CurrentVersion\GameDVR","AppCaptureEnabled",0)
        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\Windows\CurrentVersion\GameDVR","AudioCaptureEnabled",0)
        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\Windows\CurrentVersion\GameDVR","CursorCaptureEnabled",0)
        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\Windows\CurrentVersion\GameDVR","HistoricalCaptureEnabled",0)
        regedit._setHKCUdwordREG('TWEAKS',r"System\GameConfigStore","GameDVR_Enabled",0)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\GameDVR","AllowgameDVR",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Services\xbgm","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Services\XboxGipSvc","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Services\XblAuthManager","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Services\XblGameSave","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Services\XboxNetApiSvc","Start",0)

    def _latencyTolerance(self):
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","D3PCLatency",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","F1TransitionLatency",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","LOWLATENCY",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","Node3DLowLatency",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PciLatencyTimerControl",20)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RMDeepL1EntryLatencyUsec",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RmGspcMaxFtuS",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RmGspcMinFtuS",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RmGspcPerioduS",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RMLpwrEiIdleThresholdUs",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RMLpwrGrIdleThresholdUs",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RMLpwrGrRgIdleThresholdUs",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RMLpwrMsIdleThresholdUs",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","VRDirectFlipDPCDelayUs",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","VRDirectFlipTimingMarginUs",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","VRDirectJITFlipMsHybridFlipDelayUs",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","vrrCursorMarginUs",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","vrrDeflickerMarginUs",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","vrrDeflickerMaxUs",1)

    def _optimizeSearch(self):
        regedit._setHKCUdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Search","BingSearchEnabled",0)
        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\InputPersonalization","RestrictImplicitInkCollection",1)
        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\InputPersonalization","RestrictImplicitTextCollection",1)
        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\Personalization\Settings","AcceptedPrivacyPolicy",0)
        regedit._setHKCUregszREG('TWEAKS',r"Software\Microsoft\Windows\CurrentVersion\Search","CortanaCapabilities","")
        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\Windows\CurrentVersion\Search","IsAssignedAccess",0)
        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\Windows\CurrentVersion\Search","IsWindowsHelloActive",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\Windows\Windows Search","AllowSearchToUseLocation",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\Windows\Windows Search","ConnectedSearchPrivacy",3)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\Windows\Windows Search","ConnectedSearchSafeSearch",3)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\Windows\Windows Search","ConnectedSearchUseWeb",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\Windows\Windows Search","ConnectedSearchUseWebOverMeteredConnections",0)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Microsoft\PolicyManager\default\Experience\AllowCortana","value",0)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\SearchCompanion","DisableContentFileUpdates",1)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\Windows Search","AllowCloudSearch",0)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\Windows Search","AllowCortanaAboveLock",0)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\Windows Search","AllowSearchToUseLocation",0)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\Windows Search","ConnectedSearchPrivacy",3)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\Windows Search","ConnectedSearchUseWeb",0)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\Windows Search","ConnectedSearchUseWebOverMeteredConnections",0)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\Windows Search","DisableWebSearch",1)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\Windows Search","DoNotUseWebResults",1)

    def _ntfsTweaks(self):
        commands = [r'fsutil behavior set memoryusage 2',
                    r'fsutil behavior set mftzone 4',
                    r'fsutil behavior set disablelastaccess 1',
                    r'fsutil behavior set disabledeletenotify 0',
                    r'fsutil behavior set encryptpagingfile 0']
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            _printg('TWEAKS',cmd)

    def _disableBing(self):
        regedit._setHKCUdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Search","BingSearchEnabled",0)
        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\InputPersonalization","RestrictImplicitInkCollection",1)
        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\InputPersonalization","RestrictImplicitTextCollection",1)
        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\Personalization\Settings","AcceptedPrivacyPolicy",0)
        regedit._setHKCUregszREG('TWEAKS',r"Software\Microsoft\Windows\CurrentVersion\Search","CortanaCapabilities","")
        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\Windows\CurrentVersion\Search","IsAssignedAccess",0)
        regedit._setHKCUdwordREG('TWEAKS',r"Software\Microsoft\Windows\CurrentVersion\Search","IsWindowsHelloActive",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\Windows\Windows Search","AllowIndexingEncryptedStoresOrItems",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\Windows\Windows Search","AllowSearchToUseLocation",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\Windows\Windows Search","ConnectedSearchPrivacy",3)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\Windows\Windows Search","ConnectedSearchSafeSearch",3)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\Windows\Windows Search","ConnectedSearchUseWeb",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\Windows\Windows Search","ConnectedSearchUseWebOverMeteredConnections",0)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Microsoft\PolicyManager\default\Experience\AllowCortana","value",0)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\SearchCompanion","DisableContentFileUpdates",1)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\Windows Search","AllowCloudSearch",0)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\Windows Search","AllowCortanaAboveLock",0)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\Windows Search","AllowSearchToUseLocation",0)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\Windows Search","ConnectedSearchPrivacy",3)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\Windows Search","ConnectedSearchUseWeb",0)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\Windows Search","ConnectedSearchUseWebOverMeteredConnections",0)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\Windows Search","DisableWebSearch",1)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\Windows Search","DoNotUseWebResults",1)

    def _disableHyperV(self):
        command = r'dism.exe /Online /Disable-Feature:Microsoft-Hyper-V'
        subprocess.Popen(command,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
        _printg('TWEAKS',command)

    def _disableLazyMode(self):
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile","NoLazyMode",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile","AlwaysOn",1)

    def _disableMaintenance(self):
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\Maintenance","MaintenanceDisabled",1)

    def _disableAutoLoggers(self):
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\AppModel","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\Cellcore","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\Circular Kernel Context Logger","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\CloudExperienceHostOobe","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\DataMarket","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\DefenderApiLogger","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\DefenderAuditLogger","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\DiagLog","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\HolographicDevice","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\iclsClient","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\iclsProxy","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\LwtNetLog","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\Mellanox-Kernel","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\Microsoft-Windows-AssignedAccess-Trace","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\Microsoft-Windows-Setup","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\NBSMBLOGGER","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\PEAuthLog","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\RdrLog","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\ReadyBoot","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\SetupPlatform","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\SetupPlatformTel","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\SocketHeciServer","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\SpoolerLogger","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\SQMLogger","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\TCPIPLOGGER","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\TileStore","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\Tpm","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\TPMProvisioningService","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\UBPM","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\WdiContextLog","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\WFP-IPsec Trace","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\WiFiDriverIHVSession","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\WiFiDriverIHVSessionRepro","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\WiFiSession","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\WMI\Autologger\WinPhoneCritical","Start",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\WUDF","LogEnable",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\WUDF","LogLevel",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\Windows\CloudContent","DisableThirdPartySuggestions",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\Windows\CloudContent","DisableWindowsConsumerFeatures",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Lsa\Credssp","DebugLogLevel",0)

    def _disableWindowsInsider(self):
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\PolicyManager\current\device\System","AllowExperimentation",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\PolicyManager\default\System\AllowExperimentation","value",0)

    def _disableRemoveOneDrive(self):
        subprocess.run(['taskkill', '/f', '/im', 'OneDrive.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        onedrive_setup_path = r'C:\Windows\SYSWOW64\ONEDRIVESETUP.EXE'

        try:
            if path.exists(onedrive_setup_path):
                subprocess.run([onedrive_setup_path, '/UNINSTALL'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                _printg('TWEAKS',f'{onedrive_setup_path} /UNINSTALL')
            else:
                raise FileNotFoundError

        except FileNotFoundError:
            _printr('TWEAKS',f'{onedrive_setup_path} NOT FOUND!')
        finally:
            rmtree('C:\\OneDriveTemp', ignore_errors=True)
            rmtree(path.expanduser('~/OneDrive'), ignore_errors=True)
            rmtree(path.expandvars('%LOCALAPPDATA%\\Microsoft\\OneDrive'), ignore_errors=True)
            rmtree(path.expandvars('%PROGRAMDATA%\\Microsoft OneDrive'), ignore_errors=True)
            _printg('TWEAKS','Removed OneDrive Files!')

            regedit._setHKCRdwordREG('TWEAKS',r"CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}\ShellFolder","Attributes",0)
            regedit._setHKCRdwordREG('TWEAKS',r"Wow6432Node\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}\ShellFolder","Attributes",0)
            regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\Windows\OneDrive","DisableFileSync",1)
            regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\Windows\OneDrive","DisableFileSyncNGSC",1)
            regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\Windows\OneDrive","DisableMeteredNetworkFileSync",0)
            regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Policies\Microsoft\Windows\OneDrive","DisableLibrariesDefaultSaveToOneDrive",0)


    def _optimizeResourcePolicy(self):
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\CPU\HardCap0","CapPercentage",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\CPU\HardCap0","SchedulingType",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\CPU\Paused","CapPercentage",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\CPU\Paused","SchedulingType",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\CPU\SoftCapFull","CapPercentage",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\CPU\SoftCapFull","SchedulingType",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\CPU\SoftCapLow","CapPercentage",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\CPU\SoftCapLow","SchedulingType",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Flags\BackgroundDefault","IsLowPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Flags\Frozen","IsLowPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Flags\FrozenDNCS","IsLowPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Flags\FrozenDNK","IsLowPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Flags\FrozenPPLE","IsLowPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Flags\Paused","IsLowPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Flags\PausedDNK","IsLowPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Flags\Pausing","IsLowPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Flags\PrelaunchForeground","IsLowPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Flags\ThrottleGPUInterference","IsLowPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\Critical","BasePriority",82)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\Critical","OverTargetPriority",50)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\CriticalNoUi","BasePriority",82)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\CriticalNoUi","OverTargetPriority",50)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\EmptyHostPPLE","BasePriority",82)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\EmptyHostPPLE","OverTargetPriority",50)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\High","BasePriority",82)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\High","OverTargetPriority",50)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\Low","BasePriority",82)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\Low","OverTargetPriority",50)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\Lowest","BasePriority",82)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\Lowest","OverTargetPriority",50)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\Medium","BasePriority",82)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\Medium","OverTargetPriority",50)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\MediumHigh","BasePriority",82)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\MediumHigh","OverTargetPriority",50)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\StartHost","BasePriority",82)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\StartHost","OverTargetPriority",50)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\VeryHigh","BasePriority",82)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\VeryHigh","OverTargetPriority",50)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\VeryLow","BasePriority",82)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Importance\VeryLow","OverTargetPriority",50)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\IO\NoCap","IOBandwidth",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Memory\NoCap","CommitLimit",4294967295)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ResourcePolicyStore\ResourceSets\Policies\Memory\NoCap","CommitTarget",4294967295)
    
    def _disableMitigations(self):
        command = r'powershell set-ProcessMitigation -System -Disable DEP, EmulateAtlThunks, SEHOP, ForceRelocateImages, RequireInfo, BottomUp, HighEntropy, StrictHandle, DisableWin32kSystemCalls, AuditSystemCall, DisableExtensionPoints, BlockDynamicCode, AllowThreadsToOptOut, AuditDynamicCode, CFG, SuppressExports, StrictCFG, MicrosoftSignedOnly, AllowStoreSignedBinaries, AuditMicrosoftSigned, AuditStoreSigned, EnforceModuleDependencySigning, DisableNonSystemFonts, AuditFont, BlockRemoteImageLoads, BlockLowLabelImageLoads, PreferSystem32, AuditRemoteImageLoads, AuditLowLabelImageLoads, AuditPreferSystem32, EnableExportAddressFilter, AuditEnableExportAddressFilter, EnableExportAddressFilterPlus, AuditEnableExportAddressFilterPlus, EnableImportAddressFilter, AuditEnableImportAddressFilter, EnableRopStackPivot, AuditEnableRopStackPivot, EnableRopCallerCheck, AuditEnableRopCallerCheck, EnableRopSimExec, AuditEnableRopSimExec, SEHOP, AuditSEHOP, SEHOPTelemetry, TerminateOnError, DisallowChildProcessCreation, AuditChildProcess'
        subprocess.Popen(command,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
        _printg('TWEAKS',command)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\HypervisorEnforcedCodeIntegrity","Enabled",0)

        regedit._setHKLMbinaryREG('TWEAKS',r"Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\csrss.exe","MitigationAuditOptions",b'222222222222222222222222222222222222222222222222')
        regedit._setHKLMbinaryREG('TWEAKS',r"Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\csrss.exe","MitigationOptions",b'222222222222222222222222222222222222222222222222')

        regedit._setHKLMdwordREG('TWEAKS',r"System\CurrentControlSet\Control\Session Manager\kernel","DisableTsx",1)

        regedit._setHKLMdwordREG('TWEAKS',r"Software\Microsoft\PolicyManager\default\DmaGuard\DeviceEnumerationPolicy","value",2)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\DeviceGuard","HVCIMATRequired",0)
        regedit._setHKLMdwordREG('TWEAKS',r"Software\Policies\Microsoft\Windows\DeviceGuard","EnableVirtualizationBasedSecurity",0)

        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel","DisableExceptionChainValidation",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel","KernelSEHOPEnabled",0)

        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","MoveImages",0)

        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","FeatureSettings",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","FeatureSettingsOverride",3)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","FeatureSettingsOverrideMask",3)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","MoveImages",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ControlSet001\Control\Session Manager\Memory Management","FeatureSettings",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ControlSet001\Control\Session Manager\Memory Management","FeatureSettingsOverride",3)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ControlSet001\Control\Session Manager\Memory Management","FeatureSettingsOverrideMask",3)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ControlSet001\Control\Session Manager\Memory Management","EnableCfg",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ControlSet001\Control\Session Manager\Memory Management","MoveImages",0)

        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","EnableCfg",0)

        regedit._setHKLMdwordREG('TWEAKS',r"System\CurrentControlSet\Control\Session Manager","ProtectionMode",0)

        commands = [r'sc config SysMain start= auto',
                    r'sc start SysMain',
                    r'powershell "ForEach($v in (Get-Command -Name \"Set-ProcessMitigation\").Parameters[\"Disable\"].Attributes.ValidValues){Set-ProcessMitigation -System -Disable $v.ToString() -ErrorAction SilentlyContinue}"',
                    r'powershell "Remove-Item -Path \"HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\*\" -Recurse -ErrorAction SilentlyContinue"',
                    r'sc stop SysMain',
                    r'sc config SysMain start= disabled']
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            _printg('TWEAKS',cmd)

        regedit._setHKLMdwordREG('TWEAKS',r"System\CurrentControlSet\Control\Session Manager","ProtectionMode",0)

    def _disableSubMitigations(self):
        regedit._setHKLMbinaryREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel","MitigationOptions",b'222222222222222222222222222222222222222222222222')

    def _disableSehop(self):
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel","DisableExceptionChainValidation",1)

    def _ioTweaksBoost(self):
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\I/O System","PassiveIntRealTimeWorkerPriority",18)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\KernelVelocity","DisableFGBoostDecay",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\dwm.exe\PerfOptions","CpuPriorityClass",4)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\dwm.exe\PerfOptions","IoPriority",3)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\lsass.exe\PerfOptions","CpuPriorityClass",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\lsass.exe\PerfOptions","IoPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\lsass.exe\PerfOptions","PagePriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\ntoskrnl.exe\PerfOptions","CpuPriorityClass",4)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\ntoskrnl.exe\PerfOptions","IoPriority",3)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\SearchIndexer.exe\PerfOptions","CpuPriorityClass",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\SearchIndexer.exe\PerfOptions","IoPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\svchost.exe\PerfOptions","CpuPriorityClass",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\TrustedInstaller.exe\PerfOptions","CpuPriorityClass",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\TrustedInstaller.exe\PerfOptions","IoPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\wuauclt.exe\PerfOptions","CpuPriorityClass",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\wuauclt.exe\PerfOptions","IoPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\audiodg.exe\PerfOptions","CpuPriorityClass",2)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\audiodg.exe\PerfOptions","CpuPriorityClass",2)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\dwm.exe\PerfOptions","CpuPriorityClass",4)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\dwm.exe\PerfOptions","IoPriority",3)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\lsass.exe\PerfOptions","CpuPriorityClass",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\lsass.exe\PerfOptions","IoPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\lsass.exe\PerfOptions","PagePriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\ntoskrnl.exe\PerfOptions","CpuPriorityClass",4)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\ntoskrnl.exe\PerfOptions","IoPriority",3)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\SearchIndexer.exe\PerfOptions","CpuPriorityClass",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\SearchIndexer.exe\PerfOptions","IoPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\svchost.exe\PerfOptions","CpuPriorityClass",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\TrustedInstaller.exe\PerfOptions","CpuPriorityClass",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\TrustedInstaller.exe\PerfOptions","IoPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\wuauclt.exe\PerfOptions","CpuPriorityClass",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\wuauclt.exe\PerfOptions","IoPriority",0)

    def _kernel(self):
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Services\DXGKrnl","MonitorLatencyTolerance",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Services\DXGKrnl","MonitorRefreshLatencyTolerance",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Services\DXGKrnl","MonitorLatencyTolerance",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Services\DXGKrnl","MonitorRefreshLatencyTolerance",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel","DpcWatchdogProfileOffset",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel","DisableExceptionChainValidation",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel","KernelSEHOPEnabled",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel","DisableAutoBoost",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel","DpcTimeout",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel","ThreadDpcEnable",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel","DpcWatchdogPeriod",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel","InterruptSteeringDisabled",1)

    def _latencyCapTweaks(self):
        result = subprocess.run(['REG', 'QUERY', 'HKLM\\System\\CurrentControlSet\\Services', '/S', '/F', 'IoLatencyCap'], stdout=subprocess.PIPE, text=True)

        for line in result.stdout.split('\n'):
            stripped_line = line.strip()
            if stripped_line.startswith('HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\') and stripped_line.endswith('\\Parameters'):
                key = stripped_line
                subprocess.run(['Reg.exe', 'add', key, '/v', 'IoLatencyCap', '/t', 'REG_DWORD', '/d', '0', '/f'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
                str_value = key.replace('HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\', '').replace('\\Parameters', '')
                _printg('TWEAKS',str_value)

    def _additionalTweaks(self):
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel","DistributeTimers",1)

        commands = [r'powercfg -setacvalueindex scheme_current SUB_DISK dbc9e238-6de9-49e3-92cd-8c2b4946b472 1',
                    r'powercfg -setacvalueindex scheme_current SUB_DISK fc95af4d-40e7-4b6d-835a-56d131dbc80e 1']

        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            _printg('TWEAKS',cmd)

        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\Power","LowLatencyScalingPercentage",100)

        command = r'lodctr /r'
        subprocess.Popen(command,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
        _printg('TWEAKS',command)

        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FlyoutMenuSettings","ShowSleepOption",0)

        command = r'FSUTIL behavior set disablelastaccess 1'
        subprocess.Popen(command,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
        _printg('TWEAKS',command)

    def _optimizeMMCSS(self):
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Low Latency","Affinity",0)
        regedit._setHKLMregszREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Low Latency","Background Only","False")
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Low Latency","BackgroundPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Low Latency","Clock Rate",10000)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Low Latency","GPU Priority",8)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Low Latency","Priority",2)
        regedit._setHKLMregszREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Low Latency","Scheduling Category","Medium")
        regedit._setHKLMregszREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Low Latency","SFIO Priority","High")
        regedit._setHKLMregszREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Low Latency","Latency Sensitive","True")

        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games","Affinity",0)
        regedit._setHKLMregszREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games","Background Only","False")
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games","BackgroundPriority",0)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games","Clock Rate",10000)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games","GPU Priority",18)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games","Priority",2)
        regedit._setHKLMregszREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games","Scheduling Category","High")
        regedit._setHKLMregszREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games","SFIO Priority","High")
        regedit._setHKLMregszREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games","Latency Sensitive","True")

        regedit._setHKLMregszREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Window Manager","Background Only","True")
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Window Manager","Clock Rate",10000)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Window Manager","GPU Priority",8)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Window Manager","Priority",5)
        regedit._setHKLMregszREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Window Manager","Scheduling Category","Medium")
        regedit._setHKLMregszREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Window Manager","SFIO Priority","Normal")

        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\csrss.exe\PerfOptions","CpuPriorityClass",4)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\csrss.exe\PerfOptions","IoPriority",4)

        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\PriorityControl","IRQ8Priority",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ControlSet001\Control\PriorityControl","IRQ8Priority",1)

        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Control\PriorityControl","IRQ16Priority",2)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\ControlSet001\Control\PriorityControl","IRQ16Priority",2)

        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\svchost.exe\PerfOptions","CpuPriorityClass",1)
        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\svchost.exe\PerfOptions","IoPriority",0)

        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Services\DXGKrnl\Parameters","ThreadPriority",15)
        regedit._setHKLMdwordREG('TWEAKS',r"SYSTEM\CurrentControlSet\Services\nvlddmkm\Parameters","ThreadPriority",15)

        regedit._setHKLMdwordREG('TWEAKS',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile","SystemResponsiveness",0)


    def _doAll(self):
        self._monitorLatencyTolerance()
        self._speedUpStartupTime()
        self._disableDMARemapping()
        self._microsoftMultimediaTweaks()
        self._hardenSMB()
        self._enableMemoryMappingForPcieDevices()
        self._hardenSecurity()
        self._healthMonitor()
        self._gameDVRXboxDisable()
        self._latencyTolerance()
        self._optimizeSearch()
        self._ntfsTweaks()
        self._disableBing()
        self._disableHyperV()
        self._disableLazyMode()
        self._disableMaintenance()
        self._disableAutoLoggers()
        self._disableWindowsInsider()
        self._disableRemoveOneDrive()
        self._optimizeResourcePolicy()
        self._disableMitigations()
        self._disableSubMitigations()
        self._disableSehop()
        self._ioTweaksBoost()
        self._kernel()
        self._latencyCapTweaks()
        self._additionalTweaks()
        self._optimizeMMCSS()

