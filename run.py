from init import *

if __name__ == '__main__':
    p = Project()

    # ask a user appropriately based on settings
    if not p.get_project_root():
        termprint("", "\nProvide an absolute path or directory will be created on local directory:")
        termprint("WARNING", "\t%s" % os.getcwd())
        termprint("INFO", "You can modify settings.py and provide a relative directory instead")
        response = p.ask_user('\nPackage folder name (full path): ')

    else:
        termprint("", "\nProvide a package name.")
        termprint("", "\nThe package will be created inside directory:")
        termprint("INFO", "\t%s\n" % p.get_project_root())
        termprint("WARNING", "Note: By Providing an absolute path (/tmp/myapp) will omit settings")
        response = p.ask_user('\nPackage folder name (folder name): ')

    if response and len(str(response)) > 5:
        p.set_destination(response)

    self.run()