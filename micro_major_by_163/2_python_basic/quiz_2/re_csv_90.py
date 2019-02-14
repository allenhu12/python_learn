before_ls = []
after_ls = []
ls1=[]
#try:
tf = open("data.csv","r",encoding="utf-8")
for line in tf.readlines():
    if line != "":
        ls = line.split(',')
        before_ls.append(line.strip("\n").split(","))
print(before_ls)
tf.close()
line_lenghth = len(before_ls[0])
line_number = len(before_ls)
print(line_lenghth,line_number)
i = 0
j = 0
tf = open("data1.csv","w+",encoding="utf-8")
for i in range(0,line_lenghth):
    ls1 = []
    for j in range(0,line_number):
        ls1.append(before_ls[line_number-j-1][i])
    outline = ""
    out_line = ",".join(ls1)
    out_line += "\n"
    after_ls.append(out_line.strip(" "))
print(after_ls)
tf.writelines(after_ls)
tf.close()
#except:
#    print("open file error")

