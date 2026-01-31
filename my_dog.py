class MyDog:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("My dog's name is ", self.name)

x = MyDog("Tagpi")

def calculate_force(mass, acc):
    # This function calculates the force based on mass and acceleration
    # Mass should be in kilograns
    # Acceleration should be in meters per second squared
    force = mass * acc # calculating force
    return force

x.show_name()

frc = calculate_force(9, 7)
print("Force is: ", frc)


