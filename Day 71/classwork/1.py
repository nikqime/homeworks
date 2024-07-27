class Car:
    def __init__(self, brand, model, current_speed, max_speed):
        # კუთვნილებები (attributes)
        self.brand = brand
        self.model = model
        self.current_speed = current_speed
        self.max_speed = max_speed

    # მეთოდი აქსელერაციისთვის
    def accelerate(self):
        if self.current_speed < self.max_speed:
            self.current_speed += 10
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed
        else:
            print("მაქსიმალურ სიჩქარეზეა")