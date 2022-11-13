#-*- encoding: utf-8 -*-
#!/usr/bin/pixiv_venv python3.7
"""
[File]      : main.py
[Time]      : 2022/10/31 06:18:00
[Author]    : InaKyui
[License]   : (C)Copyright 2022, InaKyui
[Version]   : 1.3
[Descption] : Entrance.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 1.3"


from projects import princess_connect_redive_cn

def main():
    pcr_cn = princess_connect_redive_cn.PrincessConnectRedive()
    pcr_cn.main_mission("F:\\LDPlayer\\LDPlayer4.0\\adb.exe")

if __name__ == "__main__":
    main()