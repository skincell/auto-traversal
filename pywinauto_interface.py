import pywinauto


# build the system
# first connect to the correct location
# Second if it isn't there then run the correct window


def setup_app(application_path):

    # TODO Look into replacing these try and excepts
    # Using a try and except here to see if we can connect or need to start a new application.
    try:
        pywinauto.Application(backend="uia").connect(application_path)
    except pywinauto.application.AppNotConnected:

        try:
            pywinauto.Application(backend="uia").start(application_path)
        except pywinauto.application.AppNotConnected:
            # TODO make this a proper Exception
            print("The Automation Layer had trouble attaching itself to the Application")


# This function is supposed to attach the automation layer to the ccorrect application
def start_up_automation(application_path, windows_title):

    auto_app = setup_app(application_path)
    dia_spac = auto_app.window() # Should control the correct window. We now just need to decide the controller that we want.
