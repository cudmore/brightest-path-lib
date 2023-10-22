import os
import sys
from setuptools import setup, find_packages

VERSION = "1.0.13"

packages = find_packages(exclude=["tests"])
print(f"found packages: {packages}")

setup_requires = ['numpy']

# load the readme
_thisPath = os.path.abspath(os.path.dirname(__file__))
with open(os.path.abspath(_thisPath+"/README.md")) as f:
    long_description = f.read()

setup(
    name="brightest-path-lib",
    description="A library of path-finding algorithms to find the brightest path between points in an image.",
    long_description=long_description,
    long_description_content_type = 'text/markdown',
    author="Vasudha Jha",
    url="https://github.com/mapmanager/brightest-path-lib",
    project_urls={
        "Issues": "https://github.com/mapmanager/brightest-path-lib/issues",
        "CI": "https://github.com/mapmanager/brightest-path-lib/actions",
        "Changelog": "https://github.com/mapmanager/brightest-path-lib/releases",
    },
    license="GNU General Public License, Version 3",
    version=VERSION,
    #packages=["brightest_path_lib"],
    #packages=find_packages(),
    packages=packages,
    setup_requires=setup_requires,
    install_requires=["numpy"],
    extras_require={
        'dev': [
            'mkdocs',
            'mkdocs-material',
            'mkdocs-jupyter',
            'mkdocstrings',
            'mkdocs-material-extensions'
        ],
        "test": [
            "pytest", 
            "pytest-cov", 
            "scikit-image", 
            "pooch"
        ]
    },
    python_requires=">=3.7",
)