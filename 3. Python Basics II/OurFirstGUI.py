# Our first GUI

# Display the image below to the right hand side where the 0 is going to be ' ',
# and the 1 is going to be '*'. This will reveal an image!

picture = [
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0]
]

for array in picture:
    for item in array:
        if item:
            print('*', end='')
        else:
            print(' ', end='')
    print()
