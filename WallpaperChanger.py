import ctypes
import datetime

def main():
    # I want my background to change after 6 AM and 8 PM
    time = datetime.datetime.now()
    hour = time.hour

    # 19:00 : evening wallpaper
    if hour==19:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\shuzo\\Pictures\\Camera Roll\\New Desktop Backgrounds\\Evening.png" , 0)

    # 4:00 : morning wallpaper
    if hour==4:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\shuzo\\Pictures\\Camera Roll\\New Desktop Backgrounds\\Morning.png" , 0)

if __name__ == "__main__":
    main()