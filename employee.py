"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self,name,contract,*args):
        self.name = name
        self.contract=contract
        self.data=args

    def get_pay(self):
        if self.contract=="salary":
            if len(self.data)==1:
                total=self.data[0]
            if len(self.data)==2:
                total=args[0]+args[1]
            if len(self.data)==3:
                total=args[0]+args[1]*args[2]
        elif self.contract=="hourly":
            if len(self.data)==2:
                total=self.data[0]*self.data[1]
            if len(self.data)==3:
                total=args[0]*args[1]+self.data[2]
            if len(self.data)==4:
                total=args[0]*args[1]+args[2]*args[3]
        self.total=total
        return total
    def __str__(self):
        if self.contract=="salary":
            if len(self.data)==1:
                str=f"{self.name} works on a monthly salary of {self.data[0]}.  Their total pay is {self.total}."
            if len(self.data)==2:
                str=f"{self.name} works on a monthly salary of {self.data[0]} and receives a bonus commission of {self.data[1]}.  Their total pay is {self.total}."
            if len(self.data)==3:
                str=f"{self.name} works on a monthly salary of {self.data[0]} and receives a commission for {self.data[1]} contract(s) at {self.data[2]}/contract.  Their total pay is {self.total}."
        elif self.contract=="hourly":
            if len(self.data)==2:
                str=f"{self.name} works on a contract of {self.data[0]} hours at {self.data[1]}/hour.  Their total pay is {self.total}."
            if len(self.data)==3:
                str=f"{self.name} works on a contract of {self.data[0]} hours at {self.data[1]}/hour and receives a bonus commission of {self.data[2]}.  Their total pay is {self.total}."
            if len(self.data)==4:
                str=f"{self.name} works on a contract of {self.data[0]} hours at {self.data[1]}/hour and receives a commission for {self.data[2]} contract(s) at {self.data[3]}/contract.  Their total pay is {self.total}."
        return str
    


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',"salary",4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',"hourly",100,25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',"salary",3000,4,200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',"hourly",150,25,3,220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',"salary",2000,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',"hourly",120,30,600)

