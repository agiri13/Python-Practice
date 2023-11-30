subject_id,student_id
10030,55000
10030,55804
10250,55804
10510,55000
#1. Use pandas to read the csv file, Data.csv
# Processing -> count the number of students per subject
#Sample output
10030 : 2
10250 : 1
10510 : 1

import pandas as pd
file = pd.read_csv('Data.csv')
num = file['subject_id'].value_counts()


#2. Use base Python only to read the csv file, Data.csv
# Processing -> count the number of students per subject
import csv
path = 'Data.csv'
counts={}
with open(path,'r') as file:
  reader = csv.Dictreader(file)
  for r in reader:
    class = row['subject_id']
    if class in counts:
      counts[class] += 1
    else:
      counts[class] = 1

for class, count in counts.items():
  print(f'{class},{count}')
  
  
  
  #SQL, datatable in a database
  select subject_id,count(student_id) 
  from datatable 
  group by subject_id
  having count(subject_id)=2;
  #having agg_fn condtion
  
  
  #1,1,2,3,5,8........
  n = 1 ; [1]
  n = 5 ; [1,1,2,3,5]
  def function(n):
    seq = []
    a, b = 0,1
    while len(seq) < n:
      seq.append(a)
      a,b = b, a+b
    return seq
    
  n = int(input('Enter number: '))
  fib = function