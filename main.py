import numpy
import os
import time
frame = numpy.array([[0, 0, 0, 0, 0, 0, 0],
					[0, 1, 1, 1, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 1, 1, 1, 0],
					[0, 0, 0, 0, 0, 0, 0]])

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


while True:
    # boucle infini qui affiche toutes les frames successives (ctrl + c pour arrêter le script)
    print(frame)
    time.sleep(0.2)
    os.system("cls")
    frame = compute_next_frame(frame)