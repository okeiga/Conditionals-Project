def main():
    time =input("Tell me the time to help you decide what meal to eat ")
    hours=convert(time)

    if 7.0 <= hours <=8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <=hours <=19.0:
        print("dinner time")

def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + minutes/60

if __name__ == "__main__":
    main()
