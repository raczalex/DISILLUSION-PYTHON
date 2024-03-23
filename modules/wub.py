import subprocess
from utilities import print

class WUB():
    def __init__(self) -> None:
        pass

    def _enableWUBx64(self):
        subprocess.run(['resources\\Wub_x64.exe', '/E'])
        print._printg('WUB','Windows Updates Enabled! (x64)')

    def _enableWUBx86(self):
        subprocess.run(['resources\\Wub.exe', '/E'])
        print._printg('WUB','Windows Updates Enabled! (x86)')

    def _disableWUBx64(self):
        subprocess.run(['resources\\Wub_x64.exe', '/D'])
        print._printg('WUB','Windows Updates Disabled! (x64)')

    def _disableWUBx64Protect(self):
        subprocess.run(['resources\\Wub_x64.exe', '/D', '/P'])
        print._printg('WUB','Windows Updates Disabled And Sevices Protected! (x64)')

    def _disableWUBx86(self):
        subprocess.run(['resources\\Wub.exe', '/D'])
        print._printg('WUB','Windows Updates Disabled! (x86)')

    def _disableWUBx86Protect(self):
        subprocess.run(['resources\\Wub.exe', '/D','/P'])
        print._printg('WUB','Windows Updates Disabled And Services Protected! (x86)')