from setuptools import find_packages, setup

setup(
    name='lib',
    packages=find_packages(include=['lib']),
    version='0.1.0',
    description='My First Python Library - Longitude and Latitude',
    author='Matthew Jesse Thomas - NomDePlume',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)