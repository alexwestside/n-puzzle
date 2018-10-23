from setuptools import setup, find_packages

setup(
    name='n-puzzle',
    packages=find_packages(),
    entry_points={'console_scripts': ['npuzzle=src.npuzzle:main'], }
)
