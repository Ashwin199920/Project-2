reg =   [[0,0,"$zero"],
        [1,0,"$at"],
        [2,0,"$v0"],
        [3,0,"$v1"],
        [4,0,"$a0"],
        [5,0,"$a1"],
        [6,0,"$a2"],
        [7,0,"$a3"],
        [8,0,"$t0"],
        [9,0,"$t1"],
        [10,0,"$t2"],
        [11,0,"$t3"],
        [12,0,"$t4"],
        [13,0,"$t5"],
        [14,0,"$t6"],
        [15,0,"$t7"],
        [16,0,"$s0"],
        [17,0,"$s1"],
        [18,0,"$s2"],
        [19,0,"$s3"],
        [20,0,"$s4"],
        [21,0,"$s5"],
        [22,0,"$s6",],
        [23,0,"$s7"],
        [24,0,"$t8"],
        [25,0,"$t9"],
        [26,0,"$k0"],
        [27,0,"$k1"],
        [28,0,"$gp"],
        [29,0,"$sp"],
        [30,0,"$fp"],
        [31,0,"$ra"] ]
LO = 0


def print_reg():
  x = [x*2 for x in range(16)]
  for i in x:
    print(reg[i][2] + "=", "$"% (reg[i][1])+'    '+reg[i+1][2] + "=", "$"% (reg[i+1][1]))
  print("LO_REG = " + str(LO))
  return

pc = 0

def PC_plus4():
  global pc
  pc += 4


def bin_to_dec(b):
    if (b[0] == "0"):
        return int(b, base=2)
    else:
        for j in reversed(range(len(b))):
            if b[j] == '1':
                break
        pos_num = ''
        for i in range(0, j, 1):
            pos_num += str(1 - int(b[i]))
        for i in range(j, len(b), 1):
            pos_num += b[i]

        neg_num = '-' + pos_num
        #decimal = int(pos_num, base = 10)
        #decimal =
        #y = dec(int(t))
        #print(str(dec))
        return int(neg_num, base=2)


def hex_to_bin(line):
    h = line.replace("\n", "")
    i = int(h, base=16)
    b = bin(i)
    b = b[2:].zfill(32)
    print(f'Instruction {h} in binary is {b}')
    return (b)


def process(b):
    b_op = b[0:6]
    b_rs = b[6:11]
    b_rt = b[11:16]
    b_imm = b[16:]
    b_rd = b[16:21]
    b_sh = b[21:26]
    b_func = b[26:]

    #print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
    asm = ""

    if (b_op == '001000'):  # ADDI
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)

        reg[rt][1] = int(reg[rs][1]) + int(imm)
        updateReg1 = reg[rt][1]

        reg1 = reg[rt][2]
        # reg2 = reg[rs][2]

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "addi " + rt + ", " + rs + ", " + imm
        PC_plus4()
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')
        print(f'Updated registers: {reg1} = {updateReg1}')
        print(f'pc = {pc}')


    elif (b_op == '000000') and (b_func == '100000'):  # ADD
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        rd = int(b_rd, base=2)

        reg[rd][1] = int(reg[rs][1] + int(reg[rt][1]))
        updateReg1 = reg[rd][1]
        reg1 = reg[rd][2]

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        rd = "$" + str(rd)
        asm = "add " + rd + ", " + rs + ", " + rt
        PC_plus4()
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_rd} | {b_sh} | {b_func}')
        print(f'in asm: {asm}')
        print(f'Updated registers: {reg1} = {updateReg1}')
        print(f'pc = {pc}')
        #print (f'NO idea about op = {b_op}')

    elif (b_op == '000000') and (b_func == '100010'):  # SUB
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        rd = int(b_rd, base=2)

        reg[rd][1] = int(reg[rs][1] - int(reg[rt][1]))
        updateReg1 = reg[rd][1]
        reg1 = reg[rd][2]

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        rd = "$" + str(rd)
        asm = "sub " + rd + ", " + rs + ", " + rt
        PC_plus4()
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_rd} | {b_sh} | {b_func}')
        print(f'in asm: {asm}')
        print(f'Updated registers: {reg1} = {updateReg1}')
        print(f'pc = {pc}')

    elif (b_op == '001100'):  # ANDI
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)

        reg[rt][1] = int(reg[rs][1]) & int(imm)
        updateReg1 = reg[rt][1]

        reg1 = reg[rt][2]

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "andi " + rt + ", " + rs + ", " + imm
        PC_plus4()
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')
        print(f'Updated registers: {reg1} = {updateReg1}')
        print(f'pc = {pc}')

    elif (b_op == '000000') and (b_func == '101010'):  # SLT
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        rd = int(b_rd, base=2)

        if(reg[rs][1] < reg[rt][1]):
          reg[rd][1] = 1
        else:
          reg[rd][1] = 0

        updateReg1 = reg[rd][1]
        reg1 = reg[rd][2]

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        rd = "$" + str(rd)
        asm = "slt " + rd + ", " + rs + ", " + rt
        PC_plus4()
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_rd} | {b_sh} | {b_func}')
        print(f'in asm: {asm}')
        print(f'Updated registers: {reg1} = {updateReg1}')
        print(f'pc = {pc}')

    elif (b_op == '100011'):  # LW
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "lw " + rt + ", " + imm + '(' + rs + ')'
        PC_plus4()
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')
        print(f'pc = {pc}')

    elif (b_op == '101011'):  # SW
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "sw " + rt + ", " + imm + '(' + rs + ')'
        PC_plus4()
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')
        print(f'pc = {pc}')

    return (asm)


# here begins main

input_file = open("machinecode.txt", "r")
output_file = open("asm.txt", "w")
line_count = 0

for line in input_file:
    line_count += 1
    print(f'\n Line {line_count}:', end='')
    bin_str = hex_to_bin(line)
    asmline = process(bin_str)
    output_file.write(asmline + '\n')

input_file.close()
output_file.close()