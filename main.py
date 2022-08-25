from operator import truediv


def dark_tunnel():
    print("""You are in a dark tunnel.

    Exits are: north
    """)

def the_field():
    print("""You are in a green field.

    Exits are: south, east
    """)

def bottom_of_mountain():
    print("""you are next to a huge moutain 

   there is a pathway heading up the mountain exits are east and west
    """)

def walking_up_the_mountain():
    print("""You are up walking up the mountain

    there is a cave (north), keep on walking up the mountain (east) or turn back (west)
    """)

def cave():
    print("""You are up walking into a cave and rocks fall behind you 

    the cave has only one exit and that is north
    """)

def waterfall():
    print("""You are up at the top of a mountain and you see a huge waterfall 

    you can walk back (west) or you can walk to the waterfall (east)
    """)

def death():
    print("""you are running step by step until boom the floor colapses and you are launched derectly into a gaint spiders mouth

    should have not run i guess
    """)

def monster_battle():
    print("""You are up walking into a open area you hear a sound, it is behind you

    you can look behind you, or run
    """)

def cave2():
    print("""You are up walking into the waterfall and rocks fall behind you 

    the cave has only one exit and that is north
    """)

def spider():
    print("""You see giant cobwebs about three time your size until you find the producer there is a gigantic spider looking and you hungryly 
    you can fight it or run
    """)

room = dark_tunnel
show_room = True
finished = False
while not finished:
    if show_room:
        room()
        show_room = False
    command = input("# ")
    if command == "north" and room == dark_tunnel:
        room = the_field
        show_room = True
    elif command == "help":
        show_room = True  
    elif command == "south" and room == the_field:
        room = dark_tunnel  
        show_room = True     
    elif command == "east" and room == the_field:
        room = bottom_of_mountain 
        show_room = True  
    elif command == "west" and room == bottom_of_mountain:
        room = the_field
        show_room = True    
    elif command == "east" and room == bottom_of_mountain:
        room = walking_up_the_mountain
        show_room = True  
    elif command == "west" and room == walking_up_the_mountain:
        room = bottom_of_mountain
        show_room = True  
    elif command == "north" and room == walking_up_the_mountain:
        room = cave
        show_room = True  
    elif command == "east" and room == walking_up_the_mountain:
        room = waterfall
        show_room = True  
    elif command == "west" and room == waterfall:
        room = walking_up_the_mountain
        show_room = True 
    elif command == "east" and room == waterfall:
        room = cave2
        show_room = True
    elif command == "north" and room == cave:
        room = monster_battle
        show_room = True
    elif command == "north" and room == cave2:
        room = monster_battle
        show_room = True
    elif command == "run" and room == monster_battle:
        room = death
        show_room = True
    elif command == "look behind me" and room == monster_battle:
        room = spider
        show_room = True
    elif command == "run" and room == spider:
        room = death
        show_room = True
    else:
        print("Sorry I don't understand.")
    
    
    
