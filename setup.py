#!/usr/bin/env python
"""
django-mailwhimp
======

Django-mailwhimp is a django application for interacting with MailChimp.
"""

from setuptools import setup, find_packages

setup(
    name='django-mailwhimp',
    version='0.1',
    author='Kit Sunde',
    author_email='kit@mediapop.co',
    url='http://github.com/Celc/django-mailwhimp',
    description='django-mailwhimp integrates mailchimp into Django',
    long_description=__doc__,
    packages=find_packages(exclude=("tests",)),
    zip_safe=False,
    install_requires=[
        'mailsnake'
    ],
    test_suite='runtests.runtests',
    include_package_data=True,
    entry_points={},
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django'
    ],
)
