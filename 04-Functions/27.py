def main():
    m_text=input()
    print(f(m_text))
    

def f(f_text):
    temp=0
    for i in f_text[:3]:
        temp+=int(i)

    if int(temp) % 7 ==int(f_text[-1]):
        return True
    return False



if __name__=='__main__':
    main()