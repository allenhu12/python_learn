import jieba
f = open("白鹿原.txt")
ls = jieba.lcut(f.read())
A = set(ls)
maxw = ""
for w in A:
    if len(w) > len(maxw):
        maxw = w
    if len(w) == len(maxw) and w > maxw:
        maxw = w
print(maxw)
f.close()
