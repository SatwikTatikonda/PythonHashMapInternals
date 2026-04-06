class Entry:
    def __init__(self,key,value):
        self.key=key 
        self.value=value

class HashMapInternals:

    print("in hashmap")
    loadFactor=0.75
    capacity=16

    def __init__(self):
        self.size=0
        self.buckets=[None]*self.capacity
    
    def getBucketIndex(self,key):

        return hash(key)%self.capacity
    
    def put(self,key,value):

        if(self.size>=self.capacity*self.loadFactor):
            self.rehash()

        index=self.getBucketIndex(key)
        if(self.buckets[index]):

                for entry in self.buckets[index]:
                    if(entry.key==key):
                        entry.value=value
                        return

        # this is poll scm test
        
        else:
            self.buckets[index]=[]
        
        self.buckets[index].append(Entry(key,value))
        self.size+=1
    
    def get(self,key):

        index=self.getBucketIndex(key)
        if(self.buckets[index]):

            for entry in self.buckets[index]:
                
                if(entry.key==key):
                    return entry.value
        
        return None

    def isContains(self,key):

        index=self.getBucketIndex(key)
        if self.buckets[index]:

            for entry in self.buckets[index]:
                if(entry.key==key):
                    return True 
        
        return False
    

    def remove(self,key):

        index=self.getBucketIndex(key)
        if self.buckets[index]:

            for entry in self.buckets[index]:
                if entry.key==key:
                    self.buckets[index].remove(entry)
                    self.size-=1
                    return 

    def rehash(self): 

        oldbuckets=self.buckets
        self.capacity=self.capacity*2
        if self.capacity>2**30:
            raise Exception("HashMap size exceeded")
        self.buckets=[None]*self.capacity
        self.size=0
        for bucket in oldbuckets:
            if bucket is not None:
                for entry in bucket:
                    self.put(entry.key,entry.value)
    


if __name__ == "__main__":
    map = HashMapInternals()
    map.put("A", 1)
    map.put("B", 2)
    map.put("C", 3)
    map.put("D", 4)
    map.put("E", 5)
    map.put("F", 6)
    map.put("G", 7)
    map.put("H", 8)
    map.put("I", 9)
    map.put("J", 10)
    map.put("K", 11)
    map.put("L", 12)
    map.put("M", 13)
    map.put("N", 14)
    map.put("O", 15)
    map.put("P", 16)
    map.put("Q", 17)
    map.put("R", 18)
    map.put("S", 19)
    map.put("T", 20)
    map.put("U", 21)
    map.put("V", 22)
    map.put("W", 23)
    map.put("X", 24)
    map.put("Y", 25)
    map.put("Z", 26)
    print(map.get("A"))
    print(map.get("B"))
    print(map.get("C"))
    print(map.get("D"))
    print(map.get("E"))
    print(map.get("F"))
    print(map.get("G"))
    print(map.get("H"))
    print(map.get("I"))
    print(map.get("J"))
    print(map.get("K"))
    print(map.get("L"))
    print(map.get("M"))
    print(map.get("N"))
    print(map.get("O"))
    print(map.get("P"))
    print(map.get("Q"))
    print(map.get("R"))
    print(map.get("S"))
    print(map.get("T"))
    print(map.get("U"))
    print(map.get("V"))
    print(map.get("W"))
    print(map.get("X"))
    print(map.get("Y"))
    print(map.get("Z"))    
        


            

    
