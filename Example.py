"""
Pylint Tutorial
"""
import time as t


# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods
# pylint:disable=bad-whitespace
# pylint: disable=unused-argument
class Car:
    """Example class"""
    static_color = 'black'
    def __init__(self, color):
        self.color = color

def crash(car1:Car, car2:Car):
    '''An example function'''
    car1.color = 'burnt'

# keyword and default arguments
# function that calculates cylinder volume
def cylinder_volume(height, radius = 5.0):
    """Volume of a cylinder
    Parameters:
    height (float): Height of the cylinder
    radius (float): Radius of the cylinder (default 5.0)
    Returns:
    float:Volume of the cylinder
    """
    return height * 3.14159 * radius**2

def int2hex(integer):
    """Function that converts an integer to a hexadecimal string"""
    try:
        hexadecimal = hex(integer)
        return hexadecimal
    except:
        print('An integer should be provided as input')
        hexadecimal = 0
    # finally:
    #     return hexadecimal




if __name__ == "__main__":

    start_timer = t.time()
    MY_CAR = Car('blue')
    crash(Car('red'), MY_CAR)

    # call the function
    int2hex(5)

    # list
    numbers = [1,2,3,4,5]

    # dictionary - students and grades
    grades = {'Eduardo':10, 'Andrea':9.5, 'Patricia':3.5}

    # tuple - latitude and longitude
    coordinates = (48.137 , 11.576)



    # calling the function using positional arguments
    print(cylinder_volume(10.3, 7.2))

    # calling the function using keyword arguments
    print(cylinder_volume(height = 10.3, radius = 7.2))
    end_timer = t.time()
    
    exeTime = end_timer - start_timer
    print(f"execution time took {exeTime * 1000} milliseconds")
    