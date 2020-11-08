"""
The Game of Life is a   cellular automaton   devised by the British mathematician   John Horton Conway   in 1970.
It is the best-known example of a cellular automaton.

Conway's game of life is described here:

A cell   C   is represented by a   1   when alive,   or   0   when dead,   in an   m-by-m   (or m×m)   square array of cells.

We calculate   N   - the sum of live cells in C's   eight-location neighbourhood,   then cell   C   is alive or dead in the next generation based on the following table:

   C   N                 new C
   1   0,1             ->  0  # Lonely
   1   4,5,6,7,8       ->  0  # Overcrowded
   1   2,3             ->  1  # Lives
   0   3               ->  1  # It takes three to give birth!
   0   0,1,2,4,5,6,7,8 ->  0  # Barren
Assume cells beyond the boundary are always dead.

The "game" is actually a zero-player game, meaning that its evolution is determined by its initial state, needing no input from human players.   One interacts with the Game of Life by creating an initial configuration and observing how it evolves.


Task
Although you should test your implementation on more complex examples such as the   glider   in a larger universe,   show the action of the blinker   (three adjoining cells in a row all alive),   over three generations, in a 3 by 3 grid.


"""

import random
import math
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]


class Grid:
    def __init__(self, size=3):
        self.x = size
        self.y = size
        self.grid = [[0 for x in range(self.x)] for y in range(self.y)]
        self.coords = [[(x,y) for x in range(self.x)] for y in range(self.y)]

    def __eq__(self, other):
        return self.grid == other.grid

    def __str__(self):
        return '\n'.join([' '.join([str(x) for x in self.grid[y]]) for y in range(len(self.grid))]) + '\n'


    def set_random_starting_position(self, n=5):
        for i in range(n):
            x = math.floor(random.random() * self.x)
            y = math.floor(random.random() * self.y)
            self.set_val_to_coord(1, (x,y))


    def set_val_to_coord(self, val, coord):
        if self.coord_in_grid(coord):
            x=coord[0]
            y=coord[1]
            self.grid[y][x] = val
        else:
            return

    def get_val_from_coord(self, coord):
        if self.coord_in_grid(coord):
            x = coord[0]
            y = coord[1]
            return self.grid[y][x]

    def get_all_coordinates(self):
        return [item for y in self.coords for item in y]

    def coord_in_grid(self, coord):
        return coord in self.get_all_coordinates()

    def is_neighbour(self, coord1, coord2):
        return abs(coord1[0] - coord2[0]) <= 1 and abs(coord1[1] - coord2[1]) <= 1

    def get_all_neighbours(self, coord):
        return [neighbour for neighbour in self.get_all_coordinates() if self.is_neighbour(coord, neighbour)
                and coord != neighbour
                ]


    def get_score(self, coord):
        return sum([self.get_val_from_coord(neighbour) for neighbour
                    in self.get_all_neighbours(coord)])

    def get_next_state(self, current_state, score):
        """  C   N                 new C
           1   0,1             ->  0  # Lonely
           1   4,5,6,7,8       ->  0  # Overcrowded
           1   2,3             ->  1  # Lives
           0   3               ->  1  # It takes three to give birth!
           0   0,1,2,4,5,6,7,8 ->  0  # Barren"""

        if current_state == 1:
            if score <= 1:
                return 0
            elif score <=3:
                return 1
            else:
                return 0
        else:
            if score == 3:
                return 1
            else:
                return 0


    def next(self):
        for coord in self.get_all_coordinates():
            current_state = self.get_val_from_coord(coord)
            score = self.get_score(coord)
            self.set_val_to_coord(self.get_next_state(current_state, score), coord)

        return self


def next(self, grid, img):
    for coord in grid.get_all_coordinates():
        current_state = grid.get_val_from_coord(coord)
        score = grid.get_score(coord)
        grid.set_val_to_coord(grid.get_next_state(current_state, score), coord)

    img.set_data(grid.grid)
    return grid





def plot_image(grid, update, updateInterval):
    fig, ax = plt.subplots()
    img = ax.imshow(grid.grid, interpolation='nearest')

    ani = animation.FuncAnimation(fig, update, fargs=(grid, img),
                                  frames=10,
                                  interval=updateInterval,
                                  save_count=50)

    plt.show()




def main():

    updateInterval = 500

    t2 = Grid(20)
    t2.set_random_starting_position(1000)
    # print(t2)

    plot_image(t2, next, updateInterval)



    # t3 = Grid()
    # t3.set_val_to_coord(1, (0,0))
    # t3.set_val_to_coord(1, (1, 1))
    # print(t3)
    # t3.set_val_to_coord(1, (1, 0))
    # t3.set_val_to_coord(1, (2, 0))
    #
    # print(t3)
    # t3.next()
    # print('\n')
    # print(t3)
    #
    # for i in range(3):
    #     t3.next()
    #     print(t3)





if __name__ =='__main__':
    main()


