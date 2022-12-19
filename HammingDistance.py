s1 = input("First String:")
s2 = input("Second String:")
distance = 0
if len(s1) != len(s2):
    print("Strings are not equal.")
    exit()
else:
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    print("Hamming distance: ", distance)
