import random
file = open("codebusters_test.txt", "w")

def unspace(c):
    ns = ""
    for i in c:
        if (ord(i) < 65 or ord(i) > 90) or (ord(i) < 97 and ord(i) > 122):
            continue
        ns += i
    return ns

def upper(l):
    if ord(l) >= 97 and ord(l) <= 122:
        return chr(ord(l) - 32)
    elif (ord(l) >= 65 and ord(l) <= 90) or ord(l) == 32:
        return l
    return ""

def lower(l):
    if ord(l) >= 65 and ord(l) <= 90:
        return chr(ord(l) + 32)
    elif (ord(l) >= 97 and ord(l) <= 122) or ord(l) == 32:
        return l
    return ""

CIPHER_TYPE = "aristocrat"

HINT = True

pref = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth", "twenty-first", "twenty-second", "twenty-third", "twenty-fourth", "twenty-fifth", "twenty-sixth", "twenty-seventh"]

TEST_LENGTH = random.randrange(12, 18)

qnum = 0

cs = ["Aristocrat", "Patristocrat", "Xenocrypt", "Affine1"]

for _ in range(0, TEST_LENGTH):
    qnum += 1

    CIPHER_TYPE = random.randrange(0, len(cs))

    uc = cs[CIPHER_TYPE]
    #uc = cs[3]

    print("QUESTION", str(qnum) + ":")

    if uc == "Aristocrat" or uc == "Patristocrat" or uc == "Xenocrypt":

        arr = [i for i in range(0, 26)]

        shuf = []

        for i in range(0, 26):
            sh = random.randrange(len(arr))
            while sh == len(shuf):
                sh = random.randrange(len(arr))
            shuf.append(arr[sh])
            del arr[sh]

        if uc == "Xenocrypt":
            quotes = open("spanquotes.txt", "r").read()
        else:
            quotes = open("quotes.txt", "r").read()
        quotes = quotes.split("--")


        fst = True
        author = ""

        while fst or len(qi) < 56 or len(qi) > 126:
            fst = False
            qi = quotes[random.randint(3, len(quotes) - 1)]
            oqi = qi
            author = qi[:qi.index("\"")].split("\n")[0]
            qi = qi[qi.index("\"")+1:]
            if "\"" in qi:
                qi = qi[:qi.index("\"")]
            qi = "".join([upper(i) for i in qi])
            oqi = qi
            if CIPHER_TYPE == 1:
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


        print("\nSolve this", uc, " which is a quote by", author)

        if HINT:
            oo = oqi.split(" ")
            oo = oqi.split(" ")
            ind = 0
            while len(oo[ind]) < 3 or len(oo[ind]) > 5:
                ind += 1
            print("The", pref[ind], "word of the message is", oo[ind])
        print("\n")
        print(qi)
        #print(oqi)
        print("\n")
        print(st)
        print(nst, "\n\n")

    elif uc == "Affine1":

        quotes = open("quotes.txt", "r").read()
        quotes = quotes.split("--")


        fst = True
        author = ""

        while fst or len(qi) < 30 or len(qi) > 50:
            qi = quotes[random.randint(3, len(quotes) - 1)]
            fst = False
            #author = qi[:qi.index("\"")].split("\n")[0]

        a = random.randrange(0, 26)
        b = random.randrange(0, 26)

        print("\nEncode this quote by " + author + " as an affine cipher, with values of a=" + str(a) + " and b=" + str(b) + "\n\n")
        print("".join([upper(i) for i in list(qi)]), "\n\n")
