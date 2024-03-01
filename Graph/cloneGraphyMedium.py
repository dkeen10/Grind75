# https://leetcode.com/problems/clone-graph/description/


"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
"""

from typing import Optional
import collections


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    
    def DFS(self, node, cloned_nodes):
        neighbour = []
        clone = Node(node.val)
        cloned_nodes[node] = clone
        for it in node.neighbors:
            if it not in cloned_nodes:
                neighbour.append(self.dfs(it, cloned_nodes))
            else:
                neighbour.append(cloned_nodes[it])
        clone.neighbors = neighbour
        return clone


    def cloneGraph_DFS(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloned_nodes = {}
        if not node.neighbors:
            clone = Node(node.val)
            return clone
        return self.dfs(node, cloned_nodes)
    

    # def __init__(self):
    #     # Initialize an empty unordered map to keep track of nodes that have already been cloned.
    #     self.cloningGraph = {}


    def cloneGraph_DFS_v2(self, node: Optional['Node']) -> Optional['Node']:
        # Check if the input node is null. If it is, return null.
        if not node:
            return None
        
        # Check if the input node already exists in the map. If it does, return its corresponding clone.
        if node in self.cloningGraph:
            return self.cloningGraph[node]
        
        # If the node is new, create a new clone with the same value as the input node and add it to the map.
        clone = Node(node.val, [])
        self.cloningGraph[node] = clone

        # Iterate through each of the input node's neighbors and recursively clone them, adding them to the clone's list of neighbors.
        for neighbor in node.neighbors:
            clone.neighbors.append(self.cloneGraph_DFS_v2(neighbor))

        return clone


    def cloneGraph_BFS(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        ump = {}
        # To find the neighbours present or not in constant time

        qu = collections.deque()
        # For bfs traversal
        ump[node] = Node(node.val, [])
        qu.append(node)
        while qu:
            curr = qu.popleft()

            for it in curr.neighbors:
                if it not in ump:
                    ump[it] = Node(it.val, [])
                    qu.append(it)
                ump[it].neighbors.append(ump[curr])
        return ump[node]
    

    def cloneGraph_V3(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited = {} # dictionary to store the cloned nodes
        
        def dfs(node):
            if node in visited:
                return visited[node] # if node already visited, return the corresponding cloned node
            
            clone_node = Node(node.val, []) # create a new clone node
            
            visited[node] = clone_node # add the original node and its clone to the dictionary
            
            for neighbor in node.neighbors: # visit all the neighbors of the node
                clone_node.neighbors.append(dfs(neighbor)) # if neighbor not visited, create a new clone node and append to the neighbors list of the clone node we are currently visiting. Otherwise, append the corresponding cloned node to the neighbors list.
            
            return clone_node
        
        return dfs(node) # start DFS from the first node and return its clone


def main():
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    sol = Solution()
    print(sol.cloneGraph(adjList))


if __name__ == "__main__":
    main()
