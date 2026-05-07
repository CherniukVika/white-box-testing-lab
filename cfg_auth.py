import ast
import networkx as nx
import matplotlib.pyplot as plt

# Читання коду
with open("auth.py", "r", encoding="utf-8") as f:
    code = f.read()

tree = ast.parse(code)
func = tree.body[0]  # перша функція

G = nx.DiGraph()

prev = []
counter = 0

for stmt in func.body:
    label = ast.unparse(stmt)
    node = f"n{counter}"
    G.add_node(node, label=label)
    for p in prev:
        G.add_edge(p, node)
    prev = [node]
    counter += 1

paths = list(nx.all_simple_paths(G, source="n0", target=prev[0]))

print("Шляхи виконання (all_simple_paths):")
for path in paths:
    print(path)

# Збереження графу
nx.nx_pydot.write_dot(G, "cfg.dot")

M = G.number_of_edges() - G.number_of_nodes() + 2
print("Цикломатична складність:", M)