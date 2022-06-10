class TuringMachine:
    def __init__(self, in_state_transfer_tab: dict, in_pointer: int, mode='standard'):
        self.tape = None
        self.state_transfer_tab = in_state_transfer_tab
        self.states = set([x[0] for x in in_state_transfer_tab.keys()])
        self.pointer = in_pointer
        self.state = 1
        self.mode = 'standard'

    def input(self, in_tape: list):
        self.tape = in_tape
        self.print_tape()

    def calculate(self):
        if self.tape is None:
            print('Input tape to the Turing Machine first!')
            exit(-1)
        while self.state in self.states:
            curr_tape_num = self.tape[self.pointer]
            transfer_info = self.state_transfer_tab[(self.state, curr_tape_num)]
            self.tape[self.pointer] = transfer_info[0]
            if transfer_info[1] == 'L':
                self.pointer -= 1
            elif transfer_info[1] == 'R':
                self.pointer += 1
                if self.pointer >= len(self.tape):
                    self.tape.extend([0 for x in range(len(self.tape))])
            self.state = transfer_info[2]
            self.print_tape()

    def print_tape(self):
        state_str = str(self.state) + ':'
        print(state_str, end=' ')
        for i in self.tape:
            print(i, end=' ')
        print("\n" + ' ' * len(state_str), end=' ')
        for i in range(len(self.tape)):
            print('^' if i == self.pointer else ' ', end=' ')
        print("")

    def print_output(self):
        print('Output =', end=' ')
        output_num = 0
        output_num_list = []
        for i in range(self.pointer, len(self.tape)):
            if self.tape[i] == 1:
                output_num += 1
            else:
                if output_num > 0:
                    output_num_list.append(output_num)
                output_num = 0
        if output_num > 0:
            output_num_list.append(output_num)
        for output_num in output_num_list:
            if self.mode == 'standard':
                output_num -= 1
            print(output_num, end=' ')