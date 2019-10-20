import random

CIPHER_TYPE = "aristocrat"

HINT = True

pref = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth", "twenty-first", "twenty-second", "twenty-third", "twenty-fourth", "twenty-fifth", "twenty-sixth", "twenty-seventh"]

uc = list(CIPHER_TYPE)

uc[0] = upper(uc[0])

uc = "".join(uc)


def unspace(c):
    ns = ""
    for i in c:
        if (ord(i) < 65 or ord(i) > 90) and (ord(i) < 97 and ord(i) > 122):
            continue
        ns += i
    return ns

def upper(l):
    if ord(l) >= 97 and ord(l) <= 122:
        l = chr(ord(l) - 32)
    return l

def lower(l):
    if ord(l) >= 65 and ord(l) <= 90:
        l = chr(ord(l) + 32)
    return l

arr = [i for i in range(0, 26)]

shuf = []

for i in range(0, 26):
    sh = random.randrange(len(arr))
    while sh == len(shuf):
        sh = random.randrange(len(arr))
    shuf.append(arr[sh])
    del arr[sh]

quotes = open("quotes.txt", "r").read()

quotes = quotes.split("--")


fst = True
author = ""

while fst or len(qi) < 56 or len(qi) > 126:
    fst = False
    qi = quotes[random.randint(3, len(quotes) - 1)]
    author = qi[:qi.index("\"")].split("\n")[0]
    qi = qi[qi.index("\"")+1:]
    if "\"" in qi:
        qi = qi[:qi.index("\"")]
    qi = "".join([upper(i) for i in qi])
    oqi = qi
    if CIPHER_TYPE == "patristocrat":
        qi = unspace(qi)
    ns = ""
    for i in qi:
        if ord(i) < 65 or ord(i) > 90:
            ns += i
            continue
        ns += chr(shuf[ord(i) - 65] + 65)
    qi = ns

st = "   ".join([chr(i + 65) for i in range(0, 26)])

nst = ""

for i in range(0, 26):
    num = qi.count(chr(i + 65))
    nst += str(num)
    if num < 10:
        nst += "   "
    else:
        nst += "  "


print("Codebusters Test Question: \n\nSolve this", uc, " which is a quote by", author)
if HINT:
    oo = oqi.split(" ")
    if random.randrange(2) == 0:
        oo = oqi.split(" ")
        ind = 0
        while len(oo[ind]) < 3 or len(oo[ind]) > 5:
            ind += 1
        print("The", pref[ind], "word of the message is", oo[ind])
    else:
        no = []
        for i in oo:
            no.append([len(i), i])
        no = [i[1] for i in sorted(no)[::-1]]
        print("The quote is about", "".join(unspace([lower(i) for i in no[0]])))
print("\n")
print(qi)
print("\n")
print(st)
print(nst)
