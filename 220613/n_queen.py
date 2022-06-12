# 시간초과

from itertools import permutations

def solution(n):
    answer = 0
    for case in permutations(range(n)):
        p = set()
        m = set()
        for i in range(n):
            if (i + case[i] in p) or (i - case[i] in m):
                break
            else:
                if i == (n - 1):
                    answer += 1
                    break
                p.add(i + case[i])
                m.add(i - case[i])
    return answer
