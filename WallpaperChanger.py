import ctypes
import datetime
import random

def changeCommand(fileName):
    # Takes filename as input and executes ctypes.windll.user32.SystemParametersInfoW
    # Use string format()

    folderPath = "C:\\Users\\shuzo\\Pictures\\Camera Roll\\Wide Desktop\\{f}"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, folderPath.format(f = fileName) , 0)


def main():
    # 2 screen mode
    # I want my background to change after 4:00 and 19:00
    time = datetime.datetime.now()
    hour = time.hour
    day = time.today().weekday()

    # Weekend Wallpaper
    if day==5 or day==6:
        changeCommand("Weekend.png")

    # Monday, Wednesday, Friday, CHF10
    elif day == 0 or day == 2 or day == 4:
        # Between 4:00 and 19:00, morning wallpaper
        if hour >= 4 and hour < 19:
            changeCommand("CHF10Series3.png")
        # After 19:00 and before 4:00, evening wallpaper
        else:
           
            changeCommand("Weekend.png")

    # Tuesday, Thursday, CHF20
    else:
        # Between 4:00 and 19:00, morning wallpaper
        if hour >= 4 and hour < 19:
            changeCommand("Quack20CHF.png")
        # After 19:00 and before 4:00, evening wallpaper
        else:
            changeCommand("Weekend.png")

if __name__ == "__main__":
    main()