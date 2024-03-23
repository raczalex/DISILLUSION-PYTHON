import subprocess
from utilities import regedit
from utilities import print

class Debloat():
    def __init__(self) -> None:
        pass

    def _disableUnneccesaryBloatware(self):
        regedit._setHKCUdwordREG('DEBLOAT',r"Software\Microsoft\Windows\CurrentVersion\Privacy",'TailoredExperiencesWithDiagnosticDataEnabled',0)
        regedit._setHKCUdwordREG('DEBLOAT',r"Software\Microsoft\Windows\CurrentVersion\Diagnostics\DiagTrack",'ShowedToastAtLevel',1)
        regedit._setHKCUdwordREG('DEBLOAT',r"Software\Microsoft\Input\TIPC",'Enabled',0)
        regedit._setHKLMdwordREG('DEBLOAT',r"Software\Policies\Microsoft\Windows\System",'UploadUserActivities',0)
        regedit._setHKLMdwordREG('DEBLOAT',r"Software\Policies\Microsoft\Windows\System",'PublishUserActivities',0)
        regedit._setHKCUdwordREG('DEBLOAT',r"Control Panel\International\User Profile",'HttpAcceptLanguageOptOut',1)
        regedit._setHKLMdwordREG('DEBLOAT',r"Software\Policies\Microsoft\Windows\System",'SaveZoneInformation',1)
        regedit._setHKLMdwordREG('DEBLOAT',r"Software\Policies\Microsoft\Windows\System",'DisableDiagnosticTracing',1)
        regedit._setHKLMdwordREG('DEBLOAT',r"Software\Policies\Microsoft\Windows\WDI\{9c5a40da-b965-4fc3-8781-88dd50a6299d}",'ScenarioExecutionEnabled',0)

    def _debloatChrome(self):
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'TranslateEnabled',1)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'TaskManagerEndProcessEnabled',1)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'UserFeedbackAllowed',0)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'SpellCheckServiceEnabled',0)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'SpellcheckEnabled',0)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'MediaRouterCastAllowAllIPs',1)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'AllowDinosaurEasterEgg',1)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'DefaultGeolocationSetting',2)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'DefaultCookiesSetting',1)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'DefaultFileHandlingGuardSetting',3)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'DefaultFileSystemReadGuardSetting',3)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'DefaultFileSystemnv11GuardSetting',3)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'DefaultImagesSetting',1)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'DefaultPopupsSetting',2)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'DefaultSensorsSetting',2)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'DefaultSerialGuardSetting',2)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'DefaultWebBluetoothGuardSetting',2)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'DefaultWebUsbGuardSetting',2)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'EnableMediaRouter',1)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'ShowCastIconInToolbar',1)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'CloudPrintProxyEnabled',0)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'PrintRasterizationMode',0)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'PrintingEnabled',1)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'DefaultPluginsSetting',1)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'SafeBrowsingProtectionLevel',0)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'SafeBrowsingExtendedReportingEnabled',0)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'HomepageIsNewTabPage',0)
        regedit._setHKLMregszREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'HomepageLocation',"google.com")
        regedit._setHKLMregszREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'NewTabPageLocation',"google.com")
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome\Recommended",'MetricsReportingEnabled',0)
        regedit._setHKCUdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome\Recommended",'MetricsReportingEnabled',0)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome\Recommended",'DeviceMetricsReportingEnabled',0)
        regedit._setHKCUdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome\Recommended",'DeviceMetricsReportingEnabled',0)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'MetricsReportingEnabled',0)
        regedit._setHKCUdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'MetricsReportingEnabled',0)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'DeviceMetricsReportingEnabled',0)
        regedit._setHKCUdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'DeviceMetricsReportingEnabled',0)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'Install{8A69D345-D564-463C-AFF1-A69D9E530F96}',5)
        regedit._setHKLMregszREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'TargetChannel{8A69D345-D564-463C-AFF1-A69D9E530F96}',"stable")
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'Update{8A69D345-D564-463C-AFF1-A69D9E530F96}',3)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'Install{4CCED17F-7852-4AFC-9E9E-C89D8795BDD2}',0)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'AutoUpdateCheckPeriodMinutes',43200)
        regedit._setHKLMregszREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'DownloadPreference',"cacheable")
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'UpdatesSuppressedStartHour',23)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'UpdatesSuppressedStartMin',48)
        regedit._setHKLMdwordREG('DEBLOAT',r"SOFTWARE\Policies\Google\Chrome",'UpdatesSuppressedDurationMin',55)

    def _disableUselessServicesFromTaskScheduler(self):

        commands = [r'schtasks /Change /TN "Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Application Experience\PcaPatchDbTask" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Application Experience\ProgramDataUpdater" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Application Experience\StartupAppTask" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Autochk\Proxy" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Customer Experience Improvement Program\Consolidator" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Customer Experience Improvement Program\UsbCeip" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Defrag\ScheduledDefrag" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Device Information\Device" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Device Information\Device User" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\DiskCleanup\SilentCleanup" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\DiskFootprint\Diagnostics" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\DiskFootprint\StorageSense" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\DUSM\dusmtask" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\EnterpriseMgmt\MDMMaintenenceTask" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Feedback\Siuf\DmClient" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Feedback\Siuf\DmClientOnScenarioDownload" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Flighting\FeatureConfig\ReconcileFeatures" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Flighting\FeatureConfig\UsageDataFlushing" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Flighting\FeatureConfig\UsageDataReporting" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Flighting\OneSettings\RefreshCache" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Input\LocalUserSyncDataAvailable" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Input\MouseSyncDataAvailable" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Input\PenSyncDataAvailable" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Input\TouchpadSyncDataAvailable" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\International\Synchronize Language Settings" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\LanguageComponentsInstaller\Installation" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\LanguageComponentsInstaller\ReconcileLanguageResources" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\LanguageComponentsInstaller\Uninstallation" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\License Manager\TempSignedLicenseExchange" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Management\Provisioning\Cellular" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Management\Provisioning\Logon" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Maintenance\WinSAT" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Maps\MapsToastTask" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Maps\MapsUpdateTask" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Mobile Broadband Accounts\MNO Metadata Parser" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\MUI\LPRemove" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\NetTrace\GatherNetworkInfo" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\PI\Sqm-Tasks" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\PushToInstall\Registration" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Ras\MobilityManager" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\RecoveryEnvironment\VerifyWinRE" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\RemoteAssistance\RemoteAssistanceTask" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\RetailDemo\CleanupOfflineContent" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Servicing\StartComponentCleanup" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\SettingSync\NetworkStateChangeTask" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Setup\SetupCleanupTask" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Setup\SnapshotCleanupTask" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\SpacePort\SpaceAgentTask" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\SpacePort\SpaceManagerTask" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Speech\SpeechModelDownloadTask" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Storage Tiers Management\Storage Tiers Management Initialization" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Sysmain\ResPriStaticDbSync" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Sysmain\WsSwapAssessmentTask" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Task Manager\Interactive" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\TPM\Tpm-HASCertRetr" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\TPM\Tpm-Maintenance" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\UPnP\UPnPHostConfig" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\User Profile Service\HiveUploadTask" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\WDI\ResolutionHost" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Windows Filtering Platform\BfeOnServiceStartTypeChange" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\WOF\WIM-Hash-Management" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\WOF\WIM-Hash-Validation" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Work Folders\Work Folders Logon Synchronization" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Work Folders\Work Folders Maintenance Work" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\Workplace Join\Automatic-Device-Join" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\WwanSvc\NotificationTask" /Disable',
                    r'schtasks /Change /TN "Microsoft\Windows\WwanSvc\OobeDiscovery" /Disable']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('DEBLOAT',cmd)

    def _doAll(self):
        self._disableUnneccesaryBloatware()
        self._debloatChrome()
        self._disableUselessServicesFromTaskScheduler()