def main():
    with open("6/input") as f:
        window = [""] * 14
        for index, char in enumerate(f.readline()):
            window[index % 14] = char
            
            if len(set(window)) == 14:
                print(index + 1)
                break

if __name__ == "__main__":
    main()