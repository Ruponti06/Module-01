usd = input('Enter USD Amount: ')
usd_number = int(usd)
# print(type(usd_number))
exchange_rate = 102
bdt = usd_number * exchange_rate
print(usd_number,'USD is equal to Tk.', bdt)
