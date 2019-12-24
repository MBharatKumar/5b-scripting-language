from operator import itemgetter
sentenceslist=[]
class rev:
    def __init__(self,sentence):
        self.sentence=sentence
    def rever(self):
        temp=""
        temp="  ".join(reversed(self.sentence.split(" ")))
        count=0
        for i in range(0,len(temp)):
            ch=temp[i]
            if ch in ['a','e','i','o','u']:
                count+=1
        sentenceslist.append({"sentence" : temp,"count" : count})

s1=rev(input("Enter string1"))
s1.rever()
s2=rev(input("Enter string2"))
s2.rever()
s3=rev(input("Enter string3"))
s3.rever()
print(sentenceslist)
sortedarr=sorted(sentenceslist,key=itemgetter("count"),reverse=True)
for i in sortedarr:
    print(i['sentence'],i['count'])
