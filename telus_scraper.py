from bs4 import BeautifulSoup as soup
import requests as req

def get_telus_pharm_avail(pharma_id):
    
    # get the html and parse it using beautiful soup
    url = f'https://pharmaconnect.ca/Appointment/{pharma_id}/Slots?serviceType=ImmunizationCovid'
    
    html = req.get(url)
    
    html_soup = soup(html.text, 'html.parser')
    
    # find the dates currently on the page, and add them to a list
    html_dates = html_soup.findAll('div', class_='b-days-selection appointment-availability__days-item')
    dates = [i.get('data-selected-id') for i in html_dates]
    
    slots_data = {}
    # get all the slot availabilites for both days and add to a dictionary
    for date in dates:
        
        slots_data[date] = []
        
        date_html = html_soup.find(id=date)
        
        date_slots = date_html.findAll('div', class_="appointment-availability__period-text")
        
        for i in date_slots:
            slots_data[date].append(i.get_text())
    
    resp = {}
    # for each day, create a response object friendly to vacc hunters API (wip)
    for key in slots_data.keys():
        resp[key] = {}

        resp[key]['numberAvailable'] = len(slots_data[key]) + 1
        resp[key]['numberTotal'] = len(slots_data[key]) + 1
        resp[key]['date'] = key
        resp[key]['vaccine'] = 0
        resp[key]['inputType'] = 1
        resp[key]['tags'] = 'Telus'
        resp[key]['location'] = 0
    
    return resp