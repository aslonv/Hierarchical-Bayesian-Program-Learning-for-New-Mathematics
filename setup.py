# setup.py
from setuptools import setup, find_packages

setup(
    name="hierarchical-bayesian-math-invention",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pyro-ppl",
        "torch",
        "sympy",
        "numpy",
        "scipy",
        "matplotlib",
    ],
)