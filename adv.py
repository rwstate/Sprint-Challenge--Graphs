from room import Room
from player import Player
from world import World
from util import reverse_direction
from util import backtrack

import random
from ast import literal_eval

# import sys

# sys.setrecursionlimit(10 ** 7)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']


traversal_path = []
rooms = {}
while len(rooms) < len(room_graph):
    # get id of current room
    current = player.current_room.id
    # print(current, traversal_path)

    # initialize graph entry if room not visited before
    if current not in rooms:
        exits = player.current_room.get_exits()
        rooms[current] = {}
        for exit1 in exits:
            rooms[current][exit1] = "?"
        rooms[current]["backtrack"] = -1
    print(len(rooms), len(room_graph), player.current_room.id, rooms[player.current_room.id])
    exits = [i for i in rooms[current]]
    random.shuffle(exits)
    # iterate over exits
    for exit1 in exits:

        # check if exit is known and skip to next exit if it is
        if rooms[current][exit1] != "?":
            continue

        # take the exit, add it to the traversal path and record the connection between the rooms
        traversal_path.append(exit1)
        player.travel(exit1)
        dest = player.current_room.id
        rooms[current][exit1] = dest

        if dest not in rooms:
            exits = player.current_room.get_exits()
            rooms[dest] = {}
            for exit2 in exits:
                rooms[dest][exit2] = "?"
            reverse = reverse_direction(exit1)
            rooms[dest][reverse] = current
            rooms[dest]['backtrack'] = reverse
        
        reverse = reverse_direction(exit1)
        rooms[dest][reverse] = current
        break

    # check if player has moved. if not, there were no unknown exits and we need to backtrack
    if current == player.current_room.id:
        # print(rooms[current])
        # print(current, "dead end")
        back_path = backtrack(current, rooms, traversal_path)
        # print(back_path, "backtrack")
        for direction in back_path:
            player.travel(direction)
            traversal_path.append(direction)
            
print(f"explored {len(rooms)} rooms in {len(traversal_path)} moves")

      




    

# print(rooms)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
