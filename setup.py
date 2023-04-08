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
    name='csv2graph',
    version='0.1',
    packages=find_packages(),
    install_requires=['requests'],
    url='https://github.com/TheCodingHornet/csv2graph',
    license='GNU',
    author='Simon STEPHAN',
    author_email='simon.stephan@u-bourgogne.fr',
    description='Library for reading CSV files and creating a graph of linked objects'
)
