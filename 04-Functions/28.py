import collections

def main():
    dice="1112233456666"
    print(f(dice))

def f(dice):
    temp=None
    ctr=1
    stack=[]
    sign=[]
    sign.append(0)
    ##return collections.Counter(dice).most_common(1)[0]
    for i in dice:
        if i == temp:
           ctr+=1
        else:
            stack.append(ctr)
            sign.append(i)
            ctr=1
        temp = i

    res=[list(x) for x in zip(stack, sign)]

    return max(res)


if __name__=='__main__':
    main()