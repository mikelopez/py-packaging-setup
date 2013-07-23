from base import *

class PythonPackage(ProjectBase):
    user_response = None

    def __init__(self):
        super(PythonPackage, self).__init__()
        self.user_response = self.intro()

    def start(self):
        """ Start the process of copying the files needed """
        dirs_ok = self.create_base_directories()





