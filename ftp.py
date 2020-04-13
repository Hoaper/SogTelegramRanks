from ftplib import FTP
import render
from config import host, user, pswd

class FtpControl:
    def __init__(self, host, user, password):
        self.ftp = FTP(host=host, user=user, passwd=password)

    def quit(self):
        self.ftp.quit()

    def edit(self, steam, rank, color):
        self.ftp.cwd('addons/sourcemod/configs/')
        try:
            with open('custom-chatcolors.cfg', 'wb') as f:
                self.ftp.retrbinary('RETR ' + 'custom-chatcolors.cfg', f.write)
            if render.save(steam, rank, color):
                if self.upload():
                    return True
        except Exception:
            return False
    def upload(self):
        try:
            with open('/home/guest/Рабочий стол/python/python/Bots/Telegram/Rank Prefixes/custom-chatcolors.cfg',
                      'rb') as file:
                if self.ftp.pwd() == 'addons/sourcemod/configs':
                    self.ftp.cwd('addons/sourcemod/configs')
                self.ftp.storbinary('STOR ' + 'custom-chatcolors.cfg', file)
            return True
        except Exception:
            return False
