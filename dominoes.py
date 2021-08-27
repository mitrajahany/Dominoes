import random
Dominos = [[i, j] for i in range(7) for j in range(i, 7)]
pairs = [[6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]
stock, player, computer, snake, status = [], [], [], [], ''


def shuffle():
    global Dominos, player, computer, stock
    random.shuffle(Dominos)
    stock = Dominos[:14]
    player = Dominos[14:21]
    computer = Dominos[21:28]
    return first()


def first():
    global Dominos, player, computer, stock, pairs, status
    if not [a for a in player if a in pairs] and not [a for a in computer if a in pairs]:
        return shuffle()
    if [a for a in player if a in pairs] and [a for a in computer if a in pairs]:
        player_max = max([a for a in player if a in pairs])
        computer_max = max([a for a in computer if a in pairs])
        if player_max > computer_max:
            player.remove(player_max), snake.append(player_max)
            status = 'computer'
        elif computer_max > player_max:
            computer.remove(computer_max), snake.append(computer_max)
            status = 'player'
    elif [a for a in player if a in pairs]:
        player_max = max([a for a in player if a in pairs])
        player.remove(player_max), snake.append(player_max)
        status = 'computer'
    elif [a for a in computer if a in pairs]:
        computer_max = max([a for a in computer if a in pairs])
        computer.remove(computer_max), snake.append(computer_max)
        status = 'player'


def result(self):
    global Dominos, player, computer, stock, snake, status
    if self == 1:
        print('=' * 70)
        print('Stock size:', len(stock))
        print('Computer pieces:', len(computer), '\n')
        print('{}'.format(snake).replace(']]', ']').replace('[[', '[').replace(', [', '[') if len(snake) <= 6 else
              '{}...{}'.format(snake[0:3], snake[-3:]).replace(', [', '[').replace('[[', '[').replace(']]', ']'), '\n')
        print("Your pieces:")
        for count, item in enumerate(player, 1):
            print(f"{count}:{item}")
        print()
        print("Status: It's your turn to make a move. Enter your command." if status == 'player' else
              input("Status: Computer is about to make a move. Press Enter to continue..."))
        return move('player') if status == 'player' else move('computer') if status == 'computer' else move(3)
    if self == 2:
        print('=' * 70)
        print('Stock size:', len(stock))
        print('Computer pieces:', len(computer), '\n')
        print('{}'.format(snake).replace(']]', ']').replace('[[', '[').replace(', [', '[') if len(snake) <= 6 else
              '{}...{}'.format(snake[0:3], snake[-3:]).replace(', [', '[').replace('[[', '[').replace(']]', ']'), '\n')
        print("Your pieces:")
        for count, item in enumerate(player, 1):
            print(f"{count}:{item}")
        print()
        print('Status: The game is over. The computer won!' if status == 'player' else
              'Status: The game is over. You won!')


def move(self):
    global Dominos, player, computer, stock, snake, status
    if self == 'player':
        try:
            num = int(input())
            if 0 < num <= len(player):
                if player[abs(num) - 1][0] == snake[-1][1]:
                    pass
                elif player[abs(num) - 1][1] == snake[-1][1]:
                    player[abs(num) - 1][0], player[abs(num) - 1][1] = player[abs(num) - 1][1], player[abs(num) - 1][0]
                else:
                    print("Illegal move. Please try again.")
                    return move('player')
                snake.append(player[abs(num) - 1])
                del player[abs(num) - 1]
                status = 'computer'
                return result(2) if not player else result(1)
            elif 0 > num >= -len(player):
                if player[abs(num) - 1][1] == snake[0][0]:
                    pass
                elif player[abs(num) - 1][0] == snake[0][0]:
                    player[abs(num) - 1][0], player[abs(num) - 1][1] = player[abs(num) - 1][1], player[abs(num) - 1][0]
                else:
                    print("Illegal move. Please try again.")
                    return move('player')
                snake.insert(0, player[abs(num) - 1])
                del player[abs(num) - 1]
                status = 'computer'
                return result(2) if not player else result(1)
            elif num == 0:
                if stock:
                    player.append(stock[0])
                    del stock[0]
                    status = 'computer'
                else:
                    print('Stock is empty')
                    return move('player')
                return result(2) if not player else result(1)
            else:
                raise ValueError
        except ValueError:
            print('Invalid input. Please try again.')
            return move('player')
    if self == 'computer':
        left = [a for a in computer if a[1] == snake[0][0]]
        right = [a for a in computer if a[0] == snake[-1][0]]
        if left:
            snake.insert(0, left[0])
            computer.remove(left[0])
            status = 'player'
        elif right:
            snake.append(right[0])
            computer.remove(right[0])
            status = 'player'
        else:
            computer.remove(computer[0])
            status = 'player'
    return result(2) if not computer else result(1)


shuffle(), result(1)
