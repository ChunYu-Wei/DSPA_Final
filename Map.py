class Map:
    class ListNode:
        def __init__(self, key, value, next = None):
            self.value = value
            self.key = key
            self.next = next
 
    def __init__(self):
        self.COF = 787
        self.COF2 = 787*787
        self.COF3 = 787*787*787
        self.HASHSIZE = 10091
        self.hashtable = [None] * self.HASHSIZE
        

    def hashfunction(self, x):
        l = len(x)
        a = ord(x[0])
        b = ord(x[1]) if l >= 2 else 0
        c = ord(x[2]) if l >= 3 else 0
        d = ord(x[3]) if l >= 4 else 0
        return (a+b*self.COF+c*self.COF2+d*self.COF3)%self.HASHSIZE

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
                self.hashtable[pos] = self.ListNode(key, value)
            else:
                prenode.next = self.ListNode(key, value)
    
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