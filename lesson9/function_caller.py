def say_hi():
    print("Hi")
    return

def main():
    print("Before hi")
    say_hi()       # ← call
    print("After hi")

main()


# What happens:
# Python runs main().
# Inside main, it sees say_hi().
# Python pauses main at that line and jumps into say_hi.
# say_hi runs, hits return.
# Python says: "Done with say_hi, now continue where I left off in main."
# It prints "After hi".