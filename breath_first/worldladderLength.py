    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)   

        visited = set()
        que = deque()

        visited.add(beginWord)
        que.append(beginWord)

        level = 0
        while len(que) > 0:

            for _ in range(len(que)):

                cur = que.popleft()
                if cur == endWord:
                    return level+1;

                for i in range(len(cur)):
                    for j in range(97,97+26):
                        nbr = cur[0:i] + chr(j) + cur[i+1:]

                        if nbr in visited: 
                            continue

                        if nbr not in wordList:
                            continue

                        visited.add(nbr)
                        que.append(nbr)
            level += 1
            
        return 0 
