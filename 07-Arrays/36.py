
'''
2 3
1 5
5 0 3 7 5
9 0 9 1 2
2 1
3 5
7 4
2 6
'''


def f(ar):
    ar_temp=[]
    if isinstance(ar[0], list):
        for x in ar:
            for y in x:
                ar_temp.append(y)
        return f(ar_temp)   
    else:
       return ar

        


if __name__=="__main__":
    ar1=[2,3],[1,5]
    ar2=[5,0,3,7,5],[9,0,9,1,2]
    ar3=[2,1],[3,5],[7,4],[2,6]
    print(f(ar1))
    print(f(ar2))
    print(f(ar3))
