
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# Определение DataFrame
data = pd.DataFrame({'whoAmI': lst})

# Создаем новые столбцы для каждого уникального значения в 'whoAmI'
for value in data['whoAmI'].unique():
    data[value] = data['whoAmI'].apply(lambda x: 1 if x == value else 0)

# Удаляем исходный столбец 'whoAmI'
data.drop('whoAmI', axis=1, inplace=True)

data.head()

