import pandas as pd
import matplotlib.pyplot as plt

"""
Dataset sourced from:

https://www.kaggle.com/datasets/anshtanwar/monthly-food-price-estimates

https://www.kaggle.com/datasets/iamsouravbanerjee/
customer-shopping-trends-dataset

"""


def generate_inflation_plot_3_countries(dataset, country1, country2, country3):
    """
    This function generates a line graph comparing inflation for every year
    for 3 countries. Retunrs None
    Uses the world_food_price_inflation_2007_2023.csv dataset

    Parameters:
        dataset : csv file
        country1 : string
        country2 : string
        country3 : string

    """

    # loading data
    food_inflation_df = pd.read_csv(dataset)

    # The year 2007 has no inflation data
    food_inflation_df.dropna(axis=0, inplace=True)

    # Date column is in str format, converting it into datetime
    food_inflation_df['date'] = pd.to_datetime(food_inflation_df['date'])

    # Creating separate variables for each country
    c1 = food_inflation_df[food_inflation_df['country'] == country1]
    c1_dates = c1['date']

    c2 = food_inflation_df[food_inflation_df['country'] == country2]
    c2_dates = c2['date']

    c3 = food_inflation_df[food_inflation_df['country'] == country3]
    c3_dates = c3['date']

    # Building the plot
    plt.figure()

    plt.plot(c1_dates, c1['Inflation'], label=country1)
    plt.plot(c2_dates, c2['Inflation'], label=country2)
    plt.plot(c3_dates, c3['Inflation'], label=country3)

    # labelling
    plt.legend(loc='upper right')
    plt.xlabel("Year")
    plt.ylabel("Inflation(%)")
    plt.title('Food price inflations of Afghanistan,Myanmar,Nigeria')
    plt.xticks(rotation=45)

    # Save as png, bbox_inches makes sure labels are not cut out.
    plt.savefig('figures/line_graph_comparing_inflations.png',
                bbox_inches='tight',
                dpi=200)
    plt.show()


def generate_bar_chart_inflation_sicnce_start(dataset):
    """
    This function generates 3 graphs, 2 bar charts and one line graph.
    Returns None.
    Uses the world_food_inflation_details.csv dataset

    Paramenters:
        dataset: csv file
    """

    # load data
    temp_df = pd.read_csv(dataset)

    # Removing the '%' symbol from the column, making it easier to use.
    temp_df['total_food_price_increase_since_start_date'] =\
        temp_df['total_food_price_increase_since_start_date'].str.replace(
            '%', '')

    # Converting the str inflation value to numeric, making it usable.
    temp_df['total_food_price_increase_since_start_date'] =\
        pd.to_numeric(temp_df['total_food_price_increase_since_start_date'])

    # Sorting the values in Ascending Order of Inflation values since start.
    temp_df = temp_df.sort_values('total_food_price_increase_since_start_date')

    # Creating a barchart
    plt.figure()
    plt.bar(temp_df['country'],
            temp_df['total_food_price_increase_since_start_date'])

    # Labelling
    plt.title('Increase in Inflation since 2008')
    plt.xlabel('Countries')
    plt.ylabel('Inflation(%) Since 2008')
    plt.xticks(rotation=90)

    # Save figure as png, bbox_inches makes sure the saved
    # figure does not cut out labels
    plt.savefig("figures/total_increase_inflation.png",
                bbox_inches='tight',
                dpi=200)

    plt.show()

    # Creating a line-graph
    plt.figure()
    plt.plot(temp_df['country'],
             temp_df['total_food_price_increase_since_start_date'])

    # labelling
    plt.xlabel('Countries')
    plt.ylabel('Inflation(%) Since 2008')
    plt.xticks(rotation=90)

    # Save figure as png.
    plt.savefig("figures/increase_in_inflation_line_graph.png",
                bbox_inches='tight',
                dpi=200)
    plt.show()

    # Removing the top 4 countries from the dataset
    # to visualise other countries.
    temp2 = temp_df.query(
        'country != ["Sudan","South Sudan", "Lebanon", "Syrian Arab Republic"]'
    )

    # Creating bar-chart
    plt.figure()

    bars = plt.bar(temp2['country'],
                   temp2['total_food_price_increase_since_start_date'])

    # Labelling
    plt.title("Increase in Inflation since 2008")
    plt.xlabel('Countries')
    plt.ylabel('Inflation(%) Since 2008')
    plt.xticks(rotation=90)

    # access the bar attributes to place the text in the appropriate location
    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x(), yval + 10, yval, ha='center', rotation='vertical')

    # Save figure as png.
    plt.savefig("figures/Inflation_since_start_(excluding last 4 countries)",
                bbox_inches='tight',
                dpi=200)
    plt.show()


def generate_pie_chart_transaction_types(dataset):
    """
    This function generates a pie chart for the shopping trends dataset.
    Returns None.
    Uses the shopping_trends_updated.csv dataset

    Parameters:
        dataset : csv file.

    """
    # loading data
    shopping_trends_df = pd.read_csv(dataset)

    # Using groupby function to group transactions by payment methods.
    # And then extracting sum of all purchases in that group.
    grouped_payments = shopping_trends_df.groupby(
        'Payment Method').sum()['Purchase Amount (USD)']

    # Creating variables for each category
    bank_transfer_total = grouped_payments['Bank Transfer']
    venmo_total = grouped_payments['Venmo']
    cash_total = grouped_payments['Cash']
    credit_card_total = grouped_payments['Credit Card']
    paypal_total = grouped_payments['PayPal']
    debit_card_total = grouped_payments['Debit Card']

    # Creating the pie-chart
    plt.figure()

    plt.pie([bank_transfer_total, venmo_total, cash_total,
            credit_card_total, paypal_total, debit_card_total],
            labels=['Bank Transfer', 'Venmo', 'Cash',
                    'Credit Card', 'PayPal', 'Debit Card'],
            autopct='%.1f%%')

    # labelling
    plt.title('Breakdown of Transaction type')
    plt.savefig("figures/pie_chart_transaction_type.png",
                bbox_inches='tight',
                dpi=200)

    plt.show()


def main():
    # Calling the line graph fucntion
    generate_inflation_plot_3_countries(
        'world_food_price_inflation_2007_2023.csv',
        'Afghanistan', 'Myanmar', 'Nigeria')

    # Calling the Bar charts function
    generate_bar_chart_inflation_sicnce_start(
        'world_food_inflation_details.csv')

    # Calling the pie chart function
    generate_pie_chart_transaction_types('shopping_trends_updated.csv')


if __name__ == "__main__":
    main()
