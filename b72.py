v=['a','e','i','o','u','A','E','I','O','U']
def vowel(s):
    for i in v:
        if i in s:
            return "yes"
    return "no"
s=list(input("Enter the string"))
print(vowel(s))
