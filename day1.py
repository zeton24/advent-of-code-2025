with open("data/day1-input.txt", "r") as file:
# with open("test-input-day1.txt", "r") as file:
    content = file.read()

current_number = 50
password = 0 # part1 - finishing on 0
password2 = 0 # part2 - only crossing 0

for line in content.splitlines():
    direction, value = line[0], int(line[1:])
    previous_numer = current_number
    if direction == "R":
        new_number = current_number + value
        current_number = new_number % 100
        password2 += new_number // 100
        if current_number == 0: password2 -= 1
    elif direction == "L":
        if value <= current_number:
            current_number -= value
        else:
            password2 += value // 100
            if current_number == 0 and value % 100 == 0: password2 -= 1
            value -= current_number  # jedziemy na zero
            value = value % 100  # tylko co to trzeba przejechac w lewo
            if value == 0:
                current_number = 0
            else:
                current_number = 100 - value
                if previous_numer != 0 and previous_numer < current_number:
                    password2 += 1
    else:
        print('whooopsi!')
    # print(previous_numer, line, current_number, password2)
    if current_number == 0:
        password += 1
    elif current_number < 0 or current_number > 99:
        print(previous_numer, line, current_number)
        break

print(f'Your answer is: {password + password2}')
