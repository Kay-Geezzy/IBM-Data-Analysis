import pandas as pd
The dataset is available on the IBM Cloud at the below url.
dataset_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"

Load the data available at dataset_url into a dataframe.
# your code goes here
df = pd.read_csv(dataset_url)
Explore the data set
It is a good idea to print the top 5 rows of the dataset to get a feel of how the dataset will look.

Display the top 5 rows and columns from your dataset.
# your code goes here
df.head()
Respondent	MainBranch	Hobbyist	OpenSourcer	OpenSource	Employment	Country	Student	EdLevel	UndergradMajor	...	WelcomeChange	SONewContent	Age	Gender	Trans	Sexuality	Ethnicity	Dependents	SurveyLength	SurveyEase
0	4	I am a developer by profession	No	Never	The quality of OSS and closed source software ...	Employed full-time	United States	No	Bachelor’s degree (BA, BS, B.Eng., etc.)	Computer science, computer engineering, or sof...	...	Just as welcome now as I felt last year	Tech articles written by other developers;Indu...	22.0	Man	No	Straight / Heterosexual	White or of European descent	No	Appropriate in length	Easy
1	9	I am a developer by profession	Yes	Once a month or more often	The quality of OSS and closed source software ...	Employed full-time	New Zealand	No	Some college/university study without earning ...	Computer science, computer engineering, or sof...	...	Just as welcome now as I felt last year	NaN	23.0	Man	No	Bisexual	White or of European descent	No	Appropriate in length	Neither easy nor difficult
2	13	I am a developer by profession	Yes	Less than once a month but more than once per ...	OSS is, on average, of HIGHER quality than pro...	Employed full-time	United States	No	Master’s degree (MA, MS, M.Eng., MBA, etc.)	Computer science, computer engineering, or sof...	...	Somewhat more welcome now than last year	Tech articles written by other developers;Cour...	28.0	Man	No	Straight / Heterosexual	White or of European descent	Yes	Appropriate in length	Easy
3	16	I am a developer by profession	Yes	Never	The quality of OSS and closed source software ...	Employed full-time	United Kingdom	No	Master’s degree (MA, MS, M.Eng., MBA, etc.)	NaN	...	Just as welcome now as I felt last year	Tech articles written by other developers;Indu...	26.0	Man	No	Straight / Heterosexual	White or of European descent	No	Appropriate in length	Neither easy nor difficult
4	17	I am a developer by profession	Yes	Less than once a month but more than once per ...	The quality of OSS and closed source software ...	Employed full-time	Australia	No	Bachelor’s degree (BA, BS, B.Eng., etc.)	Computer science, computer engineering, or sof...	...	Just as welcome now as I felt last year	Tech articles written by other developers;Indu...	29.0	Man	No	Straight / Heterosexual	Hispanic or Latino/Latina;Multiracial	No	Appropriate in length	Easy
5 rows × 85 columns

Find out the number of rows and columns
Start by exploring the numbers of rows and columns of data in the dataset.

Print the number of rows in the dataset.
# your code goes here
num_rows = df.shape[0]
print (num_rows)
11552

Print the number of columns in the dataset.
print (num_columns)
# your code goes here
num_columns = df.shape[1]
print (num_columns)
85
Identify the data types of each column
Explore the dataset and identify the data types of each column.

Print the datatype of all columns.

print
# your code goes here
print(df.dtypes.to_string())
Respondent                  int64
MainBranch                 object
Hobbyist                   object
OpenSourcer                object
OpenSource                 object
Employment                 object
Country                    object
Student                    object
EdLevel                    object
UndergradMajor             object
EduOther                   object
OrgSize                    object
DevType                    object
YearsCode                  object
Age1stCode                 object
YearsCodePro               object
CareerSat                  object
JobSat                     object
MgrIdiot                   object
MgrMoney                   object
MgrWant                    object
JobSeek                    object
LastHireDate               object
LastInt                    object
FizzBuzz                   object
JobFactors                 object
ResumeUpdate               object
CurrencySymbol             object
CurrencyDesc               object
CompTotal                 float64
CompFreq                   object
ConvertedComp             float64
WorkWeekHrs               float64
WorkPlan                   object
WorkChallenge              object
WorkRemote                 object
WorkLoc                    object
ImpSyn                     object
CodeRev                    object
CodeRevHrs                float64
UnitTests                  object
PurchaseHow                object
PurchaseWhat               object
LanguageWorkedWith         object
LanguageDesireNextYear     object
DatabaseWorkedWith         object
DatabaseDesireNextYear     object
PlatformWorkedWith         object
PlatformDesireNextYear     object
WebFrameWorkedWith         object
WebFrameDesireNextYear     object
MiscTechWorkedWith         object
MiscTechDesireNextYear     object
DevEnviron                 object
OpSys                      object
Containers                 object
BlockchainOrg              object
BlockchainIs               object
BetterLife                 object
ITperson                   object
OffOn                      object
SocialMedia                object
Extraversion               object
ScreenName                 object
SOVisit1st                 object
SOVisitFreq                object
SOVisitTo                  object
SOFindAnswer               object
SOTimeSaved                object
SOHowMuchTime              object
SOAccount                  object
SOPartFreq                 object
SOJobs                     object
EntTeams                   object
SOComm                     object
WelcomeChange              object
SONewContent               object
Age                       float64
Gender                     object
Trans                      object
Sexuality                  object
Ethnicity                  object
Dependents                 object
SurveyLength               object
SurveyEase                 object

Print the mean age of the survey participants.
# your code goes here
mean_age = df['Age'].mean()
print (mean_age)
30.77239449133718

The dataset is the result of a world wide survey. Print how many unique countries are there in the Country column.
# your code goes here
unique_countries = df['Country'].nunique()
print(unique_countries)
135
