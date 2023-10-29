# filename: robot_animation.py

import time

def robot_animation():
    frames = [
        r"   __",
        r"o-''|\_____/)",
        r" \_/|_)     )",
        r"    \  __  /",
        r"    (_/ (_/"
    ]

    while True:
        for frame in frames:
            print(frame)
            time.sleep(0.5)
            # Clear the console screen
            print("\033c", end="")

robot_animation()