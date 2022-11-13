#-*- encoding: utf-8 -*-
#!/usr/bin/pixiv_venv python3.7
"""
[File]      : project.py
[Time]      : 2022/10/31 06:18:00
[Author]    : InaKyui
[License]   : (C)Copyright 2022, InaKyui
[Version]   : 1.3
[Descption] : Class project.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 1.3"


import os
import sys
import json
import time

from libs.common import function_log
from libs.common import print_message
from libs.mission import Mission

class Project:
    """Sum data.

    Attributes:
        name - project name.
        country - country of the project.
    """

    def __init__(self, name:str, country:str):
        # Recode basic information.
        self.name = name
        self.country = country
        self.resolution = [1280,720]
        # File path information.
        self.adb_path = ""
        self.package_name = ""
        self.activity_name = ""
        self.missions = {
            "start_mission": [],
            "random_mission": [],
            "finish_mission": []
        }

        # Recode statistics inforamtion.
        self.pass_count = 0
        self.fail_count = 0
        self.pass_rate = 0
        self.avg_time = 0

        # Recode profile status.
        self.config_ext = False
        self.coordinate_ext = False
        self.config_info = ["name", "country", "resolution",
                            "adb_path", "package_name", "activity_name"]
        self.statis_info = ["pass_count", "fail_count",
                            "pass_rate", "avg_time"]
        self.__lib_path = sys.path[0]

        # Load config & coordinate & statistics.
        self.__load_config()
        self.__load_coordinate()
        self.__load_statistics()

    def __path_exists(self, path:str):
        try:
            if not os.path.exists(path):
                print_message("Fail", "Can't find path: " + path)
                os.mkdir(path)
                print_message("Success", "Create path: " + path)
        except:
            print_message("Error", "Create path: " + path)
            raise FileExistsError

    def __load_config(self):
        """Load config information."""

        config_path = os.path.join(self.__lib_path, "configs", "{0}_{1}.json".format(self.name, self.country))
        if os.path.exists(config_path):
            self.config_ext = True
            with open(config_path, "r") as fr:
                config_content = fr.read()
            config_dict = json.loads(config_content)
            for sci in self.config_info:
                self.__dict__[sci] = config_dict[sci]

            # Converting mission dictionaries to classes.
            for mission_mode in config_dict["missions"].keys():
                for mission_dict in config_dict["missions"][mission_mode]:
                    mission = Mission(mission_dict["name"], mission_dict["steps"])
                    mission.adb_path = self.adb_path
                    self.missions[mission_mode].append(mission)

            print_message("Success", "[{}] Config information loaded!".format(self.name))
        else:
            print_message("Warning", "[{}] Config information lost!".format(self.name))

    def __save_config(self):
        """Save config information."""

        self.__path_exists(os.path.join(self.__lib_path, "configs"))
        config_path = os.path.join(self.__lib_path, "configs", "{0}_{1}.json".format(self.name, self.country))
        with open(config_path, "wt", encoding="utf-8") as fw:
            json_dict = {}
            for sci in self.config_info:
                json_dict[sci] = self.__dict__[sci]
            json_dict["missions"] = {}

            for mission_mode in self.missions.keys():
                mission_list = []
                for mission in self.missions[mission_mode]:
                    mission_dict = mission.get_config_dict()
                    mission_list.append(mission_dict)
                json_dict["missions"][mission_mode] = mission_list
            json_str = json.dumps(json_dict, indent=4)
            fw.write(json_str)

        print_message("Success", "[{}] Config information saved!".format(self.name))

    def __load_coordinate(self):
        """Load coordinate information."""

        coordinate_path = os.path.join(self.__lib_path, "coordinates", "{0}_{1}.json".format(self.name, self.country))
        if os.path.exists(coordinate_path):
            self.coordinate_ext = True
            with open(coordinate_path, "r") as fr:
                coordinate_content = fr.read()
            coordinate_dict = json.loads(coordinate_content)
            for mission_mode in self.missions.keys():
                for mission in self.missions[mission_mode]:
                    mission.coordinate = coordinate_dict[mission.name]

            print_message("Success", "[{}] Coordinate information loaded!".format(self.name))
        else:
            print_message("Warning", "[{}] Coordinate information lost!".format(self.name))

    def __save_coordinate(self):
        """Save coordinate information."""

        self.__path_exists(os.path.join(self.__lib_path, "coordinates"))
        coordinate_path = os.path.join(self.__lib_path, "coordinates", "{0}_{1}.json".format(self.name, self.country))
        with open(coordinate_path, "wt", encoding="utf-8") as fw:
            json_dict = {}
            for mission_mode in self.missions.keys():
                for mission in self.missions[mission_mode]:
                    json_dict[mission.name] = mission.coordinate
            json_str = json.dumps(json_dict, indent=4)
            fw.write(json_str)
        print_message("Success", "[{}] Coordinate information saved!".format(self.name))

    def __load_statistics(self):
        """Load statistics information."""

        statistics_path = os.path.join(self.__lib_path, "statistics",
                                       "{0}_{1}.json".format(self.name, self.country))
        if os.path.exists(statistics_path) and self.config_ext:
            with open(statistics_path, "r") as fr:
                statistics_content = fr.read()
            statistics_dict = json.loads(statistics_content)
            for sti in self.statis_info:
                self.__dict__[sti] = statistics_dict[sti]

            for mission_mode in self.missions.keys():
                for mission in self.missions[mission_mode]:
                    for si in self.statis_info:
                        mission.__dict__[si] = statistics_dict["missions"][mission.name][si]

            print_message("Success", "[{}] Statistics information loaded!".format(self.name))
        else:
            print_message("Warning", "[{}] Statistics information lost!".format(self.name))

    def __save_statistics(self):
        """Save statistics information."""

        self.__path_exists(os.path.join(self.__lib_path, "statistics"))
        statistics_path = os.path.join(self.__lib_path, "statistics", "{0}_{1}.json".format(self.name, self.country))
        with open(statistics_path, "wt", encoding="utf-8") as fw:
            json_dict = {}
            for sci in self.statis_info:
                json_dict[sci] = self.__dict__[sci]
            json_dict["missions"] = {}

            for mission_mode in self.missions.keys():
                for mission in self.missions[mission_mode]:
                    mission_dict = mission.get_statistics_dict()
                    json_dict["missions"][mission.name] = mission_dict
            json_str = json.dumps(json_dict, indent=4)
            fw.write(json_str)

        print_message("Success", "[{}] Statistics information saved!".format(self.name))

    def start(self):
        """Start project."""
        return

    def finish(self):
        """Finish project."""
        return

    def main_mission(self):
        """Mission scheduling."""
        return

    def __repr__(self):
        """Print class property."""
        key_length = max(len(key) for key in self.__dict__)
        for key in self.__dict__:
            print("{0}:{1}".format(key.capitalize().ljust(key_length, " "),
                                   self.__dict__[key]))

    def __del__(self):
        """Save information before release."""
        self.__save_config()
        self.__save_coordinate()
        self.__save_statistics()
        return