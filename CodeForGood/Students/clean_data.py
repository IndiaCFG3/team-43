import pandas as pd
import re
from .models import Student

# filepath = get from drag drop
# filepath = r"student.csv"
df = pd.read_csv("student.csv")
print(df)


for d in df.itertuples():
    print(d)
    if re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', d.email):
        print('correct')
    else:
        print('incorrect')
        df = df.replace(to_replace = d.email, value = 'NaN')
    if len(str(d.ph_no)) ==10:
        print('correct')
    else:
        print('incorrect')
        df = df.replace(to_replace = d.ph_no, value = 'NaN')

print(df)
df.to_csv('clean_student.csv')

df_records = df.to_dict()

model_instances = [Student(
    =record['field_1'],
    field_2=record['field_2'],
) for record in df_records]

MyModel.objects.bulk_create(model_instances)