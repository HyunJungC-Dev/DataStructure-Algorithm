def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    can_borrow = 0
    for i in set_lost:
        if i - 1 in set_reserve:
            set_reserve.remove(i - 1)
            can_borrow += 1
        elif i + 1 in set_reserve:
            set_reserve.remove(i + 1)
            can_borrow += 1
    return n - len(set_lost) + can_borrow
