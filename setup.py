from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = "-e ."
def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements"""
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove("-e .")
    
    return requirements 


setup(    name="ML_Predict_and_Reduce_Energy_Costs",
    version="0.0.1",
    author="Dejene",    
    author_email="hailudjj@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")    
 )

