from bs4 import BeautifulSoup
import requests

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'delaware', 'District-of-Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode-Island', 'South-Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

def scrape_state_president_election_polls(state):
    print(state)
    URL: str = f'https://projects.fivethirtyeight.com/polls/president-general/2024/{state}/'
    page = requests.get(URL)
    if page.status_code==200:
        soup = BeautifulSoup(page.content, 'html.parser')
        polls_div = soup.find("div", class_="polls")
        rows = polls_div.find_all("tr", class_='visible-row')
        polls = {
            'Harris': [],
            'Trump': []
        }
        print(state)
        for row in rows:
            percentage_elements = row.find_all("div", class_="heat-map")
            harris = percentage_elements[0].string
            trump = percentage_elements[-1].string
            polls['Harris'].append(harris)
            polls['Trump'].append(trump)
        return polls
    else:
        return None

        


def main():
    state_dictionary = {}
    index = 0
    for state in states:
        index+=1
        poll = scrape_state_president_election_polls(state.replace(' ', '-').lower())
        state_dictionary[state]= poll
        print(f'{index}/{len(states)}')
    print(state_dictionary)


main()
