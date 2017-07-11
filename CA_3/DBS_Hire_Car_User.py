#CA 3 Programming for Big data. B8IT105 (B8IT105_1617_TMD3)
#Stuart O'Rourke
#Student Number: 10334192
#DBS Car Rental.


from car import * # import all instances of the car class

class Dealership(object):
		
	def __init__(self):
		self.electric_cars = []
		self.petrol_cars = []
		self.diesel_cars = []
		self.hybrid_cars = []
        
#Pool inventory control, 40 cars in Pool
	
	def current_stock(self): 
		for i in range(5):
			self.electric_cars.append(ElectricCar())
			for i in range(20):
				self.petrol_cars.append(PetrolCar())
				for i in range(8):
					self.diesel_cars.append(DieselCar())
					for i in range(7):
						self.hybrid_cars.append(HybridCar())

#Pool of cars, current status

	def stock_count(self): 
	 print 'Petrol car Pool: ' + str(len(self.petrol_cars))
	 print 'Electric car Pool: ' + str(len(self.electric_cars))
	 print 'Diesel Car Pool: ' + str(len(self.diesel_cars))
	 print 'Hybrid Car Pool: ' + str(len(self.hybrid_cars))
	
	def rent(self, car_list, amount):
		if len(car_list) < amount:
			print 'Sorry! Not enough cars available in Pool, at current time! :'
			return
        total = 0
        #while total < amount:
        #car_list.pop()# removes car from top of stack.
           #total = total + 1 # increments variable total. 

#User Rental process interaction.
	def process_rental(self):
		licence = raw_input('Do you have a Full European Licence or International Licence\n: Y/N') 
		if licence =='N':
			print 'Sorry! Your licence does not meet our requirements '
			#licence = 'N'
        #while licence = 'N':
			print 'Thank you for visiting DBS Car Hire, Sorry we are unable to help you today'        
	
	propulsion = raw_input('Which of these Cars would you like to hire ?:\n D-Diesel\n E-Electric\n H-Hybrid\n P-Petroleum\n : ')
	Quantity = int(raw_input('How many would you like to hire in this transaction ?: '))
        if propulsion == 'D':
            self.rent(self.diesel_cars, Quantity)
        elif propulsion == 'E':
            self.rent(self.electric_cars, Quantity)
        elif propulsion =='H':
            self.rent(self.hybrid_cars, Quantity)
        elif propulsion =='P':
            self.rent(self.petrol_cars, Quantity)
        
        self.stock_count()

#Return cars to Pool count
	
	
	def returns(self, car_list, amount):
		total = 0 #initialise total to zero for counting.
        if amount < 0:
            print 'Positive whole numbers only'
        else:
            while total < amount:
                car_list.append(1)
                total = total + 1
            print 'Car passed inspection, Serviced and Fueled/charged.'

# Pool list of returned cars

	def CarReturn(self):
		enginetype = raw_input("What type of car are you returning?\nElectric - E\nPetrol - P\nHybrid - H\nDiesel - D\n: ")
        quan_car = int(raw_input('How many cars are you returning?\n: '))
        if type == 'E' and len(self.electric_cars) + quan_car <= 5:
            self.returns(self.electric_cars, quan_car)
        elif type == 'P' and len(self.petrol_cars) + quan_car <= 20:
            self.returns(self.petrol_cars, quan_car)
        elif type == 'H' and len(self.hybrid_cars) + quan_car <= 7:
            self.returns(self.hybrid_cars, quan_car)
        elif type == 'D'and len(self.diesel_cars) +  quan_car <= 8:
            self.returns(self.diesel_cars, quan_car)
			
#User section allows user input
	def user(self):
		print 'Welcome to DBS Car Hire:\n'
		self.stock_count()
		use = raw_input("Would you like to Hire 'H' or Return 'R' a vehicle?\n: ")
		if use == 'R':
			self.process_rental()
		else:
			self.CarReturn()
		
if __name__ == '__main__':
    rent = Dealership()
    rent.current_stock()
    cont = 'Y'
    
    while cont == 'Y':
        try:
            rent.user()
        except:
            print 'Thank you for using DBS Car Hire.'
        cont = raw_input('Do you wish to continue? Y/N: ')
    
