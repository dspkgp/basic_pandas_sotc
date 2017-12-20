import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

filepath = os.getcwd() + '\Book10.xlsx'
df = pd.read_excel(filepath)

# Renaming different columns for future use
df.rename(columns={'Total Exp':'Experience', 'Emp ID':'ID',
					'Functional Appraiser':'Appraiser', 'ZBO Dept':'zbo'}, inplace=True)

# Getting years of experience in years only
def cleanExp(experience):
    experience = experience.split()
    experience = map(lambda t : t.strip() , experience)
    experience = list(filter(lambda t : t.isdigit(), experience))

    return float(experience[0])+float(experience[1])/12

# Cleaning different columns from DataFrame
df['Experience'] = df['Experience'].map(cleanExp)
df['Role'] = df['Designation'].map(lambda Designation:Designation.split('-')[0].strip())
df['Department'] = df['Department'].map(lambda Department:Department.split('-')[0].strip())
df['Location'] = df['Location'].map(lambda location:location.split('IN:',2)[1].split('-')[0].strip())
df['zbo'] = df['zbo'].map(lambda dept:dept.split('-')[-1])

# Droping columns from DataFrame
column_list = ['Designation','Employee Category','Functional Appraiser ID','Date of Birth','Date of join']
for column in column_list:
	df.drop(column, inplace=True, axis=1)


# Getting count of Employees w.r.t. each Attributes
role_name=[]
role_count=[]

department_name=[]
department_count=[]

location_name=[]
location_count=[]

region_name=[]
region_count=[]

zone_name=[]
zone_count=[]

grade_name=[]
grade_count=[]

appraiser_name=[]
appraiser_count=[]

def get_unique_name_and_count(column, uniquename, count):

	for i in range(len(df[column].unique())):
		uniquename.append(str(df[column].unique()[i]))

	for element in df[column].unique():
		count.append(df[df[column]==element]['ID'].count())

get_unique_name_and_count('Appraiser', appraiser_name, appraiser_count)
get_unique_name_and_count('Grade', grade_name, grade_count)
get_unique_name_and_count('Zone', zone_name, zone_count)
get_unique_name_and_count('Region', region_name, region_count)
get_unique_name_and_count('Location', location_name, location_count)
get_unique_name_and_count('Department', department_name, department_count)
get_unique_name_and_count('Role', role_name, role_count)

# import ipdb;ipdb.set_trace()
"""
plotting for different results
and to get insights from the dataset
"""

#plot-1: plotting no of male and female employees
f = df[df['Gender']=='Female']['ID'].count()
m = df[df['Gender']=='Male']['ID'].count()
df1 = pd.DataFrame([f,m])
df1.index = ['Female','Male']
df1.plot(kind='bar', stacked=True, label='Gender', figsize=(8,6))
plt.ylabel('No of employee')
plt.legend()
plt.title('No. of male and female employees')
plt.show()
# plt.close()


#plot-2: plotting age distribution of employees
figure = plt.figure(figsize=(8,6))
bins = [10,20,30,40,40,50,60]
plt.hist(df['Age'], bins, histtype='bar',color=['c'],label='Age', rwidth=0.8)
plt.xlabel('Age')
plt.ylabel('No of employee')
plt.legend()
plt.title('Age distribution of employees')
plt.show()
# plt.close()

#plot-3: age distribution with gender
figure = plt.figure(figsize=(8,6))
plt.hist([df[df['Gender']=='Female']['Age'],df[df['Gender']=='Male']['Age']], stacked=True, color = ['g','r'],
	bins = [10,20,30,40,40,50,60],label = ['Female','Male'])
plt.xlabel('Age')
plt.ylabel('Number of employee')
plt.legend()
plt.title('Age distribution with gender')
plt.show()
# plt.close()

#plot-4: plotting distribution w.r.t experience
figure = plt.figure(figsize=(8,6))
bins = [0,2,4,6,8,10,12,14]
plt.hist(df['Experience'], bins, histtype='bar',color=['y'],label='Age', rwidth=0.8)
plt.xlabel('Experience (in years)')
plt.ylabel('No of employee')
plt.legend()
plt.title('Distribution w.r.t experience')
plt.show()
# plt.close()

def plotting_barplot(name,count,heading):
	figure=plt.figure(figsize=(13,8))
	x = [i for i in range(len(name))]
	ax2 = plt.subplot2grid((1,1),(0,0))
	ax2.bar(x,count,label='Grade',color='r')
	plt.xticks(x,name,rotation=90)
	plt.subplots_adjust(left=0.09,bottom=0.2,right=0.94,top=0.90,wspace=0.2, hspace=0)
	plt.title('No. of employees w.r.t.' +  str(heading))
	plt.ylabel('No of employee')
	plt.show()
	# plt.close()

plotting_barplot(location_name,location_count,'location')
plotting_barplot(role_name,role_count,'role')
plotting_barplot(department_name,department_count,'department')
plotting_barplot(region_name,region_count,'region')
plotting_barplot(zone_name,zone_count,'zone')
plotting_barplot(grade_name,grade_count,'grades')
plotting_barplot(appraiser_name,appraiser_count,'appraiser')
