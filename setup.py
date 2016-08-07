#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    'click',
    'redis',
]

setup(
    name='toothbrush',
    version='0.0.1',
    author='Bright SAS',
    author_email='oss@brightfor.me',
    url='https://github.com/brightforme/toothbrush',
    description='Get/Set your env var in Redis',
    long_description=open('README.rst').read(),
    py_modules=['toothbrush'],
    zip_safe=False,
    install_requires=install_requires,
    entry_points='''
        [console_scripts]
        toothbrush=toothbrush:toothbrush
    ''',
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
