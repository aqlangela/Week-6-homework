import random

random.seed(0)

SIZE = 10


class PancakeStack():
    def __init__(self, stack = None):
        self.stack = stack

    def get_size(self):
        return len(self.stack)

    # Check if the current level has a smaller size
    def check_smaller(self, index):
        if self.stack[index] < self.stack[index-1]:
            return True
        return False
        
    # Find the proper location
    # Put it before the first number it's smaller than
    def get_location(self, index):
        for j in range(1, index+1):
            if self.stack[j] > self.stack[0]:
                return (j - 1)
        return 0

    # Slide the pan under pancake at desired index and flip to top
    def flip(self, index):
        self.stack = self.stack[:index+1][::-1] + self.stack[index+1:]

def sort_pancakes(pancakes):
    pancakes_size = pancakes.get_size()
    count = 0
    for i in range(1, pancakes_size):
        # Only run when the current level has a smaller size
        if pancakes.check_smaller(i):
            # Flip above
            pancakes.flip(i-1)
            # Flip this pancake up to the top
            pancakes.flip(i)
            # Flip to its proper location
            location = pancakes.get_location(i)
            pancakes.flip(location)
            # Flip the pancakes at top back to their positions before last filp
            pancakes.flip(location-1)
            count += 1
            print("After flip %d at index %d:" % (count, i), pancakes.stack)
    return pancakes.stack


if __name__ == "__main__":
    my_stack = random.sample(range(1, 20), SIZE)
    print("Unsorted pancakes:", my_stack)
    case_one = PancakeStack(my_stack)
    print("Final order of pancakes:", sort_pancakes(case_one))
    
    
    
