import os, hashlib

def md5(fname, chunks_of_4K=1):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        chunks = 0
        for chunk in iter(lambda: f.read(4096), b""):
            chunks += 1
            if chunks > chunks_of_4K: break
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def different(path1, path2):
    os.system('cmp "%s" "%s" > cmp.txt' % (dict1[m][i], dict1[m][j]))
    x = file('cmp.txt', 'r').read().strip()
    return x==''


    
dict1 = {}
roots = ['/mnt/hgfs/D/backup12/Beannie',
]
skips = ['README.TXT']

count = 0
for root in roots:
    for root,dirs,filenames in os.walk(root):
        for filename in filenames:
            if any([x in filename for x in skips]): continue
            #count += 1
            #if count % 1000 == 0:
            #    print "file #", count
            path = os.path.join(root, filename)
            m = md5(path)
            if not dict1.has_key(m):
                dict1[m] = [path]
            else:
                dict1[m].append(path)
                print "md5:", m
                while 1:
                    if len(dict1[m]) <= 1:
                        break
                    for i,x in enumerate(dict1[m]):
                        print "  %s. %s" % (i, x)

                    same_found = False
                    for i,x in enumerate(dict1[m]):
                        for j,x in enumerate(dict1[m]):
                            if i >= j: continue
                            if different(dict1[m][i], dict1[m][j]): 
                                print "%s,%s: different!!!" % (i,j)
                            else:
                                print "%s,%s: same" % (i,j)
                                same_found = True
                    if not same_found: break
                    option = raw_input("enter index to delete or press enter to skip delete: ")
                    option = option.strip()
                    if option == "": break
                    try:
                        i = int(option); #print "i:", i
                        path = dict1[m][i]; #print "path:", path
                        try:
                            option = raw_input('rm %s? ' % path)
                            if option=='y':
                                os.remove(path)
                                del dict1[m][i]
                        except Exception as e:
                            print e
                    except:
                        print "invalid index ... try again"
                    
