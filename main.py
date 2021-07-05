import genData
import pandas as pd
import random
import timeit
import hashlib
import argparse
import tracemalloc

COF = 787
COF2 = 787*787
COF3 = 787*787*787
HASHSIZE = 10091
class ListNode:
    def __init__(self, key, value, next = None):
        self.value = value
        self.key = key
        self.next = next
 
def myhashfunction(x):
    l = len(x)
    a = ord(x[0])
    b = ord(x[1]) if l >= 2 else 0
    c = ord(x[2]) if l >= 3 else 0
    d = ord(x[3]) if l >= 4 else 0
    return (a+b*COF+c*COF2+d*COF3)%HASHSIZE

class Map:
    def __init__(self, hashfunction = myhashfunction):
        self.hashtable = [None] * HASHSIZE
        self.hashfunction = hashfunction

    def set(self, key, value):
        pos = self.hashfunction(key)
        curnode = self.hashtable[pos]
        prenode = None
        while(curnode != None and curnode.key != key):
            prenode = curnode
            curnode = curnode.next

        if(curnode != None):
            curnode.value = value
        else:
            if(prenode == None):
                self.hashtable[pos] = ListNode(key, value)
            else:
                prenode.next = ListNode(key, value)
    
    def get(self, key):
        pos = self.hashfunction(key)
        curnode = self.hashtable[pos]
        while(curnode != None and curnode.key != key):
            curnode = curnode.next
        if(curnode == None):
            return None
        else:
            return curnode.value

    def delete(self, key):
        pos = self.hashfunction(key)
        curnode = self.hashtable[pos]
        if(curnode.key == key):
            self.hashtable[pos] = curnode.next
            del curnode
        else:
            while(curnode.next != None and curnode.next.key != key):
                curnode = curnode.next
            if(curnode.next != None):
                tem = curnode.next
                curnode.next = curnode.next.next
                del tem

def testUniform(hashfunction):
    random.seed(9)
    dic = {"hashidx": [],
           "size": []
           }
    cnt = [0]*HASHSIZE

    time = 0
    for i in range(100000):
        tem = genData.genKey()
        
        start = timeit.default_timer()
        cnt[hashfunction(tem)] += 1
        #cnt[int(hashlib.sha1(tem.encode()).hexdigest(), 16)%HASHSIZE] += 1
        #cnt[int(hashlib.md5(tem.encode()).hexdigest(), 16)%HASHSIZE] += 1
        stop = timeit.default_timer()
        time += stop - start
    print(time)

    ave = 0
    for i in range(HASHSIZE):
        dic["hashidx"].append(i)
        dic["size"].append(cnt[i])
        ave += cnt[i]
    ave /= HASHSIZE

    var = 0
    for i in range(HASHSIZE):
        var += (cnt[i]-ave)**2       
    var /= HASHSIZE

    print(max(dic["size"]), var)
    datas = pd.DataFrame(dic)
    datas.to_csv('out.csv', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default='./testcase/in.test',help="Input file")
    args = parser.parse_args()
    map = Map()
    dic = {}
    with open("{}".format(args.input), 'r', newline='') as file_in:
        f_lines = file_in.read()
        f_lines = f_lines.splitlines()
        
        result = True

        out = 0
        out_golden = 0
        time = 0
        time_golden = 0

        for lines in f_lines:
            s_list = lines.split(' ')
            
            if lines.startswith("set"): 
                start = timeit.default_timer() 
                dic[s_list[1]] =  int(s_list[2])
                stop = timeit.default_timer()
                time_golden += stop - start
            elif lines.startswith("delete"):
                start = timeit.default_timer()
                del dic[s_list[1]] 
                stop = timeit.default_timer()
                time_golden += stop - start
            elif  lines.startswith("get"):
                start = timeit.default_timer()
                out_golden = dic.get(s_list[1])
                stop = timeit.default_timer()
                time_golden += stop - start  
            
            
            if lines.startswith("set"):  
                start = timeit.default_timer()
                map.set(s_list[1], int(s_list[2]))
                stop = timeit.default_timer()
                time += stop - start
            elif lines.startswith("delete"):
                start = timeit.default_timer()
                map.delete(s_list[1])
                stop = timeit.default_timer()
                time += stop - start
            elif  lines.startswith("get"):
                start = timeit.default_timer()
                out = map.get(s_list[1])
                stop = timeit.default_timer()
                time += stop - start
            
        
            if(out != out_golden):
                result = False
                break
                    

        if(result == True):
            print("Succeed!")
            print("Time Used by my Map: {}".format(time))
            print("Time Used by std Dictionary: {}".format(time_golden))
        else:
            print("Fail:(")
