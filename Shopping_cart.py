# Simple Shopping Cart Program

groceries = []
costs = []
total = 0

while True:
    grocery = input('Enter a grocery to buy (q to quit):')
    if grocery.lower() == 'q':
        break
    else:
        cost = float(input(f'Enter the cost of grocery {grocery}: GH$'))
        groceries.append(grocery)
        costs.append(cost)

print('!!!!!YOUR CART !!!!!')

for grocery in groceries:
    print(grocery, end='')
    
for cost in costs:
    total += cost
    
print()
print(f'Your total cost is: GH${total}')   