
class animal:
    def __init__(self, arm_length, leg_length, number_of_eyes, tail, furry, name):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.number_of_eyes = number_of_eyes
        self.tail = tail
        self.furry = furry
        self.name = name

def describe_animal(self):
        
        tail_status = "has a tail" if self.tail else "does not have a tail"
        furry_status = "is furry" if self.furry else "is not furry"

        print(f"The {self.name} has the following physical characteristics:")
        print(f"  - Arm length: {self.arm_length} cm")
        print(f"  - Leg length: {self.leg_length} cm")
        print(f"  - Number of eyes: {self.number_of_eyes}")
        print(f"  - It {tail_status}.")
        print(f"  - It {furry_status}.")

spider = animal(arm_length=30.0, leg_length=30.0, number_of_eyes=8, tail=False, furry=True, name="Spider")

describe_animal(spider)