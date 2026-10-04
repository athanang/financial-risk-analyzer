print('=========== STOCK PORTFOLIO ANALYZER ===========\n'
      'Portfolio: ')

import pandas as pd

data = {
    'Stock': ['Apple', 'Nvidia', 'Microsoft'],
    'Shares': [5, 8, 3],
    'Buy_price': [200, 150, 450],
    'Current_price': [230, 175, 500]
}

df = pd.DataFrame(data)

df['Invested'] = df['Buy_price'] * df['Shares']
df['Current_value'] = df['Current_price'] * df['Shares']
df['Profit_loss'] = df['Current_value'] - df['Invested']
df['Return'] = df['Profit_loss'] / df['Invested'] * 100

total = {
    'Stock': 'Total',
    'Shares': df['Shares'].sum(),
    'Buy_price': 0,
    'Current_price': 0,
    'Invested': df['Invested'].sum(),
    'Current_value': df['Current_value'].sum(),
    'Profit_loss': df['Profit_loss'].sum(),
    'Return': df['Profit_loss'].sum() / df['Invested'].sum() * 100
}
df['Weight'] = df['Invested'] / total['Invested'] * 100
total['Weight'] = df['Weight'].sum()

Best_Performer = df.loc[df['Return'].idxmax(), 'Stock']
Worst_Performer = df.loc[df['Return'].idxmin(), 'Stock']
Average_return = df['Return'].mean()

df.loc[len(df)] = total

print(df.to_string(index=False, float_format='%.2f'))

print('\nPORTFOLIO SUMMARY\n'
      '-----------------')
print(f'Total Invested: {total["Invested"]:.2f}\n'
      f'Current Value: {total["Current_value"]:.2f}\n'
      f'Total Profit: {total["Profit_loss"]:.2f}\n'
      f'Total Return: {total["Return"]:.2f}%')

print(f'\nBest Performer: {Best_Performer}')
print(f'Worst Performer: {Worst_Performer}')
print(f'\nAverage Return: {Average_return:.2f}%')