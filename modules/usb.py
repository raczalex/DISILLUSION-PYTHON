import subprocess
from utilities import regedit
from utilities import print

class USB():
    def __init__(self) -> None:
        pass

    def _disableHiddenUsbPowerSavings(self):
        usb_power_saving_services = [
            "EnhancedPowerManagementEnabled",
            "AllowIdleIrpInD3",
            "EnableSelectiveSuspend",
            "DeviceSelectiveSuspended",
            "SelectiveSuspendEnabled",
            "SelectiveSuspendOn",
            "EnumerationRetryCount",
            "ExtPropDescSemaphore",
            "WaitWakeEnabled",
            "D3ColdSupported",
            "WdfDirectedPowerTransitionEnable",
            "EnableIdlePowerManagement",
            "IdleInWorkingState"
        ]

        
        for service in usb_power_saving_services:
            try:
                result = subprocess.run(['reg', 'query', r'HKLM\SYSTEM\CurrentControlSet\Enum', '/s', '/f', service], capture_output=True, text=True)
                service_entries = [line.strip() for line in result.stdout.splitlines() if 'HKEY' in line]
                for entry in service_entries:
                    subprocess.run(['Reg', 'add', entry, '/v', service, '/t', 'REG_DWORD', '/d', '0', '/f'],text=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
                    print._printg('USB',f'{service} 0')
            except subprocess.CalledProcessError as e:
                print._printr(f'USB',f'ERROR: {e}')
                print._printr(f'USB',f'COMMAND OUTPUT: {e.stdout.decode()}')
            except Exception as e:
                print._printr(f'USB',f'ERROR: {e}')

    def _usbControllerPriority(self):
        result = subprocess.run(['wmic', 'path', 'Win32_IDEController', 'get', 'PNPDeviceID'], capture_output=True, text=True)
        controller_entries = [line.strip() for line in result.stdout.splitlines() if 'PCI\\VEN_' in line]

        for entry in controller_entries:
            regedit._setHKLMregszREG('USB',f'System\\CurrentControlSet\\Enum\\{entry}\\Device Parameters\\Interrupt Management\\Affinity Policy','DevicePriority','')
            print._printg('USB',entry)

    def _enableMSIForController(self):
        result = subprocess.run(['wmic', 'path', 'Win32_USBController', 'get', 'PNPDeviceID'], capture_output=True, text=True)
        controller_entries = [line.strip() for line in result.stdout.splitlines()]

        for entry in controller_entries:
            regedit._setHKLMregszREG('USB',f'System\\CurrentControlSet\\Enum\\{entry}\\Device Parameters\\Interrupt Management\\Affinity Policy','DevicePriority','')

            regedit._setHKLMdwordREG('USB',f'System\\CurrentControlSet\\Enum\\{entry}\\Device Parameters\\Interrupt Management\\MessageSignaledInterruptProperties','MSISupported',1)

    def _usbPowerSavingDisableSelectiveSuspendRegistryValues(self,device_id):
        base_key = f"HKLM\\SYSTEM\\CurrentControlSet\\Enum\\{device_id}\\Device Parameters"
        wdf_key = f"{base_key}\\WDF"

        registry_values = [
            ["/v", "SelectiveSuspendOn", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "SelectiveSuspendEnabled", "/t", "REG_BINARY", "/d", "00", "/f"],
            ["/v", "EnhancedPowerManagementEnabled", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "AllowIdleIrpInD3", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "IdleInWorkingState", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "EnhancedPowerManagementEnabled", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "AllowIdleIrpInD3", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "EnableSelectiveSuspend", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "DeviceSelectiveSuspended", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "SelectiveSuspendEnabled", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "SelectiveSuspendOn", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "D3ColdSupported", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "IdleInWorkingState", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "EnhancedPowerManagementEnabled", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "AllowIdleIrpInD3", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "DeviceSelectiveSuspended", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "SelectiveSuspendEnabled", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "SelectiveSuspendOn", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "fid_D1Latency", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "fid_D2Latency", "/t", "REG_DWORD", "/d", "0", "/f"],
            ["/v", "fid_D3Latency", "/t", "REG_DWORD", "/d", "0", "/f"]
        ]

        for value in registry_values:
            subprocess.run(['Reg', 'add', base_key, *value], text=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
            

            if wdf_key in value:
                base_key += "\\WDF"

    def _usbPowerSavingsDisableSelectiveSuspendAndMore(self):
        try:
            result = subprocess.run(['wmic', 'path', 'Win32_USBController', 'get', 'PNPDeviceID'], capture_output=True, text=True)
            usb_controllers = [line.strip() for line in result.stdout.splitlines() if 'PCI\\VEN_' in line]

            for controller in usb_controllers:
                self._usbPowerSavingDisableSelectiveSuspendRegistryValues(controller)

            print._printg('USB','Registry values set successfully.')
        except subprocess.CalledProcessError as e:
            print._printr('USB',f'ERROR: {e}')

    def _usbThreadPriority(self):
        regedit._setHKLMdwordREG('USB',r"SYSTEM\CurrentControlSet\Services\usbxhci\Parameters","ThreadPriority",31)
        regedit._setHKLMdwordREG('USB',r"SYSTEM\CurrentControlSet\Services\USBHUB3\Parameters","ThreadPriority",31)
        regedit._setHKLMdwordREG('USB',r"SYSTEM\CurrentControlSet\Services\nvlddmkm\Parameters","ThreadPriority",31)
        regedit._setHKLMdwordREG('USB',r"SYSTEM\CurrentControlSet\Services\NDIS\Parameters","ThreadPriority",31)
        regedit._setHKLMdwordREG('USB',r"SYSTEM\CurrentControlSet\Services\DXGKrnl\Parameters","ThreadPriority",15)

    def _directXTweak(self):
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\DirectDraw", "DisableAGPSupport", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\DirectDraw", "DisableAGPSupport", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\DirectDraw", "UseNonLocalVidMem", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\DirectDraw", "UseNonLocalVidMem", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D", "UseNonLocalVidMem", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\Direct3D", "UseNonLocalVidMem", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\DirectDraw", "DisableDDSCAPSInDDSD", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\DirectDraw", "DisableDDSCAPSInDDSD", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\DirectDraw", "EmulationOnly", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\DirectDraw", "EmulationOnly", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\DirectDraw", "EmulatePointSprites", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\DirectDraw", "EmulatePointSprites", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D\Drivers", "ForceRgbRasterizer", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers", "ForceRgbRasterizer", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\DirectDraw", "EmulateStateBlocks", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\DirectDraw", "EmulateStateBlocks", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D", "EnableDebugging", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D", "FullDebug", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D", "DisableDM", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D", "EnableMultimonDebugging", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D", "LoadDebugRuntime", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D\Drivers", "EnumReference", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers", "EnumReference", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D\Drivers", "EnumSeparateMMX", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers", "EnumSeparateMMX", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D\Drivers", "EnumRamp", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers", "EnumRamp", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D\Drivers", "EnumNullDevice", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers", "EnumNullDevice", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D", "FewVertices", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\Direct3D", "FewVertices", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\DirectDraw", "DisableMMX", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\DirectDraw", "DisableMMX", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D", "DisableMMX", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\Direct3D", "DisableMMX", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D", "MMX Fast Path", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\Direct3D", "MMX Fast Path", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D", "MMXFastPath", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\Direct3D", "MMXFastPath", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D", "UseMMXForRGB", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\Direct3D", "UseMMXForRGB", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D\Drivers", "UseMMXForRGB", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers", "UseMMXForRGB", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D\Drivers", "EnumSeparateMMX", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers", "EnumSeparateMMX", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\DirectDraw", "ForceNoSysLock", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Wow6432Node\Microsoft\DirectDraw", "ForceNoSysLock", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D", "DisableVidMemVBs", 0)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D", "MMX Fast Path", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D", "FlipNoVsync", 1)
        regedit._setHKLMdwordREG('USB',r"SOFTWARE\Microsoft\Direct3D\Drivers", "SoftwareOnly", 0)
        regedit._setHKLMdwordREG('USB',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers", "DpiMapIommuContiguous", 1)
        regedit._setHKLMdwordREG('USB',r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers", "HwSchedMode", 2)

    def _doAll(self):
        self._disableHiddenUsbPowerSavings()
        self._usbControllerPriority()
        self._enableMSIForController()
        self._usbPowerSavingsDisableSelectiveSuspendAndMore()
        self._usbThreadPriority()
        self._directXTweak()    