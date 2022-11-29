from imports import *


f1 = MAIN_PATH + "categories.txt"
f2 = MAIN_PATH + "chains.txt"
f3 = MAIN_PATH + "products.txt"
categories, chains, products = [],[],[]

for i in [f1,f2,f3]:
    with open(i, "r") as f:
        d = f.read()
        d = d.replace('\n', ',').split(",")
        if i==f1:categories=d
        if i==f2:chains=d
        if i==f3:products=d



  
def scrape_links(url):
    p = []
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(url)
    driver.maximize_window()
    sleep(20)
    element = driver.find_element(By.TAG_NAME,"body")
    for i in range(200):
        element.send_keys(Keys.PAGE_DOWN)
        sleep(.5)
    page = driver.page_source
    soup = BeautifulSoup(''.join(page), 'html.parser')
    #html_document = requests.get(url).text 
    #soup = BeautifulSoup(html_document, 'html.parser')
    data = soup.findAll('div',attrs={'class':'ecosystem-item w-dyn-item'})
    for div in data:
        links = div.findAll('a')
        for a in links:
            url = ("https://chainlinkecosystem.com" + a['href'])
            if url not in p:    
                p.append(url)
    return p





def parse_data(partner):
    partner_struct = {
            "name":None,
            "status":None,
            "chains":[],
            "category":None,
            "integrations":[],
            "year":None }
    
    req = requests.get(partner)
    soup = BeautifulSoup(req.content, "html.parser")
    data = soup.findAll("div", {"class": "product-profile-text-image-wrapper"})
    partner_struct["name"] = soup.find("div", {"class": "product-profile-name"}).text.lower()
    partner_struct["status"] = soup.find("div", {"class": "live-text"}).text.lower()
    
    for elem in data:
        elem = elem.text.lower()
        if elem in categories:
            partner_struct["category"] = elem
        elif elem in chains:
            partner_struct["chains"].append(elem)
            partner_struct["chains"] = [*set(partner_struct["chains"])]
        elif elem in products:
            partner_struct["integrations"].append(elem)
            partner_struct["integrations"] = [*set(partner_struct["integrations"])]
        elif elem in ["2017","2018","2019","2020","2021","2022"]:
            partner_struct["year"] = elem        
    return  partner_struct




def scrape_ecosystem():
    system("clear")
    from progress.bar import Bar
    partnerships = scrape_links("https://chainlinkecosystem.com/ecosystem/")
    link_partnerships=[]
    bar = Bar('Processing', max=len(partnerships))
    for i in range(len(partnerships)):
        try:
            dd = parse_data(partnerships[i])
            #dd = json.dumps(dd, indent=4)
            link_partnerships.append(dd)
            bar.next()
        except:
            pass
    with open(MAIN_PATH + "link_partnerships.json", "w") as f:
        json.dump(link_partnerships, f, indent=4)
    bar.finish()
    print("Process complete.")