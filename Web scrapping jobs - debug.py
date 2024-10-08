import json
import requests
from openpyxl import Workbook # import Workbook class from module openpyxl
import re

api_url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"

########################################################################################

################################   Proper function #####################################

########################################################################################

def get_number_of_jobs_T(technology):
    number_of_jobs = 0
    response = requests.get(api_url)
    if response.ok:             
        data = response.json()
    for jobs in data:
        skills = jobs.get('Key Skills')
        if technology in skills:
            number_of_jobs = number_of_jobs + 1
            
    
    print(number_of_jobs)
    return technology,number_of_jobs

########################################################################################

#########   Second version of the function, which produced different results. ##########

########################################################################################

def get_number_of_jobs_S(technology):
     number_of_jobs = 0
     response = requests.get(api_url)
     if response.ok:             
         data = response.json()
     for jobs in data:
        
         skills = jobs.get('Key Skills')   
         #print("skills = ", skills)
         seperate_skills = re.split(r"[|,.-]", skills)       #splits the words, using the symbols between them. This way it doesn't split words like "digital margeting"
         #print("seperate skills = ",seperate_skills)            
         for skill in seperate_skills:                           #splits the list into seperate words
             cleaned_skill = skill.strip(",.|- ").lower()            #Strips the words from characters around them and make them lower case
             #print("cleaned skill = ", cleaned_skill)
             if technology.lower() == cleaned_skill:                 #makes the input lower case and compares it to each word from the skill list
                 #print(cleaned_skill, "=", technology)
                 number_of_jobs = number_of_jobs + 1
    
     return number_of_jobs




#######################################################################################################

#########   Debugging function to compare 2 functions results and print the ones not counted ##########

#######################################################################################################





def get_number_of_jobs_D(technology):
    number_of_jobs = 0
    number_of_jobs_s = 0
    response = requests.get(api_url)
    if response.ok:             
        data = response.json()

    for jobs in data:
        skills = jobs.get('Key Skills')
        seperate_skills = re.split(r"[|,.-]", skills) 
        if technology in skills:
            number_of_jobs += 1

        for skill in seperate_skills:
            cleaned_skill = skill.strip(",.|- ").lower()
            if technology.lower() != cleaned_skill and technology in skill:
                number_of_jobs_s += 1
                print(f"Original skill: {skill}")
                print(f"Cleaned skill: {cleaned_skill}")
                print(f"Technology: {technology.lower()}")

    return number_of_jobs, number_of_jobs_s

print(get_number_of_jobs_D('Python'))



#######################################################################################################

#################################################   Conclusion ########################################

#######################################################################################################


#The second version doesn't include possible double words when taking one word input, resulting in ignoring some of the words. 
#In this example the input is "Python", and some of the phrases in data contained "Python Developer" or "Ethernetpython", these cases were not counted.
#On top of that, the for loop for each word in the list "seperate_skills" took much more memory and time to compute the result.
