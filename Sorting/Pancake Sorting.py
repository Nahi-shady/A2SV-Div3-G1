class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []
        for i in range(n, 0, -1):
            max_idx = arr.index(i)
            if max_idx == i-1:
                continue
            if max_idx > 0:
                arr[:max_idx+1] = arr[:max_idx+1][::-1]
                result.append(max_idx+1)
            arr[:i] = arr[:i][::-1]
            result.append(i)
        return result

        