'''
setup.py file, which is the standard way to package a Python project so it can be:

Installed like any other Python library
Reused across projects
Shared or deployed (locally or remotely)

use https://docs.python.org/3.11/distutils/setupscript.html for setup param format refrence
'''
#still have doubt about this file

from setuptools import setup, find_packages
from typing import List

#definig variables to insert in setup
PROJECT_NAME = 'MLOPS DESIGN'
VERSION = '0.01'
DESCRIPTION = 'MODULAR CODING PROJECT'
AUTHOR = 'VEDANT MAHESHWARI'
AUTHOR_EMAIL = 'vedantmaheshwari23@gmail.com'

#this is to get the requirement file
REQUIREMENTS_FILE_NAME = 'requirments.txt'
HYPHEN_E_DOT = '-e .'

# def get_requirements_list() -> list[str]:
#     with open(REQUIREMENTS_FILE_NAME) as requirement_file:
#         requirement_list = requirement_file.readline()

#         #by default '/n' chracter is there when moving to new line, can create problem in installing dependences 
#         #hence removing it and adding the requirements in list
#         requirement_list = [requirement.replace('/n','') for requirement in requirement_list]

#         #Install this project as an editable package
#         #removes '-e .' so that multiple time the files won't be created if the setup is executed multiple times
#         if HYPHEN_E_DOT in requirement_list:
#             requirement_list.remove(HYPHEN_E_DOT)
        
#     return requirement_list

def get_requirements_list() -> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement.strip() for requirement in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list


setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(), #find_packages() goes inside src/__init__.py and gets all the packages to install
      install_requires = get_requirements_list() #this gets the requirements list to be downloaded
     )