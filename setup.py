# to develop the whole application as PACKAGE
from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path :str)-> list:
    """this function will return the list of requirements from the requirements.txt file    """
    requirements=[]
    with open(file_path) as f:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproj',
    version='0.1',
    author='Anumitha',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') #we cant write the whole list of libraries here..so we will write the requirements.txt file and then we will read that file here
)
