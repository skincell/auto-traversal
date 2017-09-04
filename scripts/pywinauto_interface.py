import pywinauto


# build the system
# first connect to the correct location
# Second if it isn't there then run the correct window
# This class acts as a game interface and data collection device.
# This class mashes together the interface and data collection functionality.
# The data collection and game interface might need to be unlinked wheen using a provided API for a game.
class game_interface_data_collection:

    def __init__(self, application_path):

        self.auto_app = self.setup_app(application_path)
        # If we need dialogs then we can do that
        pass

    def setup_app(self, application_path):

        # TODO Look into replacing these try and excepts
        # Using a try and except here to see if we can connect or need to start a new application.
        try:
            # Connect and connect are two different functions that do similar things..
            app = pywinauto.Application(backend="uia").connect(path=application_path)
            return app
        except pywinauto.application.ProcessNotFoundError:
            print("Could not connect to application. Trying to start application instead.")
        try:
            app = pywinauto.Application(backend="uia").start(application_path)
            return app
        except pywinauto.application.AppNotConnected:
            # TODO make this a proper Exception
            print("Could not start application. Please check your application path.")

    # These commands must work for the interface setup.
    def send_command(self, command):

        self.auto_app.top_window().set_focus()

        self.auto_app.top_window().type_keys(command)


        pass

    def write_image_data(self):
        image_data = ""
        Image = self.auto_app.top_window().capture_as_image()
        Image.save("img1.png", "PNG")
        print Image

