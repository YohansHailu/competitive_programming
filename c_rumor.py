# changed
def find(node, parents):
    if parents[node] == node:
        return node
    parents[node] = find(parents[node], parents)
    return parents[node]
 
def union(a, b, parents, rank):
    root_a = find(a, parents)
    root_b = find(b, parents)
 
    if rank[root_a] < rank[root_b]:
        root_a, root_b = root_b, root_a
 
    parents[root_b] = root_a
    rank[root_a] += rank[root_b]
 
 
 
n, m = map(int, input().split())
gold = map(int, input().split())
 
parents = {i:i for i in range(1,n+1)}
rank = {i:1 for i in range(1,n+1)}
 
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b, parents,rank)
 
costs = {} 
for node, cost in enumerate(gold, 1):
    root = find(node, parents)
 
    if root in costs:
        costs[root] = min(costs[root], cost)
    else:
        costs[root] = cost
 
print(sum(costs.values()))
