# -*- coding: utf-8 -*-
#
# Nom du fichier:       setup.py
# Date de création:     08/04/2023
# Version:              0.0.1
# Auteur:               Simon STEPHAN <simon.stephan@u-bourgogne.fr>
#
# Copyright (c) 2023,
# Tous droits réservés. 
#

from setuptools import setup, find_packages

setup(
    name="csv2graph",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "networkx",
        "pandas"
    ],
    entry_points={
        "console_scripts": [
            "csv2graph=csv2graph.csv2graph:main"
        ]
    },
    python_requires=">=3.6",
    license="GNU",
    description="A Python library to convert CSV files to graph objects",
    author="Simon STEPHAN",
    author_email="simon.stephan@u-bourgogne.fr",
    url="https://github.com/TheCodingHornet/csv2graph"
)
