# -*- coding: utf-8 -*-
#
# Nom du fichier:       csv2graph.py
# Date de création:     08/04/2023
# Version:              0.0.1
# Auteur:               Simon STEPHAN <simon.stephan@u-bourgogne.fr>
#
# Copyright (c) 2023,
# Tous droits réservés. 
#
import networkx as nx
import pandas as pd


class csv2graph:

    def __init__(self, filename):

        # CSV file
        self.filename = filename

        # Graph
        self.graph = nx.MultiGraph()

        # Alignments
        self.nodes_alignments = {}
        self.edges_alignments = {}

        # edges and nodes
        self.nodes = {}
        self.edges = []

    def read_csv(self, **kwargs):
        df = pd.read_csv(self.filename, **kwargs)
        return df

    def add_node(self, node_class, _id, _label=None, _datas="_", **kwargs):

        if _label is None:
            _label = node_class.__name__

        lbl = _label
        count = len(self.nodes_alignments)
        while self.nodes_alignments.get(_label) is not None:
            _label = f"{lbl}_{count}"
            count += 1

        self.nodes_alignments[_label] = {
            "_id": _id,
            "_datas": _datas,
            "_class": node_class,
            **kwargs
        }

    def add_edge(self, edge_class, start_node, end_node, _id=None, _label=None, oriented=False, _datas="_", **kwargs):

        if _label is None:
            _label = edge_class.__name__

        lbl = _label
        count = len(self.edges_alignments)
        while self.edges_alignments.get(_label) is not None:
            _label = f"{lbl}_{count}"
            count += 1

        self.edges_alignments[_label] = {
            "_id": _id,
            "_datas": _datas,
            "_start_node": start_node,
            "_end_node": end_node,
            "_class": edge_class,
            "_oriented": oriented,
            **kwargs
        }

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def create_graph(self):

        # Read CSV file
        df = self.read_csv()

        nodes_dict = {}  # dictionnaire pour stocker les nodes existants

        for _, row in df.iterrows():
            # Create nodes
            nodes = {}
            for label, alignment in self.nodes_alignments.items():
                node_cls = alignment["_class"]()
                node_data = {}
                for key in alignment:
                    if key.startswith("_"): continue
                    val = row[alignment[key]]
                    if val is not None:
                        if hasattr(node_cls, key) or key == alignment["_id"]:
                            setattr(node_cls, key, row[alignment[key]])
                        else:
                            node_data[key] = row[alignment[key]]

                setattr(node_cls, alignment["_datas"], node_data)
                node_id = getattr(node_cls, alignment["_id"])
                if node_id in nodes_dict:  # si un node avec le même identifiant existe déjà
                    nodes[label] = nodes_dict[node_id]  # utilise le node existant
                else:
                    nodes[label] = node_cls
                    nodes_dict[node_id] = node_cls
                    # self.graph.add_node(node_cls)

            # Create edges
            for label, alignment in self.edges_alignments.items():
                edge = alignment["_class"]()
                edge_data = {}
                for key in alignment:
                    if key.startswith("_"): continue
                    val = row[alignment[key]]
                    if val is not None:
                        if hasattr(edge, key) or key == alignment["_id"]:
                            setattr(edge, key, row[alignment[key]])
                        else:
                            edge_data[key] = row[alignment[key]]
                setattr(edge, alignment["_datas"], edge_data)
                edge._orientation = alignment["_oriented"]
                edge._start_node = nodes[alignment["_start_node"]]
                edge._end_node = nodes[alignment["_end_node"]]
                self.edges.append(edge)

                edge_attrs = dict(vars(edge).items())
                self.graph.add_edge(edge._start_node, edge._end_node, **edge_attrs)

        # Return the list of nodes and edges
        return self.graph
