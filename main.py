#https://github.com/MaryamKhorsandi/python-average-calculator.git

def avg(numbers):
    return sum(numbers) / len(numbers)


while True:
    numbers = input().split()
    try:
        numbers = [float(n) for n in numbers]

        if len(numbers) == 0:
            print("Invalid Input! Enter a valid input.")
            continue

        print(f"{avg(numbers):.2f}")
        break

    except:
        print("Invalid Input! Enter a valid input.")
