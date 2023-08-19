import random # importing libraries

def generate_random_vector(dim): #creating the function named generate_random_numbers
    return [random.random() for _ in range(dim)] #returning the random values of float in different dimentions
