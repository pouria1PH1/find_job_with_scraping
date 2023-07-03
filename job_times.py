
#description:find job with scraping  in job times
 

#import dependencies

from bs4 import BeautifulSoup
import requests
import time


favorite_skills=input("enter your favorite skill : ")
time_of_job=int(input("How long do you want the post to be uploaded, for example, 7 days ago or 10 days ago: "))


#create def for find job
def find_job():
    
    html_txt=requests.get("https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python%2C&txtLocation=&cboWorkExp1=-1").text
    soap=BeautifulSoup(html_txt,"lxml")
    div_jobs=soap.find_all("div",class_="srp-job-bx")


    for index,div in enumerate(div_jobs):
        day=div.find("span",class_="posting-time").text
        time_posted=day.replace("d","")
        time_posted=time_posted.replace("h","")
        time_int=int(time_posted.replace("d",""))
        skill=div.find("div",class_="srp-keyskills").text.replace(" ","")
        company_name=div.find("h4").text
        h3=div.h3   
        a=h3.a
        link_job=a["href"]
        if time_int<time_of_job and  favorite_skills  in skill:
            
            file_text=open(r"C:\Users\ols\Desktop\scriping.txt","a")
            
            file_text.write(f"""
            companyNmae: 
            {company_name.strip()}    

            skills:{skill.strip()}   
            time_posted:
            {time_posted+" days ago"}
            link_job:
            {link_job}
            \n
            """)
    print("done")

            


if __name__=="__main__":
    while True:
        find_job()
        print("please wait 10 min")
        time.sleep(10*60)
            










    
        