import sys
from selenium import webdriver

class CoronaStats():
    def __init__(self, country, website):
        self.driver = webdriver.Chrome('ChromeDriver\chromedriver.exe')
        self.country = country
        self.website = website


    # Reading data where it found the country name
    def scrapping_data(self, table):
        # Get number of rows
        country_element = table.find_element_by_xpath("//td[contains(., '{}')]".format(self.country))
        row = country_element.find_element_by_xpath("./..")
        data = row.text.split(" ")
        return data

    def get_data(self):
        try:
            self.driver.get(self.website)
            table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]')
            data = self.scrapping_data(table)
            if len(data) == 10:
                #For the Countries whose New Death and Serious Critical data doesn't exist.
                total_cases = data[1]
                new_cases = data[2]
                total_deaths = data[3]
                total_recovered = data[4]
                active_cases = data[5]
                serious_critical = 0
            else:
                total_cases = data[1]
                new_cases = data[2]
                total_deaths = data[3]
                total_recovered = data[5]
                active_cases = data[6]
                serious_critical = data[7]

            total_deaths_cal = total_deaths.split(',')
            total_deaths_cal = "".join(total_deaths_cal)
            total_recovered_cal = total_recovered.split(',')
            total_recovered_cal = "".join(total_recovered_cal)
            closed_cases = int(total_deaths_cal) + int(total_recovered_cal)

            self.driver.close()
            return total_cases, new_cases, total_deaths, active_cases, total_recovered, serious_critical, closed_cases
        except Exception as e:
            print(e)
            self.driver.quit()
            sys.exit()
