def GenomicRangeQuery(S, P, Q):
    # A=1, C=2, G=3, T=4. P[k] represents start of substring and Q[k] represents end
    # find least valuable nucleotide in substring
    adenine_last_seen = [-1] * len(S)
    cytosine_last_seen = [-1] * len(S)
    guanine_last_seen = [-1] * len(S)
    thymine_last_seen = [-1] * len(S)
        
    for i in range(len(S)):
        calcPSums(S, adenine_last_seen, 'A', i)
        calcPSums(S, cytosine_last_seen, 'C', i)
        calcPSums(S, guanine_last_seen, 'G', i)
        calcPSums(S, thymine_last_seen, 'T', i)
    
    answers = [0] * len(P)
    for j in range(len(P)):
        if adenine_last_seen[Q[j]] >= P[j]:
            answers[j] = 1
        elif cytosine_last_seen[Q[j]] >= P[j]:
            answers[j] = 2
        elif guanine_last_seen[Q[j]] >= P[j]:
            answers[j] = 3
        else:
            answers[j] = 4
    return answers
    
def calcPSums(S, last_seen, C, i):
    if S[i] == C:
        last_seen[i] = i
    elif i > 0:
        last_seen[i] = last_seen[i-1]
