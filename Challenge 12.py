#This problem was asked by Amazon.

#There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
#Given N, write a function that returns the number of unique ways you can climb the staircase. 
#The order of the steps matters.

#For example, if N is 4, then there are 5 unique ways:

# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers
# X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

#create function with varibles number of steps and step size
def get_step_combos(num_steps, step_sizes):
    # set empty list tp store combos
    combos = list()
    
    #if numbeer of steps less then smallest subszie then return empty combos
    if num_steps < min(step_sizes):
        return combos
    
    #loop for each value in step size list
    for step_size in step_sizes:
        #if number of steps equal to step size append to combos
        if num_steps == step_size:
            combos.append([step_size])
        # if number steps greater then step size
        elif num_steps > step_size:
            # create variable which stores the combos of step sziie for number of steps
            child_combos = get_step_combos(num_steps - step_size, step_sizes)
            # loop through new variable and append the combination to combo list
            for child_combo in child_combos:
                combos.append([step_size] + child_combo)
    return combos


get_step_combos(4, [1, 2])
