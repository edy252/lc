class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = list(pref)

        running_xor = arr[0]
        for i in range(1, len(arr)):
            arr[i] ^= running_xor
            running_xor ^= arr[i]

        return arr