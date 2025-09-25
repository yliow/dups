"""
Takes two paths path1, path2 and compares:

If path2 has a file X that is found in path1, ask user if he/she want to
delete X.
  
"""

import os, hashlib

def md5(fname, chunks_of_4K=1000):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        chunks = 0
        for chunk in iter(lambda: f.read(4096), b""):
            chunks += 1
            if chunks > chunks_of_4K: break
            hash_md5.update(chunk)
    return hash_md5.hexdigest()



def main(path1, path2, to_delete_substring):
    print "scanning path1:", path1
    dict1 = {}
    count = 0
    for root,dirs,filenames in os.walk(path1):
        for filename in filenames:
            #count += 1
            #if count % 1000 == 0:
            #    print "file #", count
            path = os.path.join(root, filename)
            m = md5(path)
            if not dict1.has_key(m):
                dict1[m] = [path]
            else:
                dict1[m].append(path)
                #for i,x in enumerate(dict1[m]):
                #    print i, x

    print "scanning path2"
    count = 0
    for root,dirs,filenames in os.walk(path2):
        for filename in filenames:
            #count += 1
            #if count % 1000 == 0:
            #    print "file #", count
            path = os.path.join(root, filename)
            m = md5(path)
            if not dict1.has_key(m):
                dict1[m] = [path]
            else:
                dict1[m].append(path)
                #print "md5:", m
                while 1:
                    if len(dict1[m]) <= 1:
                        break
                    if all([to_delete_substring not in _ for _ in dict1[m]]):
                        break
                    for i,x in enumerate(dict1[m]):
                        print "  %s. %s" % (i, x)

                    done = False
                    for i,x in enumerate(dict1[m]):
                        for j,x in enumerate(dict1[m]):
                            if not i < j: continue
                            if done: break
                            try:
                                if 'backup12' in dict1[m][i] and \
                                   to_delete_substring in dict1[m][j] and \
                                   os.path.split(dict1[m][i])[-1] == os.path.split(dict1[m][j])[-1]:

                                    os.system('diff "%s" "%s" > diff.txt' % (dict1[m][i], dict1[m][j]))
                                    diff = file('diff.txt', 'r').read().strip()
                                    if diff == '':
                                        #os.system('ls -la "%s"' % dict1[m][i])
                                        #os.system('ls -la "%s"' % dict1[m][j])
                                        print "> rm %s" % dict1[m][j]
                                        #option = raw_input("continue? ")
                                        option = 'y'
                                        if option == 'y':
                                            try:
                                                os.remove(dict1[m][j])
                                                del dict1[m][j]
                                            except Exception as e:
                                                print e
                                        done = True
                                        print
                            except Exception as e:
                                print e
                                print
                        if done: break
                    break
                    '''
                    else:
                        option = raw_input("enter index to delete or press enter to skip delete: ")
                        option = option.strip()
                        if option == "": break
                        try:
                            i = int(option); #print "i:", i
                            path = dict1[m][i]; #print "path:", path
                            try:
                                os.remove(path)
                                del dict1[m][i]
                            except Exception as e:
                                print e
                        except:
                            print "invalid index ... try again" 
                    '''

    # rm empty directory
    cmd = "find '%s' -type d -empty -delete" % path2
    os.system(cmd)

#import glob
#fs = glob.glob('/mnt/hgfs/D/backup10/My Documents/work/projects/*')
#gs = []
#for f in fs:
#    x = os.path.split(f)[-1]
#    gs.append(x)
gs = [0]
for g in gs:
    #directory = 'My Documents/work/projects/' + g
    #path1 = '/mnt/hgfs/D/backup12/%s' % directory
    #path2 = '/mnt/hgfs/D/backup12/%s' % directory
    #to_delete_subdir = '/Videos/'
                                            
    path1 = '/mnt/hgfs/D/backup12/Beannie' 
    path2 = '/mnt/hgfs/D/backup10/Beannie' 
    to_delete_substring = '/backup07/'
    main(path1, path2, to_delete_substring)
