import json

def load_commands():
    with open('command_mapping.json') as data_file:
        command_mapping = json.load(data_file)
    return command_mapping

# structure for storing the graph
# TODO storing graphs and adding data/determining if the graph is being connected - no way to tell if node is different from others!!!
# TODO Research Research

# Goes to some keyboard interface or api for game
def run_command(command):

    # Detect if movement occurs
    return True

# Feedback mechanism - has to be visual

# Controls the actual interface
def controller(command_mapping, graph_storage_structure):

    auto_movement_engaged = True

    # movement loop
    while auto_movement_engaged:

        # command loop
        for command in command_mapping:

            command_successful = run_command(command)

            if command_successful:

                # Determine if it is a new node
                # Add it if it is a new node
                # Consolidate/improve the graph structure underneath

                pass




        pass




