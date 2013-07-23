from init import *

if __name__ == '__main__':
    p = Project()
    if not p.get_project_root():
        termprint("", "Provide an absolute path or director will be crested on local directory:\n")
        termprint("WARNING", "\t%s" % os.getcwd())
        p.ask_user('Project folder name (full path): ')
    else:
        termprint("", "Creating foder name inside\n")
        termprint("INFO", "%s\n", p.get_prjoect_root())
        p.ask_user('Project folder name (folder name): ')