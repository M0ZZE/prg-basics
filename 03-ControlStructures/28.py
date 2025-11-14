def main():
      
    last_number=1
    second_last=0
    temp=0

    for i in range(21):
        print(f'{second_last}')
        temp=second_last
        second_last=last_number
        last_number=temp+last_number


if __name__ == "__main__":
        main()

    