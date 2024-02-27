# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:01:54 2023

@author: adity
"""

from PyPDF2 import PdfFileReader
#Importing required modules
from PyPDF2 import PdfReader

#Creating a pdf reader object
reader = PdfReader("D:/BTech/T.Y.Btech/Sem 2/IR 4.0/CPS Unit 1 Notes.pdf")

#Printing number of pages in pdf file
print(len(reader.pages))

#Getting a specific page from the pdf file
page = reader.pages[10]

#Extracting text from page
text = page.extract_text()
print(text)
################################################
import re
chat2='Hi: I have a problem with my order number 4400980834'
pattern = 'order [^\d{10}]'
matches = re.findall(pattern, chat2)
matches
############################################
# Regular expression pattern identificatoin

import re
text1="My mobliel number is 8767671386"
text2="My slternet moblile number is 9423386223"
text3="My international mobile number is (123)-436-72956"
pat1='\d{10}'
mob_numb=re.findall(pat1, text1)
print(mob_numb)
    
# Now to find international number we have to print character as it is so use 
# "\(" to print "("

pat2 = '\(\d{3}\)-\d{3}-\d{5}'
international_numb = re.findall(pat2, text3)
print(international_numb)

#####################################################################
import re
text1="My email id is aditya_gaikwad6735r@gmail.com"
text2="My alternate email id is gaikwadaditya6735@gmail.com"
text3="My official mail id is adityagaikwad_20mk20@sanivanicoe.org.in"

pat1 = r'[a-z]*.[a-z]*[0-9]*[a-z]*@[a-z]*\.com'
my_email=re.findall(pat1, text1)
print(my_email)
##################################################################

text1="My mail Id is Aditya.gaikwad@sanjivani.org.in"

pat1 = r'[A-Z][a-z]*.[a-z]*@[a-z]*\.org.in'
my_email=re.findall(pat1, text1)
print(my_email)
########################################################
import re
chat2="Hi: I have problem with my order number 496724"
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat2)
matches
############################################
import re
chat1="Hello, I am having problem with my order number # 496723224"
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat1)
matches
####################################################
chat3 = 'My order 2132153 is having an issue, I was charged 300$ when online '
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat3)
matches
#############################################################
def get_pattern_match(pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        return matches
    
get_pattern_match('order[^\d]*(\d*)',chat1)
################################################################
text = '''
Born	Elon Reeve Musk

June 28, 1971 (age 51)
Pretoria, South Africa
Citizenship	
South Africa (1971–present)
Canada (1989–present)
United States (2002–present)
Alma mater	
Queen's University
Wharton School of the University of Pennsylvania (BS)
Occupation	
Entrepreneurengineer
Years active	1995–present
Net worth	US$ 209 billion (January 2021)[1]
Height	188 cm (6 ft 2 in)

Title	

Founder, CEO, Lead Designer of SpaceX
CEO and Product Architect of Tesla, Inc.
CEO of Twitter
Co-founder, CEO of Neuralink
Founder of The Boring Company
Co-founder of Zip2
Founder of X.com (now PayPal)
Co-founder of OpenAI
Chairman of SolarCity
Political party	Independent
Spouse(s)	
Justine Wilson
(m. 2000; div. 2008)
Talulah Riley
(m. 2010; div. 2012)
(m. 2013; div. 2016)
Partner(s)	Grimes (2018–2021)
Children	7 (1 deceased)
Parent(s)	
Errol Musk (father)
Maye Musk (mother)
Relatives	
Kimbal Musk (brother)
Tosca Musk (sister)
Lyndon Rive (cousin)
Awards	Fellow of the Royal Society (2018)
'''
get_pattern_match(r'age (\d+)', text)
get_pattern_match(r'Born(.*)', text)
match = get_pattern_match(r'Born(.*)', text)
match[0].strip()

match1 = get_pattern_match(r'Born.*\n(.*)\(age', text)
match1 
get_pattern_match()
####################################################################3
text = '''
Born	Elon Reeve Musk

June 28, 1971 (age 51)
Pretoria, South Africa
Citizenship	
South Africa (1971–present)
Canada (1989–present)
United States (2002–present)
Alma mater	
Queen's University
Wharton School of the University of Pennsylvania (BS)
Occupation	
Entrepreneurengineer
Years active	1995–present
Net worth	US$ 209 billion (January 2021)[1]
Height	188 cm (6 ft 2 in)

Title	

Founder, CEO, Lead Designer of SpaceX
CEO and Product Architect of Tesla, Inc.
CEO of Twitter
Co-founder, CEO of Neuralink
Founder of The Boring Company
Co-founder of Zip2
Founder of X.com (now PayPal)
Co-founder of OpenAI
Chairman of SolarCity
Political party	Independent
Spouse(s)	
Justine Wilson
(m. 2000; div. 2008)
Talulah Riley
(m. 2010; div. 2012)
(m. 2013; div. 2016)
Partner(s)	Grimes (2018–2021)
Children	7 (1 deceased)
Parent(s)	
Errol Musk (father)
Maye Musk (mother)
Relatives	
Kimbal Musk (brother)
Tosca Musk (sister)
Lyndon Rive (cousin)
Awards	Fellow of the Royal Society (2018)
'''


def extract_personal_information(text):
    def get_pattern_match(pattern, text):
        age=get_pattern_match('age (\d+)', text)
        full_name = get_pattern_match('Born(.*)\n', text)
        birth_date = get_pattern_match('Born.*\n(.*)\(age', text)
        birth_place = get_pattern_match('\(age.*\n(.*)', text)
        return {
            'age': age,
            'name': full_name,
            'birth_date': birth_date,
            'birth_place': birth_place
            }
extract_personal_information(text)
##################################################################3
def extract_personal_information(text):
    age = get_pattern_match('age(\d+)',text)
    full_name = get_pattern_match('Born(.*)\n',text)
    birth_date = get_pattern_match('Born.*\n(.*)\(age',text)
    birth_place = get_pattern_match('\(age.*\n(.*)',text)
    return{
        'age':age,
        'name': full_name,
        'birth_date':birth_date,
        'birth_place':birth_place
        }
extract_personal_information(text)
################################################################3#
text = '''
Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 66)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parent	
Dhirubhai Ambani (father)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)
'''

get_pattern_match(r'age (\d+)',text)
get_pattern_match
get_pattern_match(r'Born(.*)',text)
match[0].strip()
get_pattern_match(r'Born.*\n(.*)\(age',text)
###################################################################
#1.
import re
text='''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla 
'''

pattern = 'https://twitter\.com/([a-zA-Z0-9_]+)'
re.findall(pattern, text)

#####################################################################
#2. Extract Concentration Risk Types. It will be a text that appears after
text ='''
Concentration of Risk: Credit Risk 
Financial instruments that potentially subject us to a concentration of credit risk 
consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, 
and interest rate swaps. Our cash balances are primarily invested in 
money market funds or on deposit at high credit quality financial institutions 
in the U.S. These deposits are typically in excess of insured limits. As of September 30, 
2021 and December 31,
'''
pattern = 'Concentration of Risk: ([^\n]*)'
re.findall(pattern, text)
########################################################################
text2 = '''

Tesla's gross cost of operating lease vehicles in FY2021 Q1. was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion..

'''

pattern = 'FY(\d{4} (?:Q[1-4][S[1-2]))' #match this (?:for this or for that)
matches = re.findall(pattern, text2)
matches
################################
text3='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. 
Tesla's revenue is 40 billion Tesla's CFO number (999)-333-7777
'''
pattern = '\(\d{3}\)-\d{3}-\d{4}'
matches = re.findall(pattern, text3)
matches
##############################################################
text4 = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''

pattern = 'Note \d - ([^\n]*)'
matches = re.findall(pattern, text4)
matches
######################################################################################

text5 = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
pattern = 'FY\d{4} Q[1-4]'

matches = re.findall(pattern, text5)
matches
######################################################################
text5 = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. Fy2020 Q4 it was $3 billion. 
'''

pattern =  'FY\d{4} Q[1-4]'
 
matches = re.findall(pattern, text5, flags=re.IGNORECASE)
matches
##########################################################################
#Extract only financial number
import re
text5 = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
pattern = '\$([0-9\.]+)'
#if we will put ([0-9\.]+), it will show all the digits, but if will put \$([0-9\.]+)
#then only dollor related figures will be highlighted and once we will put 
#will be displayed

matches = re.findall(pattern, text5)
matches
###################################################################








