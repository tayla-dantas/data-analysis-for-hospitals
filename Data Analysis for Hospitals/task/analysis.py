import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


pd.set_option('display.max_columns', 8)
general = pd.read_csv('./general.csv')
prenatal = pd.read_csv('./prenatal.csv')
sports = pd.read_csv('test/sports.csv')

prenatal.rename(columns={'Sex': 'gender', 'HOSPITAL': 'hospital'}, inplace=True)
sports.rename(columns={'Male/female': 'gender', 'Hospital': 'hospital'}, inplace=True)
prenatal_df = pd.DataFrame(prenatal)
sports_df = pd.DataFrame(sports)
general_df = pd.DataFrame(general)

new_data = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)
new_data.drop(columns=['Unnamed: 0'], inplace=True)

new_data = new_data.dropna(how='all')

new_data.loc[new_data.gender == 'male', 'gender'] = "m"
new_data.loc[new_data.gender == 'man', 'gender'] = "m"
new_data.loc[new_data.gender == 'female', 'gender'] = "f"
new_data.loc[new_data.gender == 'woman', 'gender'] = "f"
new_data.loc[new_data.hospital == 'prenatal', 'gender'] = "f"


new_data.iloc[:, 6:] = new_data.iloc[:, 6:].fillna(0)
sample_data = new_data.sample(n=20, random_state=30)

general_all_diagnosis = new_data.loc[new_data.hospital == 'general', 'diagnosis']
share_general_stomach =  general_all_diagnosis.value_counts().get('stomach', 0) / general_all_diagnosis.value_counts().agg('sum')

sports_all_diagnosis = new_data.loc[new_data.hospital == 'sports', 'diagnosis']
share_sports_dislocation =  sports_all_diagnosis.value_counts().get('dislocation', 0) / sports_all_diagnosis.value_counts().agg('sum')

general_all_age = new_data.loc[new_data.hospital == 'general', 'age'].median()
sports_all_age = new_data.loc[new_data.hospital == 'sports', 'age'].median()
prenatal_all_age = new_data.loc[new_data.hospital == 'prenatal', 'age'].median()

difference_median = general_all_age - sports_all_age


new_pivoted = new_data.pivot_table(index="hospital", columns='blood_test', values='diagnosis', aggfunc="count", fill_value=0)

max_column = new_pivoted['t'].idxmax()


max_value = new_pivoted.loc[max_column,'t' ]

#print("The answer to the 1st question is " + str(new_data.hospital.value_counts().idxmax()))
#print("The answer to the 2st question is " + str(round(share_general_stomach,3)))
#print("The answer to the 3st question is " + str(round(share_sports_dislocation,3)) )
#print("The answer to the 4st question is " + str(round(difference_median)))
#print("The answer to the 5st question is " + max_column + ', '+ str(round(max_value)) + " blood tests")


#histograma
new_data.plot(y=['age'], kind='hist', alpha=0.5)
plt.show()

value_counts = new_data['diagnosis'].value_counts()

#gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart for Specific Column')
plt.axis('equal')
plt.show()

#gráfico de violino
sns.violinplot(y=new_data['height'])
plt.title('Violin Plot for Specific Column')
plt.show()

print("The answer to the 1st question: 15-35")
print("The answer to the 2nd question: pregnancy")
print("The answer to the 3rd question: It's because of the measurement system")