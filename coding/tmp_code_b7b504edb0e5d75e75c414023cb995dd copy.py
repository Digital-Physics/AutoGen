import time
from IPython.display import clear_output

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
            clear_output(wait=True)

create_ascii_robot_animation()