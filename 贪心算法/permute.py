def permutation(nums, p, q, s):
    if p == q:
        s.append(list(nums))
    else:
        for i in range(p, q):
            nums[i], nums[p] = nums[p], nums[i]
            permutation(nums, p + 1, q, s)
            nums[i], nums[p] = nums[p], nums[i]
    return s


if __name__ == '__main__':

    vlist = ['b', 'ba', 'ab']
    result = permutation(vlist, 0, len(vlist), [])
    for i in result:
        print(i)
