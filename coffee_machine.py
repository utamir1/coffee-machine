import enum

class Action(enum.Enum):
    """
    possible actions for the coffee machine state
    """

    BUY = 'buy'
    FILL = 'fill'
    TAKE = 'take'
    EXIT = 'exit'
    REMAINING = 'remaining'

    @staticmethod
    def ask_action():
        """
        ask user to input the action for the next state of the machine
        """
        possible_values = ','.join(action.value for action in Action)
        while True:
            answer = input(f'Write action ({possible_values}):\n')
            try:
                return Action(answer)
            except ValueError:
                print(f'Action is not valid: {answer}')

class CoffeeMachine:
    """
    represents a coffee machine.
    Every time the user inputs a string to the console, the program invokes a method.
    """

    def __init__(self):
        # set initial resources [water, milk, beans, cups, money]
        self.resources = [
            ['water', 400],
            ['milk', 540],
            ['coffee beans', 120],
            ['disposable cups', 9],
            ['money', 550]
        ]

        self.running = True

    def execute_action(self, action):
        if action == Action.BUY:
            self.buy_coffee()
        elif action == Action.FILL:
            self.fill_machine()
        elif action == Action.TAKE:
            self.take_money()
        elif action == Action.REMAINING:
            self.show_resources()
        elif action == Action.EXIT:
            self.running = False
        else:
            raise NotImplementedError(action)

    def show_resources(self):
        print('The coffee machine has:')
        for i in range(len(self.resources) - 1):
            print(f'{self.resources[i][1]} of {self.resources[i][0]}')
        print(f'${str(self.resources[-1][1])} of {self.resources[-1][0]}\n')
        return

    def get_enough_resources(self, coffee_type_reqs):
        for i in range(len(self.resources) - 1):
            if self.resources[i][1] < coffee_type_reqs[i]:
                print('Sorry, not enough ' + self.resources[i][0] + '\n')
                return False
        return True

    def change_inventory(self, coffee_type_reqs):
        for i in range(len(self.resources) - 1):
            self.resources[i][1] -= coffee_type_reqs[i]
        self.resources[-1][1] += coffee_type_reqs[-1]
        return

    def buy_coffee(self):
        # define coffee requirements [water, milk, beans, cups, money]
        # coffee_type can be 1 - espresso, 2 - latte, 3 - cappuccino
        coffee_reqs = {
            '1': [250, 0, 16, 1, 4],
            '2': [350, 75, 20, 1, 7],
            '3': [200, 100, 12, 1, 6]
        }
        coffee_type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n')
        if coffee_type == 'back':
            return
        coffee_type_reqs = coffee_reqs.get(str(coffee_type))
        # check if enough resources
        if self.get_enough_resources(coffee_type_reqs):
            print('I have enough resources, making you a coffee! \n')
            self.change_inventory(coffee_type_reqs)
        return

    def fill_machine(self):
        self.resources[0][1] += int(input('Write how many ml of water do you want to add: '))
        self.resources[1][1] += int(input('Write how many ml of milk do you want to add: '))
        self.resources[2][1] += int(input('Write how many grams of coffee beans do you want to add: '))
        self.resources[3][1] += int(input('Write how many disposable cups of coffee do you want to add: '))
        print('\n')
        return

    def take_money(self):
        print('I gave you $' + str(self.resources[-1][1]) + '\n')
        self.resources[-1][1] = 0
        return


def main():
    machine = CoffeeMachine()
    while machine.running:
        action = Action.ask_action()
        machine.execute_action(action)

if __name__ == "__main__":
    main()
