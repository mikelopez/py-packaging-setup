__author__ = 'Marcos Lopez'
__email__ = 'dev@scidentify.info'
import sys
import os

# run this script from the same directory as your base setup/docs

class InitDev:
  project_name = 'test_projectname'
  create_directory = 'test_createdirectory'
  project_directory = 'test_createdirectory/test_projectname'
  recopy_docs = False
  recopy_setup = False

  def __init__(self, project_name=None, create_directory=None):
    if project_name:
      self.project_name = project_name
    if create_directory:
      self.create_directory = create_directory
    

  def ask_user(self, msg):
    """
    ask a question
    get a response
    return clean string (no spaces, dots, commas)
    """
    s = raw_input(msg)
    return s.replace(' ','').replace('.','').replace(',','')

  def set_data(self, project_name=None,create_directory=None):
    """ 
    set the project name/directory and set the project_directory var
    overwrite self.project_name and self.create_directory if local args
    """
    if project_name: 
      self.project_name = project_name
    if create_directory:
      self.create_directory = create_directory
    self.project_directory = '%s/%s' % (self.create_directory, self.project_name)

  def checkdir(self, filestring):
    """
    copy the filestring to the destination and check if it copied ok
    """
    if "docs" in filestring:
      os.system('cp -r src/%s %s/' % (filestring, self.project_directory))
    else:
      os.system('cp -r %s %s/' % (filestring, self.project_directory))
    if os.path.exists('%s/%s' % (self.project_directory, filestring)):
      print '\n... copied %s script base\n' % filestring
    else:
      print '... FAILED to copy %s file to %s\n' % (filestring, self.project_directory)
      print 'cp -r src/%s %s/\n\n' % (filestring, self.project_directory)

  def copy_readme(self):
    """
    create the readme file
    once its created, it is dynamically written containing project_name
    """
    os.system('touch %s/README.md' % self.project_directory)
    if os.path.exists('%s/README.md' % self.project_directory):
      o = open('%s/README.md' % self.project_directory, 'w')
      o.write('Project README for %s' % self.project_name)
      o.write('<br /><br />')
      o.write('<b>Installation</b><br />')
      o.write('- add "django.template.loaders.eggs.Loader" to your TEMPLATE_LOADERS in settings.py<br />')
      o.write('- add app-name to INSTALLED_APPS in settings.py<br />')
      o.write("- (optional) add url(r'^app_name/', include('app_name.urls')), to your urls.py file (project)<br />")
      o.close()
      print '... Copied readme base\n'
    else:
      print '... FAILED to copy read me to %s\n' % self.project_directory


  def recopy_files(self, filestring):
    """
    Recopy the files if you make any updates to the template files
    """
    if os.path.exists('%s/%s' % (self.project_directory, filestring)):
      print '%s already exist' % filestring
    else:
      self.checkdir(filestring)
      print 'Copied %s AGAIN!' % filestring


  def run(self):
    """
    Run the process
    1) create the directory
    2) copy setup.py
    3) copy docs/ directory
    4) create a gitignore base file
    ----
    """
    if self.create_directory[-1] == '/':
      # fix trailing slash
      self.create_directory = self.create_directory[0:-1]
      self.set_data()

    if not os.path.exists(self.project_directory):
      os.mkdir(self.project_directory)
    else:
      print 'Project name %s in %s already exists' % (self.project_name, self.create_directory)

      # recopy docs or setup.py file (if any changes were made and you want to update an existing project)
      if not self.recopy_docs:
        s = self.ask_user('Recopy docs/ folder? ')
        if s == 'y':
          self.recopy_files('docs')
          print 'Copied doc files over...'
      else:
        self.recopy_files('docs')
      #
      if not self.recopy_setup:
        s = self.ask_user('Recopy setup.py file? ')
        if s == 'y':
          self.recopy_files('setup.py')
          print 'Copied setup.py files over...'
      else:
        self.recopy_files('setup.py')
      sys.exit()

    # try gitignore :)
    gitignore = """*.pyc
*.swp
*DS_*
*local_settings.py*
*build/
*dist/
*.egg-info*
"""
    # a very basic setup.py file (not using this here )
    setuppy = """
from distutils.core import setup
setup(name='%s',
      version='1.0',
      py_modules=['.'],
)
    """ % self.project_name
    if os.path.exists('%s' % self.project_directory):
      if not os.path.exists('%s/.gitignore' % self.project_directory):
        o = open('%s/.gitignore' % self.project_directory, 'w')
        o.write(gitignore)
        o.close()
      #if not os.path.exists('%s/setup.py' % self.project_directory):
      #  o = open('%s/setup.py' % self.project_directory, 'w')
      #  o.write(setuppy)
      #  o.close()
      # always use the setup.py file in this directory
      self.checkdir('setup.py')
      self.checkdir('MANIFEST.in')
      self.checkdir('docs')
      self.copy_readme()

    print '\n\nHooray! Created project %s in %s' % (self.project_name, self.create_directory)
    print '\n\n==========='
    print '\nUpdate setup.py: modify APP-NAME & name as needed'



if __name__ == '__main__':
  # set these values 
  PROJ_NAME = ''
  CREATE_DIR = ''

  cl = InitDev(project_name=PROJ_NAME, create_directory=CREATE_DIR)
  if not PROJ_NAME:
    cl.project_name = cl.ask_user('Project folder name (no space): ')
  if not CREATE_DIR:
    cl.create_directory = cl.ask_user('Parent Directory to place folder in: ')

  cl.set_data()
  cl.run()
