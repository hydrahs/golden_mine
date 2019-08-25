""" try:
    f =open('E:/paragram/leanrgit/learngit/readme.txt','r+')
    print(f.read())
finally:
    if f:
        f.close() """
with open('E:/paragram/leanrgit/learngit/readme.txt','r') as f:
    print(f.read())
