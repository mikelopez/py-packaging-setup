from base import *

class PythonPackage(ProjectBase):
    user_response = None

    def __init__(self):
        super(PythonPackage, self).__init__()
        self.user_response = self.intro()
                
    def remove_stuff_post_error(self):
        """ Remove the project created if there were errors """
        os.system('rm %s' % self.destination)

    def start(self):
        """ Start the process of copying the files needed """
        dirs_ok = self.create_base_directories()
        if dirs_ok:
            read_me = self.create_readme()
            if not read_me:
                self.remove_stuff_post_error()
                termprint("ERROR", "Failed to create readme!\n\nExiting\n")
            setups = self.create_setup()
            if not setups:
                self.remove_stuff_post_error()
                termprint("ERROR", "Failed to create setup.py file\n\nExiting!")
            # not checking response cause gitignore is created if it doesnt exist
            gitignore = self.create_gitignore()

        termprint("INFO", "Successfully created the package at:\n")
        termprint("WARNING", "\t%s" % self.destination)




