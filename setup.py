from setuptools import setup, find_packages

packages = find_packages()

setup(
    name='n-puzzle',
    packages=packages,
    entry_points={'console_scripts': ['npuzzle=src.npuzzle:main'], }
)
