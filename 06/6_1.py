def main():
    with open("6/input") as f:
        window = [""] * 4
        for index, char in enumerate(f.readline()):
            window[index % 4] = char
            
            if len(set(window)) == 4:
                print(index + 1)
                break

if __name__ == "__main__":
    main()