with open('data.txt') as f:
    data = f.read().split()

connections = {}
triangles = set()

for connection in data:
    src, dst = connection.split("-")
    if src in connections: connections[src].add(dst)
    else: connections[src] = {dst}

    if dst in connections: connections[dst].add(src)
    else: connections[dst] = {src}

    intersect = connections[src].intersection(connections[dst])
    for item in intersect:
        triangles.add(tuple(sorted((src, dst, item))))

print(len([*filter(lambda x: x[0][0] == "t" or x[1][0] == "t" or x[2][0] == "t", triangles)]))