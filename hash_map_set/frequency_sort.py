def frequency_sort(s):
    hash={}

    for l in (s):
        hash[l]=hash.get(l,0)+1
    
    return "".join([x[0]*x[1] for x in sorted(hash.items(),key=lambda x: x[1],reverse=True)])


print(frequency_sort("tree"))