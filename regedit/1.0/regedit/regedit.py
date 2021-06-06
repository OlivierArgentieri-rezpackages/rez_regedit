import winreg

class Regedit:
    @staticmethod
    def set_reg(regpath, name, value):
        try:
            winreg.CreateKey(winreg.HKEY_CURRENT_USER, regpath)
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, 
                                           winreg.KEY_WRITE)
            winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
            winreg.CloseKey(registry_key)
            return True
        except WindowsError:
            return False

    @staticmethod
    def get_reg(regpath, name):
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, regpath, 0,
                                           winreg.KEY_READ)
            value, regtype = winreg.QueryValueEx(registry_key, name)
            winreg.CloseKey(registry_key)
            return value
        except WindowsError:
            return None

    @staticmethod
    def rem_reg_value(regpath, name):
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, regpath, 0, 
                                           winreg.KEY_ALL_ACCESS)
            winreg.DeleteValue(registry_key, name)
            return True
        except WindowsError as e:
            return False

    @staticmethod
    def rem_reg_key(regpath):
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, regpath, 0, 
                                           winreg.KEY_ALL_ACCESS)
            winreg.DeleteKey(registry_key, "")
            return True
        except WindowsError as e:
            return False