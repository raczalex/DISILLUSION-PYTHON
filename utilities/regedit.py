import winreg
from subprocess import Popen,PIPE
from os import getlogin
from utilities import print

def _getHKCUvalueREG(REG_PATH,name):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None
    
def _getHKLMvalueREG(REG_PATH,name):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH, 0,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None
    
def _setHKCUdwordREG(header:str,REG_PATH,name,value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_DWORD, value)
        print._printg(header,f'{name} {value}')
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

def _setHKCUregszREG(header:str,REG_PATH,name,value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
        print._printg(header,f'{name} {value}')
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False
    
def _setHKCUbinaryREG(header:str,REG_PATH,name,value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_BINARY, value)
        print._printg(header,f'{name} {value.decode("utf-8")}')
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False
    

def _setHKLMdwordREG(header:str,REG_PATH,name,value):
    try:
        winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_DWORD, value)
        print._printg(header,f'{name} {value}')
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False
    
def _setHKLMdwordREGKEYSET(header:str,REG_PATH,name,value):
    try:
        winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH, 0, 
                                       winreg.KEY_SET_VALUE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_DWORD, value)
        print._printg(header,f'{name} {value}')
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

def _setHKLMregszREG(header:str,REG_PATH,name,value):
    try:
        winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
        print._printg(header,f'{name} {value}')
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False
    
def _setHKLMbinaryREG(header:str,REG_PATH,name,value):
    try:
        winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_BINARY, value)
        print._printg(header,f'{name} {value.decode("utf-8")}')
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False
    
def _setHKUregszREG(header:str,REG_PATH,name,value):
    try:
        winreg.CreateKey(winreg.HKEY_USERS, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_USERS, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
        print._printg(header,f'{name} {value}')
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False
    
def _setHKUdwordREG(header:str,REG_PATH,name,value):
    try:
        winreg.CreateKey(winreg.HKEY_USERS, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_USERS, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_DWORD, value)
        print._printg(header,f'{name} {value}')
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False
    
def _setHKUbinaryREG(header:str,REG_PATH,name,value):
    try:
        winreg.CreateKey(winreg.HKEY_USERS, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_USERS, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_BINARY, value)
        print._printg(header,f'{name} {value.decode("utf-8")}')
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False
    

def _setHKCRregszREG(header:str,REG_PATH,name,value):
    try:
        winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False
    
def _setHKCRdwordREG(header:str,REG_PATH,name,value):
    try:
        winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_DWORD, value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False



def _getSID():
    out = Popen("wmic useraccount get name, sid", stdout=PIPE)
    out = out.communicate()[0].decode().replace("\r", "")
    for line in out.split("\n"):
        if line.startswith(getlogin()):
            sid = line.replace(getlogin(), "").strip()
            break
    return sid

def _deleteSubKey(root, sub):
    
    try:
        open_key = winreg.OpenKey(root, sub, 0, winreg.KEY_ALL_ACCESS)
        num, _, _ = winreg.QueryInfoKey(open_key)
        for i in range(num):
            child = winreg.EnumKey(open_key, 0)
            _deleteSubKey(open_key, child)
            print._printg('SUBKEYDEL',f'DELETED {open_key}')
        try:
           winreg.DeleteKey(open_key, '')
        except Exception as e:
           print._printr('SUBKEYDEL',f'ERROR {e}')
           pass
        finally:
           winreg.CloseKey(open_key)
    except Exception as e:
        print._printr('ERROR',e)
        pass


