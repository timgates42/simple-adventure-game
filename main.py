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

    the cave has three only one exit and that is north
    """)

def waterfall():
    print("""You are up at the top of a mountain and you see a huge waterfall 

    you can walk back (west) or you can walk to the waterfall (east)
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
    else:
        print("Sorry I don't understand.")
    
    
    
