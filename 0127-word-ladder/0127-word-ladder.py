class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        allowance = set(wordList)
        
        n = len(beginWord)
        start = 97
        span = 26
        
        queue = deque([beginWord])
        seen = {beginWord}
        steps = 1
        
        while queue:
            for _ in range(len(queue)):
                word = queue.pop()
                if word == endWord:
                    return steps
                for i in range(n):
                    for j in range(start, start + span):
                        nextWord = word[:i] + chr(j) + word[i+1:]
                        if nextWord in allowance and nextWord not in seen:
                            seen.add(nextWord)
                            queue.appendleft(nextWord)
            steps += 1
        return 0