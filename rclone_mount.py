"""
A script for mounting rclone drives on Windows and keeping terminal window hidden.

Make sure python is installed and default app to open .py files is python.
Change the drives dict below to your preference.

In order to run this script on every boot:
1) Press Win + R
2) Type shell:startup, click OK
3) Paste the rclone_mount.py into the Startup folder

29.06.2024
"""

drives = \
{
#   "Drive Name"   : "Mount Path or Drive Letter"
    "Google Drive" : "G:",
    "One Drive"    : "O:"
}

import subprocess
from os import system
from time import sleep

def cmd_no_print(command):
    return subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode

def net_is_connected():
    ping_list = ["google.com", "microsoft.com", "cloudflare.com", "amazon.com"]
    
    ping_error  = 0
    for adress in ping_list:
        ping_error += cmd_no_print(f"ping -n 1 {adress}")

    if ping_error == len(ping_list):
        return 0
    else:
        return 1

def mount_rclone(drives):
    for drive_name, mount_location in drives.items():
        system(f"start conhost.exe powershell /c \"rclone.exe mount '{drive_name}:' '{mount_location}'\" --no-console")


while not net_is_connected():
    sleep(10)

mount_rclone(drives)