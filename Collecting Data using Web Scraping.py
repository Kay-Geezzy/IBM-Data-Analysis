#this url contains the data you need to scrape
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"
The data you need to scrape is the name of the programming language and average annual salary.
It is a good idea to open the url in your web broswer and study the contents of the web page before you start to scrape.

Import the required libraries

# Your code here
import requests
from bs4 import BeautifulSoup
import pandas as pd
Download the webpage at the url

#your code goes here
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"
data  = requests.get(url).text 
Create a soup object

#your code goes here
soup = BeautifulSoup(data,"html.parser")
table = soup.find('table')
Scrape the Language name and annual average salary.

#your code goes here
Language = []
salaries = []
​
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    if len(cols) >= 2:
        language = cols[1].text.strip()
        salary = cols[3].text.strip()
        Language.append(language)
        salaries.append(salary)
Save the scrapped data into a file named popular-languages.csv

# your code goes here
data = pd.DataFrame({'Programming Language': Language, 'Average Annual Salary': salaries})
data.to_csv('popular-languages.csv', index=False)
