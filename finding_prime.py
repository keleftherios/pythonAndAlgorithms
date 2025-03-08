def finding_prime(number):
    num = abs(number)
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_numbers(number):
    result = []
    for i in range(2, abs(number)):
        if finding_prime(i) is True:
            result.append(str(i))
    return ' '.join(result)


def prime_numbers_v2(number):
    result = []
    for num in range(2, abs(number)):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            result.append(str(num))
    return ' '.join(result)


if __name__ == "__main__":
    number1 = 17
    number2 = 20

    print(f"Number {number1} is prime: {finding_prime(number1)} ")
    assert finding_prime(number1) == True, "Wrong answer..."

    print(f"Number {number2} is prime: {finding_prime(number2)} ")
    assert finding_prime(number2) == False, "Wrong answer..."

    N = 100
    print(f"Prime numbers until {N}, using function 'prime_numbers'    : {prime_numbers(100)}")
    print(f"Prime numbers until {N}, using function 'prime_numbers_v2' : {prime_numbers_v2(100)}")
