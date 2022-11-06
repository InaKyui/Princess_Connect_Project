#-*- encoding: utf-8 -*-
#!/usr/bin/pixiv_venv python3.7
"""
[File]      : coordinate.py
[Time]      : 2022/10/26 00:11:56
[Author]    : InaKyui
[License]   : (C)Copyright 2022, InaKyui
[Version]   : 1.0
[Descption] : Descption.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 1.0"

import os
import sys
import json
import time

class Coordinate:
    """Sum data.

    Attributes:
        name - project name.
        country - country of the project.
    """

    def __init__(self, action, x, y, error_x, error_y, idle, resolution_x=1280, resolution_y=720):
        # Basic information.
        self.x = x
        self.y = y
        self.error_x = error_x
        self.error_y = error_y
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y
        self.idle = idle
        self.action = action

    def get_coordinate_dict(self):
        return self.__dict__