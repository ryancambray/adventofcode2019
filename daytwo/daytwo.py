
def calculate_position_zero():
    with open("puzzle.txt", "r") as file:
        # Add csv into list
        csv = file.read().split(",")

        code = 0
        position_one = 1
        position_two = 2
        index_to_override = 3

        while code < len(csv):
            # get values from csv that we are going to use
            op_code = int(csv[code])
            index_one = int(csv[position_one])
            index_two = int(csv[position_two])
            index_three = int(csv[index_to_override])

            index_one_value = int(csv[index_one])
            index_two_value = int(csv[index_two])

            if op_code == 1:
                override = index_one_value + index_two_value
                csv[index_three] = override

            elif op_code == 2:
                override = index_one_value * index_two_value
                csv[index_three] = override

            elif op_code == 99:
                # Finished, halt
                print("op code 99 found. Halting program. Position 0 value is: {}".format(csv[0]))
                quit(0)

            else:
                print("Unknown OP code. Something has gone wrong.")
                raise Exception("UNKNOWN OP CODE")

            code += 4
            position_one += 4
            position_two += 4
            index_to_override += 4

calculate_position_zero()
