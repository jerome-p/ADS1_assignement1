import pandas as pd
import matplotlib.pyplot as plt

"""
Dataset sourced from:
    https://www.kaggle.com/datasets/anshtanwar/monthly-food-price-estimates
    https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023/discussion/445863
"""

def generate_inflation_plot_3_countries(dataset,country1,country2,country3):    
    """
    
    This function generates line plots for 3 countries from the world food
    inflation dataset.
    """
    
    food_inflation_df = pd.read_csv(dataset)
    
    #The year 2007 has no inflation data
    food_inflation_df.dropna(axis=0, inplace= True)
    
    #Date column is in str format, converting it into datetime
    food_inflation_df['date'] = pd.to_datetime(food_inflation_df['date'])
    
    c1 = food_inflation_df[food_inflation_df['country']==country1]
    c1_dates = c1['date'] 
    
    c2 = food_inflation_df[food_inflation_df['country']==country2]
    c2_dates = c2['date'] 
    
    c3 = food_inflation_df[food_inflation_df['country']==country3]
    c3_dates = c3['date'] 
    
    plt.figure()
    
    plt.plot(c1_dates,c1['Inflation'], label=country1)
    plt.plot(c2_dates,c2['Inflation'], label=country2)
    plt.plot(c3_dates,c3['Inflation'], label=country3)
    
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Inflation")
    plt.title('Line graph comparing inflations')
    plt.xticks(rotation=45)
    
    
    
    
generate_inflation_plot_3_countries('world_food_price_inflation_2007_2023.csv', 
                        'Afghanistan', 'Myanmar', 'Nigeria')


shopping_trends_df = pd.read_csv('shopping_trends_updated.csv')

print(shopping_trends_df['Payment Method'].unique())

grouped_payments = shopping_trends_df.groupby(
                            'Payment Method').sum()['Purchase Amount (USD)']

bank_transfer_total = grouped_payments['Bank Transfer']
venmo_total = grouped_payments['Venmo']
cash_total = grouped_payments['Cash']
credit_card_total = grouped_payments['Credit Card']
paypal_total = grouped_payments['PayPal']
debit_card_total = grouped_payments['Debit Card']

plt.figure()

plt.pie([bank_transfer_total,venmo_total,cash_total,
        credit_card_total,paypal_total,debit_card_total], 
        labels=['Bank Transfer','Venmo','Cash',
                'Credit Card','PayPal','Debit Card'],
        autopct='%.1f%%')

plt.title('Pie chart of transaction type')
plt.figure()
plt.bar(shopping_trends_df['Category'],shopping_trends_df['Review Rating'])
plt.title("Comparison of review ratings for each category of items sold")



temp_df = pd.read_csv('world_food_inflation_details.csv')
print(temp_df.head())

print(temp_df[['country','total_food_price_increase_since_start_date']])

temp_df['total_food_price_increase_since_start_date'] = temp_df['total_food_price_increase_since_start_date'].str.replace('%', '')

temp_df['total_food_price_increase_since_start_date'] = pd.to_numeric(temp_df['total_food_price_increase_since_start_date'])
temp_df = temp_df.sort_values('total_food_price_increase_since_start_date')


plt.figure()
plt.bar(temp_df['country'], temp_df['total_food_price_increase_since_start_date'])
plt.title('Total increase of ')
plt.xticks(rotation=90)

plt.figure()
line = plt.plot(temp_df['country'],temp_df['total_food_price_increase_since_start_date'])
plt.xticks(rotation=90)

temp2 = temp_df.query('country != ["Sudan", "South Sudan", "Lebanon", "Syrian Arab Republic"]' )
plt.figure()
bars = plt.bar(temp2['country'], temp2['total_food_price_increase_since_start_date'])
plt.xticks(rotation=90)

# access the bar attributes to place the text in the appropriate location
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + 10, yval, ha = 'center')
    
plt.show()


#myexplode = [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#plt.pie(temp2['total_food_price_increase_since_start_date'], labels=temp2['country'], explode= myexplode)
