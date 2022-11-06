import time

def print_message(status: str, message: str):
    print("[{0}][{1}]".format(time.strftime("%H:%M:%S", time.localtime()),
            status).ljust(20, " ") + " {}".format(message))
