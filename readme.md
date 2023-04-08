# csv2graph

`'csv2graph'` is a Python class that can read a CSV file and create a NetworkX graph from its content.
Description

The csv2graph class can read a CSV file and create a NetworkX graph from it, where the nodes and edges are defined by
the columns of the CSV file. The class provides methods to add nodes and edges to the graph, and allows to specify the
data to be stored in the nodes and edges. It also allows to define the mapping between the columns of the CSV file and
the attributes of the nodes and edges.
Installation

The class can be installed via pip:

```commandline
pip install csv2graph
```

## Example

This is an example of a CSV file that can be used to create a graph:

```csv
id,id_person1,person1_firstname,person1_lastname,id_person2,person2_firstname,person2_lastname,relation_type,relation_mechanism,relation_date
1,1,Alice,Smith,2,Bob,Jones,Friend,Introduction,2022-02-18
2,3,Charlie,Chan,4,David,Lee,Colleague,Work,2021-11-05
3,2,Bob,Jones,3,Charlie,Chan,Friend,Shared Interest,2020-03-21
4,4,David,Lee,1,Alice,Smith,Enemy,Personal Conflict,2019-09-12
```

For this example, I created two classes, Person and Relation, that represent the nodes and edges of the graph.

```python
# This is the class that represents the nodes of the graph
class Person:
    fname = ""
    lname = ""

# This is the class that represents the edges of the graph
class Relation:
    type = ""
    mechanism = ""
    date = ""
```

The following code creates a graph where each row of the CSV file represents a relation between two persons, and where
the attributes of the nodes are the first and last names of the persons. 

```python
import csv2graph

# Create the csv2graph object
csv2graph_obj = csv2graph('data.csv')

# Add nodes to the graph
csv2graph_obj.add_node(Person, _id="identifier", _label="Person1", firstname='person1_firstname',
                       lastname='person1_lastname')
csv2graph_obj.add_node(Person, _id="identifier", _label="Person2", firstname='person2_firstname',
                       lastname='person2_lastname')

# Add edges to the graph
csv2graph_obj.add_edge(Relation, start_node="Person1", end_node="Person2", type="relation_type",
                       mechanism="relation_mechanism", date="relation_date")

# Create the graph
graph = csv2graph_obj.create_graph()

# Print the nodes and edges of the graph
print(graph.nodes())
print(graph.edges())
```

## Tests

The class comes with a test suite that can be run via pytest:

```commandline
pytest csv2graph.py
```

## Dependencies

The class depends on the following Python packages:

    networkx
    pandas