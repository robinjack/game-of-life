from main import *





def test_Grid():

    g = Grid()

    assert len(g.grid) == 3
    assert len(g.grid[0]) == 3
    t = Grid(1)
    assert t.coords == [[(0,0)]]
    t2 = Grid(2)
    assert t2.coords == [[(0,0), (1,0)],
                         [(0, 1), (1, 1)],
                         ]

def test_set_val_to_coord():
    g = Grid()
    val= 1
    coord=(0,0)
    g.set_val_to_coord(val=val, coord=coord)

    assert g.grid[0][0]==1

def test_get_val_from_coord():
    g = Grid()
    val = 1
    coord = (0, 0)

    assert g.get_val_from_coord((0, 0)) == 0
    g.set_val_to_coord(val=val, coord=coord)
    assert g.get_val_from_coord(coord)==val

# get all coordinates

def test_get_all_coordinates():
    g=Grid()

    assert set(g.get_all_coordinates()) == set([(0,0), (1,0), (2,0),
                                       (0,1), (1,1), (1,2),
                                       (0,2), (2,1), (2,2)])
#
#
def test_coord_in_grid():
    g = Grid()
    test_coord = (-1,0)
    assert not g.coord_in_grid(test_coord)
#
def test_get_all_neighbours():
    g = Grid()
    assert set(g.get_all_neighbours((0,0))) == {(0,1), (1,0), (1,1)}
    assert set(g.get_all_neighbours((1, 1))) == {(0, 0), (0, 1), (0, 2), (1,0), (1,2), (2,0), (2,1), (2,0), (2,2)}
#
#
def test_get_score():

    results = {(0,0): 3, (0,1): 5, (0,2): 3,
               (1,0): 5, (1,1): 8, (1,2): 5,
               (2, 0): 3, (2, 1): 5, (2, 2): 3,
               }
    g= Grid()
    for coord in g.get_all_coordinates():
        g.set_val_to_coord(1, coord)

    for coord in g.get_all_coordinates():
        assert results[coord] == g.get_score(coord)
#
#
def test_get_next_state():

    """  C   N                 new C
   1   0,1             ->  0  # Lonely
   1   4,5,6,7,8       ->  0  # Overcrowded
   1   2,3             ->  1  # Lives
   0   3               ->  1  # It takes three to give birth!
   0   0,1,2,4,5,6,7,8 ->  0  # Barren"""

    g = Grid()
    for coord in g.get_all_coordinates():
        g.set_val_to_coord(1, coord)

    assert g.get_next_state(0, 0) == 0
    assert g.get_next_state(1, 5) == 0
    assert g.get_next_state(1, 2) == 1
    assert g.get_next_state(0, 3) == 1
    assert g.get_next_state(0, 4) == 0
#
#
#
#
#
def test_next():
    g = Grid(size=4)

    for coord in [(1, 1), (1, 2), (2, 2,), (2, 1)]:
        g.set_val_to_coord(1, coord)

    assert g == g.next()

def test_set_random_starting_position():
    g= Grid()
    g.set_random_starting_position()
    num_vals_set = sum([sum(x) for x in g.grid])

    assert num_vals_set <= 5 and num_vals_set >=1







    #determine if square is in the grid

    # retrieve coordinates around square, that are in the grid

    # sum squares in grid


    # calculate next value










    #



