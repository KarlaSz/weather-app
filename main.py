from requests import get
from json import loads #change dict to string, read file load + s -string
from terminaltables import AsciiTable

CITIES = ['Szczecin', 'Wrocław']

def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    # print(response.text) #read oryginal text from file
    # print(loads(response.text)) #read file as string
    rows = [
        ['Miasto', 'Godzina pomiaru', 'Temperatura']
    ]

    for row in loads(response.text):
        if row['stacja'] in CITIES:
            rows.append([
                row['stacja'],
                row['godzina_pomiaru'],
                row['temperatura']
            ])

    table = AsciiTable(rows)
    print(table.table)

if __name__ == '__main__':
    print('Aplikacja pogodowa 2025')
    main()