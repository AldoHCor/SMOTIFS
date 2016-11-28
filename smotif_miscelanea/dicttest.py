import heapq
#directory syntax testing
dic = {'8': 'a','9': 's','8': 'd','9': 'f','9': 'g','5': 'h','4': 'j','3': 'k','2': 'l','8': 'x'}

dic_keys = dic.keys()
print dic_keys
i = 0
#Get largest values
Lar_ = heapq.nlargest(5, dic_keys)

print Lar_

i = 0

while i < len(Lar_):
    if Lar_[i] in dic:
        print  dic[Lar_[i]], Lar_[i]
        i = i + 1

        
""" #Or this
print dic[Lar_[0]]
print dic[Lar_[1]]
print dic[Lar_[2]]
print dic[Lar_[3]]
print dic[Lar_[4]]


"""
