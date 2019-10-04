n = input()

if n < 10:
    print(n)

maybe_prime = False
digits = list()
counter = 2
while n > 1:
    if n % counter == 0:
        n = n / counter

        if counter == 10:
            digits.append(n)
            break

        digits.append(counter)
        counter = 2
    else:
        counter += 1
        if counter == 10:
            maybe_prime = True
            print(-1)
            break

digits.sort(reverse=True)

num = list()
index = 0
while index < len(digits)-1:
    if len(digits) > 2 and digits[index] * digits[index+1] < 10:
        digits.insert(index, digits[index] * digits[index+1])
        digits.remove(digits[index+1])
        digits.remove(digits[index+1])
    else:
        index += 1

digits.sort()
digits = int(''.join(str(i) for i in digits))

if maybe_prime == False:
    print(digits)