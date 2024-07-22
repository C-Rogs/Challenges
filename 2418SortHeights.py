class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tups = sorted(zip(heights,names),reverse = True)
        people = list(map(lambda x: x[1], tups))
        return people