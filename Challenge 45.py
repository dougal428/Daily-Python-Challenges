#Question 45

#This problem was asked by Two Sigma.

#Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, 
#implement a function rand7() that returns an integer from 1 to 7 (inclusive).

#Answer 45


from random import randint


def rand5():
    return randint(1, 5)


def rand7():
    i = 5*rand5() + rand5() - 5  # uniformly samples between 1-25
    if i < 22:
        return i % 7 + 1
    return rand7()


num_experiments = 100000
result_dict = dict()
for _ in range(num_experiments):
    number = rand7()
    if number not in result_dict:
        result_dict[number] = 0
    result_dict[number] += 1

desired_probability = 1 / 7
for number in result_dict:
    result_dict[number] = result_dict[number] / num_experiments
    assert round(desired_probability, 2) == round(result_dict[number], 2)
