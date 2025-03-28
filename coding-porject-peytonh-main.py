# create 5 functions for different unit conversions 
# call functions using user input 
# 5 unit conversions: temperature (K,F,C); molar mass (g/mol); distance (meters to cm,mm,micro,nano,pico meters); wavelength/frequency; concentration

# creating functions for all conversion factors, I chose conversion factors that I commonly use in my chemistry classes  
def temperature_conversion():
    #the user is able to input any temperature and unit and get any output 
    input_temp = float(input("Please enter the temperature: "))
    input_unit = input("What are the units (F,K or C): ")
    output_unit = input("What units would you like to convert to (F, K, or C): ")
    if input_unit == 'F' and output_unit == 'K':
        conversion = ((input_temp-32)/1.8) + 273.15
        return conversion
    elif input_unit == 'F' and output_unit == 'C': 
        conversion = (input_temp-32)/1.8
        return conversion
    elif input_unit == 'K' and output_unit == 'C':
        conversion = input_temp - 273.15
        return conversion
    elif input_unit == 'K' and output_unit == 'F':
        conversion = (input_temp - 273.15) * 9/5
        return conversion
    elif input_unit == 'C' and output_unit == 'K':
        conversion = input_temp + 273.15
        return conversion
    else:
        conversion = (input_temp-32)/1.8
        return conversion

def molar_conversion():
    # this function converts from either grams to moles, or moles to grams, and asks for the molar mass as the conversion factor 
    print("For grams to moles, enter 'g to m', for moles to grams, enter 'm to g')")
    conversion = input("Please enter your preferred conversion: ")
    if conversion == 'g to m':
        input_mass = float(input("What is the mass of the substance (in g)? "))
        input_molar_mass = float(input("What is the molar mass of the substance?"))
        moles = input_mass / input_molar_mass
        return moles 
    else: 
        input_moles = float(input("How many moles do you have of the substance? "))
        input_molar_mass = float(input("What is the molar mass of the substance?"))
        grams = input_moles * input_molar_mass 
        return grams 

def distance_conversion():
    # this function converts from meters to any unit smaller than a meter, depending on the prefix chosen 
    # these prefixes are scales that we use to define molecular sizes 
    meters = float(input("Please enter the distance (in meters): "))
    prefix = input("What units are you converting to (centi,milli,micro,nano, or pico)? ")
    if prefix == 'centi':
        conversion = meters/10**-2
        return conversion
    elif prefix == 'milli':
        conversion = meters/10**-3
        return conversion
    elif prefix == 'micro':
        conversion = meters/10**-6
        return conversion
    elif prefix == 'nano':
        conversion = meters/10**-9
        return conversion
    else:
        conversion = meters/10**-12
        return conversion

def wavelength_conversion():
    # this performs a conversion between wavelength and frequency, using the speed of light as a conversion factor
    print("For wavelength to frequency, enter 'w to f'; for frequency to wavelength, enter 'f to w': ")
    chosen_conversion = input('Please enter your preferred conversion: ')
    if chosen_conversion == 'w to f':
        wavelength = float(input("please enter the wavelength (in meters): "))
        frequency = (2.98*10**8) / wavelength 
        return frequency 
    else:
        frequency = float(input('Please enter the frequency (in Hz): '))
        wavelength = (2.98*10**8) / frequency 
        return wavelength 

def concentration_conversion(): 
    # this is calculates the concentration of a solution in molarity, given the mass solute, volume solution, and molar mass 
    mass_substance = float(input("What is the mass of the solute?"))
    molar_mass = float(input("What is the molar mass of the solute? "))
    liters = float(input("How many liters of solvent do you have? "))
    molarity = (mass_substance/molar_mass) / liters
    return molarity 

# Creating the user interface, where they can call the conversion programs that they would like 
## printing the welcome message
print("Welcome! Here are the avaiable conversions:")
print("1: Temperature Conversion")
print("2: Molar Conversions")
print("3: Distance Conversions")
print("4: Wavelength/Frequency Conversions")
print("5: Concentration Conversions")
print("0: Quit")

## creating the loop which performs conversion 
while True:
    user_input = input("What conversion would you like to perform (1-5)? ")
    if user_input == '1':
        print(temperature_conversion())
    elif user_input == '2':
        print(molar_conversion())
    elif user_input == '3':
        print(distance_conversion())
    elif user_input == '4':
        print(wavelength_conversion())
    elif user_input == '5':
        print(concentration_conversion())
    elif user_input > '5':
        print("error. please enter a number 1-5")
    else:
        break 
print("Goodbye! See you again next time!") 