Python Packaging & Setup
------------------------

Read More: http://django-app-initdev.readthedocs.org

Create Python modules or Django Pluggable application skeleton to get started on a project.


Installation
-------------
* Copy local_settings_sample to local_settings.py ``cp local_settings_sample.py local_settings.py`` and modify ``CREATE_DIRECTORY`` variable to the directory you want, or omit this value and provide absolute paths for your projects destination.


* Once the folder has been created, change into that directory and run django-admin to create a new app ``django-admin.py startapp myapp``


Creating Python Module
----------------------
After creating a python module, Assuming the packagename is ''mypackage'', it will create directories in the following::

    /absolute/path/destination/mypackage/
                                       mypackage.py
                                       setup.py
                                       README.rst
                                       MANIFEST.in

.. note:: You can rename to anything else, you can also reconfigure this setup however you'd like as a module or add extra files and directories, just be sure to update your setup.py file. 


Using
-----
.. code-block:: python
    
    from mypackage.main import SomeClassOrSomething
    cl = SomeClassOrSomething()
    cl.goodbye()




8)

