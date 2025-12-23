from helpers.config import get_settings ,Settings

class BaseController:
    #constructors
    def __init__(self):
        self.app_settings= get_settings()

    pass