from collections import defaultdict

class DirectedEdge:
    """Class to represent a directed edge with weight."""
    def __init__(self, from_vertex, to_vertex, weight, index):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight
        self.index = index

    def __repr__(self):
        return f"({self.from_vertex}, {self.to_vertex}, {self.weight:.2f})"

class EdgeWeightedDigraph:
    """Class to represent an edge-weighted directed graph using a hash table (dictionary)."""
    def __init__(self):
        self.V = 0
        self.E = 0
        self.adj = defaultdict(list)  # Dictionary where each key is a vertex and value is a list of edges
        self.edge_counter = 0  # Track insertion order globally

    def add_edge(self, v, w, weight):
        """Adds a directed edge to the graph while keeping the order from the file."""
        edge = DirectedEdge(v, w, weight, self.edge_counter)
        self.edge_counter += 1
        self.adj[v].append(edge)  # Append to maintain file order

    def print_graph(self):
        """Prints the adjacency list in sorted order while maintaining insertion order per vertex."""
        for vertex in sorted(self.adj.keys()):  # Ensure vertex order is sorted (adj[0], adj[1], etc.)
            edges_str = " -> ".join(str(edge) for edge in self.adj[vertex][::-1])  # Reverse the list before printing
            print(f"adj[{vertex}] -> {edges_str}")

    def load_graph_from_file(self, filename):
        """Loads the graph from a text file."""
        try:
            with open(filename, "r") as file:
                lines = [line.strip() for line in file if line.strip()]  # Remove empty lines

                if len(lines) < 2:
                    raise ValueError("Error: File must contain at least two lines for V and E.")

                # Handle case where V and E are on separate lines
                if len(lines[0].split()) == 1 and len(lines[1].split()) == 1:
                    self.V = int(lines[0])  # First line contains V
                    self.E = int(lines[1])  # Second line contains E
                    edge_lines = lines[2:]  # Edges start from line 3
                else:
                    self.V, self.E = map(int, lines[0].split())  # First line contains V and E together
                    edge_lines = lines[1:]  # Edges start from line 2

                # Read and add edges in the **exact order from the file**
                for line in edge_lines:
                    parts = line.split()
                    if len(parts) != 3:
                        print(f"Warning: Skipping invalid line -> {line.strip()}")
                        continue 

                    v, w, weight = map(str.strip, parts)
                    self.add_edge(int(v), int(w), float(weight))
        except FileNotFoundError:
            print("Error: File not found!")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

def hashtable_demo():
    """Function to load and print the edge-weighted directed graph."""

    graph = EdgeWeightedDigraph()  
    graph.load_graph_from_file("./utils/tinyEWD.txt")  
    graph.print_graph()  

if __name__ == "__main__":
    hashtable_demo()