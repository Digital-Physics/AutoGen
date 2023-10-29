import time

# Define the frames for the robot animation
frames = [
    """
       .-""""""-.
     .'          '.
    /   O      O   \\
   :           `    :
   |                |   
   :    .------.    :
    \  '        '  /
     '.          .'
       '-......-'
    """,
    """
       .-""""""-.
     .'          '.
    /   O      O   \\
   :           `    :
   |                |   
   :    .------.    :
    \  '        '  /
     '.          .'
       '-......-'
    """,
    """
       .-""""""-.
     .'          '.
    /   O      O   \\
   :           `    :
   |                |   
   :    .------.    :
    \  '        '  /
     '.          .'
       '-......-'
    """
]

# Print the frames of the robot animation
for frame in frames:
    print(frame)
    time.sleep(0.5)