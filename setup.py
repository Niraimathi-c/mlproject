from setuptools import find_packages,setup
from typing import List
hypen_dot_e="-e ."

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
        if hypen_dot_e in requirements:
            requirements.remove(hypen_dot_e)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='nirai',
    author_email='nirai6161@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)