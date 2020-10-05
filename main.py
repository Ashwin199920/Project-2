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

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "addi " + rt + ", " + rs + ", " + imm
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')

    elif (b_op == '000000') and (b_func == '100000'):  # ADD
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        rd = int(b_rd, base=2)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        rd = "$" + str(rd)
        asm = "add " + rd + ", " + rs + ", " + rt
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_rd} | {b_sh} | {b_func}')
        print(f'in asm: {asm}')
        #print (f'NO idea about op = {b_op}')

    elif (b_op == '000000') and (b_func == '100010'):  # SUB
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        rd = int(b_rd, base=2)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        rd = "$" + str(rd)
        asm = "sub " + rd + ", " + rs + ", " + rt
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_rd} | {b_sh} | {b_func}')
        print(f'in asm: {asm}')

    elif (b_op == '001100'):  # ANDI
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "andi " + rt + ", " + rs + ", " + imm
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')

    elif (b_op == '000000') and (b_func == '101010'):  # SLT
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        rd = int(b_rd, base=2)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        rd = "$" + str(rd)
        asm = "slt " + rd + ", " + rs + ", " + rt
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_rd} | {b_sh} | {b_func}')
        print(f'in asm: {asm}')

    elif (b_op == '100011'):  # LW
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "lw " + rt + ", " + imm + '(' + rs + ')'
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')

    elif (b_op == '101011'):  # SW
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "sw " + rt + ", " + imm + '(' + rs + ')'
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')

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
