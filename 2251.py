from heapq import heappush, heappop

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # We sort by flower bloom start not flower bloom end because we want 
        flowers.sort()
        sorted_people = sorted(people)
        # We use people_map since sorted_people will not give the solution in order of people.
        people_map = {}
        min_heap = []
        # We always increment i and we do not look back because flowers that bloomed in the past may appear for later people. Even if we pop that flower, we will never push it again to heap because if it ended for person i, it will end for person i+1
        i = 0

        print(flowers)


        for people_i in sorted_people:
            # Add all flowers that bloom before or equal to people_i, and add their end times
            while i < len(flowers) and flowers[i][0] <= people_i:
                heappush(min_heap, flowers[i][1])
                # print(flowers[i][1])
                i += 1

            # Remove all flowers that ended before people_i
            while min_heap and min_heap[0] < people_i:
                heappop(min_heap)

            people_map[people_i] = len(min_heap)

        
        return [people_map[x] for x in people]