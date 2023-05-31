class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for path in paths:
            directory, *files = path.split(' ')
            for file in files:
                name, content = file.split('(')
                dic[content].append(directory + '/' + name)

        return [i for i in dic.values() if len(i)>1]