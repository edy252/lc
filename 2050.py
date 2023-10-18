class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0] * n

        maxTime = [0] * n
        # for i in range(1, n+1):
        #     max_incoming_val[i] = time[i-1]

        graph = collections.defaultdict(list)
        for relation in relations:
            graph[relation[0]-1].append(relation[1]-1)
            indegree[relation[1]-1] += 1
        q = []

        for node, indegree_val in enumerate(indegree):
            # If node with no indegree, that means there is no dependency on it, and thus maxtime to get from any node to this node is time[node]
            if indegree_val == 0:
                q.append(node)
                maxTime[node] = time[node]

        while q:
            node = q.pop(0)
            for neighbor in graph[node]:
                maxTime[neighbor] = max(maxTime[neighbor], maxTime[node] + time[neighbor])

                # If we don't dec indegree of a neighbor that still has indegrees, we will move to deeper neighbors without completely calculating the complete maxtime of this neighbor. 
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)


        # print(maxTime)      



        return max(maxTime)