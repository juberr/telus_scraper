from bs4 import BeautifulSoup as soup
import requests as req

def get_telus_pharm_avail(pharma_id):
    
    # get the html and parse it using beautiful soup
    url = f'https://pharmaconnect.ca/Appointment/{pharma_id}/Slots?serviceType=ImmunizationCovid'
    
    html = req.get(url)
    
    html_soup = soup(html.text, 'lxml')
    
    # find the dates currently on the page, and add them to a list
    html_dates = html_soup.findAll('div', class_='b-days-selection appointment-availability__days-item')

    if not html_dates:
        return

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

        resp[key]['numberAvailable'] = len(slots_data[key]) 
        resp[key]['numberTotal'] = len(slots_data[key]) 
        resp[key]['date'] = key
        resp[key]['vaccine'] = 0
        resp[key]['inputType'] = 1
        resp[key]['tags'] = 'Telus'
        resp[key]['location'] = 0
    
    return resp

def get_all_telus_avail():

    out = {}

    UUIDS = ['a6fef7d9-0ecc-44d1-85af-ef6c8d2b6501',
'31327823-3ce8-445a-9db6-b0f00778e34d',
'9ca91d85-3bc2-4442-a67a-a7bf0f9dc45f',
'fbaa7876-0a33-4a96-90d3-6d4c33a0d2e7',
'fa3d20f4-ba61-47aa-b2e4-3b94d8e2b87c',
'1091db37-0eed-4421-b5bd-816281cba33e',
'0df4ec73-d93c-48d7-b2ef-7f3cb7de4254',
'3d67d43f-ab3d-4323-8ae8-9caea14dab0f',
'64f4a10c-3274-4b30-ad50-7acdb5c292a3',
'a7fefabb-b892-4fdb-8f92-725224a6e9fd',
'98ce6782-aa56-4b11-b677-61f73c956e42',
'fcdc7062-8782-46a3-bf10-5d3a750ae538',
'8f9b1c44-e98b-4d4c-8d4c-09226873e9e3',
'4e7769f9-6164-4825-afc9-187355752979',
'2598bf15-5615-4e07-bf91-b822cf318ce1',
'004d1fbb-053f-46ec-9d0b-a69974cfe07b',
'6948feca-0618-4adb-81af-78fc411bb165',
'358813f0-b10d-4fe0-9d3b-8d550957587a',
'4c46a1d6-8102-4368-8e0b-e95e92a22e30',
'd1f8cb8d-1472-45cd-8c83-1037e2e01897',
'8d11d6df-c116-4732-b1f4-aebd614b0129',
'4adf7a17-c43c-42df-bc0b-6c786580830d',
'd7df060c-2004-4c38-b8ea-62cdab8838a0',
'ffb8a810-48fe-4170-8ccc-2dcc34db034d',
'6b1c7212-b0c4-4032-9230-419fc8c59787',
'3e934dff-f4d6-40d9-9a98-3bbaddad51cf',
'41199cd6-dbf3-42ad-b239-e83a36c17d21',
'db4c8f2b-9c1d-4282-9f16-a6f5fbdab9ad',
'7bfc94a7-7f07-4f6f-8e30-acf4be761754',
'64e72053-a93a-4de2-8fc8-6d3ccc2e467b',
'14640fcc-9f5d-41b5-a941-cde0651037be',
'2be2617d-93f9-4c75-a279-46d6385f6474',
'6415702c-cca0-45d8-8d16-525ffe73d0bf',
'69ab4120-36e7-413c-8668-705cf8baabdc',
'2ed835c0-d0bb-4796-a58e-485daaf28615',
'9a851f98-57de-4447-a0aa-3f1d808fbbd4',
'46a40558-64a8-4172-820d-4d82e0926b23',
'58a91a7f-b3b6-4d5d-84c8-8e937c261588',
'b6fa79dd-d757-46b1-bb85-7e9e820dcf19',
'225e3094-978a-45ce-9312-44ef4946c9ea',
'38a65b84-aabc-4b61-9eb9-480eabacfca6',
'7f258269-ec4e-45da-8157-c50cf68c5059',
'9901804e-36f8-41b7-833d-026197dbeea5',
'cff531af-e936-4d69-b64a-3b1cb5e87d9f',
'42337e27-6bf7-4b53-b028-a7baeb742bb1',
'56881eb2-43af-426c-b3c4-dbb1a6e22e21',
'64228a58-93d1-444e-ac83-7de284ce19b7',
'cd59a54b-7c5c-4351-a862-6282ea47dc50',
'cbfc3baf-423c-4308-9954-b69d361d7393',
'3aec4289-a832-49e8-bdc8-458d966891f3',
'bf2f314a-e64b-4dae-9fcf-773cc1c88285',
'270774d4-b7d3-4aa8-8cb9-b3488e53a273',
'c39c23ad-75f1-46e2-bf88-e79e8f1be9b9',
'cf93f697-a306-4112-b899-c820cb4036ec',
'0152d717-e9e9-484b-b815-a1aba96ccdbf',
'eb36ed78-df68-46b7-8921-eb283c2a8536',
'92358f79-fdb7-4600-8475-67979a7d3723',
'ff38dc2c-4b68-479a-a6a5-5c0f6bd992c5',
'5f676232-df5e-4a1c-b19e-532fbadedacf',
'2c0d7e45-14af-4387-87f5-4c12530cef7b',
'2d397a09-4ecb-4711-a645-4b61b3ec75a6',
'debb3ac2-0559-4aad-9f4d-ab14a74f8be9',
'b29f9f02-8388-4e8f-ba53-282c3ef88a6c',
'3f832d1f-cde9-4c12-af36-a22b66a6e9d5',
'f2427fbc-d73a-4841-be32-faa795e1aa06',
'f8f9edfe-dc37-4b94-899b-b6268df1c767',
'3de6c343-a6bc-463f-af8b-58fea6723877',
'32f0f6b8-374b-41bf-9872-dd68af726293',
'd4e1e654-49db-4c5d-a59b-25e95eb798e7',
'99f2d7fd-ac2f-415f-a9b8-edadcbd1901a',
'c8028fe4-0b02-4ff8-b081-e56e8d021ae8',
'6d9d37c5-21f3-45cb-b206-976cb3ae4abd',
'0f920718-d583-4578-b2e8-ad8b431765bd',
'd62bd819-50f1-4664-be8a-1eed8499dbd3',
'dca573a2-1cfc-44a5-80fd-295636014a37',
'4e9b3521-c471-4c67-a67f-a66894704fdf',
'64c9744d-92da-468d-ab0d-0016dec21e5d',
'699ba399-06b2-45cc-ab93-c2478bc7841f',
'8499f47f-07d2-4b35-bf1e-356c0e216612',
'bc4c9f09-bc69-4814-8cb9-32cc01c917c9',
'5c00f1db-aedc-4886-be42-9f2e8ad8fea9',
'bf3d0153-02ec-43b2-9065-fdfbc4b5174b',
'c51be7c4-df90-4429-92f1-fc328ab5a5ed',
'de3fff78-f813-4148-8aa6-0c6be19a48a0',
'b81dd95e-4f3c-43ae-af4c-9dfc8ac08bbc',
'0c8b1de7-d781-4b1d-93e4-b3c91e4b9847',
'd2d56a98-ffd0-4979-a287-6e36f61ea783',
'dd255e03-d65c-4f65-a210-a3ad3869816f',
'5eaf9bc2-64d2-45b3-bd3d-9cec7f11a835',
'7f4214d6-f9bf-4331-a232-b243d74dc23f',
'f260ce73-4e9b-4892-a42d-19947a64a187',
'2102e99c-4750-478e-8ed4-c7f2b8edbf44',
'dbaaec8c-a8e6-4646-93f3-084ac42934d4',
'62bcece5-761b-4d8f-81b5-05a0a68dae52',
'b5af536c-8619-407e-a61e-795b9b01084f',
'a7cd340d-418d-4766-a8d3-ede7cfc8b2b2',
'40726488-7928-4ddb-8100-474ed0210ffe',
'92fa9c91-5037-4242-8599-82ce1a40f1f9',
'b4d60d88-6759-4542-908c-e4f990553145',
'5449a681-427c-4a18-a8ab-a1d2ae74c798',
'6bed1d8f-fa49-4f3a-9144-6726ba8ca613',
'3cc3aa8d-042d-464d-8f75-b58372af21c6',
'de4e88c6-2f2d-46f5-979a-157886be324c',
'f16ab264-8d93-427c-8b1e-28fb08d1e04f',
'3ab2e46d-9350-4d89-a3d3-03c65a86207f',
'2c45638b-6ed8-4e59-b172-ab389b774979',
'f91016d5-b051-4d6a-b877-19e167dea65b',
'11f94c85-09af-41a9-879e-d838c19ccfe5',
'e2b79096-e29d-45b3-b276-4db8629384d4',
'63226e1c-1839-4a4e-81b8-9aee9b236a0e',
'4c58c93a-e163-40f7-858d-8f6a0c04b3a2',
'9c67680e-9890-4c83-a3a4-f0ab99e32662',
'3dab39b7-d85d-4437-9551-4e83b42cfdf2',
'8307044a-15aa-48e0-9930-475097ae1998',
'7aef6ccb-2775-4f86-aa53-d2a5f49ceccc',
'bb32ff86-fc7b-416f-a9bb-2b33ff1f26d9',
'1ddf199a-9bfe-4ed6-8db6-364cadd3968d',
'5f4c48bd-fbee-4fa6-9c7c-a3ca4b1443ec',
'5e79c04e-4dcd-4239-8fab-bf8673a6973f',
'52d3b831-3825-45dc-b873-586e6b360ccf',
'7ae54f81-fa01-4f2a-9e1d-df3e7cc1d60f',
'9baac9e6-2c45-4a03-b189-079355e62618',
'e893f152-faa8-4f4b-b441-a06b743563dc',
'66f6f054-8837-4d56-b9fb-5c54ae90acfb',
'03b71cc6-5026-4e1f-a1ba-1b0d41e49d10',
'c5224e08-5799-4428-8f69-f9d7536146ab',
'a5710951-af6f-4910-ae11-dc4cea8085e2']

    for i in UUIDS:
        out[i] = get_telus_pharm_avail(i)

    return out

import json 

with open('output.json', 'w') as f:
    json.dump(get_all_telus_avail(), f, indent=4)



