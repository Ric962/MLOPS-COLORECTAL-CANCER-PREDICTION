from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-COLORECTAL-CANCER-PREDICTION",
    version="0.1",
    author="Uday Chaware",
    packages=find_packages(),
    install_requires=requirements
)