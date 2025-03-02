L, C = map(int, input().split())
arr = sorted(input().split())
vowels = {'a', 'e', 'i', 'o', 'u'}

def check(s):
    vowel_cnt = sum(1 for x in s if x in vowels)
    consonant_cnt = len(s) - vowel_cnt
    return vowel_cnt >= 1 and consonant_cnt >= 2


def sol(start, password):
    if len(password) == L:
        if check(password):
            print("".join(password))
        return

    for i in range(start, C):
        sol(i + 1, password + [arr[i]])

        
sol(0, [])
