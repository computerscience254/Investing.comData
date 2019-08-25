import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import sys
sys.path.append("..")
from config import SQLALCHEMY_DATABASE_URI
from Utilis import seeder

def get_data(url, header, data):
    print("Getting data ......")
    response = requests.post(url, headers=header, data=data)
    if response.status_code != 200:
        raise Exception("Response code is {}".format(response.status_code))
    else:
        return response.content

def parse_data(content):
    print("Parsing data ......")
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', {"id":"curr_table"})    
    #Generate lists
    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    F=[]
    G=[]
    for row in table.findAll("tr"):
        cells = row.findAll('td')
        if len(cells) == 7: #Only extract table body not heading
            A.append(cells[0].find(text=True))
            B.append(cells[1].find(text=True))
            C.append(cells[2].find(text=True))
            D.append(cells[3].find(text=True))
            E.append(cells[4].find(text=True))
            F.append(cells[5].find(text=True))
            G.append(cells[6].find(text=True))
    return A, B, C, D, E, F, G

def generate_csv(A, B, C, D, E, F, G, header):
    titles = ['Date', 'Price', 'Open', 'High', 'Low', 'Vol']
    print("Generating csv ......")
    df = pd.DataFrame(G, columns=['Date'])
    df[str(titles[0])] = A
    df[str(titles[1])] = B
    df[str(titles[2])] = C
    df[str(titles[3])] = D
    df[str(titles[4])] = E
    df[str(titles[5])] = F
    title = str(header['Referer'][35:]) + '.csv'
    os.chdir("../")
    df.to_csv("Data/{}".format(title))
    print("Generated csv")

def push_to_db(A, B, C, D, E, F, G, header):
    print(str(SQLALCHEMY_DATABASE_URI))
    c , conn = seeder.create_connection(SQLALCHEMY_DATABASE_URI)
    title = str(header['Referer'][35:].replace("-historical-data", "").replace("-", ""))
    seeder.sql_insert_company(name=title)
    length = len(A)
    for i in range(0,length, 1):
        seeder.sql_insert_data(date=G[i], price=A[i], open_price=B[i], high=C[i], low=D[i], vol=E[i], name=title, c=c, connection=conn)