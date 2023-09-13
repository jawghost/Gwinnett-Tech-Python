def main():
    my_coin = Coin()

    print('This side is up:', my_coin.get_sideup())

    print('I am tossing the coin...')

    print('I am tossing the coin ...')
    my_coin.toss()

    my_coin.sideup = 'Heads'

    print('This side is up:', my_coin.get_sideup())

main()
