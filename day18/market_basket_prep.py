import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

data = {
    'TransactionID': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5],
    'Activity': [
        'Coding', 'Chess', 'Pizza',
        'Coding', 'Chess',
        'Hiking', 'Photography', 'Pizza',
        'Hiking', 'Photography',
        'Coding', 'Pizza'
    ]
}

df = pd.DataFrame(data)

basket = (
    df.groupby(['TransactionID', 'Activity'])['Activity']
    .count()
    .unstack()
    .fillna(0)
)

basket_sets = (basket > 0).astype(int)

print("One-Hot Encoded Basket:")
print(basket_sets)