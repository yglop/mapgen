def get_neighbors(grid_size, tile_id):
    neighbors = set()
    #   @@@@
    #   @//@
    #   @//@
    #   @@@@
    if (
            (tile_id[0] > 0 and tile_id[0] < grid_size) and
            (tile_id[1] > 0 and tile_id[1] < grid_size)
        ):
        neighbors = (
            (tile_id[0]+1, tile_id[1]+0), 
            (tile_id[0]+0, tile_id[1]+1), 
            (tile_id[0]-1, tile_id[1]+0), 
            (tile_id[0]+0, tile_id[1]-1), 
        )
    #   @//@
    #   @@@@
    #   @@@@
    #   @@@@
    elif (
            (tile_id[0] == 0) and
            (tile_id[1] > 0 and tile_id[1] < grid_size)
        ):
        neighbors = (
            (tile_id[0]+1, tile_id[1]+0), 
            (tile_id[0]+0, tile_id[1]+1), 
            (tile_id[0]+0, tile_id[1]-1),
        )
    #   @@@@
    #   @@@@
    #   @@@@
    #   @//@
    elif (
            (tile_id[0] == grid_size) and
            (tile_id[1] > 0 and tile_id[1] < grid_size)
        ):
        neighbors = (
            (tile_id[0]-1, tile_id[1]+0), 
            (tile_id[0]+0, tile_id[1]+1), 
            (tile_id[0]+0, tile_id[1]-1),
        )
    #   @@@@
    #   @@@/
    #   @@@/
    #   @@@@
    elif (
            (tile_id[0] > 0 and tile_id[0] < grid_size) and
            (tile_id[1] == grid_size)
        ):
        neighbors = (
            (tile_id[0]+1, tile_id[1]+0), 
            (tile_id[0]-1, tile_id[1]+0), 
            (tile_id[0]+0, tile_id[1]-1),
        )
    #   @@@@
    #   /@@@
    #   /@@@
    #   @@@@
    elif (
            (tile_id[0] > 0 and tile_id[0] < grid_size) and
            (tile_id[1] == 0)
        ):
        neighbors = (
            (tile_id[0]+1, tile_id[1]+0), 
            (tile_id[0]-1, tile_id[1]+0), 
            (tile_id[0]+0, tile_id[1]+1),
        )
    #   /@@@
    #   @@@@
    #   @@@@
    #   @@@@
    elif (
            (tile_id[0] == 0) and
            (tile_id[1] == 0)
        ):
        neighbors = (
            (tile_id[0]+1, tile_id[1]+0), 
            (tile_id[0]+0, tile_id[1]+1), 
        )
    #   @@@/
    #   @@@@
    #   @@@@
    #   @@@@
    elif (
            (tile_id[0] == 0) and
            (tile_id[1] == grid_size)
        ):
        neighbors = (
            (tile_id[0]+1, tile_id[1]+0), 
            (tile_id[0]+0, tile_id[1]-1), 
        )
    #   @@@@
    #   @@@@
    #   @@@@
    #   /@@@
    elif (
            (tile_id[0] == grid_size) and
            (tile_id[1] == 0)
        ):
        neighbors = (
            (tile_id[0]-1, tile_id[1]+0), 
            (tile_id[0]+0, tile_id[1]+1), 
        )
    #   @@@@
    #   @@@@
    #   @@@@
    #   @@@/
    elif (
            (tile_id[0] == grid_size) and
            (tile_id[1] == grid_size)
        ):
        neighbors = (
            (tile_id[0]-1, tile_id[1]-0), 
            (tile_id[0]-0, tile_id[1]-1), 
        )
        
    return neighbors