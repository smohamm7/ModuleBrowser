import pkgutil as pkg

# print (list(pkg.iter_modules()))
# print (pkg.iter_modules())
moduleList = list(pkg.iter_modules())
seen = set()
uniq = []
pathList = []
for i in moduleList:
    pathList.append(i[0])
# print ("#################################################################")
# print (pathList)
# print ("#################################################################")
for x in pathList:
    if x not in seen:
        uniq.append(x)
        seen.add(x)
# print ("#################################################################")
# print (uniq)
# print ("#################################################################")
# print ("#################################################################")
# print (seen)
# print ("#################################################################")
uniqStr = []
for i in uniq:
    i = str(i)
    uniqStr.append(i)

for i in uniqStr:
    print (i[12:-2])


