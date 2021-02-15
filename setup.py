from setuptools import setup, find_packages

setup(
    name="patient-analysis",
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'numpy',
        'pytest',
        'yapf',
    ],
)
