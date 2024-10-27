
Objective: Determine the number of jobs currently open for various technologies and for various locations
Collect the number of job postings for the following locations using the API:

#Import required libraries
import pandas as pd
import json
​
Write a function to get the number of jobs for the Python technology.
Note: While using the lab you need to pass the payload information for the params attribute in the form of key value pairs. Refer the ungraded rest api lab in the course Python for Data Science, AI & Development link

The keys in the json are
Job Title

Job Experience Required

Key Skills

Role Category

Location

Functional Area

Industry

Role

You can also view the json file contents from the following json URL.

api_url="http://127.0.0.1:5000/data"
def get_number_of_jobs_T(technology):
    payload={"Key Skills": technology}
    response=requests.get(api_url, params=payload)
    if response.ok:
        data= response.json()
        number_of_jobs = len(data)
    #your code goes here
    return technology,number_of_jobs
Calling the function for Python and checking if it works.

get_number_of_jobs_T("Python")
('Python', 1173)
Write a function to find number of jobs in US for a location of your choice
 def get_number_of_jobs_L(location):
    payload = {"Location": location}
    response = requests.get(api_url, params=payload)
    if response.ok:
        data = response.json()
        number_of_jobs = len(data)
    #your coe goes here
    return location,number_of_jobs
Call the function for Los Angeles and check if it is working.

#your code goes here
get_number_of_jobs_L('Los Angeles')
('Los Angeles', 640)
Store the results in an excel file
Call the API for all the given technologies above and write the results in an excel spreadsheet.

If you do not know how create excel file using python, double click here for hints.

Create a python list of all technologies for which you need to find the number of jobs postings.

#your code goes here
countries = ['Los Angeles', 'New York', 'San Francisco', 'Washington DC', 'Seattle', 'Austin', 'Detroit']
Import libraries required to create excel spreadsheet

# your code goes here
!pip install openpyxl
from openpyxl import Workbook
Collecting openpyxl
  Downloading openpyxl-3.1.3-py2.py3-none-any.whl (251 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 251.3/251.3 kB 29.5 MB/s eta 0:00:00
Collecting et-xmlfile (from openpyxl)
  Downloading et_xmlfile-1.1.0-py3-none-any.whl (4.7 kB)
Installing collected packages: et-xmlfile, openpyxl
Successfully installed et-xmlfile-1.1.0 openpyxl-3.1.3
Create a workbook and select the active worksheet

# your code goes here
wb=Workbook()
ws=wb.active
ws.append(countries)
Find the number of jobs postings for each of the technology in the above list. Write the technology name and the number of jobs postings into the excel spreadsheet.

#your code goes here
def get_number_of_jobs_TL(technology, countries):
    number_of_jobs_list = []
    for location in countries:
        payload={"Key Skills": technology, "Location": location}
        response=requests.get(api_url, params=payload)
        if response.ok:
            data=response.json()
            number_of_jobs = len(data)
            number_of_jobs_list.append(number_of_jobs)
    return number_of_jobs_list
get_number_of_jobs_TL("Python", countries)
[24, 143, 17, 258, 133, 15, 170]
Save into an excel spreadsheet named 'github-job-postings.xlsx'.

#your code goes here
wb.save('github-job-posting.xlsx')
In the similar way, you can try for below given technologies and results can be stored in an excel sheet.
Collect the number of job postings for the following languages using the API:

C
C#
C++
Java
JavaScript
Python
Scala
Oracle
SQL Server
MySQL Server
PostgreSQL
MongoDB
# your code goes here
technologies = ['C', 'C#', 'C++', 'Java', 'JavaScript', 'Python', 'Scala', 'Oracle', 'SQL Server', 'MySQL Server', 'PostgreSQL', 'MongoDB']
​
def get_number_of_jobs_TL(technologies, countries):
    final_list = []
    for technology in technologies:
        number_of_jobs_list = [technology]
        for location in countries:
            payload={"Key Skills": technology, "Location": location}
            response=requests.get(api_url, params=payload)
            if response.ok:
                data=response.json()
                number_of_jobs = len(data)
                number_of_jobs_list.append(number_of_jobs)
​
        final_list.append(number_of_jobs_list)
    return final_list
​
get_number_of_jobs_TL(technologies, countries)
[['C', 296, 1622, 214, 2664, 1668, 224, 1973],
 ['C#', 5, 41, 3, 68, 49, 5, 60],
 ['C++', 3, 43, 3, 55, 41, 4, 32],
 ['Java', 43, 326, 38, 516, 354, 32, 353],
 ['JavaScript', 7, 51, 7, 61, 52, 5, 41],
 ['Python', 24, 143, 17, 258, 133, 15, 170],
 ['Scala', 0, 8, 0, 3, 4, 1, 5],
 ['Oracle', 17, 95, 19, 143, 110, 11, 115],
 ['SQL Server', 3, 36, 2, 53, 31, 5, 34],
 ['MySQL Server', 0, 0, 0, 0, 0, 0, 0],
 ['PostgreSQL', 0, 1, 0, 3, 1, 0, 2],
 ['MongoDB', 2, 25, 2, 32, 21, 1, 25]]
