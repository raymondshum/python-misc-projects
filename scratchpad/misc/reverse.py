def reverse(answer: int) -> bool:
    mid: int = (answer // 2) + 1
    for num in range(0, mid):
        rev_num = int(str(num)[::-1])
        if rev_num + num == answer:
            print(f"{rev_num} + {num} = {answer}")
            return True
    print(f"No answer found for: {answer}")
    return False

def main():
    print(reverse(443), end="\n\n")
    print(reverse(63), end="\n\n")
    print(reverse(10))

if __name__ == "__main__":
    main()