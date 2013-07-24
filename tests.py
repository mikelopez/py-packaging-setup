import settings
import os, sys
from termprint import termprint
from unittest import TestCase, TestSuite, TextTestRunner
from create_python_package import *


CREATE_DIRECTORY = getattr(settings, "CREATE_DIRECTORY", None)

class TestInitDev(TestCase):
  """ test init dev """

  project_name = ''
  create_directory = ''

  def setUp(self):
    pass

  def break_row(self):
    """ Print a row separation for logs and stdout """
    termprint("", "\n\n")
    termprint("INFO", "-".join(["-" for x in range(0, 50)]))

  def test_askuser(self):
    """
    Test ask user prompt
    """
    self.break_row()
    termprint("INFO", '\n.... Testing test_askuser(): Enter a random package name')
    cl = PythonPackage()
    cl.start()
    # dpending what you entered    
    self.assertEquals(cl.destination.split('/')[-1], cl.user_response)
    termprint("", "Cleaning files")
    os.system('rm -rf %s' % cl.destination)


  def test_directory_exists(self):
    """ 
    Make sure we catch if the directory exists or not
    """
    self.break_row()
    termprint("INFO", "\n\n.... Testing for duplicate catch. \n\
      Enter another unique random package name (Not the same as previous)")
    cl = PythonPackage()
    cl.start()
    # create the base destination directory
    self.assertTrue(cl.create_base_directories())
    # now retry - should return false
    self.assertFalse(cl.create_base_directories())
    termprint("", "Cleaning files")
    os.system('rm -rf %s' % cl.destination)


  def test_create_readme(self):
    """ 
    Create the readme file 
    """
    self.break_row()
    termprint("INFO", "\n\n.... Test the readme, enter another unique package name")
    cl = PythonPackage()
    cl.start()
    self.assertTrue(cl.create_base_directories())
    # create the readme
    self.assertTrue(cl.create_readme())
    self.assertTrue(os.path.exists("%s/README.rst"%cl.destination, "r").open())
    self.assertTrue(cl.user_response in open("%s/README.rst"%cl.destination, "r").open())
    termprint("", "Cleaning files")
    os.system('rm -rf %s' % cl.destination)


  def test_create_setup(self):
    """ Create the setup file """
    termprint("INFO", "\n\n.... Test the readme, enter another unique package name")
    self.break_row()
    cl = PythonPackage()
    cl.start()
    self.assertTrue(cl.create_base_directories())
    # can now create the setup (skipping readme for test)
    self.assertTrue(cl.create_setup())
    self.assertTrue(os.path.exists('%s/setup.py' % cl.destination))
    termprint("", "Cleaning files")
    os.system('rm -rf %s' % cl.destination)




  



if __name__ == '__main__':
  suite = TestSuite()
  suite.addTest(TestInitDev("test_askuser"))
  suite.addTest(TestInitDev("test_directory_exists"))
  suite.addTest(TestInitDev("test_create_readme"))
  suite.addTest(TestInitDev("test_create_setup"))

  TextTestRunner(verbosity=2).run(suite)

