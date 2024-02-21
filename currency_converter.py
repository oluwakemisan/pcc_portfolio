def weight_converter():
    #kg,g
    value = float(input("enter a value: "))
    original_unit = int(input('original: enter 1 for (kg) or 2 for (g) for the value:'))
    final_unit = int(input('final: enter 1 for (kg) or 2 for (g) for the value:'))
    if original_unit == 1:
        if final_unit == 1:
            print(f'{value}kg is equivalent to {value}kg\n')
        elif final_unit == 2:
            result = value*1000
            print(f'{value}kg is equivalent to {result}g\n')
        else:
            print('Please Enter a valid unit')
    elif original_unit == 2:
        if final_unit == 1:
            print(f'{value}g is equivalent to {value/1000}kg\n')
        elif final_unit == 2:
            
            print(f'{value}g is equivalent to {value}g\n')
        else:
            print('please Enter a valid unit')
    else:
        print("Please enter a valid number")      
    
def length_converter():   
      #CM to M and M to CM
    value = float(input('input a length value: '))
    original_length = int(input('original: enter 1 for (CM) or 2 for (M) for the value:'))
    final_unit = int(input('final: enter 1 for (CM) or 2 for (M) for the value:'))
    if original_length == 1 and final_unit == 2:
            print(f'{value}CM is equivalent to {value/100}M\n')
    elif original_length == 2 and final_unit == 1:
            print(f'{value}M is equivalent to {value*100}CM\n')
    else:
        print("Please enter a valid number range")
        
def temperature_converter():
    # fahrenheit ('f), celsius ('c), kelvin('k)
    value = float(input('Input a temperature value: '))
    original_temperature = int(input('Original Temperature: enter 1 for (c) or 2 for (f) or 3 for (k) : '))
    final_temperature = int(input('Final Temperature: enter 1 for (c) or 2 for (f) or 3 for (k): '))
    if original_temperature == 1 and final_temperature == 2:
        print(f'{value}C is equivalent to {value*9/5+32}F\n')
    elif original_temperature ==1 and final_temperature ==3:
        print(f'{value}C is equivalent to {value+273.15}K\n')
    elif original_temperature == 2 and final_temperature == 1:
        print(f'{value}F is equivalent to {(value -32)*(5/9)}C\n')
    elif original_temperature ==2 and final_temperature ==3:
        print(f'{value}F is equivalent to {(value-32)*(5/9)+(273.15)}k\n')
    elif original_temperature == 3 and final_temperature ==1:
        print(f'{value}K is equivalent to {value-273.15}C\n')
    elif original_temperature ==3 and final_temperature ==2:
        print(f'{value}K is equivalent to {(value -273.15)*(9/5) +32}F\n')
    else:
        print('Enter a valid number range')    
        
def currency_converter():
      # Naira, Pounds, US dollars, Euro
      value = float(input('Enter the amount to convert'))
      original_currency = int(input('Original Currency: enter 1 for (NGN), 2 for (USD), 3 for (EUR),4 for (GBP): '))
      final_currency = int(input('Final Currency: enter 1 for (NGN), 2 for (USD), 3 for (EUR),4 for (GBP): '))
      if original_currency ==1 and final_currency ==2:
          print(f'{value}NGR is equivalent to {value*0.000658}USD\n')
      elif original_currency == 1 and final_currency ==3:
          print(f'{value}NGR is equivalent to {value*0.000622}EUR\n')
      elif original_currency == 1 and final_currency ==4:
          print(f'{value}NGR is equivalent to {value*0.00053}GBP\n')
      elif original_currency == 2 and final_currency ==1:
          print(f'{value}USD is equivalent to {value*1520.12}NGR\n')
      elif original_currency ==2 and final_currency ==3:
          print(f'{value}USD is equivalent to {value*0.92004}EUR\n')
      elif original_currency ==2 and final_currency ==4:
          print(f'{value}USD is equivalent to {value*0.78628}GBD\n')
      elif original_currency ==3 and final_currency ==1:
          print(f'{value}EUR is equivalent to {value*1607.136}NGN\n')
      elif original_currency ==3 and final_currency ==2:
          print(f'{value}EUR is equivalent to {value*1.08692}UDS\n')
      elif original_currency ==3 and final_currency ==4:
          print(f'{value}EUR is equivalent to {value*0.85461}GBP\n')
      elif original_currency ==4 and final_currency ==1:
          print(f'{value}GBP is equivalent to {value*1884.665}NGR \n')
      elif original_currency == 4 and final_currency ==2:
          print(f'{value}GBP is equivalent to {value*1.27182}USD \n')
      elif original_currency ==4 and final_currency ==3:
          print(f'{value}GBP is equivalent to {value*1.17012}EUR \n')
      else:
        print('Enter a valid number range')

          
while True:
    print('This is a unit converter')
    print('press (1) to convert to weight')
    print('press (2) to convert to length')
    print('press (3) to convert to temperature')
    print('press (4) to convert to currency')
    print('press (5) to exit the program')
    
    value = int(input('Enter:'))
    
    if value == 1:
        weight_converter()
    elif value ==2:
        length_converter()
    elif value ==3:
        temperature_converter()
    elif value ==4:
        currency_converter()
    elif value ==5:
       print('existing program')
       break