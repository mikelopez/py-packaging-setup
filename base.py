"""
Create a python module or django pluggable app skeleton

Author: Marcos Lopez - dev@scidentify.info

"""
import os
import sys
from termprint import termprint
from settings import CREATE_DIRECTORY as cdir
from string_messages import ERR_SET_DESTINATION, ERR_DIRECTORY_EXISTS,\
                            INTRO_ABS_QUESTION,  INTRO_ABS_INFO,  \
                            INTRO_ABS_ENTER_DATA_MSG, INTRO_REL_QUESTION,\
                            INTRO_REL_WARNING, INTRO_REL_ENTER_DATA_MSG, \
                            DJANGO_REMINDER
# the root dir of the project where we copy files from
PROJECT_ROOTDIR = os.path.realpath(os.path.dirname(__file__))

class DirectoryExistsException(Exception):
    def __init__(self, message):
        s = termprint("ERROR", messages, return_text=True)
        Exception.__init__(self, s)

class NotCreatedException(Exception):
    def __init__(self, message):
        s = termprint("ERROR", messages, return_text=True)
        Exception.__init__(self, s)

class ProjectBase(object):
    destination = None
    is_django = False
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
        return dir

    def has_trailing_slash(self, dir):
        """ Check if dir string has trailing slash by checking first char"""
        return dir[-1] == '/'

    def set_destination(self, path):
        """ Check if relative or abs and set the path
        remove any trailing slashes. Remove any prefix slashes
        If there is an absolute path provided it will omit the settings
        CREATE_DIRECTORY value.
        """
        # if provided was an absolute path
        if self.has_trailing_slash(path):
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

    def get_project_name(self):
        """ Get the project name based on the folder name """
        return str(self.destination).split('/')[-1]

    def intro(self):
        """ Intro questions to ask the user to get started and 
        sets the destination
        """
        # ask a user appropriately based on settings
        if not self.get_project_root():
            termprint("", INTRO_ABS_QUESTION)
            termprint("WARNING", "\t%s" % os.getcwd())
            termprint("INFO", INTRO_ABS_INFO)
            response = self.ask_user(INTRO_ABS_ENTER_DATA_MSG)
        else:
            # provide only package name (optional absolute)
            termprint("", INTRO_REL_QUESTION)
            termprint("INFO", "\t%s\n" % self.get_project_root())
            termprint("WARNING", INTRO_REL_WARNING)
            response = self.ask_user(INTRO_REL_ENTER_DATA_MSG)
        if response and len(str(response)) > 5:
            self.set_destination(response)
        return response

    def create_base_directories(self):
        """ Create the base directory that was set to self.destination variable.
        If the directory exists, exit with an error, we are not overriding 
        and breaking anything today.
        Destination should be an absolute path that is set by self.set_destination, which 
        occurs after the intro()
        """
        termprint("INFO", "\n\t....Trying to create directory %s\n" % self.destination)
        if os.path.exists(self.destination):
            termprint("ERROR", ERR_DIRECTORY_EXISTS)
            termprint("WARNING", "\n\t%s" % self.destination)
            termprint("ERROR", "\n\nEXITING!!\n")
            return False
        else:
            os.system("mkdir %s" % self.destination)
            return True
        if os.path.exists(self.destination):
            termprint("INFO", "\nCreated Directory %s\n" % self.destination)
            return True
        else:
            termprint("ERROR", "\nFailed to create %s\n" % self.destination)
            return False

    def create_readme(self):
        """ Create the readme file """

        orig = open("%s/README_SAMPLE.rst" % PROJECT_ROOTDIR, "r").read()
        oo = orig.replace('PROJECT_NAME', self.get_project_name())
        ooo = open('%s/README.rst' % self.destination, 'w')
        ooo.write(oo)
        ooo.close()
        if os.path.exists('%s/README.rst' % self.destination):
            termprint("INFO", '... Copied readme base\n')
            return True
        else:
            termprint("ERROR", '... FAILED to copy read me to %s\n' % self.destination)
            return False

    def create_setup(self, django=False):
        """ 
        Create the setup.py file 
        Copy the setup.py file
        Create another subdirectory with the same name as the package
        Creates files:
         - /absolute_path_destination/packagename/packagename/__init__.py
         - /absolute_path_destination/packagename/packagename/packagename.py
         - /absolute_path_destination/packagename/setup.py
        """
        # original setup file to copy. If django = True, use setup_django.py
        original_file = "setup.py"
        if django:
            original_file = "setup_django.py"
        orig = open("%s/%s" % (PROJECT_ROOTDIR, original_file), "r").read()
        oo = orig.replace('APP-NAME', self.get_project_name())
        # writes to this file (destination is always setup.py
        ooo = open('%s/setup.py' % self.destination, 'w')
        ooo.write(oo)
        ooo.close()
        if not os.path.exists('%s/%s.py' % (self.destination, self.get_project_name())):
            os.system('touch %s/%s.py' % (self.destination, self.get_project_name()))
        if os.path.exists('%s/setup.py' % self.destination):
            termprint("INFO", '... Copied setup base\n')
            return True
        else:
            termprint("ERROR", '... FAILED to copy setup to %s\n' % self.destination)
            return False


    def create_gitignore(self):
        """ Creating the gitignore """
        if not os.path.exists('%s/.gitignore' % self.destination):
            os.system('cp %s/.gitignore %s/.gitignore' % (PROJECT_ROOTDIR, self.destination))
            termprint("INFO", "Created gitignore file since it wasn't found")
            return True
        return False
