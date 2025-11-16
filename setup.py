from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str)-> list:
    '''
    This function will return the list of requirements
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements    


setup(

    name = 'ML-project',
    version = '0.0.1',
    author = 'Debanshu Dutta',
    author_email = 'duttadebanshu13@gmail.com',
    packages = find_packages(),
    # get_requirements returns a list of requirement strings from the file path
    # pass the filename as a string (not a variable) and assign the list directly
    install_requires = get_requirements("requirements.txt")
)


