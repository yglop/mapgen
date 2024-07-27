import random
import numpy as np

from rooms import *
from get_neighbors import get_neighbors


class mapgen():
    def __init__(self, size=8, rooms_n=10):
        self.SIZE = size
        self.ROOMS_N = rooms_n

        self.ROOM_SIZE = 11
        self.MAP_SIZE = self.SIZE * self.ROOM_SIZE

        self.pre_map = np.full((self.SIZE, self.SIZE), fill_value=0, order="F")
        self.str_map = np.full((self.MAP_SIZE, self.MAP_SIZE), fill_value='#', order="F")

        ###
        self.gen_pre_map()
        # self.pre_map = np.array([ # DEBUG
        #     [2, 2, 0, 0, 2, 0, 2, 2],
        #     [0, 2, 2, 2, 2, 2, 2, 0],
        #     [0, 0, 0, 2, 2, 0, 0, 0],
        #     [2, 2, 2, 2, 2, 2, 2, 2],
        #     [0, 0, 2, 0, 2, 0, 0, 0],
        #     [0, 0, 0, 0, 2, 0, 0, 0],
        #     [2, 2, 2, 2, 2, 2, 2, 2],
        #     [2, 0, 2, 0, 2, 0, 0, 2],
        # ])

        self.gen_str_map()

    def gen_pre_map(self):
        tile = [random.randint(1, self.SIZE-2), random.randint(1, self.SIZE-2)]
        self.pre_map[tile[0], tile[1]] = 1

        tiles_id = [tile]

        new_tile = tile
        for i in range(self.ROOMS_N):  
            neighbors = [i for i in get_neighbors(self.SIZE-1, (tile[0], tile[1]))]
            while self.pre_map[new_tile[0], new_tile[1]] != 0:
                if len(neighbors) <= 0:
                    if len(tiles_id) <= 1:
                        break
                    tiles_id = tiles_id[:-1]
                    tile = tiles_id[-1]
                    neighbors = [i for i in get_neighbors(self.SIZE-1, (tile[0], tile[1]))]

                new_tile = random.choice(neighbors)
                neighbors.remove(new_tile)

            self.pre_map[new_tile[0], new_tile[1]] = 2
            tile = new_tile
            tiles_id.append(tile)

    ###----------------------------------------------###
    def choice_room(self, room_id):
        neighbors = get_neighbors(self.SIZE-1, (room_id[0], room_id[1]))
        not_empty_tiles = 0

        for i in neighbors:
            if self.pre_map[i] != 0:
                not_empty_tiles += 1

        x = room_id[0]
        y = room_id[1]

        if not_empty_tiles == 4:
            return random.choice(rooms4x)

        if not_empty_tiles == 3:
            if (x == self.SIZE-1) or (x < self.SIZE-1 and self.pre_map[x+1, y] == 0):
                return random.choice(rooms3x_dw)

            if (y == self.SIZE-1) or (y < self.SIZE-1 and self.pre_map[x, y+1] == 0):
                return random.choice(rooms3x_rg)

            if (x == 0) or (x > 0 and self.pre_map[x-1, y] == 0):
                return random.choice(rooms3x_up)

            if (y == 0) or (y > 0 and self.pre_map[x, y-1] == 0):
                return random.choice(rooms3x_lf)

        if not_empty_tiles == 2:
            if x == 0:
                if y == 0:
                    return random.choice(rooms2x_dr)
                elif y == self.SIZE-1:
                    return random.choice(rooms2x_dl)
                else: # 0<y<SIZE
                    if (self.pre_map[x, y+1] != 0) and (self.pre_map[x, y-1] != 0):
                        return random.choice(rooms2x_ho)
                    elif self.pre_map[x, y+1] != 0:
                        return random.choice(rooms2x_dr)
                    return random.choice(rooms2x_dl)
            elif x == self.SIZE-1:
                if y == 0:
                    return random.choice(rooms2x_ur)
                elif y == self.SIZE-1:
                    return random.choice(rooms2x_ul)
                else: # 0<y<SIZE
                    if (self.pre_map[x, y+1] != 0) and (self.pre_map[x, y-1] != 0):
                        return random.choice(rooms2x_ho)
                    elif self.pre_map[x, y+1] != 0:
                        return random.choice(rooms2x_ur)
                    return random.choice(rooms2x_ul)
            else: # 0<x<SIZE
                if y == 0:
                    if self.pre_map[x+1, y] != 0:
                        if self.pre_map[x-1, y] != 0:
                            return random.choice(rooms2x_ve)
                        return random.choice(rooms2x_dr) 
                    return random.choice(rooms2x_ur)
                elif y == self.SIZE-1:
                    if self.pre_map[x+1, y] != 0:
                        if self.pre_map[x-1, y] != 0:
                            return random.choice(rooms2x_ve)
                        return random.choice(rooms2x_dl)
                    return random.choice(rooms2x_ul)
                else: # 0<y<SIZE
                    if (self.pre_map[x, y+1] != 0) and (self.pre_map[x, y-1] != 0):
                        return random.choice(rooms2x_ho)
                    if (self.pre_map[x+1, y] != 0) and (self.pre_map[x-1, y] != 0):
                        return random.choice(rooms2x_ve)
                    if self.pre_map[x+1, y] != 0:
                        if self.pre_map[x, y+1] != 0:
                            return random.choice(rooms2x_dr)
                        return random.choice(rooms2x_dl)
                    if self.pre_map[x-1, y] != 0:
                        if self.pre_map[x, y+1] != 0:
                            return random.choice(rooms2x_ur)
                        return random.choice(rooms2x_ul)

        if not_empty_tiles == 1:
            if (x < self.SIZE-1 and self.pre_map[x+1, y] != 0):
                return random.choice(rooms1x_d)

            if (y < self.SIZE-1 and self.pre_map[x, y+1] != 0):
                return random.choice(rooms1x_r)

            if (x > 0 and self.pre_map[x-1, y] != 0):
                return random.choice(rooms1x_u)

            if (y > 0 and self.pre_map[x, y-1] != 0):
                return random.choice(rooms1x_l)

        print(not_empty_tiles, (x, y))
        return room_empty

    def add_room(self, room_id, room):
        room_id_upleft = (room_id[0]*self.ROOM_SIZE, room_id[1]*self.ROOM_SIZE)

        self.str_map[
            room_id_upleft[0]:room_id_upleft[0]+self.ROOM_SIZE,
            room_id_upleft[1]:room_id_upleft[1]+self.ROOM_SIZE
            ] = room

    def gen_str_map(self):
        for row in range(self.SIZE):
            for col in range(self.SIZE):
                if self.pre_map[row][col] == 2:
                    room = self.choice_room((row, col))
                    self.add_room((row, col), room)
                elif self.pre_map[row][col] == 1:
                    self.add_room((row, col), room_start)

    ###-----------------------------------------------###
    def write_pre_map(self):
        with open('./txtmaps/pre_map.txt', 'w') as file_pre_map:
            for row in self.pre_map:
                print(*row, file=file_pre_map)

    def write_str_map(self):
        with open('./txtmaps/str_map.txt', 'w') as file_str_map:
            for row in self.str_map:
                print(*row, file=file_str_map)


# mg = mapgen() # DEBUG
# mg.write_pre_map()
# mg.write_str_map()