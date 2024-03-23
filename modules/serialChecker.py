import wmi
import psutil
import ctypes
import os
import msvcrt
from utilities.print import _printr,_printg

class SerialChecker():
    def __init__(self):
        self.w = wmi.WMI()

    def _getBaseboardSerialNumber(self):
        try:
            for board in self.w.Win32_BaseBoard():
                return board.SerialNumber
        except Exception as e:
            return "Not Found"

    def _getMacAddresses(self):
        try:
            return [link.address for link in psutil.net_if_addrs().get('Ethernet', [])]
        except Exception as e:
            return "Not Found"

    def _getProcessorId(self):
        try:
            for processor in self.w.Win32_Processor():
                return processor.ProcessorId
        except Exception as e:
            return "Not Found"

    def _getGPUInfo(self):
        try:
            gpu_info = []
            for gpu in self.w.Win32_VideoController():
                gpu_info.append({
                    'name': gpu.Name,
                    'device_id': gpu.DeviceID,
                    'pnp_device_id': gpu.PNPDeviceID
                })
            return gpu_info
        except Exception as e:
            return "Not Found"

    def _getDiskDrivesSerialNumbers(self):
        try:
            serial_numbers = []
            kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

            system_drive = os.getenv('SystemDrive')
            system_drive_serial = ctypes.c_ulonglong(0)
            if kernel32.GetVolumeInformationW(
                    ctypes.c_wchar_p(system_drive + '\\'),
                    None, 0,
                    ctypes.byref(system_drive_serial),
                    None, None, None, 0):
                serial_numbers.append({
                    'device_id': system_drive,
                    'serial_number': f"{system_drive_serial.value:016X}",
                })

            drives = [drive.device.rstrip("\\") for drive in psutil.disk_partitions()]
            for drive in drives:
                if drive != system_drive:
                    volume_serial = ctypes.c_ulonglong(0)
                    if kernel32.GetVolumeInformationW(
                            ctypes.c_wchar_p(drive + '\\'),
                            None, 0,
                            ctypes.byref(volume_serial),
                            None, None, None, 0):
                        serial_numbers.append({
                            'device_id': drive,
                            'serial_number': f"{volume_serial.value:016X}",
                        })

            return serial_numbers
        except Exception as e:
            return "Not Found"


    def _getMotherboardSerialNumber(self):
        return self._getBaseboardSerialNumber()

    def _getWindowsUUID(self):
        try:
            for system in self.w.Win32_ComputerSystemProduct():
                return system.UUID
        except Exception as e:
            return "Not Found"

    def _getSmbiosInfo(self):
        try:
            for system in self.w.Win32_ComputerSystemProduct():
                return {
                    'serial_number': system.IdentifyingNumber,
                    'uuid': system.UUID,
                }
        except Exception as e:
           return "Not Found"
        
    def _start(self):
        _printg("Baseboard Serial Number", self._getBaseboardSerialNumber())
        _printg("MAC Addresses", self._getMacAddresses())
        _printg("Processor ID", f"{self._getProcessorId()}\n")

        gpu_info = self._getGPUInfo()
        if gpu_info:
            for gpu in gpu_info:
                _printg("GPU", gpu['device_id'])
                _printg("NAME",gpu['name'])
                _printg("Device ID", gpu['device_id'])
                _printg("PnP Device ID", f"{gpu['pnp_device_id']}\n")
        else:
            _printr("GPU","Error No GPU information available.")

        disk_info = self._getDiskDrivesSerialNumbers()    
        if disk_info:
            for drive in disk_info:
                _printg("Disk Drive",f"{drive['device_id']}")
                _printg("Serial Number",f"{drive['serial_number']}\n")
        else:
            _printr("DISK DRIVE","No disk drive information available.")

        _printg("Motherboard Serial Number", self._getMotherboardSerialNumber())

        windows_uuid = self._getWindowsUUID()
        _printg('WINDOWS UUID',windows_uuid)

        smbios_info = self._getSmbiosInfo()
        if smbios_info:
            _printg("SMBIOS SERIAL", smbios_info['serial_number'])
            _printg("SMBIOS UUID",smbios_info['uuid'])
        else:
            _printr("SMBIOS","No SMBIOS information available.")
            
        print('')
        _printg("SERIAL CHECKER",'Press any key to exit.')

        while not msvcrt.kbhit():
            pass