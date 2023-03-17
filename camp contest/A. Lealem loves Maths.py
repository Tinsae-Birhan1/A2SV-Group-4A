s = input()

for i in range(len(s)):
	if s[i] != "+":
		minu = int(s[i])
	else:
		continue
	for j in range(i, len(s)):
		if s[j] != "+":
			minuj = int(s[j])
			if minuj < minu:
				minuj, minu = minu, minuj

		else:
			continue
print(s)
