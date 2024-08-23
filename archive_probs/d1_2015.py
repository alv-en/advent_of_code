from assets import d1_2015_input

def floor_counter(input):
    acceptable_inputs=["(",")"]
    for i in list(input):
        if not i in acceptable_inputs:
            raise KeyError("input contains character(s) not accepted")
        else:
            total = len(list(input))
            floors_up=len([i for i in list(input) if i == "("])
            floors_down=total-floors_up
    return floors_up-floors_down

