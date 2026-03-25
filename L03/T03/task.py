# Exercise!
# Display the image below to the right hand side where the 0 is going to be ' ',
# and the 1 is going to be '*'.
# Print '|' at the beginning and end of each row to make the spaces visible.

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]


for image in picture:
    print('|', end="")
    for pixel in image:
      if pixel:
        print('*', end="")
      else:
        print(' ', end="")
    print('|')