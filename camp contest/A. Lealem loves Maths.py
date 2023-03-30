# s = input()

# for i in range(len(s)):
# 	if s[i] != "+":
# 		minu = int(s[i])
# 	else:
# 		continue
# 	for j in range(i, len(s)):
# 		if s[j] != "+":
# 			minuj = int(s[j])
# 			if minuj < minu:
# 				minuj, minu = minu, minuj

# 		else:
# 			continue
# print(s)

word = input()
ucount = 0
lcount = 0

for i in word: 
	if i.isupper():
		ucount += 1
	else:
		lcount += 1
if ucount > lcount:
	print(word.upper())
else:
	print(word.lower())
