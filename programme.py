import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel(r"C:/Users/geeta/Documents/student_data.xlsx")
total_marks = (df[' Math ']+df[' Physics ']+df[' Chemistry '])
df['total marks'] = total_marks
percentage = df['total marks'] /300 * 100
df['percentage'] = percentage
def grade(per):
    if per >= 90:
        return 'A+'
    elif per >= 80:
        return 'A'
    elif per >= 70:
        return 'B'
    elif per >= 60:
        return 'C'
    else:
        return "Failed"
df["Grade"] = df["percentage"].apply(grade)
top_performer = df.loc[df['total marks'].idxmax()]
print("student report",df)
print('top student',top_performer[['Name','total marks','percentage','Grade']])
grade_count = df['Grade'].value_counts()
plt.pie(grade_count.values,labels=grade_count.index,autopct='%1.1f%%')
plt.show()