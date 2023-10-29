import time

def create_ascii_robot_animation():
    frames = [
        '''
        \\o/
         |
        / \\
        ''',
        '''
         o
        /|\\
        / \\
        ''',
        '''
        \\o/
         |
        / \\
        ''',
        '''
         o
        /|\\
        / \\
        '''
    ]

    while True:
        for frame in frames:
            print(frame)
            time.sleep(0.5)

create_ascii_robot_animation()