import subprocess
from utilities import print

class Storage():
    def __init__(self) -> None:
        pass
    
    def _bootDriveSSDOptimization(self):
        commands = [r'fsutil behavior set disableLastAccess 0',
                    r'fsutil behavior set disable8dot3 1']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('STORAGE',cmd)
        
    def _bootDriveHDDOptimization(self):
        commands = [r'fsutil behavior set disableLastAccess 2',
                    r'fsutil behavior set disable8dot3 0']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('STORAGE',cmd)

    def _bootDriveDefrag(self):
        command = r'POWERSHELL "Optimize-Volume -DriveLetter C -ReTrim"'
        subprocess.Popen(command,text=True).wait()
        print._printg('STORAGE',command)


    def _tweakUserWriteCache(self):
        try:
            command_output = subprocess.check_output(['Reg.exe', 'Query', 'hklm\\SYSTEM\\CurrentControlSet\\Enum', '/f', '{4d36e967-e325-11ce-bfc1-08002be10318}', '/d', '/s'], text=True)
            key_paths = [line.strip() for line in command_output.splitlines() if "HKEY" in line]

            for key_path in key_paths:
                subprocess.run(['Reg.exe', 'add', f'{key_path}\\Device Parameters\\Disk', '/v', 'UserWriteCacheSetting', '/t', 'reg_dword', '/d', '1', '/f'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
                print._printg('STORAGE','UserWriteCacheSetting 1')

        except subprocess.CalledProcessError as e:
            print._printr('STORAGE',f'ERROR: {e}')
