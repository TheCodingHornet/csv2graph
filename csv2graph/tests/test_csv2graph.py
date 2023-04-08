# -*- coding: utf-8 -*-
#
# Nom du fichier:       ${FILE_NAME}
# Date de création:     08/04/2023
# Version:              0.0.1
# Auteur:               Simon STEPHAN <simon.stephan@u-bourgogne.fr>
#
# Copyright (c) 2023,
# Tous droits réservés. 
#
import unittest

import networkx as nx
from csv2graph import csv2graph


class Person: pass


class Relation: pass


class TestCsv2Graph(unittest.TestCase):

    def setUp(self):
        self.csv_filename = 'demofile.csv'
        self.graph_builder = csv2graph(self.csv_filename)

    def test_read_csv(self):
        df = self.graph_builder.read_csv()
        self.assertEqual(len(df), 21)

    def test_add_node(self):
        self.graph_builder.add_node(Person, _id="identifier", _label="Person1", fname="person1_firstname",
                                    lname="person1_lastname", identifier="id_person1")
        self.graph_builder.add_node(Person, _id="identifier", _label="Person2", fname="person2_firstname",
                                    lname="person2_lastname", identifier="id_person2")
        self.assertEqual(len(self.graph_builder.nodes_alignments), 2)
        self.assertIn('Person1', self.graph_builder.nodes_alignments)

    def test_add_edge(self):
        self.graph_builder.add_edge(Relation, start_node="Person1", end_node="Person2", type="relation_type",
                                    mechanism="relation_mechanism", date="relation_date")
        self.assertEqual(len(self.graph_builder.edges_alignments), 1)
        self.assertIn('Relation', self.graph_builder.edges_alignments)

    def test_create_graph(self):
        self.graph_builder.add_node(Person, _id="identifier", _label="Person1", fname="person1_firstname",
                                    lname="person1_lastname", identifier="id_person1")
        self.graph_builder.add_node(Person, _id="identifier", _label="Person2", fname="person2_firstname",
                                    lname="person2_lastname", identifier="id_person2")
        self.graph_builder.add_edge(Relation, start_node="Person1", end_node="Person2", type="relation_type",
                                    mechanism="relation_mechanism", date="relation_date")
        graph = self.graph_builder.create_graph()
        self.assertIsInstance(graph, nx.Graph)
        self.assertEqual(len(graph.nodes), 5)
        self.assertEqual(len(graph.edges), 21)


if __name__ == '__main__':
    unittest.main()
