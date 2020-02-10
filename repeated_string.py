def repeatedString(s, n):
    length = len(s)
    multiplier = n // length
    remainder = n % length
    new_string = s * multiplier
    for i in range(remainder):
        new_string += s[i]
    a_count = 0
    for i in new_string:
        if i == "a":
            a_count += 1
    return a_count


print(repeatedString("aba", 10))
# output should be 7



# got a time-out error here: trying again below:
def repeatedString2(s, n):
    a_count = 0
    for char in s:
        if char == "a":
            a_count += 1
    multiplier = n // len(s)
    a_count *= multiplier
    remainder = n % len(s)
    for i in range(remainder):
        if s[i] == "a":
            a_count += 1
    return a_count

print(repeatedString("aba", 10))
print(repeatedString2("a", 1000000000000))
