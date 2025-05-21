from bs4 import BeautifulSoup
import requests
import time

def scrape_jobs() :
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=").text
    # print(html_text) # returns a status 200 error- > to fix this add .text to the end of the requests.get().text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx")
    # go thru job in jobs and if the job was recently posted, scrape the company name and the skills required
    for job in jobs:
        published_date = job.find('span', class_ = "sim-posted").span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text
            skills = job.find('div', class_ = "srp-skills").text.replace(' ', '')
            print(f'''Company Name: {company_name.strip()} ''')
            print(f'''Required Skills: {skills.strip()} ''')
            print(f'''Posted: {published_date.strip()}''')
            
if __name__ == '__main__':
    #code for scraping every 10 minutes:
    #while True:
        #scrape_jobs()
        #time_wait = 10
        #print(f'Waiting {time_wait} seconds.')
        #time.sleep(time_wait * 60)
    scrape_jobs()