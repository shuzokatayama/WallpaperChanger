import ctypes
import datetime

def main():
    # I want my background to change after 4:00 and 19:00
    time = datetime.datetime.now()
    hour = time.hour

    # Between 4:00 and 19:00, morning wallpaper
    if hour >= 4 and hour < 19:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\shuzo\\Pictures\\Camera Roll\\New Desktop Backgrounds\\Morning.png" , 0)
    # After 19:00 and before 4:00, evening wallpaper
    else:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\shuzo\\Pictures\\Camera Roll\\New Desktop Backgrounds\\Evening.png" , 0)

if __name__ == "__main__":
    main()