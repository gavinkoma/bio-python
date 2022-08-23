#start by importing the modules broooo
import requests, webbrowser, os, sys, urllib3, json
import pandas as pd
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plot
# need this for suppressing warnings of insecure requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# heylab ="https://bio.cst.temple.edu/~tuf29449/"
# a = requests.get(heylab, verify=False)
# s = bs(a.text,'html.parser').prettify()
# print(s)

#this will set our working directory to be able to find the necessary documents
currentpath = os.getcwd()
newpath = os.chdir('/Users/gavinkoma/Documents/bio-python/week12')
currentpath2 = os.getcwd()

def main():
    france, russia, mexico = covidgetdata()
    francevacc,russiavacc,mexicovacc = popvaccdata()
    infectgraph(france, russia, mexico)
    francecompletevacc,francepop,russiacompletevacc,russiapop,mexicocompletevacc,mexicopop = popvsvaccgraph(francevacc,russiavacc,mexicovacc)
    plotpie(francecompletevacc,francepop,russiacompletevacc,russiapop,mexicocompletevacc,mexicopop)

def covidgetdata():
    franceresponse = requests.get('https://covid-api.mmediagroup.fr/v1/cases?country=France')
    russiaresponse = requests.get('https://covid-api.mmediagroup.fr/v1/cases?country=Russia')
    mexicoresponse = requests.get('https://covid-api.mmediagroup.fr/v1/cases?country=Mexico')
    #print(response)
    dictionaryfrance = json.dumps(franceresponse.json(), sort_keys= True, indent = 4)
    dictionaryrussia = json.dumps(russiaresponse.json(), sort_keys= True, indent = 4)
    dictionarymexico = json.dumps(mexicoresponse.json(), sort_keys= True, indent = 4)
    #print(dictionary)
    responsefrance_json = franceresponse.json()
    responserussia_json = russiaresponse.json()
    responsemexico_json = mexicoresponse.json()

    #okay pass to data frames

    francedata = pd.DataFrame(responsefrance_json)
    russiadata = pd.DataFrame(responserussia_json)
    mexicodata = pd.DataFrame(responsemexico_json)

    #print(francedata)
    #print(len(russiadata))
    france = (francedata.iloc[0][0],francedata.iloc[2][0])
    russia = (russiadata.iloc[0][0],russiadata.iloc[2][0])
    mexico = (mexicodata.iloc[0][0],mexicodata.iloc[2][0])

    #print(france)

#    df = pd.DataFrame(response_json, columns = response_json)


    return(france, russia, mexico)

def infectgraph(france, russia, mexico):
    #print(france[0],france[1])
    cases = [int(france[0]),int(russia[0]),int(mexico[0])]
    #print(len(cases))
    #print(cases)
    death = [int(france[1]),int(russia[1]),int(mexico[1])]
    #print(len(vacc))
    #print(vacc)

    index = ['France','Russia','Mexico']
    data = {'Covid Cases':cases, 'Deaths':death}
    dataFrame = pd.DataFrame(data=data,index=index)
    xvalues = range(len(data))
    #print(xvalues)

    #draw
    dataFrame.plot.bar(stacked=False,rot=15,title='Current Confirmed COVID Cases and Confirmed Deaths')
    plot.ylabel('Total Persons')
    plot.show(block=False)

    return

def popvaccdata():
    francevaccresponse = requests.get('https://covid-api.mmediagroup.fr/v1/vaccines?country=France')
    russiavaccresponse = requests.get('https://covid-api.mmediagroup.fr/v1/vaccines?country=Russia')
    mexicovaccresponse = requests.get('https://covid-api.mmediagroup.fr/v1/vaccines?country=Mexico')

    dictionaryvaccfrance = json.dumps(francevaccresponse.json(), sort_keys= True, indent = 4)
    dictionaryvaccrussia = json.dumps(russiavaccresponse.json(), sort_keys= True, indent = 4)
    dictionaryvaccmexico = json.dumps(mexicovaccresponse.json(), sort_keys= True, indent = 4)
    #print(dictionary)
    responsevaccfrance_json = francevaccresponse.json()
    responsevaccrussia_json = russiavaccresponse.json()
    responsevaccmexico_json = mexicovaccresponse.json()

    #okay pass to data frames

    francevacc = pd.DataFrame(responsevaccfrance_json)
    russiavacc = pd.DataFrame(responsevaccrussia_json)
    mexicovacc = pd.DataFrame(responsevaccmexico_json)

    #print(francevacc)
    #print(francevacc)

    return(francevacc,russiavacc,mexicovacc)

