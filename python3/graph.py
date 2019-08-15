import os
import random

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}


def bfs(graph, node):
    queue = list()
    queue.append(node)
    seen = set()
    seen.add(node)
    while len(queue) > 0:
        cur_node = queue.pop(0)
        print(cur_node)
        adj_nodes = graph[cur_node]
        for adj_node in adj_nodes:
            if adj_node not in seen:
                queue.append(adj_node)
                seen.add(adj_node)


def dfs(graph, node):
    stack = list()
    stack.append(node)
    seen = set()
    seen.add(node)
    while len(stack) > 0:
        cur_node = stack.pop()
        print(cur_node)
        adj_nodes = graph[cur_node]
        for adj_node in adj_nodes:
            if adj_node not in seen:
                stack.append(adj_node)
                seen.add(adj_node)


def dfs2(graph, node):
    def _dfs(graph, node):
        print(node)
        adj_nodes = graph[node]
        for adj_node in adj_nodes:
            if adj_node not in seen:
                seen.add(adj_node)
                _dfs(graph, adj_node)

    seen = set()
    seen.add(node)
    _dfs(graph, node)


def test():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['C', 'D'],
        'F': ['D']
    }
    dfs2(graph, 'A')


if __name__ == '__main__':
    test()
