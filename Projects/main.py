from projects import princess_connect_redive_cn

def main():
    pcr_cn = princess_connect_redive_cn.PrincessConnectRedive()
    pcr_cn.adb_path = "F:\\LDPlayer\\LDPlayer4.0\\adb.exe"
    pcr_cn.main_mission()

if __name__ == "__main__":
    main()