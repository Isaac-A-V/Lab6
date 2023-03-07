# Isaac Vela's Original Encoder File


def encode(password):

    up_three = [*password]

    for ii in range(0, len(up_three), 1):

        up_three[ii] = (int(up_three[ii]) + 3) % 10
        up_three[ii] = str(up_three[ii])

    up_three = ''.join(up_three)

    return str(up_three)


def main():

    option = 0
    while option != 3:

        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')

        option = int(input('Please enter an option: '))

        if option == 1:
            password = input('Please enter your password: ')
            newpass = encode(password)
            print('Your password has been encoded and stored!')


        if option == 2:
            print(f'The encoded password is {newpass}, and the original password is {password}.')




if __name__ == '__main__':
    main()

