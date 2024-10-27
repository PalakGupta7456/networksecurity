"""
for packaging and distributing the python projects.
It is used by setuptools to configuration of project, such as its metadata, dependencies, and more

"""

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements

    """
    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            #read lines from the file
            lines=file.readlines()
            ##process each line
            for line in lines:
                ## remove spaces in requirements
                requirement=line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement!='-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements_lst

#print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Palak Gupta",
    author_email="palakgupt1234@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

