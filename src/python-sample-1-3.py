# some math based programs in python

"""
Python has a vast library of functions written in modules, right out of the box. Additionally, python community is massive and they have written a lot of more libraries too.
We will use a lot of libraries in our tutorials ahead.

You can import a module by using the "import" statement
e.g.
import math
imports the math module, which is a collection of libraries, which comprise of commonly used math functions.
"""


# math module has some functions which can be used in our programs
import math

"""
Some common math operators

1. Addition is done using '+' operator. e.g. a = 10 + 12, b = a + 2
2. Subtraction is done using '-' operator. e.g. a = 10 - 12, b = a - 2
3. Multiplication is done using '*' operator. e.g. a = 10 * 12, b = a * 2
4. Division is done using '/' operator. e.g. a = 10.0 / 12.0, b = a / 2.0. Note that / operator returns the quotient.
    To get the remainder of the division use the modulo operator %. e.g. rem = 10 % 3 will be 1, and quot = 10 / 3 will be 3
5. Exponents are calculated using the '**' operator. e.g. a = 10**2 (will give us a=100), b= 5**4 (will give us 5 to the power of 4 = 625)
6. Exponential notation is supported by writing e. what 'e' notation means is the number on the LHS of e will be multiplied with 10 raised to the RHS number
    e.g. Writing 3e2 is the same as writing 300 or 3 * (10 ** 2).
    Their values are the same, but they help represent larger values much easily in the exponent form.
"""

# some pythagoras theorem
# math.sqrt takes a float number and returns a square root
side_a = 3
side_b = 4
print("The hypotenuse of the triangle with sides 3 and 4 is: " +
      str(math.sqrt(3**2 + 4**2)))

# some trigonometric functions

# to convert angles between radians and degrees
angle_in_rads = math.radians(60)  # converts 60 to radians
# converts pi/2 radians to 90 degrees
angle_in_degree = math.degrees(math.pi/2)

print(angle_in_rads)
print(angle_in_degree)

# normal trigonometric functions can be accessed as math.sin math.cos math.tan. Inverse trigonometric functions can be accessed as
# math.asin math.acos math.atan.
# round(num, x) function rounds num off to x decimal places and returns a rounded value
side_a_opp_angle = round(math.degrees(math.asin(3/5)), 2)
side_a_adj_angle = round(math.degrees(math.acos(3/5)), 2)

print("The angle opp to side_a of length 3 is: " + str(side_a_opp_angle) +
      " deg and the angle adjacent to the side_a is " + str(side_a_adj_angle) + " deg.")


# let us write some functions to calculate some physics formulae


def potential_energy(mass, height):
    pot_energy = mass * 9.81 * height
    return pot_energy


def kinetic_energy(mass, velocity):
    kin_energy = 0.5 * mass * (velocity ** 2)
    return kin_energy


def distance_after_time(current_position, velocities, tm):
    # current_position is a tuple of representing current x and y coordinates (x, y)
    x_pos = current_position[0]
    y_pos = current_position[1]
    # velocities is a tuple of representing current x and y velocities
    x_vel = velocities[0]
    y_vel = velocities[1]
    # calculate the x and y displacement
    new_x_pos = x_vel * tm
    new_y_pos = y_vel * tm

    x_displacement = new_x_pos - x_pos
    y_displacement = new_y_pos - y_pos
    magnitude_displacement_vector = round(math.sqrt(
        x_displacement ** 2 + y_displacement ** 2), 2)
    angle_of_displacement_vector = round(math.degrees(
        math.atan(y_displacement / x_displacement)), 2)

    # return the displacement vector
    return (
        magnitude_displacement_vector,
        angle_of_displacement_vector
    )


print("The potential energy of a ball of mass 10kgs at a height of 15 meters is " +
        str(round(potential_energy(10, 15), 2)))

print("The kinetic energy of a ball of mass 10kgs moving at 15m/s is " +
        str(round(kinetic_energy(10, 15), 2)))


curr_pos = (10, 5)
velocities = (6, 2.3)
disp_vec = distance_after_time(curr_pos, velocities, 10)
print("The the displacement vector magnitude for a object travelling for 10 seconds is: " +
      str(disp_vec[0]) + "m and the angle is: " + str(disp_vec[1]) + " degrees")
