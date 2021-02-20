#Question 21

#This problem was asked by Snapchat.

#Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
#find the minimum number of rooms required.

#For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.



#create function with intake of the time intervals
def get_num_classrooms(timing_tuples):
    #if none return 0
    if not timing_tuples:
        return 0
    #else create dict to enter start and end times seperately
    start_times = dict()
    end_times = dict()
    #for each time in start and end in tuple list
    for start, end in timing_tuples:
        #if start time not alreasy in put in at numerical ordering
        if start not in start_times:
            start_times[start] = 0
        #add one in numerical order
        start_times[start] += 1

        #if end time not alreasy in put in at numerical ordering
        if end not in end_times:
            end_times[end] = 0
        #add one in numerical order
        end_times[end] += 1

    #find which time earliest start and latest end
    global_start, global_end = min(start_times), max(end_times)

    #create max class count variable - set to zero
    max_class_count = 0
    #create current class count variable - set to zero
    current_class_count = 0
    
    #loop through class time, for range between earliest start time and latest start time of classes
    for i in range(global_start, global_end):
        #for each start time
        if i in start_times:
            #add one to current class count cia the start time index
            current_class_count += start_times[i]
            #if current class count count greater than max class count so far
            if current_class_count > max_class_count:
                #make it the new max class count
                max_class_count = current_class_count
        #for each end time
        if i in end_times:
            #minus one to current class count cia the end time index
            current_class_count -= end_times[i]
            
    #return thee number class rooms needed
    return max_class_count


assert get_num_classrooms([]) == 0
assert get_num_classrooms([(30, 75), (0, 50), (60, 150)]) == 2
assert get_num_classrooms([(30, 75), (0, 50), (10, 60), (60, 150)]) == 3
assert get_num_classrooms([(60, 150)]) == 1
assert get_num_classrooms([(60, 150), (150, 170)]) == 2
assert get_num_classrooms([(60, 150), (60, 150), (150, 170)]) == 3
