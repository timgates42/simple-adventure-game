def dark_tunnel():
    print("""You are in a dark tunnel.

    Exits are: north
    """)

def the_field():
    print("""You are in a green field.

    Exits are: south, east
    """)

room = dark_tunnel
show_room = True
finished = False
while not finished:
    if show_room:
        room()
        show_room = False
    command = input("# ")
    if command == "north":
        room = the_field
        show_room = True
    else:
        print("Sorry I don't understand.")