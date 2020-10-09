import setuptools

from os import path

p = path.abspath(path.dirname(__file__))
readme_filepath = path.join(p, 'README.md')
README = "See https://github.com/danhagen/atm-controller for full documentation."
if path.isfile(readme_filepath):
    with open(readme_filepath) as f:
        README = f.read()

setuptools.setup(
    name="danpy",
    version="0.1.0",
    url="https://github.com/danhagen/atm-controller",
    author="Daniel A Hagen",
    author_email="daniel.8.hagen@gmail.com",
    description="Simple ATM Controller",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=['atm'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
