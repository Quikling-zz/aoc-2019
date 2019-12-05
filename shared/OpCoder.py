from sys import maxsize

class OpCoder:
    def __init__(self, op_codes):
        self.op_codes = op_codes
        self.instr = 0

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
            param_list = list(zip(self.op_codes[i + 1:i + 4], [False, False, True]))
        elif op in [3, 4]:
            if op == 3:
                param_list = list(zip(self.op_codes[i + 1:i + 2], [True]))
            else:
                param_list = list(zip(self.op_codes[i + 1:i + 2], [False]))
        elif op in [5, 6]:
            param_list = list(zip(self.op_codes[i + 1:i + 3], [False, False]))
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
        if mode == 1 or dest:
            return param
        elif mode == 0:
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
        elif op in [3, 4]:
            dest = self.get_param_val(param_list.pop())
            if op == 3:
                user_in = int(input('Enter input instruction: '))
                self.set_op_code(dest, user_in)
            elif op == 4:
                print('Output: {}'.format(dest))
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
            self.instr = maxsize
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
        while self.instr < len(self.op_codes):
            op, param_list = self.get_next()
            self.execute(op, param_list)
