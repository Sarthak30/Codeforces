for i in range(input()):
    S = list(raw_input())
    ret = []
    for b in [1, 2, 3, 4, 6, 12][::-1]:
        a = 12 / b
        tmp = [S[k::b] for k in range(b)]
        for x in tmp:
            if not 'O' in set(x):
                ret.append("%dx%d" % (12 / b, b))
                break
    print len(ret), ' '.join(ret)
