"""
Create a python module or django pluggable app skeleton

Author: Marcos Lopez - dev@scidentify.info

"""
from termprint import termprint
from settings import CREATE_DIRECTORY as cdir

class Project:
    def __init__(self):
        pass

    def __ask_user(self, msg):
        """
        Ask a question
        Get a response
        return clean string (no spaces, dots, commas)
        """
        s = raw_input(msg)
        return s.replace(' ','').replace('.','').replace(',','')

    pass
