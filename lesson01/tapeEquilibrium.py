
import sys

def solution(mylist):
	"This function will find an index number of array mylist, which is equi"

        der=sum(mylist)
	N=len(mylist)
	izq=0
	if N == 0: return -1;
	min=sys.maxint
	pmin=0

	for P in xrange(1,N):
		izq=izq+mylist[P-1]
		der=der-mylist[P-1]
		diff=abs(der-izq)
		print(P,izq,der,diff)
		if diff < min: 
			min=diff
			pmin=P
	print ("La menor diff es: ",min," con el indice igual a: ",P);
	return min

mylist=[2,2];

print mylist
var=solution(mylist);
print var 

