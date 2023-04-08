# -*- coding: utf-8 -*-
#
# Nom du fichier:       main.py
# Date de création:     08/04/2023
# Version:              0.0.1
# Auteur:               Simon STEPHAN <simon.stephan@u-bourgogne.fr>
#
# Copyright (c) 2023,
# Tous droits réservés. 
#

from democlass import Person, Relation
from csv2graph import csv2graph

# Header : id , id_person1 , person1_firstname , person1_lastname , id_person2 , person2_firstname , person2_lastname , relation_type , relation_mechanism , relation_date

# Créer un objet Csv2Graph avec le nom de fichier CSV en entrée
csv_to_graph = csv2graph("democsv/demofile.csv")

# Les nœuds présents dans la ligne du CSV sont configurés pour le graphe
csv_to_graph.add_node(Person, _id="identifier", _label="Person1", fname="person1_firstname", lname="person1_lastname", identifier="id_person1")
csv_to_graph.add_node(Person, _id="identifier", _label="Person2", fname="person2_firstname", lname="person2_lastname", identifier="id_person2")

# Les relations présentes dans la ligne du CSV sont configurées pour le graphe
csv_to_graph.add_edge(Relation, start_node="Person1", end_node="Person2", type="relation_type", mechanism="relation_mechanism", date="relation_date")

print(csv_to_graph.create_graph())
