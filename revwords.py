def main():
    text = input()
    print ("original:   "+text)
    print("reversed:",end=" ")
    print(' '.join(text.split()[: :-1]))
    return

main()