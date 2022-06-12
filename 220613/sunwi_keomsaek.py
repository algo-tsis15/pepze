#시간초과

def ispassed(p_s, q_s):
    for i in range(4):
        if (q_s[i] != '-') and (p_s[i] != q_s[i]):
            return False
    if (q_s[4] != '-') and (int(p_s[4]) < int(q_s[4])):
        return False
    return True

def solution(info, query):
    answer = []
    for q in query:
        q_s = q.split()
        q_s = q_s[::2] + q_s[-1:]
        cnt = 0
        for person in info:
            p_s = person.split()
            if (ispassed(p_s, q_s)):
                cnt += 1
        answer.append(cnt)
    return answer
