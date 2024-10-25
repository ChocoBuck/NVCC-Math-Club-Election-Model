from typing import Optional
from bs4 import BeautifulSoup
import requests

states: list[str] = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'delaware', 'District-of-Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode-Island', 'South-Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
HARRIS: int = 0
TRUMP: int = 1

def scrape_state_president_election_polls(state: str) -> Optional[list[dict[str, str]]]:
    URL: str = f'https://projects.fivethirtyeight.com/polls/president-general/2024/{state}/'
    page: 'Response' = requests.get(URL)
    if page.status_code != 200:
        return None
    soup: BeautifulSoup = BeautifulSoup(page.content, 'html.parser')
    polls_div = soup.find("div", class_="polls")
    rows = polls_div.find_all("tr", class_='visible-row')
    polls: list[dict[str, str]] = []
    for row in rows:
        percentage_elements = row.find_all("div", class_="heat-map")
        harris = percentage_elements[0].string
        trump = percentage_elements[-1].string
        polls.append({
            'Harris': harris,
            'Trump': trump
        })
    return polls

        


def scrape_list_of_states() -> list[dict[str, Optional[list[dict[str, str]]]]]:
    state_percentages: dict[str, Optional[list[dict[str, str]]]] = []
    for state in states:
        poll: Optional[list[dict[str, str]]]= scrape_state_president_election_polls(state.replace(' ', '-').lower())
        state_percentages.append({state: poll})
    return state_percentages


def calculate_percentage_differences(state_dictonary):
    for state in state_dictonary:
        state_name = state_dictonary['state']
        for polls in state_dictonary['polls']:
            for poll in polls:
                difference = poll['Harris'] - poll['Trump']
                print(difference)

def main() -> None:
    blah1 = scrape_list_of_states(states)
    print(blah1)
    calculate_percentage_differences(blah1)

if __name__ == '__main__':
    main()
