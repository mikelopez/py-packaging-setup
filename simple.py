import os, sys

srcs = raw_input('Source files: ')
project_dsts = raw_input('Project name: ')
dsts = raw_input('Project Destination Directory:' )

if os.path.exists('%s/%s' % (project_dsts, dsts)):
  print 'Already exists...'
  sys.exit()

if not os.path.exists('%s/%s' % ()):
  os.mkdir('%s/%s' % (project_dsts, dsts))
  os.system('cp -r %s/* %s/%s' % (srcs, dsts, project_dsts))
  print 'Created %s' % project_dsts


