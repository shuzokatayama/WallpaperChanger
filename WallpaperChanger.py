import ctypes

def main():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\shuzo\\Pictures\\Camera Roll\\New Desktop Backgrounds\\Green Hoes Background.png" , 0)

if __name__ == "__main__":
    main()