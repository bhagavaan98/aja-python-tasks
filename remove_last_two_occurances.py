strng='orange,apple,banana,apple,melon,apple,strawberry'
res=strng.rsplit('apple')
print(res)
res='APPLE'.join(strng.rsplit('apple',2))
print(res)