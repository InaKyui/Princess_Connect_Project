# python virgo_venv
# -*- encoding: utf-8 -*-
'''
@File    :   mission.py
@Time    :   2022/09/12 22:43:32
@Author  :   Yuisaka
@Version :   1.0
@Contact :   kzyuisaka@outlook.com
'''

import os
import time
import random
import datetime
import subprocess

from libs.common import print_message

class Mission:
    """Mission"""

    def __init__(self, name:str, steps:list=[]):
        # Basic information.
        self.name = name
        self.steps = steps
        # Current result.
        # self.result = None
        # self.error_message = ""
        # Statistics inforamtion.
        self.pass_count = 0
        self.fail_count = 0
        self.pass_rate = 0
        self.avg_time = 0
        # Recode coordinate information.
        self.resolution = [1280, 720]
        self.coordinate = {}

    def __click(self, step):
        # Calculate coordinate.
        x = round(self.coordinate[step]["x"] * self.resolution[0], 0)
        y = round(self.coordinate[step]["y"] * self.resolution[1], 0)
        error_x = self.coordinate[step]["error_x"]
        error_y = self.coordinate[step]["error_y"]
        idle = self.coordinate[step]["idle"]
        # Calculate actual coordinate and idle time.
        actual_x = x + random.randint(-error_x, error_x)
        if actual_x < 0:
            actual_x = 0
        actual_y = y + random.randint(-error_y, error_y)
        if actual_y < 0:
            actual_y = 0
        actual_time = random.randint(idle * 100, idle * 100 + 300)

        # Click.
        click_cmd = "{0} shell input tap {1} {2}".format(
                    self.adb_path, str(actual_x), str(actual_y))
        print_message("Debug", "[{0}][{1}] {2}".format(
                            self.name, step, click_cmd))
        obj = subprocess.Popen(click_cmd, shell=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print_message("Success", "[{0}][{1}] Click ({2}, {3})".format(
                            self.name, step, str(actual_x), str(actual_y)))
        # Idle.
        print_message("Success", "[{0}][{1}] Wait {2} seconds".format(
                           self.name, step, str(actual_time / 100)))
        time.sleep(actual_time / 100)

    def run_mission(self):
        total_count = self.pass_count + self.fail_count
        start_time = datetime.datetime.now()
        try:
            for step in self.steps:
                if self.coordinate[step]["action"] == "click":
                    self.__click(step)
            self.pass_count = self.pass_count + 1
            end_time = datetime.datetime.now()
            duration_time = (end_time - start_time).seconds
            self.avg_time = round(((total_count * self.avg_time) + duration_time) / total_count + 1, 2)
            return True
        except:
            self.fail_count = self.fail_count + 1
            return False
        finally:
            self.rate = round(self.pass_count / (self.pass_count + self.fail_count), 4) * 100

    def get_config_dict(self):
        config_dict = {
            "name": self.name,
            "steps": self.steps
        }
        return config_dict

    def get_statistics_dict(self):
        statistics_dict = {
            "pass_count": self.pass_count,
            "fail_count": self.fail_count,
            "pass_rate": self.pass_rate,
            "avg_time": self.avg_time,
        }
        return statistics_dict

    def __repr__(self):
        """Print class property."""
        key_length = max(len(key) for key in self.__dict__)
        for key in self.__dict__:
            print("{0}:{1}".format(key.capitalize().ljust(key_length, " "),
                                   self.__dict__[key]))

    def __del__(self):
        """"""
        return
