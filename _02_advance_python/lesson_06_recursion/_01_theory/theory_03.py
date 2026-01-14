def count_workers(sp):
    res = 0
    for item in sp:
        if isinstance(item, int):
            res += item
        else:
            res += count_workers(item)
    return res


if __name__ == '__main__':
    count_Angola = 18
    count_New_York = [20, [10, 7]]
    count_Chicago = 15
    count_USA = [count_New_York, count_Chicago]
    count_all = [count_Angola, count_USA]
    print(count_all)
    print(count_workers(count_all))

