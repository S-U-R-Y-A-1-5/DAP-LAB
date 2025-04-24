sentence = "the sky is blue and the grass is green"
words=sentence.split()
seen=set()
has_duplicates=False
for i in words:
    if i in seen:
        has_duplicates=True
    else:
        seen.add(i)
print(f"{sentence} Has Duplicates:{has_duplicates}")

