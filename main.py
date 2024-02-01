


def travel_rooms(room_data_list):
    # Create a mapping of room names to integers
    room_to_int = {}
    for i, room_data in enumerate(room_data_list):
        room = room_data['Room']
        room_to_int[room] = i

    # Create a reverse mapping of integers to room names
    int_to_room = {}
    for room, i in room_to_int.items():
        int_to_room[i] = room

    # Create an adjacency list using the integer values for rooms and string values for exits
    adjacency_list = []
    for room_data in room_data_list:
        if 'Room' in room_data and 'Exits' in room_data:
            room = room_to_int[room_data['Room']]
            exits = room_data['Exits'].split(', ')
            adjacency_list.append([room] + exits)

    current_room = 'Entrance'  # Start at the entrance
    score = 0  # Initialize score
    while True:
        # Look up the room data using the integer value of the current room
        room_data = room_data_list[room_to_int[current_room]]

        print(f"Room: {room_data['Room']}")
        print(f"Description: {room_data['Room Description']}")

        if 'Item' in room_data:
            print(f"You see a {room_data['Item']}")

        exits = []
        for rd in adjacency_list:
            if rd[0] == room_to_int[current_room]:
                exits = rd[1:]
                break

        print("Exits:")
        for exit in exits:
            print(exit.split('/')[0])  # Print only the first half of the exit

        action = input("What do you want to do? ").lower()  # Convert user input to lowercase

        if action.lower() == "examine":
            if 'Item' in room_data:
                print(f"Item Description: {room_data.get('Item Description', 'No description available.')}")
            else:
                print("There's nothing to examine.")
        elif action.lower() == "look":
            print(f"Description: {room_data['Room Description']}")
        elif action.lower() == "take":
            if 'Item' in room_data:
                print(f"You have taken the {room_data['Item']}.")
                score += 1  # Increase score
                del room_data['Item']  # Remove the item from the room
            else:
                print("There's nothing to take.")
        else:
            action_is_exit = False
            for exit in exits:
                exit_name = exit.split('/')[0].lower()  # Convert exit name to lowercase
                if action == exit_name:
                    current_room = exit.split('/')[-1]
                    action_is_exit = True
                    break
            if not action_is_exit:
                print("Invalid action. Please try again.")

        print(f"Score: {score}")  # Print the current score



def main():
  room_data_list = [
      {
    'Room': 'Entrance',
            'Room Description': 'You are at the entrance of a mysterious castle.',
            'Exits': 'North/Hallway',
        },
        {
            'Room': 'Hallway',
            'Room Description': 'You are in a long hallway with portraits on the walls.',
            'Exits': 'South/Entrance, East/Kitchen, West/Living Room',
            'Item': 'Key',
            'Item Description': 'A small, rusty key.'
        },
        {
            'Room': 'Kitchen',
            'Room Description': 'You are in a large kitchen. There are pots and pans everywhere.',
            'Exits': 'West/Hallway',
            'Item': 'Knife',
            'Item Description': 'A sharp-looking kitchen knife.'
        },
        {
            'Room': 'Living Room',
            'Room Description': 'You are in a cozy living room. There is a fireplace burning brightly.',
            'Exits': 'East/Hallway',
            'Item': 'Book',
            'Item Description': 'An old, dusty book.'
        },
        {
            'Room': 'Library',
            'Room Description': 'You step into a vast library with towering bookshelves. Some books seem to emit a faint glow.',
            'Exits': 'West/Hallway',
            'Item': 'Enchanted Scroll',
            'Item Description': 'A scroll with mystical symbols.'
        },
        {
            'Room': 'Secret Passage',
            'Room Description': 'You discover a hidden passage behind a bookshelf in the library.',
            'Exits': 'East/Library, North/Hidden Chamber',
            'Item': 'Lantern',
            'Item Description': 'A lantern that provides a warm, magical light.'
        },
        {
            'Room': 'Hidden Chamber',
            'Room Description': 'You enter a secret chamber filled with ancient artifacts.',
            'Exits': 'South/Secret Passage',
            'Item': 'Crystal Orb',
            'Item Description': 'A crystal orb that seems to hold mysterious powers.'
        },
        {
            'Room': 'Garden',
            'Room Description': 'You find yourself in a beautiful garden with vibrant flowers and singing birds.',
            'Exits': 'North/Hallway, East/Statue Courtyard',
            'Item': 'Flute',
            'Item Description': 'A silver flute that produces enchanting melodies.'
        },
        {
            'Room': 'Statue Courtyard',
            'Room Description': 'You enter a courtyard adorned with majestic statues.',
            'Exits': 'West/Garden',
            'Item': 'Artifact Shard',
            'Item Description': 'A shard from a powerful ancient artifact.'
        },
  ]

  # Start the game
  travel_rooms(room_data_list)

if __name__ == "__main__":
  main()

