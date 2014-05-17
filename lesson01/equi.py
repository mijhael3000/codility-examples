def solution(mylist):
	"This function will find an index number of array mylist, which is equi"

        suma=sum(mylist)
	N=len(mylist)
	izq=0
	print suma
	if N == 0: return -1;

	for P in xrange(N):
		der=suma-izq-mylist[P]
		if izq == der:
			print ("El indice encontrado el P es ", P, " y su valor es ", mylist[P]);
			return P
			break;
		izq=izq+mylist[P]

	return -1

#mylist=[10];
mylist=[-7,1,5,2,-4,3,0];

print mylist
var=solution(mylist);
print var 

