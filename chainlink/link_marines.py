from imports import *
import pprint, re
system('clear')


# Scrape finds each element by class and return the soup object 
def scrape_links(url, div_class):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    data = soup.findAll('div',attrs={'class':div_class})
    return data


# Creates a object for month for $LINK holders 
# Each month object has the following fields: month, year, rank, brothers
# Adds the object month_stat to a list all_months, and appends to json file link_marine_stats.json
def link_marines_data():
    month_stat = {
        "month":None,
        "year":None,
        "rank":None,
        "brothers":None,
    }
    
    month = scrape_links("https://www.chainlinkecosystem.com/ranks", 'ranks-faq-main shadow') 
    all_months = []
    for i in range(len(month)):
        header = month[i].find('div',attrs={'class':'ranks-top'}) # date info
        date = header.findAll('div',attrs={'class':'strong'})
        ranks = month[i].findAll('div',attrs={'class':'rank-data-grid'}) #rank, brothers, link held
        date = month[i].find('div',attrs={'class':'rank-text'}).text.split()
        
        date = date[-2:]
        month_stat["month"] = date[0]
        month_stat["year"] = date[1]
        for r in ranks:
            rank = r.find('div', attrs={'class':'rank-gray-wrap'})
            brothers = r.find('div', attrs={'class':'ranks-brothers-text'})
            try:
                month_stat["rank"] = rank.text
                month_stat["brothers"] = brothers.text
                all_months.append(month_stat.copy())
            except:
                pass
    for i in (all_months):
        print(i)
    with open (MAIN_PATH + "link_marine_stats.json", "w") as f:
        json.dump(all_months, f, indent=4)






 