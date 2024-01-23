fh=open("output8.txt",'w')
a=[45,6,7,34,67,6,1,9,0,2,8,77] 
fh.write("before swapping:"+str(a) )  
a.sort()
fh.write("after swapping:"+str(a))  
b=[1,2,5,3,7,9,19,13]
fh.write("before swapping:"+str(b) )  
b.sort(reverse=True)
fh.write("after swapping:"+str(b) ) 
fh.close()