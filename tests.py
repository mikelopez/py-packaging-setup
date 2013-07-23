from unittest import TestCase, TestSuite, TextTestRunner
from initdev import InitDev

import os, sys

CREATE_DIRECTORY = '/home/user/public-repos'

class TestInitDev(TestCase):
  """ test init dev """

  project_name = ''
  create_directory = ''

  def setUp(self):
    pass

  def test_askuser(self):
    """
    test ask user prompt
    """
    print '\n.... Testing test_askuser():'
    cl = InitDev()
    s = cl.ask_user("Type the letter lowercase x: ")
    self.assertEquals(s, 'x')

  def test_set_data(self):
    """
    test set_data function
    1) takes optional project-name, create-directory args
      if they are set, they override self.project-name and 
      self.create-directory
    2) set self.project_directory to project-name/create-directory
    """
    print '\n.... Testing test_set_data():'
    cl = InitDev()
    cl.create_directory = 'create-string'
    cl.project_name = 'projectstring'
    cl.set_data()
    print '%s should be create-string/projectstring' % cl.project_directory
    self.assertEquals(cl.project_directory, 'create-string/projectstring')

    cl.set_data(project_name='project2', create_directory='create-directory2')
    print '%s should be create-directory2/project2' % cl.project_directory
    self.assertEquals(cl.project_directory, 'create-directory2/project2')


  def test_fullrun(self):
    """
    Test the run() method on the init dev class which actually does actually
    performs the copy of files
    """
    print '\n.... Testing test_fullrun():'
    files = ['.gitignore', 'docs', 'setup.py']
    cl = InitDev()
    # uncomment or use cl.ask_user
    cl.create_directory = CREATE_DIRECTORY
    cl.project_name = 'test_newproject'
    cl.set_data()
    cl.run()

    self.assertTrue(os.path.exists(cl.project_directory))
    print '...OK'
    for i in files:
      print '... checking for file %s' % i
      self.assertTrue(os.path.exists('%s/%s' % (cl.project_directory, i)))



if __name__ == '__main__':
  suite.addTest(TestInitDev("test_askuser"))
  suite.addTest(TestInitDev("test_set_data"))
  suite.addTest(TestInitDev("test_fullrun"))

  TextTestRunner(verbosity=2).run(suite)

