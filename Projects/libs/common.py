#-*- encoding: utf-8 -*-
#!/usr/bin/pixiv_venv python3.7
"""
[File]      : mission.py
[Time]      : 2022/10/31 06:18:00
[Author]    : InaKyui
[License]   : (C)Copyright 2022, InaKyui
[Version]   : 1.3
[Descption] : Public methods.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 1.3"


import os
import time

from functools import wraps

def print_message(status: str, message: str):
    print("[{0}][{1}]".format(time.strftime("%H:%M:%S", time.localtime()),
            status).ljust(20, " ") + " {}".format(message))

def function_log(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print_message("Start", func.__name__)
        ret = func(*args,**kwargs)
        print_message("Finish", func.__name__)
        return ret
    return wrapper
