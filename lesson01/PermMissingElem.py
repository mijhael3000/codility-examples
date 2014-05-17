def solution(mylist):

	N=len(mylist)
	if N==0: return 1
	mylist=sorted(mylist)
	N2=N+1
	tot=(N2*(N2+1))/2
	print tot
	suma=sum(mylist)
	print (tot,suma)
	
	value=tot-suma


	ant=mylist[0]

	for P in xrange(1,N):
		print (ant,mylist[P],N2,value)		
                if mylist[P] > N2 or ant == mylist[P] or ant <0:
                        print ("error");
                        return -1
                ant=mylist[P]
        return value


mylist=[]

print mylist
var=solution(mylist);


