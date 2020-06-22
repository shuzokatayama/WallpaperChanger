import ctypes
import datetime

def main():
    # I want my background to change after 6 AM and 8 PM
    time = datetime.datetime.now()
    hour = time.hour

    # 21:00 : evening wallpaper
    if hour==21:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\shuzo\\Pictures\\Camera Roll\\New Desktop Backgrounds\\Evening.png" , 0)

    # 6:00 : morning wallpaper
    if hour==6:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\shuzo\\Pictures\\Camera Roll\\New Desktop Backgrounds\\Morning.png" , 0)

if __name__ == "__main__":
    main()