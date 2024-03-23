import subprocess
from utilities.print import _printg,_printr
from utilities.console import _printThreeColumnsDictWithNumbersColored
from pystyle import Colors

class Uninstall():
    def __init__(self) -> None:
        pass

    def _getAppxPackages(self):
        try:
            command_output = subprocess.check_output(['powershell', 'Get-AppxPackage -AllUsers | Format-Table Name, PackageFullName, PackageUserInformation'], text=True)

            packages = []
            lines = command_output.split('\n')
            for line in lines[3:-3]:
                parts = line.split()
                name = parts[0]
                full_name = parts[1]
                user_info = parts[2]

                if user_info.lower() != 'uninstalled':
                    packages.append({'Name': name, 'FullName': full_name})

            return packages

        except subprocess.CalledProcessError as e:
            _printr('UNINSTALL',f'ERROR: {e}')
            return []

    def _uninstallAppxPackage(self,package_full_name):
        try:
            subprocess.run(['powershell', f'Remove-AppxPackage -Package {package_full_name} -AllUsers -Confirm:$false'])
            _printg('UNINSTALL',f'Successfully uninstalled {package_full_name}')

        except subprocess.CalledProcessError as e:
            _printr('UNINSTALL',f'ERROR RUNNING COMMAND: {e}')

    def _start(self):
        appx_packages = self._getAppxPackages()
        
        if not appx_packages:
            _printr('UNINSTALL','No AppxPackages Found.')
            return

        _printThreeColumnsDictWithNumbersColored(appx_packages)
        try:
            selection = int(input(f"\n\n   {Colors.white}[UNINSTALL]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
            print('')
        except ValueError:
            _printr('UNINSTALL','Invalid input!')
            return

        if 0 < selection <= len(appx_packages):
            selected_package = appx_packages[selection - 1]
            _printg('UNINSTALL',f'Selected AppxPackage: {selected_package["Name"]}')
            self._uninstallAppxPackage(selected_package['FullName'])
        elif selection == 0:
            _printr('UNINSTALL','Exiting.')
        else:
            _printr('UNINSTALL','Invalid selection. Exiting.')

    def _reinstallAllUWPApps(self):
        try:
            subprocess.run(['powershell', 'Get-AppxPackage -AllUsers | ForEach-Object {Add-AppxPackage -Register "$($_.InstallLocation)\\AppxManifest.xml" -DisableDevelopmentMode}'], check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            _printg('UNINSTALL','Successfully reinstalled all UWP apps.')

        except subprocess.CalledProcessError as e:
            _printr('UNINSTALL',f'ERROR RUNNING COMMAND: {e}')