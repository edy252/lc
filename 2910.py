class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        freq = Counter(nums)
        freqct = freq.values()

        min_groups = float('inf')
        # Can all groups be decomposed into groups of size groupsize or size groupsize+1?
        for groupsize in range(1, min(freqct)+1):
            this_groups = 0

            # print()
            # print('groupsize', groupsize)

            for thissize in freqct:
                groups = thissize // (groupsize)
                remainder = thissize % (groupsize)

                # We skip if remainder > number of groups because we cannot completely distribute remainder among groups, using this groupsize or groupsize+1
                if remainder > groups:
                    this_groups = float('inf')
                    break

                # By now, thissize is guaranteed to be distributed into either groupsize or groupsize+1 arrays
                this_groups += ceil(thissize / (groupsize+1))
                # print('added', ceil(thissize / (groupsize+1)), 'this_groups', this_groups)

            min_groups = min(min_groups, this_groups)

            

        return min_groups 