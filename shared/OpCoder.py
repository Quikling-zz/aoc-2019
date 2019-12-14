from collections import defaultdict
from sys import maxsize


class OpCoder:
    def __init__(self, op_codes, queue=None):
        self.queue = queue
        self.instr = 0
        self.output = None
        self.halt = False
        self.rel_base = 0
        self.op_codes = defaultdict(int)
        for i, op_code in enumerate(op_codes):
            self.op_codes[i] = op_code

    def get_next(self):
        op_code = self.get_op_code(self.instr)
        op = op_code % 100
        modes = op_code // 100
        param_list = self.get_params(op, modes, self.instr)

        return op, param_list

    def set_op_code(self, dest, val):
        self.op_codes[dest] = val

    def get_op_code(self, src):
        return self.op_codes[src]

    def get_params(self, op, modes, i):
        if op in [1, 2, 7, 8]:
            arg_list = [self.op_codes[i] for i in range(i + 1, i + 4)]
            param_list = list(zip(arg_list, [False, False, True]))
        elif op in [3, 4, 9]:
            arg_list = [self.op_codes[i] for i in range(i + 1, i + 2)]
            if op == 3:
                param_list = list(zip(arg_list, [True]))
            else:
                param_list = list(zip(arg_list, [False]))
        elif op in [5, 6]:
            arg_list = [self.op_codes[i] for i in range(i + 1, i + 3)]
            param_list = list(zip(arg_list, [False, False]))
        elif op == 99:
            param_list = []
        else:
            raise Exception('Invalid op code')

        for i, (param, dest) in enumerate(param_list):
            mode = (modes // 10**i) % 10
            param_list[i] = (param, mode, dest)

        return param_list

    def get_param_val(self, param_mode_dest):
        param, mode, dest = param_mode_dest
        if mode == 2:
            if dest:
                return param + self.rel_base
            else:
                return self.get_op_code(param + self.rel_base)
        elif mode == 1:
            return param
        elif mode == 0:
            if dest:
                return param
            else:
                return self.get_op_code(param)
        else:
            raise Exception('Invalid mode')

    def execute(self, op, param_list):
        if op in [1, 2, 7, 8]:
            src1, src2, dest = map(self.get_param_val, param_list)
            if op == 1:
                self.set_op_code(dest, src1 + src2)
            elif op == 2:
                self.set_op_code(dest, src1 * src2)
            elif op == 7:
                if src1 < src2:
                    self.set_op_code(dest, 1)
                else:
                    self.set_op_code(dest, 0)
            elif op == 8:
                if src1 == src2:
                    self.set_op_code(dest, 1)
                else:
                    self.set_op_code(dest, 0)
            self.update_instr(inc=4)
        elif op in [3, 4, 9]:
            dest = self.get_param_val(param_list.pop())
            if op == 3:
                # user_in = int(input('Input: '))
                user_in = int(self.queue.get())
                self.set_op_code(dest, user_in)
            elif op == 4:
                # print('Output: {}'.format(dest))
                self.output = dest
            elif op == 9:
                self.rel_base += dest
            self.update_instr(inc=2)
        elif op in [5, 6]:
            cond, jump = map(self.get_param_val, param_list)
            self.update_instr(inc=3)
            if op == 5 and cond != 0:
                self.update_instr(jump=jump)
            elif op == 6 and cond == 0:
                self.update_instr(jump=jump)
        elif op == 99:
            print('Halting')
            self.halt = True
        else:
            raise Exception('Invalid op code')

    def update_instr(self, inc=-1, jump=-1):
        if inc != -1:
            self.instr += inc
        elif jump != -1:
            self.instr = jump
        else:
            raise Exception('Invalid instr update')

    def run(self):
        while not self.halt and self.output is None:
            op, param_list = self.get_next()
            self.execute(op, param_list)

        out = self.output
        self.output = None
        return out
