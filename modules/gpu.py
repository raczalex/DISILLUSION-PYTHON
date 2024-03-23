import subprocess
import shutil
from utilities import regedit
from utilities import print

class GPU():
    def __init__(self) -> None:
        pass

    def _mmcssGpuTweaks(self):
        regedit._setHKLMdwordREG('GPU',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\DisplayPostProcessing","Affinity",0)
        regedit._setHKLMregszREG('GPU',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\DisplayPostProcessing","Background Only","True")
        regedit._setHKLMdwordREG('GPU',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\DisplayPostProcessing","BackgroundPriority",24)
        regedit._setHKLMdwordREG('GPU',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\DisplayPostProcessing","Clock Rate",10000)
        regedit._setHKLMdwordREG('GPU',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\DisplayPostProcessing","GPU Priority",18)
        regedit._setHKLMdwordREG('GPU',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\DisplayPostProcessing","Priority",8)
        regedit._setHKLMregszREG('GPU',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\DisplayPostProcessing","Scheduling Category","High")
        regedit._setHKLMregszREG('GPU',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\DisplayPostProcessing","SFIO Priority","High")
        regedit._setHKLMregszREG('GPU',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\DisplayPostProcessing","Latency Sensitive","True")
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","TdrLevel",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","TdrDebugMode",0)

    def _graphicsCardSchedulerTweaks(self):
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","VsyncIdleTimeout",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","TdrDebugMode",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","TdrLevel",0)
        regedit._setHKLMdwordREG('GPU',r"System\CurrentControlSet\Services\VxD\BIOS","AGPConcur",1)
        regedit._setHKLMdwordREG('GPU',r"System\CurrentControlSet\Services\VxD\BIOS","CPUPriority",1)
        regedit._setHKLMdwordREG('GPU',r"System\CurrentControlSet\Services\VxD\BIOS","FastDRAM",1)
        regedit._setHKLMdwordREG('GPU',r"System\CurrentControlSet\Services\VxD\BIOS","PCIConcur",1)
        regedit._setHKLMdwordREG('GPU',r"System\CurrentControlSet\Control\GraphicsDrivers","TdrLevel",0)
        regedit._setHKLMdwordREG('GPU',r"System\CurrentControlSet\Control\GraphicsDrivers","TdrDelay",60)
    
    def _disablePreemptionGeneral(self):
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","EnablePreemption",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","GPUPreemptionLevel",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","EnableAsyncMidBufferPreemption",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","EnableMidGfxPreemptionVGPU",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","EnableMidBufferPreemptionForHighTdrTimeout",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","EnableSCGMidBufferPreemption",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","PerfAnalyzeMidBufferPreemption",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","EnableMidGfxPreemption",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","EnableMidBufferPreemption",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","EnableCEPreemption",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","DisableCudaContextPreemption",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","DisablePreemptionOnS3S4",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","ComputePreemptionLevel",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","DisablePreemption",1)

    def _disableGpuEnergyDrv(self):
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Services\GpuEnergyDrv","Start",4)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Services\GpuEnergyDr","Start",4)

    def _latencyTolerance(self):
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","ExitLatency",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","ExitLatencyCheckEnabled",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","Latency",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","LatencyToleranceDefault",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","LatencyToleranceFSVP",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","LatencyTolerancePerfOverride",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","LatencyToleranceScreenOffIR",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","LatencyToleranceVSyncEnabled",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","RtlCapabilityCheckLatency",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","QosManagesIdleProcessors",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DisableVsyncLatencyUpdate",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DisableSensorWatchdog",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","CoalescingTimerInterval",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","InterruptSteeringDisabled",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","LowLatencyScalingPercentage",100)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","HighPerformance",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","HighestPerformance",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","MinimumThrottlePercent",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","MaximumThrottlePercent",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","MaximumPerformancePercent",100)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","InitialUnparkCount",100)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultD3TransitionLatencyActivelyUsed",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultD3TransitionLatencyIdleLongTime",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultD3TransitionLatencyIdleMonitorOff",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultD3TransitionLatencyIdleNoContext",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultD3TransitionLatencyIdleShortTime",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultD3TransitionLatencyIdleVeryLongTime",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceIdle0",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceIdle0MonitorOff",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceIdle1",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceIdle1MonitorOff",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceMemory",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceNoContext",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceNoContextMonitorOff",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceOther",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceTimerPeriod",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultMemoryRefreshLatencyToleranceActivelyUsed",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultMemoryRefreshLatencyToleranceMonitorOff",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultMemoryRefreshLatencyToleranceNoContext",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","Latency",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","MiracastPerfTrackGraphicsLatency",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","MonitorLatencyTolerance",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","MonitorRefreshLatencyTolerance",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","TransitionLatency",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DisableVsyncLatencyUpdate",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DisableSensorWatchdog",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","InterruptSteeringDisabled",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","ExitLatency",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","ExitLatencyCheckEnabled",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","Latency",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","LatencyToleranceDefault",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","LatencyToleranceFSVP",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","LatencyTolerancePerfOverride",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","LatencyToleranceScreenOffIR",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","LatencyToleranceVSyncEnabled",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","RtlCapabilityCheckLatency",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","LowLatencyScalingPercentage",100)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","MaxIAverageGraphicsLatencyInOneBucket",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultD3TransitionLatencyActivelyUsed",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultD3TransitionLatencyIdleLongTime",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultD3TransitionLatencyIdleMonitorOff",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultD3TransitionLatencyIdleNoContext",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultD3TransitionLatencyIdleShortTime",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultD3TransitionLatencyIdleVeryLongTime",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceIdle0",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceIdle0MonitorOff",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceIdle1",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceIdle1MonitorOff",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceMemory",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceNoContext",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceNoContextMonitorOff",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceOther",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultLatencyToleranceTimerPeriod",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultMemoryRefreshLatencyToleranceActivelyUsed",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultMemoryRefreshLatencyToleranceMonitorOff",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","DefaultMemoryRefreshLatencyToleranceNoContext",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","MaxIAverageGraphicsLatencyInOneBucket",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","Latency",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","MiracastPerfTrackGraphicsLatency",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","MonitorLatencyTolerance",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","MonitorRefreshLatencyTolerance",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\Power","TransitionLatency",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","MonitorLatencyTolerance",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","MonitorRefreshLatencyTolerance",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power","MonitorLatencyTolerance",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power","MonitorRefreshLatencyTolerance",0)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","RMDisablePostL2Compression",1)
        regedit._setHKLMdwordREG('GPU',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","RmDisableRegistryCaching",1)

    def _vram(self):
        commands = [r'fsutil behavior query memoryusage',
                    r'fsutil behavior set memoryusage 2']
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('GPU',cmd)

    def _setDriverAcceleration(self):
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","Acceleration.Level",0)

    def _forceContigousMemoryAllocation(self):
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PreferSystemMemoryContiguous",1)

    def _dpcsForEachCore(self):
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Services\nvlddmkm","RmGpsPsEnablePerCpuCoreDpc",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Services\nvlddmkm\NVAPI","RmGpsPsEnablePerCpuCoreDpc",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Services\nvlddmkm\Global\NVTweak","RmGpsPsEnablePerCpuCoreDpc",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","RmGpsPsEnablePerCpuCoreDpc",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power","RmGpsPsEnablePerCpuCoreDpc",1)

    def _disableWriteCombining(self):
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","DisableWriteCombining",1)

    def _disableTDR(self):
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","TdrLevel",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","TdrDelay",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","TdrDdiDelay",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","TdrDebugMode",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","TdrLimitCount",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","TdrLimitTime",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","TdrTestMode",0)

    def _optimizePowerMizer(self):
        regedit._setHKLMdwordREG('NVIDIA',r"System\CurrentControlSet\Control\Class{4d36e968-e325-11ce-bfc1-08002be10318}","PowerMizerEnable",1)
        regedit._setHKLMdwordREG('NVIDIA',r"System\CurrentControlSet\Control\Class{4d36e968-e325-11ce-bfc1-08002be10318}","PowerMizerLevel",1)
        regedit._setHKLMdwordREG('NVIDIA',r"System\CurrentControlSet\Control\Class{4d36e968-e325-11ce-bfc1-08002be10318}","PowerMizerLevelAC",1)
        regedit._setHKLMdwordREG('NVIDIA',r"System\CurrentControlSet\Control\Class{4d36e968-e325-11ce-bfc1-08002be10318}","PerfLevelSrc",8738)

    def _advancedDriverDebloat(self):
        dirs_to_remove = [
            "C:\\Nvidia\\Display.NView",
            "C:\\Nvidia\\Display.Optimus",
            "C:\\Nvidia\\Display.Update",
            "C:\\Nvidia\\GFExperience.NvStreamSrv",
            "C:\\Nvidia\\HDAudio",
            "C:\\Nvidia\\Miracast.VirtualAudio",
            "C:\\Nvidia\\MSVCRT",
            "C:\\Nvidia\\NGXCore",
            "C:\\Nvidia\\nodejs",
            "C:\\Nvidia\\NvAbHub",
            "C:\\Nvidia\\NvBackend",
            "C:\\Nvidia\\NvCamera",
            "C:\\Nvidia\\NvModuleTracker",
            "C:\\Nvidia\\NVPCF",
            "C:\\Nvidia\\NvTelemetry",
            "C:\\Nvidia\\NvVAD",
            "C:\\Nvidia\\NvvHCI",
            "C:\\Nvidia\\NVWMI",
            "C:\\Nvidia\\PhysX",
            "C:\\Nvidia\\PPC",
            "C:\\Nvidia\\ShieldWirelessController",
            "C:\\Nvidia\\Update.Core",
            "C:\\Nvidia\\GFExperience\\data",
            "C:\\Nvidia\\GFExperience\\dependencies",
            "C:\\Nvidia\\GFExperience\\locales",
            "C:\\Nvidia\\GFExperience\\osc",
            "C:\\Nvidia\\GFExperience\\swiftshader",
            "C:\\Nvidia\\GFExperience\\www"
        ]

        for directory in dirs_to_remove:
            try:
                shutil.rmtree(directory)
                print._printg('NVIDIA',f'REMOVED {directory}')
            except FileNotFoundError:
                print._printr('NVIDIA',f'NOT FOUND {directory}')
            except PermissionError:
                print._printr('NVIDIA',f'PERMISSION ERROR {directory}')
            except Exception as e:
                print._printr('NVIDIA',f'ERROR REMOVING {directory}')

    def _removeNvidiaTelemetry(self):
        regedit._setHKLMdwordREG('NVIDIA',r"SOFTWARE\NVIDIA Corporation\NvControlPanel2\Client","OptInOrOutPreference",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SOFTWARE\NVIDIA Corporation\Global\FTS","EnableRID66610",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SOFTWARE\NVIDIA Corporation\Global\FTS","EnableRID64640",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SOFTWARE\NVIDIA Corporation\Global\FTS","EnableRID44231",0)
        
        commands = [r'schtasks /change /disable /tn "NvTmRep_CrashReport1_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}"',
                    r'schtasks /change /disable /tn "NvTmRep_CrashReport2_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}"',
                    r'schtasks /change /disable /tn "NvTmRep_CrashReport3_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}"',
                    r'schtasks /change /disable /tn "NvTmRep_CrashReport4_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}"',
                    r'schtasks /change /disable /tn "NvDriverUpdateCheckDaily_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}"',
                    r'schtasks /change /disable /tn "NVIDIA GeForce Experience SelfUpdate_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}"',
                    r'schtasks /change /disable /tn "NvTmMon_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}"']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('NVIDIA',cmd)

    def _disableHiddenPowerSavingFeatures(self):
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Power","QosManagesIdleProcessors",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Power","InitialUnparkCount",100)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Power","HighPerformance",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Power","HighestPerformance",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Power","MinimumThrottlePercent",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Power","MaximumThrottlePercent",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Power","MaximumPerformancePercent",100)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Services\nvlddmkm\Global\NVTweak","DisplayPowerSaving",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Power","EnergyEstimationEnabled",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\ControlSet001\Services\nvlddmkm\Global\NVTweak","DisplayPowerSaving",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SOFTWARE\NVIDIA Corporation\Global\NVTweak","DisplayPowerSaving",0)

    def _advancedTweaks(self):
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","TCCSupported",0)
        regedit._setHKCUdwordREG('NVIDIA',r"SOFTWARE\NVIDIA Corporation\Global\NVTweak\Devices\509901423-0\Color","NvCplUseColorCorrection",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","PlatformSupportMiracast",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Services\nvlddmkm\FTS","EnableRID73779",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Services\nvlddmkm\FTS","EnableRID73780",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Services\nvlddmkm\FTS","EnableRID74361",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SOFTWARE\NVIDIA Corporation\Global\FTS","EnableRID44231",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SOFTWARE\NVIDIA Corporation\Global\FTS","EnableRID64640",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SOFTWARE\NVIDIA Corporation\Global\FTS","EnableRID66610",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SOFTWARE\NVIDIA Corporation\NvControlPanel2\Client","OptInOrOutPreference",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\services\NvTelemetryContainer","Start",4)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Services\nvlddmkm\Global\Startup","SendTelemetryData",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SOFTWARE\NVIDIA Corporation\Global\Startup\SendTelemetryData","0",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SOFTWARE\Microsoft\Windows\Dwm","OverlayTestMode",5)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\ControlSet001\Services\nvlddmkm","EnableMidBufferPreemption",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","PlatformSupportMiracast",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","RmGpsPsEnablePerCpuCoreDpc",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power","RmGpsPsEnablePerCpuCoreDpc",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","RMDisablePostL2Compression",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","RmDisableRegistryCaching",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","RmGpsPsEnablePerCpuCoreDpc",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DesktopStereoShortcuts",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","FeatureControl",4)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","NVDeviceSupportKFilter",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RmCacheLoc",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RmDisableInst2Sys",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RmFbsrPagedDMA",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RMGpuId",256)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RmProfilingAdminOnly",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","TCCSupported",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","TrackResetEngine",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","UseBestResolution",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","ValidateBlitSubRects",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Power","MaxIAverageGraphicsLatencyInOneBucket",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","PlatformSupportMiracast",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Power","CsEnabled",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Power","PerfCalculateActualUtilization",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Power","SleepReliabilityDetailedDiagnostics",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Power","EventProcessorEnabled",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Power","QosManagesIdleProcessors",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Power","DisableVsyncLatencyUpdate",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Power","DisableSensorWatchdog",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Power","InterruptSteeringDisabled",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Services\intelppm\Parameters","AcpiFirmwareWatchDog",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Services\intelppm\Parameters","AmliWatchdogAction",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Services\intelppm\Parameters","AmliWatchdogTimeout",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Services\intelppm\Parameters","WatchdogTimeout",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Session Manager\Throttle","PerfEnablePackageIdle",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Services\nvlddmkm","0x112493bd",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Services\nvlddmkm","0x11e91a61",4294967295)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\ControlSet001\Services\nvlddmkm","DisableCudaContextPreemption",1)

    def _latencyTolerance2(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","D3PCLatency",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","F1TransitionLatency",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","LOWLATENCY",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","Node3DLowLatency",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PciLatencyTimerControl",20)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RMDeepL1EntryLatencyUsec",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RmGspcMaxFtuS",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RmGspcMinFtuS",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RmGspcPerioduS",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RMLpwrEiIdleThresholdUs",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RMLpwrGrIdleThresholdUs",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RMLpwrGrRgIdleThresholdUs",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","RMLpwrMsIdleThresholdUs",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","VRDirectFlipDPCDelayUs",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","VRDirectFlipTimingMarginUs",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","VRDirectJITFlipMsHybridFlipDelayUs",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","vrrCursorMarginUs",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","vrrDeflickerMarginUs",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","vrrDeflickerMaxUs",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Services\nvlddmkm","DisablePreemption",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Services\nvlddmkm","DisableCudaContextPreemption",1)

        reg_query_command = ['reg', 'query', r'HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}', '/s', '/v', 'DriverDesc']
        result = subprocess.run(reg_query_command, capture_output=True, text=True)

        relevant_lines = [line.split()[0] for line in result.stdout.split('\n') if "HKEY AMD ATI" in line]

        if relevant_lines:
            subprocess.run(['Reg.exe', 'add', relevant_lines[0], '/v', 'KMD_EnableComputePreemption', '/t', 'REG_DWORD', '/d', '0', '/f'])
            print._printg('AMD',relevant_lines[0])
            
        else:
            print._printr('AMD','No relevant line found!')
        
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\ControlSet001\Services\nvlddmkm","EnableMidGfxPreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\ControlSet001\Services\nvlddmkm","EnableMidGfxPreemptionVGPU",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\ControlSet001\Services\nvlddmkm","EnableMidBufferPreemptionForHighTdrTimeout",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\ControlSet001\Services\nvlddmkm","EnableMidBufferPreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\ControlSet001\Services\nvlddmkm","ComputePreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\ControlSet001\Services\nvlddmkm","DisablePreemption",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\ControlSet001\Services\nvlddmkm","EnableMidBufferPreemptionForHighTdrTimeout",0)
        regedit._setHKLMdwordREG('AMD',r"CurrentControlSet\Control\GraphicsDrivers\Scheduler","EnablePreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","EnablePreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","EnablePreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","PlatformSupportMiracast",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Services\nvlddmkm","DisablePreemption",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","EnablePreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","EnablePreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power","EnablePreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnablePreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power","DisableCudaContextPreemption",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power","DisablePreemptionOnS3S4",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power","ComputePreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power","EnableMidGfxPreemptionVGPU",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power","EnableMidBufferPreemptionForHighTdrTimeout",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power","EnableAsyncMidBufferPreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power","EnableSCGMidBufferPreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power","PerfAnalyzeMidBufferPreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power","EnableMidGfxPreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power","EnableMidBufferPreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler","EnablePreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power","EnableCEPreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","GPUPreemptionLevel",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","ComputePreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","EnableMidGfxPreemptionVGPU",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","EnableMidBufferPreemptionForHighTdrTimeout",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","EnableAsyncMidBufferPreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","EnableSCGMidBufferPreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","PerfAnalyzeMidBufferPreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","EnableMidGfxPreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","EnableMidBufferPreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","EnableCEPreemption",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","DisableCudaContextPreemption",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers","DisablePreemptionOnS3S4",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power","GPUPreemptionLevel",0)

    def _moreAMDTweaks2(self):
        reg_query_command = ['reg', 'query', r'HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}', '/s', '/v', 'DriverDesc']
        result = subprocess.run(reg_query_command, capture_output=True, text=True)

        relevant_lines = [line.split()[0] for line in result.stdout.split('\n') if "HKEY AMD ATI" in line]

        if relevant_lines:
            for REGPATH_AMD in relevant_lines:
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'AsicOnLowPower', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'EnableUlps', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'GCOOPTION_DisableGPIOPowerSaveMode', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'PP_GPUPowerDownEnabled', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'PP_SclkDeepSleepDisable', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'PP_ThermalAutoThrottlingEnable', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'PP_DisableSQRamping', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'PP_DisablePowerContainment', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'KMD_EnableContextBasedPowerManagement', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'KMD_ChillEnabled', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'DisableDrmdmaPowerGating', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'DisableUVDPowerGating', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'DisableUVDPowerGatingDynamic', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'DisableVCEPowerGating', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'DisableSAMUPowerGating', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'DisablePowerGating', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'EnableUvdClockGating', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'EnableVceSwClockGating', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'DisableAllClockGating', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'PP_ForceHighDPMLevel', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'StutterMode', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'PP_Force3DPerformanceMode', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'DisableDMACopy', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'DisableBlocknv11', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'Main3D_DEF', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'Main3D', '/t', 'REG_BINARY', '/d', '3100', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'FlipQueueSize', '/t', 'REG_BINARY', '/d', '3100', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'ShaderCache', '/t', 'REG_BINARY', '/d', '3200', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'Tessellation_OPTION', '/t', 'REG_BINARY', '/d', '3200', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'Tessellation', '/t', 'REG_BINARY', '/d', '3100', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'VSyncControl', '/t', 'REG_BINARY', '/d', '3000', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'TFQ', '/t', 'REG_BINARY', '/d', '3200', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', '3D_Refresh_Rate_Override_DEF', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', '3to2Pulldown_NA', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'AAF_NA', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'Adaptive De-interlacing', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'AllowRSOverlay', '/t', 'REG_SZ', '/d', 'false', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'AllowSkins', '/t', 'REG_SZ', '/d', 'false', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'AllowSnapshot', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'AllowSubscription', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'AntiAlias_NA', '/t', 'REG_SZ', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'AreaAniso_NA', '/t', 'REG_SZ', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'ASTT_NA', '/t', 'REG_SZ', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'AutoColorDepthReduction_NA', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'DisableSAMUPowerGating', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'DisableUVDPowerGatingDynamic', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'DisableVCEPowerGating', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'EnableAspmL0s', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'EnableAspmL1', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'EnableUlps', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'EnableUlps_NA', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'KMD_DeLagEnabled', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'KMD_FRTEnabled', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'DisableDMACopy', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'DisableBlocknv11', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'StutterMode', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'EnableUlps', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'PP_SclkDeepSleepDisable', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'PP_ThermalAutoThrottlingEnable', '/t', 'REG_DWORD', '/d', '0', '/f'])
                subprocess.run(['Reg.exe', 'add', REGPATH_AMD, '/v', 'DisableDrmdmaPowerGating', '/t', 'REG_DWORD', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', f'{REGPATH_AMD}\\UMD', '/v', 'Main3D_DEF', '/t', 'REG_SZ', '/d', '1', '/f'])
                subprocess.run(['Reg.exe', 'add', f'{REGPATH_AMD}\\UMD', '/v', 'Main3D', '/t', 'REG_BINARY', '/d', '3100', '/f'])
                subprocess.run(['Reg.exe', 'add', f'{REGPATH_AMD}\\UMD', '/v', 'FlipQueueSize', '/t', 'REG_BINARY', '/d', '3100', '/f'])
                subprocess.run(['Reg.exe', 'add', f'{REGPATH_AMD}\\UMD', '/v', 'ShaderCache', '/t', 'REG_BINARY', '/d', '3200', '/f'])
                subprocess.run(['Reg.exe', 'add', f'{REGPATH_AMD}\\UMD', '/v', 'Tessellation_OPTION', '/t', 'REG_BINARY', '/d', '3200', '/f'])
                subprocess.run(['Reg.exe', 'add', f'{REGPATH_AMD}\\UMD', '/v', 'Tessellation', '/t', 'REG_BINARY', '/d', '3100', '/f'])
                subprocess.run(['Reg.exe', 'add', f'{REGPATH_AMD}\\UMD', '/v', 'VSyncControl', '/t', 'REG_BINARY', '/d', '3000', '/f'])
                subprocess.run(['Reg.exe', 'add', f'{REGPATH_AMD}\\UMD', '/v', 'TFQ', '/t', 'REG_BINARY', '/d', '3200', '/f'])
                subprocess.run(['Reg.exe', 'add', f'{REGPATH_AMD}\\DAL2_DATA__2_0\\DisplayPath_4\\EDID_D109_78E9\\Option', '/v', 'ProtectionControl', '/t', 'REG_BINARY', '/d', '0100000001000000', '/f'])
                print._printg('AMD',REGPATH_AMD)
        else:
            print._printr('AMD','No relevant line found!')

    def _disableAllPreemptions(self):
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","GPUPreemptionLevel",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","ComputePreemption",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnableMidGfxPreemptionVGPU",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnableMidBufferPreemptionForHighTdrTimeout",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnableAsyncMidBufferPreemption",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnableSCGMidBufferPreemption",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PerfAnalyzeMidBufferPreemption",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnableMidGfxPreemption",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnableMidBufferPreemption",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnableCEPreemption",0)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisableCudaContextPreemption",1)
        regedit._setHKLMdwordREG('NVIDIA',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisablePreemptionOnS3S4",1)

    def _getGPUDeviceIDS(self):
        try:
            result = subprocess.run(['wmic', 'path', 'Win32_VideoController', 'get', 'PNPDeviceID'], capture_output=True, text=True, check=True)
            lines = result.stdout.strip().split('\n')[1:]
            return [line.split('=')[-1].strip() for line in result.stdout.split('\n') if 'PCI\\VEN_' in line]
        except subprocess.CalledProcessError as e:
            print._printr('GPU',f'Error Getting PNPDeviceIDS {e}')
            print._printr('GPU',f'Error Output {e.stderr}')
            return []

    def _enableMSIModeAndMore(self):
        gpu_device_ids = self._getGPUDeviceIDS()

        for gpu_device_id in gpu_device_ids:
            regedit._setHKLMregszREG('NVIDIA',f'System\\CurrentControlSet\\Enum\\{gpu_device_id}\\Device Parameters\\Interrupt Management\\Affinity Policy','DevicePriority','')
            
            regedit._setHKLMregszREG('NVIDIA',f'SYSTEM\\CurrentControlSet\\Enum\\{gpu_device_id}\\Device Parameters\\Interrupt Management\\MessageSignaledInterruptProperties','MessageNumberLimit','')

            regedit._setHKLMdwordREG('NVIDIA',f'System\\CurrentControlSet\\Enum\\{gpu_device_id}\\Device Parameters\\Interrupt Management\\MessageSignaledInterruptProperties','MSISupported',1)
            
    def _enableGPUPStates(self):
        pnp_device_ids = self._getGPUDeviceIDS()

        for pnp_device_id in pnp_device_ids:
            result = subprocess.run(['reg', 'query', f'HKLM\\SYSTEM\\ControlSet001\\Enum\\{pnp_device_id}', '/v', 'Driver'], capture_output=True, text=True)
            driver_lines = result.stdout.split('\n')
            for line in driver_lines:
                if 'Driver' in line:
                    driver = line.split('REG_SZ')[-1].strip()
                    
                    for char in driver:
                        if char == '{':
                            class_guid = driver[driver.index(char):].rstrip()
                            break
                    
                    regedit._setHKLMdwordREG('NVIDIA',f'SYSTEM\\CurrentControlSet\\Control\\Class\\{class_guid}','DisableDynamicPstate',1)

    def _disableHDCPNvidia(self):
        try:
            pnp_device_ids = self._getGPUDeviceIDS()

            for pnp_device_id in pnp_device_ids:
                result = subprocess.run(['reg', 'query', f'HKLM\\SYSTEM\\ControlSet001\\Enum\\{pnp_device_id}', '/v', 'Driver'], capture_output=True, text=True)
                driver_lines = result.stdout.split('\n')

                for line in driver_lines:
                    if 'Driver' in line:
                        driver = line.split('REG_SZ')[-1].strip()

                        for char in driver:
                            if char == '{':
                                class_guid = driver[driver.index(char):].rstrip()
                                break

                        regedit._setHKLMdwordREG('NVIDIA',f'System\\ControlSet001\\Control\\Class\\{class_guid}','RMHdcpKeyglobZero',1)

        except Exception as e:
            print._printr('NVIDIA',f'An error occoured: {e}')

    def _generalGPUTweaks(self):
        self._mmcssGpuTweaks()
        self._graphicsCardSchedulerTweaks()
        self._disablePreemptionGeneral()
        self._disableGpuEnergyDrv()
        self._latencyTolerance()
        self._vram()

    def _nvidiaGpuTweaks(self):
        self._advancedDriverDebloat()
        self._setDriverAcceleration()
        self._forceContigousMemoryAllocation()
        self._dpcsForEachCore()
        self._disableWriteCombining()
        self._disableTDR()
        self._optimizePowerMizer()
        self._removeNvidiaTelemetry()
        self._enableMSIModeAndMore()
        self._enableGPUPStates()
        self._disableHDCPNvidia()
        self._disableHiddenPowerSavingFeatures()
        self._advancedTweaks()
        self._latencyTolerance2()
        self._disableAllPreemptions()

    def _disableOverrideRefreshRate(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","3D_Refresh_Rate_Override_DEF",0)

    def _disableSnapshot(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","AllowSnapshot",0)

    def _disableAntiAliasing(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","AAF_NA",0)
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","AntiAlias_NA","0")
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","ASTT_NA","0")

    def _disableAllowSubscription(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","AllowSubscription",0)

    def _disableAnisotropicFiltering(self):
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","AreaAniso_NA","0")

    def _disableRSOverlay(self):
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","AllowRSOverlay","false")

    def _enableAdaptiveDeInterlacing(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","Adaptive De-interlacing",1)

    def _disableAllowSkins(self):
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","AllowSkins","false")

    def _disableAutoColorDepthReduction(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","AutoColorDepthReduction_NA",0)

    def _disablePowerGating(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisableSAMUPowerGating",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisableUVDPowerGatingDynamic",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisableVCEPowerGating",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisablePowerGating",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisableDrmdmaPowerGating",1)

    def _disableClockGating(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnableVceSwClockGating",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnableUvdClockGating",1)

    def _disableASPM(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnableAspmL0s",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnableAspmL1",0)

    def _disableULPS(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnableUlps",0)
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnableUlps_NA","0")

    def _enableDeLag(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","KMD_DeLagEnabled",1)

    def _disableFRT(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","KMD_FRTEnabled",0)

    def _disableDMA(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisableDMACopy",1)

    def _enableBlockWrite(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisableBlockWrite",0)

    def _disableStutterMode(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","StutterMode",0)

    def _disableGPUMemClockSleepState(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PP_SclkDeepSleepDisable",1)

    def _disableThermalThrottling(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PP_ThermalAutoThrottlingEnable",0)

    def _disablePreemptionAMD(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","KMD_EnableComputePreemption",0)

    def _settingMain3D(self):
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","Main3D_DEF","1")
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","Main3D",b'3100')

    def _settingFlipQueueSize(self):
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","FlipQueueSize",b'3100')

    def _settingShaderCache(self):
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","ShaderCache",b'3200')

    def _configuringTFQ(self):
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TFQ",b'3200')

    def _disableHDCP(self):
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\\DAL2_DATA__2_0\DisplayPath_4\EDID_D109_78E9\Option","ProtectionControl",b'0100000001000000')

    def _disableGPUPowerDown(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PP_GPUPowerDownEnabled",1)

    def _disableAMDLogging(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Services\amdlog","Start",4)

    def _moreAMDTweaks(self):
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnableVceSwClockGating",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnableUvdClockGating",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisableVCEPowerGating",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisableUVDPowerGatingDynamic",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisablePowerGating",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisableSAMUPowerGating",1)
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisableFBCForFullScreenApp","0")
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisableFBCSupport",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisableEarlySamuInit",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PP_GPUPowerDownEnabled",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisableDrmdmaPowerGating",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PP_SclkDeepSleepDisable",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PP_ThermalAutoThrottlingEnable",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PP_ActivityTarget",30)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PP_ODNFeatureEnable",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnableUlps",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","GCOOPTION_DisableGPIOPowerSaveMode",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PP_AllGraphicLevel_DownHyst",20)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PP_AllGraphicLevel_UpHyst",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","KMD_FRTEnabled",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisableDMACopy",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DisableBlocknv11",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PP_ODNFeatureEnable",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","KMD_MaxUVDSessions",32)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DalAllowDirectMemoryAccessTrig",1)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","DalAllowDPrefSwitchingForGLSync",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","WmAgpMaxIdleClk",32)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PP_MCLKStutterModeThreshold",4096)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","StutterMode",0)
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","TVEnableOverscan",0)
        regedit._setHKLMdwordREG('AMD',r"SOFTWARE\Microsoft\Windows\Dwm","OverlayTestMode",5)
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","MLF",b'3000')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","EQAA",b'3000')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","PowerState",b'3000')
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","AreaAniso_DEF","8")
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","SurfaceFormatReplacements_DEF","1")
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","Main3D_DEF","1")
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","AnisoType_DEF","0")
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","AnisoDegree_DEF","4")
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","ForceTripleBuffering",b'3000')
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","ForceTripleBuffering_DEF","0")
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TextureOpt_DEF","1")
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TextureLod_DEF","1")
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TruformMode_DEF","2")
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","LodAdj","0")
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","ForceZBufferDepth_DEF","1")
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","Tessellation_OPTION_DEF","0")
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","NoOSPowerOptions","1")
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","ForceZBufferDepth",b'3100')
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","ForceZBufferDepth_DEF","1")
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","Tessellation_DEF","0")
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","Main3D",b'3100')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","AnisoType",b'32000000')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","AnisotropyOptimise",b'3100')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TrilinearOptimise",b'3100')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","AnisoDegree",b'3400')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TextureLod",b'31000000')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TextureOpt",b'31000000')
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TextureOpt_DEF","1")
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TruformMode_NA",b'3200')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","Tessellation_OPTION",b'3200')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","Tessellation",b'3100')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","Main3D_SET",b'302031203220332034203500')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","ForceZBufferDepth_SET",b'3020313620323400')
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","FlipQueueSize","1")
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","SurfaceFormatReplacements",b'3000')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TFQ",b'3200')
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TFQ_DEF","1")
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","ZFormats_NA",b'3100')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","PowerState",b'3000')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","AntiStuttering",b'3000')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TurboSync",b'3000')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","HighQualityAF",b'3300')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","ShaderCache",b'3200')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","ForceZBufferDepth",b'3100')
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","ForceZBufferDepth_DEF","1")
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","Tessellation_DEF","0")
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","Main3D",b'3100')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","AnisoType",b'32000000')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","AnisotropyOptimise",b'3100')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TrilinearOptimise",b'3100')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","AnisoDegree",b'3400')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TextureLod",b'31000000')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TextureOpt",b'31000000')
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TextureOpt_DEF","1")
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TruformMode_NA",b'3200')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","Tessellation_OPTION",b'3200')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","Tessellation",b'3100')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","Main3D_SET",b'302031203220332034203500')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","ForceZBufferDepth_SET",b'3020313620323400')
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","FlipQueueSize","1")
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","SurfaceFormatReplacements",b'3000')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TFQ",b'3200')
        regedit._setHKLMregszREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TFQ_DEF","1")
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","ZFormats_NA",b'3100')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","PowerState",b'3000')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","AntiStuttering",b'3000')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","TurboSync",b'3000')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","HighQualityAF",b'3300')
        regedit._setHKLMbinaryREG('AMD',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD","ShaderCache",b'3200')
        regedit._setHKLMdwordREG('AMD',r"SYSTEM\ControlSet001\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","EnableUlps",0)

    def _amdGPUTweaks(self):
        self._disableOverrideRefreshRate()
        self._disableSnapshot()
        self._disableAntiAliasing()
        self._disableAllowSubscription()
        self._disableAnisotropicFiltering()
        self._disableRSOverlay()
        self._enableAdaptiveDeInterlacing()
        self._disableAllowSkins()
        self._disableAutoColorDepthReduction()
        self._disablePowerGating()
        self._disableClockGating()
        self._disableASPM()
        self._disableULPS()
        self._enableDeLag()
        self._disableFRT()
        self._disableDMA()
        self._enableBlockWrite()
        self._disableStutterMode()
        self._disableGPUMemClockSleepState()
        self._disableThermalThrottling()
        self._disablePreemptionAMD()
        self._settingMain3D()
        self._settingFlipQueueSize()
        self._settingShaderCache()
        self._configuringTFQ()
        self._disableHDCP()
        self._disableGPUPowerDown()
        self._disableAMDLogging()
        self._moreAMDTweaks()

    def _intelGpuTweaks(self):
        reg_query_command = ['Reg', 'query', r'HKLM\System\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}', '/t', 'REG_SZ', '/s', '/e', '/f', 'Intel']
        relevant_lines = [line for line in subprocess.run(reg_query_command, capture_output=True, text=True).stdout.split('\n') if "HKEY" in line]

        for line in relevant_lines:
            registry_key = line.split()[0]

            reg_add_commands = [
                ['Reg.exe', 'add', registry_key, '/v', 'Disable_OverlayDSQualityEnhancement', '/t', 'REG_DWORD', '/d', '1', '/f'],
                ['Reg.exe', 'add', registry_key, '/v', 'IncreaseFixedSegment', '/t', 'REG_DWORD', '/d', '1', '/f'],
                ['Reg.exe', 'add', registry_key, '/v', 'AdaptiveVsyncEnable', '/t', 'REG_DWORD', '/d', '0', '/f'],
                ['Reg.exe', 'add', registry_key, '/v', 'DisablePFonDP', '/t', 'REG_DWORD', '/d', '1', '/f'],
                ['Reg.exe', 'add', registry_key, '/v', 'EnableCompensationForDVI', '/t', 'REG_DWORD', '/d', '1', '/f'],
                ['Reg.exe', 'add', registry_key, '/v', 'NoFastLinkTrainingForeDP', '/t', 'REG_DWORD', '/d', '0', '/f'],
                ['Reg.exe', 'add', registry_key, '/v', 'ACPowerPolicyVersion', '/t', 'REG_DWORD', '/d', '16898', '/f'],
                ['Reg.exe', 'add', registry_key, '/v', 'DCPowerPolicyVersion', '/t', 'REG_DWORD', '/d', '16642', '/f'],
            ]

            for cmd in reg_add_commands:
                subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
                print._printg('INTEL',cmd)

        regedit._setHKLMdwordREG('INTEL',r'Software\Intel\GMM','DedicatedSegmentSize',512)