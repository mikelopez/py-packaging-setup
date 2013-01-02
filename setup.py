from setuptools import setup, find_packages
import sys, os
import django_siteanalytics

setup(
    name='FOLDER-NAME',
    version='0.1',
    description="UPDATE-DESCRIPTION",
    long_description=open('README.md', 'r').read(),
    keywords='',
    author='',
    author_email='',
    url='',
    license='MIT',
    package_dir={'DJANGO_APP_FOLDER_NAME': 'DJANGO_APP_FOLDER_NAME'},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: Log Analysis",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Page Counters",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Topic :: Security",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities",
    ]
)
