import random
import string

st = input("Enter message: ")
words = st.split(" ")
coding = input("1 for Encryption or 0 for Decryption: ")
coding = True if (coding == "1") else False;
#print(coding)

def generate_random_string(length):
    characters = string.ascii_lowercase
    return ''.join(random.choice(characters) for _ in range(length))

r1 = generate_random_string(3)
r2 = generate_random_string(3)

if(coding):
    nwords = []
    for word in words:
        if(len(word) >= 1):
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords = []
    for word in words:
        if(len(word) >= 1):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))