def popvsvaccgraph(francevacc,russiavacc,mexicovacc):


    #franceadmin = francevacc.iloc[0][0]
    #print(franceadmin)
    francecompletevacc = francevacc.iloc[1][0]
    #print(francecompletevacc)
    #francepartial = francevacc.iloc[2][0]
    #print(francepartial)
    francepop = francevacc.iloc[4][0]
    #print(francevacc)
    russiacompletevacc = russiavacc.iloc[1][0]
    russiapop = russiavacc.iloc[4][0]

    #print(mexicovacc)
    mexicocompletevacc = mexicovacc.iloc[10][0]
    #print(mexicocompletevacc)
    mexicopop = mexicovacc.iloc[11][0]
    #print(mexicopop)

    return(francecompletevacc,francepop,russiacompletevacc,russiapop,mexicocompletevacc,mexicopop)

def plotpie(francecompletevacc,francepop,russiacompletevacc,russiapop,mexicocompletevacc,mexicopop):

    #okay so we cant just use the regular numbers because that wouldnt make sense
    #so we need to take our total population
    #and find the % of people who are partially/completely vaccinated against that population

    #okay, ive also realized that the administered section of this api is doses given total
    #not total vaccination status. this means that administered must be divided by two to account
    #for the vaccination success. this is important because without doing this, the data
    #does not match published materials at all. however, whenever divided it by two, it very closely
    #matches the data presented by the UN/WHO organizations. what we will use is the second
    #index of people_vaccinated because that matches notable better than the adminstered value

    #piedf = pd.DatFrame({''})

    #indexfrance = ['France Vaccinated Population','France Unaccinated Population']
    francevacper = (francecompletevacc/francepop)
    franceunvacper = (1-francevacper)
    francevaccdata = [francevacper,franceunvacper]

    russiavacper = (russiacompletevacc/russiapop)
    russiaunvacper = (1-russiavacper)
    russiavaccdata = [russiavacper,russiaunvacper]

    #the mexico api data was aligned differently than the other two countries
    #so i had to go back and reindex it properly to get the right data from it
    mexicovacper = (mexicocompletevacc/mexicopop)
    # print(mexicocompletevacc)
    # print(mexicopop)
    # print(mexicovacper)
    mexicounvacper = (1-mexicovacper)

    mexicovaccdata = [mexicovacper,mexicounvacper]
    labels = [" "," "," "," "," "," "]

    francedict = pd.Series({'France Vaccinated Population':francevacper,'France Unvaccinated Population':franceunvacper})
    russiadict = pd.Series({'Russia Vaccinated Population':russiavacper,'Russia Unvaccinated Population':russiaunvacper})
    mexicodict = pd.Series({'Mexico Vaccinated Population':mexicovacper,'Mexico Unvaccinated Population':mexicounvacper})

    df = pd.concat([francedict, russiadict, mexicodict], axis = 1, keys = [' ', ' ', ' '])
    axes = df.plot(kind='pie',subplots=True,startangle=90,autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '',legend=True)
    for ax in axes:
        ax.set_aspect('equal')
        ax.yaxis.set_label_coords(-0.15,0.5)

    plot.subplots_adjust(wspace=0.1, hspace=2)
    plot.show(block=False)

    #plot.pie(alldata,labels=labels, autopct='%1.1f%%')
    #plot.title('France Vaccinated Persons')
    #plot.show()





    return()







main()
