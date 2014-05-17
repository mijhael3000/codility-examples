def solution(x,y,d):
	"This function will find an index number of array mylist, which is equi"

	if x<=y and d>0 and x>0:
		D=y-x
		div=int(D/d)
		rest=D%d

		if rest > 0:
			div=div+1
		
		print div
		return div
	else:
		return -1

x=10
y=85
d=30

solution(x,y,d)
