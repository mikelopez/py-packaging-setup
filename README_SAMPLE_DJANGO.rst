Django App Readme for PROJECT_NAME
------------------------------

Django Configuration Installation 
==================================
* add ``django.template.loaders.eggs.Loader`` to your ``TEMPLATE_LOADERS`` in ``settings.py``
* add your ''app-name'' to ``INSTALLED_APPS`` in settings.py
* Optional add url(r'^app_name/', include('app_name.urls')), to your urls.py file (project)
