from pywinauto_interface import game_interface_data_collection


hobl = game_interface_data_collection("C:\Program Files (x86)\Steam\steamapps\common\Heroes of a Broken Land\hobl.exe")

hobl.send_command("{LEFT}")
hobl.write_image_data()