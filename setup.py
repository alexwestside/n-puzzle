from setuptools import setup, find_packages

setup(
    name='npuzzle',
    package_dir={'Package': 'src'},
    packages=find_packages(),
    entry_points={'console_scripts': ['npuzzle=src.__main__:main'], }
)
