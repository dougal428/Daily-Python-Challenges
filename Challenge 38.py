#Question 37

#This problem was asked by Google.

#The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

#For example, given the set {1, 2, 3}, it should return { {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3} }.

#You may also use a list or array to represent a set.

#Answer 37


def get_power_set(numbers):
    if len(numbers) == 0:
        return [set([])]

    power_set = list()

    current_number = numbers[0]
    child_power_set = get_power_set(numbers[1:])
    power_set.extend(child_power_set)

    for child_set in child_power_set:
        new_set = child_set.copy()
        new_set.add(current_number)
        power_set.append(new_set)

    return power_set


assert get_power_set([]) == [set()]
assert get_power_set([1]) == [set(), {1}]
assert get_power_set([1, 2]) == [set(), {2}, {1}, {1, 2}]
assert get_power_set([1, 2, 3]) == [
    set(), {3}, {2}, {2, 3}, {1}, {1, 3}, {1, 2}, {1, 2, 3}]
assert get_power_set([1, 2, 3, 4]) == [
    set(), {4}, {3}, {3, 4}, {2}, {2, 4}, {2, 3}, {2, 3, 4}, {1}, {1, 4},
    {1, 3}, {1, 3, 4}, {1, 2}, {1, 2, 4}, {1, 2, 3}, {1, 2, 3, 4}]
