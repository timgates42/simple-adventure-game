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

   there is a pathway heading up the mountain east and west
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
    else:
        print("Sorry I don't understand.")
    
    
    
