"""
Create a python module or django pluggable app skeleton

Author: Marcos Lopez - dev@scidentify.info

"""
import os
import sys
from termprint import termprint
from settings import CREATE_DIRECTORY as cdir
from string_messages import ERR_SET_DESTINATION, ERR_DIRECTORY_EXISTS, INTRO_ABS_QUESTION, \
                INTRO_ABS_INFO, INTRO_ABS_ENTER_DATA_MSG, INTRO_REL_QUESTION, \
                INTRO_REL_WARNING, INTRO_REL_ENTER_DATA_MSG

class ProjectBase(object):
    destination = None

    def __init__(self):
        pass

    def run(self):
        """ Run that shit! """
        self.create_base_directories()

    def ask_user(self, msg):
        """
        Ask a question
        Get a response
        return clean string (no spaces, dots, commas)
        """
        s = raw_input(msg)
        return s.replace(' ','').replace('.','').replace(',','')

    def remove_trailing_slash(self, dir):
        """ Remove a trailing slash from a directory if any.
        E.g: turns /tmp/mycoolstuff/myapp/ to: /tmp/mycoolstuff/myapp
        """
        if self.has_trailing_slash(dir):
            return dir[:-1]

    def has_trailing_slash(self, dir):
        """ Check if dir string has trailing slash by checking first char"""
        return path[:1] == '/'

    def set_destination(self, path):
        """ Check if relative or abs and set the path
        remove any trailing slashes. Remove any prefix slashes
        If there is an absolute path provided it will omit the settings
        CREATE_DIRECTORY value.
        """
        # if provided was an absolute path
        if self.has_trailing_slash(path)
            self.destination = path
        else:
            # should not copy to relative path cause no settins is set for project root
            if not cdir:
                termprint("ERROR", ERR_SET_DESTINATION)
                sys.exit(1)
            self.destination = "%s/%s" % (self.get_project_root(), path)
        # remove any trailing slashes for people who dont read    
        self.destination = self.remove_trailing_slash(self.destination)

    def get_project_root(self):
        """ Return the project root and strip trailng slash """
        return self.remove_trailing_slash(cdir)

    def intro(self):
        """ Intro questions to ask the user to get started """
        # ask a user appropriately based on settings
        if not self.get_project_root():
            termprint("", INTRO_ABS_QUESTION)
            termprint("WARNING", "\t%s" % os.getcwd())
            termprint("INFO", INTRO_ABS_INFO)
            response = self.ask_user(INTRO_ABS_ENTER_DATA_MSG)
        else:
            termprint("", INTRO_REL_QUESTION)
            termprint("INFO", "\t%s\n" % self.get_project_root())
            termprint("WARNING", INTRO_REL_WARNING)
            response = self.ask_user(INTRO_REL_ENTER_DATA_MESSAGE)
        if response and len(str(response)) > 5:
            self.set_destination(response)

    def create_base_directories(self):
        """ Create the base directory that was set to self.destination variable.
        If the directory exists, exit with an error, we are not overriding 
        and breaking anything today.
        Destination should be an absolute path that is set by self.set_destination, which 
        occurs after the intro()
        """
        if os.path.exists(self.destination):
            termprint("ERROR", ERR_DIRECTORY_EXISTS)
            termprint("WARNING", "\t%s" % self.destination)
        else:
            os.mkdir("mkdir %s" % self.destination)

        
