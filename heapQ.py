import heapq

class Member:
    def __init__(self, id, counter,counter1,counter2,isRed):
        self.id = id
        self.id1=id[:2]
        self.id2=id[2:]
        self.counter = counter
        self.counter1=[self.id1,counter1]
        self.counter2=[self.id2,counter2]
        self.isRed=isRed

    def __lt__(self, other):
        return self.counter > other.counter

    def check_id1_in_id(self,id1):
        return id1 in self.id

class PriorityQueue:
    def __init__(self):
        self.members = []

    def push(self, member):
        heapq.heappush(self.members, member)

    def pop(self):
        return heapq.heappop(self.members)

    def peek(self):
        return heapq.nlargest(1, self.members)[0]


    def replace(self, id, counter):
        for i, member in enumerate(self.members):
            if member.check_id1_in_id(id):

                if self.members[i].counter1[0] == id:
                    self.members[i].counter1[1]=counter
                elif self.members[i].counter2[0] == id:
                    self.members[i].counter2[1]=counter
                self.members[i].counter=self.members[i].counter1[1]+self.members[i].counter2[1]
                heapq.heapify(self.members)

# Example usage:
'''pq = PriorityQueue()
pq.push(Member("A1", 3))
pq.push(Member("B2", 7))
pq.push(Member("A1", 5))

print(pq.pop().counter)  # Output: 7
print(pq.pop().counter)  # Output: 5'''
