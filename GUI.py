import numpy
import os
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#creating a grid of 100x100 cells
frame = numpy.zeros((100, 100), dtype=int)
# Get the middle of the grid
center_x, center_y = frame.shape[0] // 2, frame.shape[1] // 2
# Add an initial pattern (Gosper Glider Gun)
frame[5, 1] = frame[5, 2] = 1
frame[6, 1] = frame[6, 2] = 1
frame[5, 11] = frame[6, 11] = frame[7, 11] = 1
frame[4, 12] = frame[8, 12] = 1
frame[3, 13] = frame[9, 13] = 1
frame[3, 14] = frame[9, 14] = 1
frame[6, 15] = 1
frame[4, 16] = frame[8, 16] = 1
frame[5, 17] = frame[6, 17] = frame[7, 17] = 1
frame[6, 18] = 1
frame[3, 21] = frame[4, 21] = frame[5, 21] = 1
frame[3, 22] = frame[4, 22] = frame[5, 22] = 1
frame[2, 23] = frame[6, 23] = 1
frame[1, 25] = frame[2, 25] = frame[6, 25] = frame[7, 25] = 1
frame[3, 35] = frame[4, 35] = 1
frame[3, 36] = frame[4, 36] = 1 


# Starting from the center (adjusted to be near the middle)
''' frame[center_x - 1, center_y] = frame[center_x, center_y] = 1
frame[center_x - 2, center_y] = frame[center_x - 2, center_y + 1] = 1
frame[center_x - 1, center_y + 2] = 1 '''


''' # 6. **Breeder**
frame[center_x - 2, center_y - 2] = frame[center_x - 1, center_y - 2] = frame[center_x, center_y - 2] = 1
frame[center_x - 2, center_y - 1] = frame[center_x - 1, center_y - 1] = frame[center_x, center_y - 1] = 1
frame[center_x - 2, center_y] = frame[center_x - 1, center_y] = frame[center_x, center_y] = 1
 '''


def compute_number_neighbors(paded_frame, index_line, index_column):
    
    # Define the neighborhood of the current cell (a 3x3 grid around it)
    neighborhood = paded_frame[index_line - 1:index_line + 2, index_column - 1:index_column + 2]

    # Sum all values in the 3x3 neighborhood and subtract the value of the current cell itself
    sum_of_neighbors = numpy.sum(neighborhood) - paded_frame[index_line, index_column]

    return sum_of_neighbors


def compute_next_frame(frame):
    
    paded_frame = numpy.pad(frame, 1, mode="constant") # je vous offre le code pour le zéro padding c'est cadeau !
    
    # Get the dimensions of the frame
    number_of_lines, number_of_columns = frame.shape

    # Iterate over each line in the frame
    for index_line in range(1, number_of_lines + 1):

        # Iterate over each column in the frame
        for index_column in range(1, number_of_columns + 1):

            # If the cell is dead and has exactly 3 neighbors, it becomes alive
            if paded_frame[index_line, index_column] == 0 and compute_number_neighbors(paded_frame, index_line, index_column) == 3:
                frame[index_line - 1, index_column - 1] = 1

            # If the cell is alive and does not have 2 or 3 neighbors, it dies
            elif paded_frame[index_line, index_column] == 1 and compute_number_neighbors(paded_frame, index_line, index_column) not in [2, 3]:
                frame[index_line - 1, index_column - 1] = 0

    return frame


def update(frame_num, img, frame):
    # Update the frame with the next state
    
    frame[0][:] = compute_next_frame(frame[0])
    # Set the new data for the image
    
    img.set_data(frame[0])
    # Return the updated image object
    
    return img,


# Set up the figure and animation
fig, ax = plt.subplots()
img = ax.imshow(frame, cmap="binary", interpolation="nearest")
ax.axis("off")
ani = animation.FuncAnimation(fig, update, fargs=(img, [frame]), interval=10)

plt.show()