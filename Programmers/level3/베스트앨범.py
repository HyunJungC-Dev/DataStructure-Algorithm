def solution(genres, plays):
    answer = []
    ht1 = dict()  # 장르별로 플레이 횟수가 더해서
    ht2 = dict()  # 각 장르의 노래들이 idx와 play횟수로 묶여서 들어간다.
    for i, elem in enumerate(zip(genres, plays)):
        g, p = elem
        if g not in ht1:
            ht1[g] = 0
            ht2[g] = []
        ht1[g] += p
        ht2[g].append((i, p))
        # (g, p)        # -p : play 횟수의 내림차순대로 sort or x[1]해서 reversed True해도 괜찮음.
    sort_ht1 = sorted(list(ht1.items()), key=lambda x: -x[1])

    for g, p in sort_ht1:
        sort_ht2 = sorted(ht2[g], key=lambda x: -x[1])
        # 2개가 안되면 알아서 하나만 들어간다.
        answer += list(map(lambda x: x[0], sort_ht2))[:2]
