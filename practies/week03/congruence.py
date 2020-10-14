# get answer of ax = b mod n and display solution
# input: a,b,n
# output: x, solution
# step 1: get gcd(a,n) = d
# step 2: check if b % d == 0
#           if      yes -> step 3
#           else    no root
# step 3: calculate d = n*s+a*r
#     => x0 = r*b/d mod n/d
#     => x = {(x0 + k*n/d) mod n} with k in Z
import utils.get_input

# step 1: get gcd(a,n) = d
def find_gcd_table(a, n):
    if(a > n):
        a %= n #reducing a number if a > n

    dividends = [n]
    divisors = [a]
    quotients = []
    remainders = []
    count = 0

    while (True):
        quotient = dividends[count] // divisors[count] #getting
        remainder = dividends[count] - divisors[count] * quotient

        quotients.append(quotient)
        remainders.append(remainder)

        if (remainder == 0):
            break

        dividends.append(divisors[count])
        divisors.append(remainder)
        count += 1

    table = [dividends, divisors, quotients, remainders]
    return table

#format the table for better visibility
def format_table(table):
    result = ''
    result += '  Dividend|   Divisor|  Quotient| Remainder\n'

    for i in range (0, len(table[0])):
        result += f'{table[0][i]:>10}|{table[1][i]:>10}|{table[2][i]:>10}|{table[3][i]:>10}\n'

    return result

# step 2: check if b % d == 0
#           if      yes -> step 3
#           else    no root
def d_divisible_by_b(a, b, n, d):
    if (b % d == 0):
        return True
    else:
        print(f'There is not any x that satisfied {a}x \u2261 {b} mod {n}!')
        return False


# step 3: calculate d = n*s+a*r
def get_r_s_calculation(table):
    calculation = []
    s = - table[2][len(table[2]) - 2] #s = -q1
    r = 1
    for i in range((len(table[0]) - 2), -1, -1):
        #adding calculation step of getting r and s
        calculation.append(f"{table[3][len(table[0]) - 2]} = {table[0][i]}*({r}) + {table[1][i]}*({s})")

        if (i == 0):
            break

        temp = r
        r = s                           #r(i) = s(i-1)
        s = temp - table[2][i - 1] * s  #s(i) = r(i-1) - q(i)*s(i-1)

    calculation.append([r, s])
    return calculation

# step 3.1: calculate x0 = r*b/d mod n/d
#     			  => x = {(x0 + k*n/d) mod n} with k in Z
def calculate_x(r_s, b, d, n):
    x0 = int(r_s[1]) * b / d
    mod_of_x0 = n / d

    x0 %= mod_of_x0
    x = [x0]

    if (x0 < n):
        while (x0 < n):
            x.append(x0)
            x0 += mod_of_x0

    return x

def print_split_line():
    print('----------------------------------------')

def main():
    a = int(utils.get_input.number("Enter number a: "))
    b = int(utils.get_input.number("Enter number b: "))
    n = int(utils.get_input.number("Enter number n: "))
    print_split_line()

    print(f'Finding GDC of {a},{n}:')

    table = find_gcd_table(a, n)
    print(format_table(table))
    d = table[1][len(table[1]) - 1]

    print(f'GDC of {a},{n} is {d}')
    print_split_line()

    if(not d_divisible_by_b(a,b,n,d)):
        return

    print('Calculating r and s:')
    r_s = get_r_s_calculation(table)

    for i in range (len(r_s)-1):
        print(r_s[i])

    print(f'=> r = {r_s[len(r_s)-1][0]}, s = {r_s[len(r_s)-1][1]}')
    print_split_line()

    print('Calculating x0: ')
    x = calculate_x(r_s[len(r_s) - 1], b, d, n)
    print(f'x0 = {r_s[len(r_s)-1][0]} * {b} / {d} = {x[0]:.0f}')

    print_x = '=> x = {'

    for i in range (1,len(x)):
        if i == len(x) - 1:
            print_x += str(x[i])
        else:
            print_x += str(x[i]) + ', '

    print_x += '}'
    print(f'{print_x} mod {n}')