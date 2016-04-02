# coding=utf-8
"""
Postcodes
---------
A simple library for getting access to UK Postcode data.
"""
from setuptools import setup

setup(
    name='postcodes',
    version='0.1',
    url='http://github.com/thiagovarela/postcodes',
    license='GPL',
    author='Thiago Varela',
    author_email='thiagovarela@gmail.com',
    description='A simple library for validating UK postcodes',
    long_description='A simple library for validating UK postcodes',
    packages=['postcodes'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[],
    test_requires=[],
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)