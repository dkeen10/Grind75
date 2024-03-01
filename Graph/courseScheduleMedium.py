# https://leetcode.com/problems/course-schedule/description/

"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        Kahn's algorithm is used to find the topological ordering of a Directed Acyclic Graph (DAG).  It is a greedy algorithm that selects the nodes in a graph in a way that the nodes with no incoming edges are selected first.  The algorithm works by first finding the nodes with no incoming edges and adding them to a queue.  Then, the algorithm removes the edges from the graph that are connected to the nodes in the queue.  The algorithm continues to find the nodes with no incoming edges and adds them to the queue.  The algorithm continues until the queue is empty.  If the graph is a DAG, then the algorithm will return a topological ordering of the graph.  If the graph is not a DAG, then the algorithm will return an empty list.
        There is no topological sorting for a graph that is cyclic.

        param numCourses: int dipicting the number of courses
        param prerequisites: list[list[int]] - a list of prerequisites for each course

        return: bool - True if all courses can be finished, False otherwise
        """

        # indegree is the number of incoming edges to a node. here we initialize the indegree array with 0s
        indegree = [0] * numCourses

        # adj is the adjacency list of the graph
        adjacency_list = [[] for x in range(numCourses)]
        
        # populate the adjacency list and the indegree array
        for prereq in prerequisites:
            # add the prereq to the adjacency list
            adjacency_list[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1
        
        # create a queue to store the nodes with no incoming edges
        queue = []

        # add the nodes with no incoming edges to the queue
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        # initialize the number of visited nodes
        visited = 0

        # if the queue is empty, then there is a cycle in the graph
        # while the queue is not empty, remove the edges from the graph that are connected to the nodes in the queue
        while queue:

            
            node = queue.pop(0)
            visited += 1
            # for each neighbor of the node, remove the edge from the graph
            for neighbor in adjacency_list[node]:
                indegree[neighbor] -= 1
                # if the neighbor has no incoming edges, add it to the queue
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # if the number of visited nodes is equal to the number of courses, then all courses can be finished
        return numCourses == visited

   

def main():
    numCourses = 2
    prerequisites = [[1,0]]
    print(Solution().canFinish(numCourses, prerequisites))

    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(Solution().canFinish(numCourses, prerequisites))
    

if __name__ == "__main__":
    main()