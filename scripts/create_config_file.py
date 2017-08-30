import json

commands_dict = {}

fp = open("command_mapping.json", "w")
# TODO (need to find a different way to do keymappings)
# This is a placeholder: API methods or key mappings
commands_dict["move_forward"] = "up"
commands_dict["move_left"] = "left"
commands_dict["move_right"] = "right"
commands_dict["move_backward"] = "down"

json.dump(commands_dict, fp)