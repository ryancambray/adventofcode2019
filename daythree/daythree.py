
# Load wire one's path into memory, then loop over wire two, incrementing each step and clocking when the wires cross and the co-ordinates
# that they cross on
wire_one = load_wire_one

# Each number represents the start co-ordinates, so the port. 
port = ["0,0"]
line = ["0,0"]
for step in wire_one:


def load_wire_one():
	with open("daythreewireone.txt", "r") as file:
		return file.read().split(",")

def load_wire_two():
	with open("daythreewiretwo.txt", "r") as file:
		return file.read().split(",")

def increment_manhattan_distance(current_coordinates, step, line):
	if step.startswith('R'):		
		get_current_line_and_add_next_step(step.split('R')[1], line, 0)
	elif step.startswith('L'):
		get_current_line_and_minus_next_step(step.split('L')[1], line, 0)
	elif step.startswith('D'):
		get_current_line_and_minus_next_step(step.split('D')[1], line, 1)
	elif step.startswith('U'):
		get_current_line_and_add_next_step(step.split('U')[1], line, 1)

def get_current_line_and_add_next_step(step, line, axis_to_update):
	current_line = line[-1]
	current_line.split(',')
	axis = current_line[axis_to_update] 
	axis = str(int(axis) + step)
	# Add latest co-ordinates to list
	if axis_to_update == 0:
		line.append(str(axis, current_line[1]))
	else:
		line.append(str(current_line[0], axis))

def get_current_line_and_minus_next_step(step, line, axis_to_update):
	current_line = line[-1]
	current_line.split(',')
	axis = current_line[axis_to_update] 
	axis = str(int(axis) - step)
	# Add latest co-ordinates to list
	if axis_to_update == 0:
		line.append(str(axis, current_line[1]))
	else:
		line.append(str(current_line[0], axis))