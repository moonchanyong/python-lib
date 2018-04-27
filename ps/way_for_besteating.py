def eatCookie(cookies):
    answer=[]

    for i,v in enumerate(cookies):
        if i == 0:
            answer.append(1)
            continue
        idx_idx = 0
        max_ = -1
        for idx,value in enumerate(cookies[:i]) :
            if value < v and answer[idx] > max_:
                max_ = answer[idx]
                idx_idx = idx
        if max_ == -1:
            answer.append(1)
        else:
            answer.append(max_+1)

    return max(answer)

print(eatCookie([1, 4, 2, 6, 3, 4, 1, 5]))
