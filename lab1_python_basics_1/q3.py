x=[[1,2],[0,1],[7,8]]
y=[[3,4],[3,5],[9,8]]

list1=[]
def eucdist(p1,p2):
    for i in range(len(x)):
      
     x1= (p1[i][0]-p2[i][0])**2+(p1[i][1]-p2[i][1])**2
     list1.append(x1**0.5)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False 
        for j in range(0, n-i-1):
               if arr[j] > arr[j + 1]:
                   swapped = True
                   arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped: 
             return


eucdist(x,y)
bubble_sort(list1)
print(list1)