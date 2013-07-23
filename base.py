"""
Create a python module or django pluggable app skeleton

Author: Marcos Lopez - dev@scidentify.info

"""
import os
import sys
from termprint import termprint
from settings import CREATE_DIRECTORY as cdir

class ProjectBase:
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
                termprint("ERROR", "No Absolute path provided and no settings, do either one. \
                    Set your CREATE_DIRECTORY variable in settings")
                sys.exit(1)
            self.destination = "%s/%s" % (self.get_project_root(), path)
        # remove any trailing slashes for people who dont read    
        self.destination = self.remove_trailing_slash(self.destination)

    def get_project_root(self):
        """ Return the project root and strip trailng slash """
        return self.remove_trailing_slash(cdir)
        
