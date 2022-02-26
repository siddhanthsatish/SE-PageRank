from collections import Counter
import copy

lineList = []



# q1 top 100 inlinks
def inlinks(lines):
    targets = []
    for line in lines:
        for j in range(len(line)):
            if(line[j] == '\t'): 
                targets.append(line[j+1:-1])
    
    count = Counter(targets)
    l = count.most_common(100)
    file1 = open("inlinks.txt","w")
    for i in l:
        file1.write( i[0] + " " + str(i[1]) + "\n")
    return l

# q2 top 100 page ranks
def make_pages_and_links(lines):
    pages = {}
    links = {}
    idx = 0
    print(len(lines))
    for line in lines:
        for j in range(len(line)):
            if(line[j] == '\t'): 
                if(line[:j] not in links):
                    links[line[:j]] = []
                    links[line[:j]].append(line[j+1:-1])
                else:
                    links[line[:j]].append(line[j+1:-1])
                if line[:j] not in pages:
                    pages[line[:j]] = idx
                    idx += 1
                if line[j+1:-1] not in pages:
                    pages[line[j+1:-1]] = idx
                    idx += 1
    return pages, links


def convergence_check(I, R):
    return sum(abs(x-y) for x,y in zip(I,R))

def kLargest(arr, k):
    arr.sort(reverse = True)
    marr = []
    for i in range(k):
        marr.append(arr[i])
    return marr

def Reverse(lst):
    lst.reverse()
    return lst

def pagerank(P, L, lamda, tau):
    
    
    I = [0]*len(P)
    R = [0]*len(P)

    file1 = open("pageranks.txt","w")
    
    ranks = {}

    for i in range(len(I)):
        I[i] = 1 / (float(len(P)))

    for k in range(len(R)):
        R[k] = 0.20/ float(len(P))
    print(len(P))
    itr = 1
    check = convergence_check(I, R)
    print(check)


    while(check > tau):
        print(True)
        print(itr)
        itr  += 1
        for k in range(len(R)):
            R[k] = lamda/ float(len(P))
        
        acc = 0
        for p in P:
            Q = set()
            if p in L:
                Q = set(L[p])
            if(len(Q)>0):
                for q in Q:
                    if q in P:
                        R[P[q]] +=  ((1- lamda)*(I[P[p]]))/len(Q)
            else:
                acc += ((1-lamda)*(I[P[p]]))/len(P)

        for q in P:
            R[P[q]] +=  acc

        check = convergence_check(I, R)
        print(check)
        I = copy.deepcopy(R)

    print(max(R))
    
    new = sorted(range(len(R)), key=lambda x: R[x])[-100:]
    rnew = Reverse(new)

    key_list = list(P.keys())
    val_list = list(P.values())
    
    for i in rnew:
        position = val_list.index(i)
        print( ( key_list[position], R[position] ) )
        file1.write( str(key_list[position]) + " " + str(R[position]) + "\n")

    return R


#driver code            
lamda = 0.20
tau = 0.05     
file = open( "links.srt", "r") #opening file
lines = file.readlines() #array of lines
file.close()
inlinks(lines) #top 100 inlinks 
pages, links = make_pages_and_links(lines) #pages is a dictionary {pagename: index} and links are {source: list of destinations}
pagerank(pages, links, lamda, tau) #top 100 pageranks

    


   