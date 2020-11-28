def reverse(s):
    if len(s) < 2 or type(s) != str:
        return 'not good'

    backwords = []

    i = len(s) - 1

    while i >= 0:
        backwords.append(s[i])
        i = i - 1

    return backwords


result = reverse('my name is jay')

print(f"result:{result}")
