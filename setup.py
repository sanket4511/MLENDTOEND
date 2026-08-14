from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirement(file_path: str) -> List[str]:
    """
    This function returns a list of requirements
    from the requirements.txt file.
    """

    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()

    requirements = [req.replace("\n", "") for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='project',
    version='0.0.1',
    author='Sanket',
    author_email='sanketpvt4511@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt'),
)