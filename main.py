import models
import turing_machine


def generateTape(input_list, mode='standard'):
    tape = [0]
    for index in range(len(input_list)):
        current_ones = [1 for x in range(input_list[index])]
        tape.extend(current_ones)
        if mode == 'standard':
            tape.extend([1, 0])
        else:
            tape.append(0)
    return tape


if __name__ == '__main__':
    model = models.Zero()
    turing_machine = turing_machine.TuringMachine(model.getModel(), 1)
    turing_tape = generateTape([3], mode='standard')
    turing_machine.input(turing_tape)
    turing_machine.calculate()
    turing_machine.print_output()
