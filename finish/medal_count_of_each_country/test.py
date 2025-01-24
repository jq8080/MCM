import pandas as pd
data = {
    'col1': [1, 2, 3, 4],
    'b': ['a', 'e', 'c', 'd'],
    'col3': [5, 6, 7, 8]
}
df = pd.DataFrame(data)
specific_value = 'e'
new_df = df[df['b'] == specific_value]
new_df.to_excel('new_sheet.xlsx', index=False)