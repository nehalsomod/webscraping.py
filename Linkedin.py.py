from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome("Enter-Location-Of-Your-Web-Driver")
driver.get("http://linkedin.com/uas/login")
time.sleep(5)
username = driver.find_element_by_id("username")
username.send_keys("User_email")
pword = driver.find_element_by_id("password")
pword.send_keys("user_pass")
driver.find_element_by_xpath("//button[@type='submit']").click()
profile_url = "http://www.linkedin.com/company/unacademy/"

driver.get(profile_url)

start = time.time()

initial_scroll == 0
final_scroll ==1000

while True:
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll}")
    initialScroll = finalScroll
    finalScroll +=1000

    time.sleep(3)
    end = time.sleep()
    if round(end - start) > 20:
        break
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')

    intro = soup.find('div', {'class': 'pv-text-details__left-panel'})

    print(intro)

    name_loc = intro.find("h1")
    name = name_loc.get_text().strip()
    works_at_loc = intro.find("div", {'class': 'text-body-medium'})
    works_at = works_at_loc.get_text().strip()

    location_loc = intro.find_all("span",{'class': 'text-body-small'})
    location = location_loc[1].get_text().strip()

    print("Name -->",name,"\nWorks At -->", works_at,"\nLocation -->", location)
    experience = soup.find("section", {"id": "experience-selection"}).find('ul')
    print(experience)

    li_tags = experience.find('div')
    a_tags = li_tags.find("a")
    job_title = a_tags.find("h3").get_text().strip()

    print(job_title)

    company_name = a_tags.find_all("p")[1].get_text().strip()
    print(company_name)

    joining_date = a_tags.find_all("h4")[0].find_all("span")[1].get_text().strip()

    employement_duration = a_tags.find_all("h4")[1].find_all("span")[1].get_text().strip()

    print(joining_date + "," + employment_duration)
    jobs = driver.find_element_by_xpath("//a[@data-link-to='jobs']/span")

    jobs.click()

    job_src = driver.page_source

    soup = BeautifulSoup(job_src,'lxml')

    jobs_html = soup.find_all('a',{'class': 'job-card-list__title'})

    job_title = []

    for title in jobs_html:
        job_title.append(title.text.strip())

        print(job_titles)

    company_name_html = soup.find_all('div', {'class': 'job-card-container__company-name'})
    company_names = []

    for name in company_name_html:
        company_names.append(name.text.strip())

        print(company_names)

        location_list = soup.find_all('ul',{'class': 'job-card-container__metdata-wrapper'})

        location_list = []
        
        for loc in location_html:
            res = re.sub('\n\n +','',loc.text.strip())

            location_listappend(res)

        print(loaction_list)
