import subprocess
from utilities import print

class Install():
    def __init__(self) -> None:
        if self.is_chocolatey_installed():
            print._printg("INSTALL","Chocolatey is already installed.")
        else:
            self.install_chocolatey()


    def is_chocolatey_installed(self):
        try:
            subprocess.run(["choco", "--version"], check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
            return True
        except subprocess.CalledProcessError:
            return False

    def install_chocolatey(self):
        try:
            print._printr("INSTALL","Chocolatey is not installed. Installing Chocolatey...")
            
            subprocess.run(["powershell", "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"], check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
            print._printg("INSTALL","Chocolatey is installed.")
        except subprocess.CalledProcessError:
            print._printr('INSTALL','Failed to install chocolatey!')
        

    def is_package_installed(self,package_name):
        try:
            result = subprocess.run(["choco", "list", "--exact", package_name], check=True,capture_output=True,text=True)
            if 'packages installed' in result.stdout:
                installed_packages = result.stdout.strip().split('\n')
                if len(installed_packages) > 2:
                    return True
            else:
                print._printr('INSTALL','Cannot found if the package is installed')
                return False
        except subprocess.CalledProcessError:
            return False

    def install_package(self,package_name):
        if self.is_package_installed(package_name):
            print._printg('INSTALL',f"{package_name} is already installed.")
        else:
            try:
                print._printg('INSTALL',f"Installing {package_name} using Chocolatey...")
                subprocess.run(["choco", "install", package_name, "-y"], check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
                print._printg('INSTALL',f"Installed {package_name}")
            except subprocess.CalledProcessError as c:
                print._printg('fasz',c)
                print._printr('INSTALL',f'Failed to install {package_name}!')

    def _installFirefox(self):
        self.install_package("firefox")

    def _installChrome(self):
        self.install_package("googlechrome")

    def _installOpera(self):
        self.install_package("opera")

    def _installBrave(self):
        self.install_package("brave")
    
    def _installDiscord(self):
        self.install_package("discord")

    def _installMessenger(self):
        self.install_package("messenger")

    def _installTeamSpeak(self):
        self.install_package("teamspeak")

    def _installAnyDesk(self):
        self.install_package("anydesk")

    def _installVLC(self):
        self.install_package("vlc")

    def _installMPV(self):
        self.install_package("mpv")

    def _installSpotify(self):
        self.install_package("spotify")

    def _installSteam(self):
        self.install_package("steam")

    def _installEpicGames(self):
        self.install_package("epicgameslauncher")

    def _install7Zip(self):
        self.install_package("7zip")

    def _installWinRar(self):
        self.install_package("winrar")

    def _installVSCode(self):
        self.install_package("vscode")

    def _installNotepadPlusPlus(self):
        self.install_package("notepadplusplus")
    
    def _installGit(self):
        self.install_package("git")

    def _installGitHubDesktop(self):
        self.install_package("github-desktop")

    def _installHwInfo(self):
        self.install_package("hwinfo")

    def _installGpuZ(self):
        self.install_package("gpu-z")

    def _installCPUZ(self):
        self.install_package("cpu-z")

    def _installMSIAfterburner(self):
        self.install_package("msiafterburner")

    def _installYTDLP(self):
        self.install_package("yt-dlp")

    def _installGalleryDL(self):
        self.install_package("gallery-dl")

    def _doAll(self):
        self._installFirefox()
        self._installChrome()
        self._installOpera()
        self._installBrave()
        self._installDiscord()
        self._installMessenger()
        self._installTeamSpeak()
        self._installAnyDesk()
        self._installVLC()
        self._installMPV()
        self._installSpotify()
        self._installSteam()
        self._installEpicGames()
        self._install7Zip()
        self._installWinRar()
        self._installVSCode()
        self._installNotepadPlusPlus()
        self._installGit()
        self._installGitHubDesktop()
        self._installHwInfo()
        self._installGpuZ()
        self._installCPUZ()
        self._installMSIAfterburner()
        self._installYTDLP()
        self._installGalleryDL()

    def _DISILLUSION(self):
        self._installFirefox()
        self._installChrome()
        self._installBrave()
        self._installDiscord()
        self._installMessenger()
        self._installAnyDesk()
        self._installMPV()
        self._installSpotify()
        self._installSteam()
        self._install7Zip()
        self._installVSCode()
        self._installNotepadPlusPlus()
        self._installGitHubDesktop()
        self._installHwInfo()
        self._installGpuZ()
        self._installCPUZ()
        self._installMSIAfterburner()
        self._installYTDLP()
        self._installGalleryDL()