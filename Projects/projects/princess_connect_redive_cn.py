import os
import sys
import json
import time
import random
import datetime
import subprocess

sys.path.append("\\".join(sys.path[0].split("\\")[:1]))
from libs.project import Project
from libs.mission import Mission
from libs.coordinate import Coordinate

from libs.common import print_message

class PrincessConnectRedive(Project):
    def __init__(self, name="PrincessConnectRedive", country="Cn"):
        super().__init__(name, country)
        # Define package name.
        self.package_name = "com.bilibili.priconne"
        self.activity_name = "com.bilibili.permission.PermissionActivity"

    def __start(self):
        # adb shell am start -n [package]/[activity]
        start_cmd = "{0} shell am start -n {1}".format(self.adb_path, self.package_name)
        obj = subprocess.Popen(start_cmd,
                        shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
        print_message("Success", "[Connect] " + start_cmd)
        time.sleep(15)

    def __finish(self):
        # Start adb server.
        while True:
            finish_cmd = "taskkill /f /im adb.exe"
            # print_message("[Connect] " + finish_cmd)
            obj = subprocess.Popen(finish_cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            finish_cmd = self.adb_path + " kill-server"
            # print_message("[Connect] " + finish_cmd)
            obj = subprocess.Popen(finish_cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
            # Print return data (chinese -> gbk)
            try:
                return_data = stdout.decode('utf-8').splitlines()
            except:
                return_data = stdout.decode('gbk').splitlines()
            # print_message(str(return_data))
            if return_data != []:
                break
            else:
                print_message("Error", "Please check adb")
                time.sleep(3)

    def __coordinate_turn(self, dict):
        for dk in dict.keys():
            dict[dk]["x"] = round(int(dict[dk]["x"]) / self.resolution[0], 4)
            dict[dk]["y"] = round(int(dict[dk]["y"]) / self.resolution[1], 4)
        return dict

    def __mission_receive_energy(self):
        mission_mode = "random_mission"
        if not self.config_ext:
            # Initialization step information.
            step = ["home_button", "receive_button", "blank_button"]
            mission = Mission("receive_energy", step)
            self.missions[mission_mode].append(mission)

        # If the configuration file does not exist, initialize the configuration file.
        if not self.coordinate_ext:
            # Initialize coordinate information.
            crd = {}
            crd["home_button"] = Coordinate("click", 830, 685, 20, 15, 5).get_coordinate_dict()
            crd["receive_button"] = Coordinate("click", 1200, 565, 5, 5, 3,).get_coordinate_dict()
            crd["blank_button"] = Coordinate("click", 60, 40, 10, 10, 3).get_coordinate_dict()
            crd = self.__coordinate_turn(crd)
            for mission in self.missions[mission_mode]:
                if mission.name == "receive_energy":
                    mission.coordinate = crd

    def __mission_shopping(self):
        mission_mode = "random_mission"
        if not self.config_ext:
            # Initialization step information.
            step = ["main_button", "shop_button", "first_cargo", "second_cargo",
                    "third_cargo", "fourth_cargo", "buy_button", "ok_button",
                    "blank_button"]
            mission = Mission("shopping", step)
            self.missions[mission_mode].append(mission)

        # If the configuration file does not exist, initialize the configuration file.
        if not self.coordinate_ext:
            # Initialize coordinate information.
            crd = {}
            crd["main_button"] = Coordinate("click", 120, 685, 20, 10, 5).get_coordinate_dict()
            crd["shop_button"] = Coordinate("click", 820, 575, 10, 10, 5).get_coordinate_dict()
            crd["first_cargo"] = Coordinate("click", 515, 200, 5, 5, 1).get_coordinate_dict()
            crd["second_cargo"] = Coordinate("click", 745, 200, 5, 5, 1).get_coordinate_dict()
            crd["third_cargo"] = Coordinate("click", 970, 200, 5, 5, 1).get_coordinate_dict()
            crd["fourth_cargo"] = Coordinate("click", 1200, 200, 5, 5, 1).get_coordinate_dict()
            crd["buy_button"] = Coordinate("click", 1050, 585, 100, 5, 3).get_coordinate_dict()
            crd["ok_button"] = Coordinate("click", 785, 635, 50, 10, 3).get_coordinate_dict()
            crd["blank_button"] = Coordinate("click", 185, 210, 10, 10, 3).get_coordinate_dict()
            crd = self.__coordinate_turn(crd)
            for mission in self.missions[mission_mode]:
                if mission.name == "shopping":
                    mission.coordinate = crd

    def __mission_guild(self):
        mission_mode = "random_mission"
        if not self.config_ext:
            # Initialization step information.
            step = ["main_button", "guild_button", "blank_button", "friend_button",
                    "like_button", "blank_button"]
            mission = Mission("guild", step)
            self.missions[mission_mode].append(mission)

        # If the configuration file does not exist, initialize the configuration file.
        if not self.coordinate_ext:
            # Initialize coordinate information.
            crd = {}
            crd["main_button"] = Coordinate("click", 120, 685, 20, 15, 5).get_coordinate_dict()
            crd["guild_button"] = Coordinate("click", 920, 575, 5, 5, 5).get_coordinate_dict()
            crd["blank_button"] = Coordinate("click", 60, 140, 10, 10, 3).get_coordinate_dict()
            crd["friend_button"] = Coordinate("click", 315, 465, 15, 5, 5).get_coordinate_dict()
            crd["like_button"] = Coordinate("click", 1100, 420, 10, 5, 3).get_coordinate_dict()
            crd = self.__coordinate_turn(crd)
            for mission in self.missions[mission_mode]:
                if mission.name == "guild":
                    mission.coordinate = crd

    def __mission_gashapon(self):
        mission_mode = "random_mission"
        if not self.config_ext:
            # Initialization step information.
            step = ["gashapon_button", "blank_button", "normal_button", "free_button",
                    "ok_button", "receive_button"]
            mission = Mission("gashapon", step)
            self.missions[mission_mode].append(mission)

        # If the configuration file does not exist, initialize the configuration file.
        if not self.coordinate_ext:
            # Initialize coordinate information.
            crd = {}
            crd["gashapon_button"] = Coordinate("click", 1000, 685, 20, 15, 5).get_coordinate_dict()
            crd["blank_button"] = Coordinate("click", 60, 140, 10, 10, 3).get_coordinate_dict()
            crd["normal_button"] = Coordinate("click", 1195, 100, 10, 5, 5).get_coordinate_dict()
            crd["free_button"] = Coordinate("click", 960, 460, 30, 10, 3).get_coordinate_dict()
            crd["ok_button"] = Coordinate("click", 785, 490, 15, 5, 10).get_coordinate_dict()
            crd["receive_button"] = Coordinate("click", 640, 590, 15, 5, 3).get_coordinate_dict()
            crd = self.__coordinate_turn(crd)
            for mission in self.missions[mission_mode]:
                if mission.name == "gashapon":
                    mission.coordinate = crd

    def __mission_explore(self):
        mission_mode = "random_mission"
        if not self.config_ext:
            # Initialization step information.
            step = ["adventure_button", "explore_button", "exp_button", "level_button",
                    "attack_button", "ok_button", "blank_button", "level_button",
                    "attack_button", "ok_button", "blank_button"]
            mission = Mission("explore", step)
            self.missions[mission_mode].append(mission)

        # If the configuration file does not exist, initialize the configuration file.
        if not self.coordinate_ext:
            # Initialize coordinate information.
            crd = {}
            crd["adventure_button"] = Coordinate("click", 640, 685, 20, 15, 5).get_coordinate_dict()
            crd["explore_button"] = Coordinate("click", 980, 185, 15, 15, 5).get_coordinate_dict()
            crd["exp_button"] = Coordinate("click", 780, 320, 15, 15, 5).get_coordinate_dict()
            crd["level_button"] = Coordinate("click", 960, 200, 20, 10, 5).get_coordinate_dict()
            crd["attack_button"] = Coordinate("click", 1010, 440, 15, 5, 3).get_coordinate_dict()
            crd["ok_button"] = Coordinate("click", 785, 490, 15, 5, 7).get_coordinate_dict()
            crd["blank_button"] = Coordinate("click", 60, 140, 10, 10, 5).get_coordinate_dict()
            crd = self.__coordinate_turn(crd)
            for mission in self.missions[mission_mode]:
                if mission.name == "explore":
                    mission.coordinate = crd

    def __mission_dungeons(self):
        mission_mode = "random_mission"
        if not self.config_ext:
            # Initialization step information.
            step = ["adventure_button", "dungeons_button", "last_extreme_button",
                    "ok_button", "first_enemy", "challenge_button", "my_team_button",
                    "call_button", "attack_button", "next_button", "blank_button",
                    "second_enemy", "challenge_button", "attack_button", "next_button",
                    "blank_button", "third_enemy", "challenge_button", "attack_button",
                    "next_button", "blank_button", "fourth_enemy", "challenge_button",
                    "attack_button", "next_button", "blank_button", "retreat_button",
                    "comfirm_button"]
            mission = Mission("dungeons", step)
            self.missions[mission_mode].append(mission)

        # If the configuration file does not exist, initialize the configuration file.
        if not self.coordinate_ext:
            # Initialize coordinate information.
            crd = {}
            crd["adventure_button"] = Coordinate("click", 640, 685, 20, 15, 5).get_coordinate_dict()
            crd["dungeons_button"] = Coordinate("click", 1170, 185, 15, 15, 5).get_coordinate_dict()
            crd["last_extreme_button"] = Coordinate("click", 1105, 325, 30, 30, 3).get_coordinate_dict()
            crd["ok_button"] = Coordinate("click", 785, 575, 15, 15, 5).get_coordinate_dict()
            crd["first_enemy"] = Coordinate("click", 905, 360, 5, 5, 3).get_coordinate_dict()
            crd["second_enemy"] = Coordinate("click", 635, 345, 5, 5, 3).get_coordinate_dict()
            crd["third_enemy"] = Coordinate("click", 295, 325, 5, 5, 3).get_coordinate_dict()
            crd["fourth_enemy"] = Coordinate("click", 655, 335, 5, 5, 3).get_coordinate_dict()
            crd["challenge_button"] = Coordinate("click", 1120, 610, 15, 10, 5).get_coordinate_dict()
            crd["my_team_button"] = Coordinate("click", 1150, 120, 15, 5, 3).get_coordinate_dict()
            crd["call_button"] = Coordinate("click", 1055, 275, 30, 5, 3).get_coordinate_dict()
            crd["attack_button"] = Coordinate("click", 1115, 605, 15, 10, 35).get_coordinate_dict()
            crd["next_button"] = Coordinate("click", 1110, 655, 30, 5, 5).get_coordinate_dict()
            crd["blank_button"] = Coordinate("click", 60, 140, 10, 10, 7).get_coordinate_dict()
            crd["retreat_button"] = Coordinate("click", 1085, 570, 5, 5, 3).get_coordinate_dict()
            crd["comfirm_button"] = Coordinate("click", 785, 495, 5, 5, 3).get_coordinate_dict()
            crd = self.__coordinate_turn(crd)
            for mission in self.missions[mission_mode]:
                if mission.name == "dungeons":
                    mission.coordinate = crd

    def __mission_arena(self):
        mission_mode = "random_mission"
        if not self.config_ext:
            # Initialization step information.
            step = ["adventure_button", "arena_button", "blank_button", "receive_button",
                    "blank_button", "first_person", "attack_button", "skip_button",
                    "next_button", "blank_button", "blank_button"]
            mission = Mission("arena", step)
            self.missions[mission_mode].append(mission)

        # If the configuration file does not exist, initialize the configuration file.
        if not self.coordinate_ext:
            # Initialize coordinate information.
            crd = {}
            crd["adventure_button"] = Coordinate("click", 640, 685, 20, 15, 5).get_coordinate_dict()
            crd["arena_button"] = Coordinate("click", 775, 540, 50, 20, 5).get_coordinate_dict()
            crd["blank_button"] = Coordinate("click", 60, 140, 10, 10, 3).get_coordinate_dict()
            crd["receive_button"] = Coordinate("click", 395, 455, 10, 10, 3).get_coordinate_dict()
            crd["first_person"] = Coordinate("click", 805, 235, 10, 10, 3).get_coordinate_dict()
            crd["attack_button"] = Coordinate("click", 1115, 600, 30, 10, 7).get_coordinate_dict()
            crd["skip_button"] = Coordinate("click", 1220, 475, 10, 10, 7).get_coordinate_dict()
            crd["next_button"] = Coordinate("click", 1110, 655, 30, 5, 5).get_coordinate_dict()
            crd = self.__coordinate_turn(crd)
            for mission in self.missions[mission_mode]:
                if mission.name == "arena":
                    mission.coordinate = crd

    def __mission_princess_arena(self):
        mission_mode = "finish_mission"
        if not self.config_ext:
            # Initialization step information.
            step = ["adventure_button", "princess_arena_button", "blank_button",
                    "receive_button", "blank_button", "first_person", "next_team_button",
                    "next_team_button", "attack_button", "skip_button", "next_button",
                    "blank_button", "blank_button"]
            mission = Mission("princess_arena", step)
            self.missions[mission_mode].append(mission)

        # If the configuration file does not exist, initialize the configuration file.
        if not self.coordinate_ext:
            # Initialize coordinate information.
            crd = {}
            crd["adventure_button"] = Coordinate("click", 640, 685, 20, 15, 5).get_coordinate_dict()
            crd["princess_button"] = Coordinate("click", 1100, 540, 50, 20, 5).get_coordinate_dict()
            crd["blank_button"] = Coordinate("click", 60, 140, 10, 10, 3).get_coordinate_dict()
            crd["receive_button"] = Coordinate("click", 395, 455, 10, 10, 3).get_coordinate_dict()
            crd["first_person"] = Coordinate("click", 805, 235, 10, 10, 3).get_coordinate_dict()
            crd["team_button"] = Coordinate("click", 1115, 600, 30, 10, 3).get_coordinate_dict()
            crd["attack_button"] = Coordinate("click", 1115, 600, 30, 10, 7).get_coordinate_dict()
            crd["skip_button"] = Coordinate("click", 1220, 475, 10, 10, 10).get_coordinate_dict()
            crd["next_button"] = Coordinate("click", 1075, 655, 30, 10, 5).get_coordinate_dict()
            crd = self.__coordinate_turn(crd)
            for mission in self.missions[mission_mode]:
                if mission.name == "princess_arena":
                    mission.coordinate = crd

    def __mission_complete(self):
        mission_mode = "finish_mission"
        if not self.config_ext:
            # Initialization step information.
            step = ["main_button", "mission_button", "receive_button", "blank_button"]
            mission = Mission("princess_arena", step)
            self.missions[mission_mode].append(mission)

        # If the configuration file does not exist, initialize the configuration file.
        if not self.coordinate_ext:
            # Initialize coordinate information.
            crd = {}
            crd["main_button"] = Coordinate("click", 120, 685, 20, 15, 5).get_coordinate_dict()
            crd["mission_button"] = Coordinate("click", 1115, 575, 10, 10, 5).get_coordinate_dict()
            crd["receive_button"] = Coordinate("click", 1125, 585, 100, 15, 3).get_coordinate_dict()
            crd["blank_button"] = Coordinate("click", 60, 140, 10, 10, 3).get_coordinate_dict()
            crd = self.__coordinate_turn(crd)
            for mission in self.missions[mission_mode]:
                if mission.name == "complete":
                    mission.coordinate = crd

    def __mission_quest(self):
        mission_mode = "finish_mission"
        if not self.config_ext:
            # Initialization step information.
            step = ["adventure_button", "quest_button", "blank_button", "blank_button",
                    "blank_button", "blank_button", "blank_button", "blank_button",
                    "blank_button", "map_button", "first_button", "add_button",
                    "add_button", "sweep_button", "ok_button", "sec_blank_button",
                    "sec_blank_button", "change_button", "add_button", "add_button",
                    "sweep_button", "ok_button", "sec_blank_button", "sec_blank_button",
                    "change_button", "add_button", "add_button", "sweep_button",
                    "ok_button", "sec_blank_button", "sec_blank_button", "change_button",
                    "add_button", "add_button", "sweep_button", "ok_button",
                    "sec_blank_button", "sec_blank_button", "change_button", "add_button",
                    "add_button", "sweep_button", "ok_button", "sec_blank_button",
                    "sec_blank_button", "cancel_button", "boss_button", "challenge_button",
                    "attack_button", "next_button", "next_button", "blank_button",
                    "blank_button", "blank_button", "blank_button", "blank_button",
                    "mission_button", "complete_button"]
            mission = Mission("quest", step)
            self.missions[mission_mode].append(mission)

        # If the configuration file does not exist, initialize the configuration file.
        if not self.coordinate_ext:
            # Initialize coordinate information.
            crd = {}
            crd["adventure_button"] = Coordinate("click", 640, 685, 20, 15, 5).get_coordinate_dict()
            crd["quest_button"] = Coordinate("click", 550, 565, 10, 10, 5).get_coordinate_dict()
            crd["blank_button"] = Coordinate("click", 5, 100, 3, 3, 10).get_coordinate_dict()
            crd["sec_blank_button"] = Coordinate("click", 100, 100, 3, 3, 10).get_coordinate_dict()
            crd["map_button"] = Coordinate("click", 740, 105, 1, 1, 5).get_coordinate_dict()
            crd["first_button"] = Coordinate("click", 120, 425, 5, 5, 3).get_coordinate_dict()
            crd["change_button"] = Coordinate("click", 1240, 330, 1, 1, 3).get_coordinate_dict()
            crd["boss_button"] = Coordinate("click", 1155, 355, 5, 5, 3).get_coordinate_dict()
            crd["add_button"] = Coordinate("click", 1170, 440, 5, 5, 1).get_coordinate_dict()
            crd["sweep_button"] = Coordinate("click", 1010, 445, 3, 3, 3).get_coordinate_dict()
            crd["ok_button"] = Coordinate("click", 785, 495, 3, 3, 5).get_coordinate_dict()
            crd["cancel_button"] = Coordinate("click", 890, 605, 5, 5, 3).get_coordinate_dict()
            crd["challenge_button"] = Coordinate("click", 1120, 620, 5, 5, 3).get_coordinate_dict()
            crd["attack_button"] = Coordinate("click", 1115, 605, 5, 5, 100).get_coordinate_dict()
            crd["next_button"] = Coordinate("click", 1080, 655, 5, 5, 5).get_coordinate_dict()
            crd["mission_button"] = Coordinate("click", 1215, 570, 1, 1, 3).get_coordinate_dict()
            crd["complete_button"] = Coordinate("click", 1125, 585, 5, 5, 1).get_coordinate_dict()
            crd = self.__coordinate_turn(crd)
            for mission in self.missions[mission_mode]:
                if mission.name == "quest":
                    mission.coordinate = crd
        return

    def __del__(self):
        # self.__finish()
        return super().__del__()

    def main_mission(self, adb_path):
        if not self.config_ext or not self.coordinate_ext:
            # Configuration file does not exist, initialize.
            self.__mission_receive_energy()
            self.__mission_gashapon()
            self.__mission_shopping()
            self.__mission_guild()
            self.__mission_explore()
            self.__mission_dungeons()
            self.__mission_arena()
            self.__mission_princess_arena()
            self.__mission_quest()
            self.__mission_complete()

        total_count = self.pass_count + self.fail_count
        start_time = datetime.datetime.now()
        # Run according to the configuration file.
        try:
            for mission_mode in self.missions.keys():
                mission_list = self.missions[mission_mode]
                if mission_mode == "random_mission":
                    random.shuffle(mission_list)
                    for mission in mission_list:
                        mission.adb_path = adb_path
                        mission.run_mission()
            self.pass_count = self.pass_count + 1
            end_time = datetime.datetime.now()
            duration_time = (end_time - start_time).seconds
            self.avg_time = round(((total_count * self.avg_time) + duration_time) / total_count + 1, 2)
        except:
            self.fail_count = self.fail_count + 1
        finally:
            self.rate = round(self.pass_count / (self.pass_count + self.fail_count), 4) * 100
