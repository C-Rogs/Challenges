class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort() #so that duplicates will be next to eachother 

        #DFS to recusively search for ways of achieving the target value
        def search(start, path, remaining):
            if remaining == 0:
                result.append(path)
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates [i -1]: 
                    continue #skip duplicates

                if candidates[i] > remaining:
                    break  #finish loop if sum will exceed target
                
                search(i + 1, path + [candidates[i]], remaining - candidates[i])
        
        search(0, [], target)
        return result