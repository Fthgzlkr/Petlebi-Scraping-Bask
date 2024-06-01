def toplama( x, y):
    return x+y

def bol(x,y):
    return x/y


def fibonacci(x):
    if x<=0 :
        return x
    else: 
        return fibonacci(x-1)+fibonacci(x-2)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                sayi=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=sayi