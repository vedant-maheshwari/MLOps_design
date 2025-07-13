from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = 'MLOPS DESIGN'
VERSION = '0.01'
DESCRIPTION = 'MODULAR CODING PROJECT'
AUTHOR = 'VEDANT MAHESHWARI'
AUTHOR_EMAIL = 'vedantmaheshwari23@gmail.com'
REQUIREMENTS_FILE_NAME = 'requirments.txt'
HYPHEN_E_DOT = '-e .'

def get_requirements_list() -> list[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readline()
        requirement_list = [requirement.replace('/n','') for requirement in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        
    return requirement_list

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requirements = get_requirements_list()
     )