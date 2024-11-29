def common(strs):
    if not strs:
        return ""
    strs.sort()

    first_str = strs[0]
    last_str = strs[-1]
    result = []

    for i in range(len(first_str)):
        if i <= len(last_str) and first_str[i] == last_str[i]:
            result.append(first_str[i])
        else:
            break

    return ''.join(result)


strs = ["dog","racecar","car"]
print(common(strs))
