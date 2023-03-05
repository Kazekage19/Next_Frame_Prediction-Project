from setuptools import find_packages,setup
from typing import List

e_call='-e .'
def requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirement=[]
    with open(file_path) as file:
        requirement=file.readlines()
        requirement=[req.replace("\n","") for req in requirement]
    if(e_call in requirement):
        requirement.remove(e_call)
    setup(
        name="Video Frame Predictor",
        version="0.0.1",
        author="Akshat Srivastava(Kazekage19)",
        author_email='mail2akshat@yahoo.com',
        packages=find_packages(),
        install_reqires=requirements('requirements.txt'),
    )    