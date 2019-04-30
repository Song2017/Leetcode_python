# 迪克斯特拉算法： 计算加权图中的最短路径
# graph: 起点start，a,b,终点fin之间的距离
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["a"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}
# costs: 起点到 a,b,fin的开销
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = float("inf")
# parents： 存储父节点，记录最短路径
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
# processed: 记录处理过的节点，避免重复处理
processed = []


# 返回开销最低的点
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    # print(lowest_cost_node, costs)
    return lowest_cost_node


# Dijkstra implement
# 先找离起点最近的顶点
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    # 比较当前顶点的所有邻居顶点, 得到局部最优解
    neighbors = graph[node]
    print(node, neighbors, neighbors.keys())
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # 更新起点到所有顶点的距离
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print(processed, parents)
