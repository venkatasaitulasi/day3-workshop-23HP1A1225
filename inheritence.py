class Car:
    def __init__(self, engine, body, color, tyres):
        self.engine=engine
        self.body=body
        self.color=color
        self.tyres=tyres

    def  __repr__(self):
        return f'{self.engine}, {self.body}'

    def car_prop(self):
        print(f"{self.engine} {self.body}")

class bmw(Car):
    def __init__(self, seats, music):
        self.seats=seats
        self.music=music 
    
    def __repr__(self):
        return f'(super().engine) {self.body}'