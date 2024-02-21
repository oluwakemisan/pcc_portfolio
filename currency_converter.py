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