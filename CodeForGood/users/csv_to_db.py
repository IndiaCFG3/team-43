import pandas as pd
from .models import Student,Employee,BatchStudent


def db_save():
    tmp_data=pd.read_csv('../../media/student.csv',sep=',')
    #ensure fields are named~ID,Product_ID,Name,Ratio,Description
    #concatenate name and Product_id to make a new field a la Dr.Dee's answer
    students = [
        Student(
            student_id = row.id, 
            student_name = row.name,
            score = row.score,
            rating = row.rating,
            performance = row.performance,
            email = row.email
        )
        for row in tmp_data.itertuples()
    ]
    Student.objects.bulk_create(students)

    tmp_data=pd.read_csv('../../media/employee.csv',sep=',')
    employees = [
        Employee(
            employee_id =row.id,
            # employee_name = tmp_data.ix[row]['name'],
            manager_name = row.manager,
            rating = row.rating,
            leaves_taken = row.leaves
        )
        for row in tmp_data.itertuples()
    ]
    Employee.objects.bulk_create(employees)

    tmp_data=pd.read_csv('../../media/student_batch.csv',sep=',')

    batches = [
        BatchStudent(
            # student_id = Student.objects.get(student_id = row.student_id),
            student_id = row.student_id,
            batch_id = row.batch_id,
        )
        for row in tmp_data.itertuples()
    ]
    BatchStudent.objects.bulk_create(batches)

    return 1

import pandas as pd
import re
from .models import Student

# filepath = get from drag drop
# filepath = r"student.csv"
df = pd.read_csv("student.csv")
print(df)


# for d in df.itertuples():
#     print(d)
#     if re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', d.email):
#         print('correct')
#     else:
#         print('incorrect')
#         df = df.replace(to_replace = d.email, value = 'NaN')
#     if len(str(d.ph_no)) ==10:
#         print('correct')
#     else:
#         print('incorrect')
#         df = df.replace(to_replace = d.ph_no, value = 'NaN')

# print(df)
# df.to_csv('clean_student.csv')

# df_records = df.to_dict()

# model_instances = [Student(
#     =record['field_1'],
#     field_2=record['field_2'],
# ) for record in df_records]

# MyModel.objects.bulk_create(model_instances)