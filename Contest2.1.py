Text = input()
Pattern = input()
p = 110
x = 589
# xt=300

len_t = len(Text)
len_p = len(Pattern)

d = {}
for i in range(len_t):
    if Text[i] not in d:
        d[Text[i]] = i

Hash = (x**(len_p-1)) % p
Hash_pattern = Hash_text = 0

result = []

for i in range(len_p):
    Hash_pattern = (x*Hash_pattern+d[Pattern[i]]) % p
    Hash_text = (x*Hash_text+d[Text[i]]) % p

for s in range(len_t-len_p+1):
    if Hash_pattern == Hash_text:
        match = True

        for i in range(len_p):
            if Pattern[i] != Text[s+i]:
                match = False
                break

        if match:
            result.append(s)

    if s < len_t-len_p:
        Hash_text = (Hash_text-Hash*d[Text[s]]) % p
        Hash_text = (Hash_text*x+d[Text[s+len_p]]) % p
        Hash_text = (Hash_text+p) % p
        # Hash_text=(Hash_text*x-d[Text[s]]*xt+d[Text[s+len_p]])%p

print(*result)
