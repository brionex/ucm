import os
import winreg
import ctypes
import ctypes.wintypes


class UserPath:
    def __init__(self, home=None):
        self.home = home or os.path.expanduser('~')

    @staticmethod
    def _get_new_path():
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Environment', 0, winreg.KEY_READ) as key:
            return winreg.QueryValueEx(key, 'PATH')[0]

    def location_in_new_path(self, location, check=False):
        location = os.path.normcase(os.path.realpath(
            os.path.expanduser(location.strip(';:'))))
        new_path = self._get_new_path()
        locations = location.split(os.pathsep)

        for loc in locations:
            if not loc in new_path.split(os.pathsep):
                if check:
                    raise Exception(f'Unable to find `{loc}` in:\n{new_path}')
                else:
                    return False
        return True

    def path_exists(self, location):
        location = os.path.normcase(os.path.realpath(
            os.path.expanduser(location.strip(';:'))))
        new_path = self._get_new_path()
        return location in new_path.split(os.pathsep)

    def put(self, location, front=True, app_name=None, check=False):
        location = os.path.normcase(os.path.realpath(
            os.path.expanduser(location.strip(';:'))))
        app_name = app_name or 'userpath'

        if self.path_exists(location):
            print(f"{location} ya está en el PATH.")
            return True

        head, tail = (location, self._get_new_path()) if front else (
            self._get_new_path(), location)
        new_path = f'{head}{os.pathsep}{tail}'

        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Environment', 0, winreg.KEY_WRITE) as key:
            winreg.SetValueEx(key, 'PATH', 0, winreg.REG_EXPAND_SZ, new_path)

        # Notifica a las aplicaciones sobre el cambio en las variables de entorno
        ctypes.windll.user32.SendMessageTimeoutW(
            0xFFFF,  # HWND_BROADCAST
            0x1A,  # WM_SETTINGCHANGE
            0,  # must be NULL
            'Environment',
            0x0002,  # SMTO_ABORTIFHUNG
            5000,  # milliseconds
            ctypes.wintypes.DWORD(),
        )

        return self.location_in_new_path(location, check=check)

    def remove(self, location, app_name=None):
        location = os.path.normcase(os.path.realpath(
            os.path.expanduser(location.strip(';:'))))
        new_path = self._get_new_path()

        paths = new_path.split(os.pathsep)
        if location in paths:
            paths.remove(location)
            new_path = os.pathsep.join(paths)

            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Environment', 0, winreg.KEY_WRITE) as key:
                winreg.SetValueEx(
                    key, 'PATH', 0, winreg.REG_EXPAND_SZ, new_path)

            # Notifica a las aplicaciones sobre el cambio en las variables de entorno
            ctypes.windll.user32.SendMessageTimeoutW(
                0xFFFF,  # HWND_BROADCAST
                0x1A,  # WM_SETTINGCHANGE
                0,  # must be NULL
                'Environment',
                0x0002,  # SMTO_ABORTIFHUNG
                5000,  # milliseconds
                ctypes.wintypes.DWORD(),
            )

            return not self.path_exists(location)
        else:
            print(f"{location} no está en el PATH.")
            return False

    def need_shell_restart(self, location):
        return not self.location_in_new_path(location) and self.location_in_new_path(location)
