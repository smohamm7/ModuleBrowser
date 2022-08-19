import pkgutil as pkg   
libPath = 'C:\\Program Files (x86)\\Python3.9.10\\lib'
libPath = 'C:\\Program Files (x86)\\Python3.9.10\\lib'
libPath = 'C:\\Program Files (x86)\\Python3.9.10\\lib'
libPath = 'C:\\Program Files (x86)\\Python3.9.10\\lib'
libPath = 'C:\\Program Files (x86)\\Python3.9.10\\lib'
libPath = 'C:\\Program Files (x86)\\Python3.9.10\\lib'
libPath = 'C:\\Program Files (x86)\\Python3.9.10\\lib'
# print ("First LibPath is: ", libPath)
# available_modules = sorted(tuple(module_item.name for module_item in pkg.iter_modules() if module_item.module_finder.path == libPath and module_item.ispkg))
# print (available_modules)

# def displayModulePath():
# 		moduleList = list(pkg.iter_modules())
# 		seen = set()
# 		uniq = []
# 		pathList = []
# 		for i in moduleList:
# 			pathList.append(i[0])

# 		for x in pathList:
# 			if x not in seen:
# 				uniq.append(x)
# 				seen.add(x)

# 		uniqStr = []
# 		for i in uniq:
# 			i = str(i)
# 			uniqStr.append(i)

# 		for i in uniqStr:
# 			actualPath = i[12:-2]
# 			print ("Second LibPath is:",actualPath, type(actualPath))
            
#             print (available_modules)

# displayModulePath()

# modules = sorted(tuple(module_item.name for module_item in pkg.iter_modules() if module_item.module_finder.path == libPath and module_item.ispkg))
def available_modules1():
    for module_item in pkg.iter_modules():
        if module_item.module_finder.path ==  libPath and module_item.ispkg:
            print (sorted(tuple(module_item.name)))
available_modules1()

def available_modules2():
    available_modules = sorted(tuple(module_item.name for module_item in pkg.iter_modules() if module_item.module_finder.path == libPath and module_item.ispkg))
    print (available_modules)
available_modules2()