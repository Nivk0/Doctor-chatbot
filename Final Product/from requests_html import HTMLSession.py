from requests_html import HTMLSession

s=HTMLSession()
num = 0
num = input("What is my disease(1)\nWhat are my symptoms(2)\nwhat are my treatments(3)\nWhat would you like to learn about(type a number)?:")
Definition = ""
num = int(num)
if num == 1:

    query = input("what disease would you like to learn about: ")
    url =f'https://www.google.com/search?q=disease+{query}'
    r = s.get(url,headers = {'User-Aent' :'Mozilla/5.0 (1Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36'})
    Definition = r.html.find('div.m6vS6b',first=True).text

if num == 2:
    query = input("what is one of your symptoms: ")
    if __name__ == '__main__':
        for i in range(0, len(query), 1):
            if (query[i] == ' '):
                query = query.replace(query[i], '-')
     
    url =f'https://www.nhs.uk/conditions/{query}/'
    r = s.get(url,headers = {'User-Agent' :'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36'})
    Definition = r.html.find('div.nhsuk-table-container',first=True).text

if num == 3:
    query = input("what diseases' treatment would you like to learn about: ")
    url =f'https://www.google.com/search?q=disease+treatent+{query}'
    r = s.get(url,headers = {'User-Agent' :'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36'})
    
    Definition = r.html.find('div.X0D4ae',first=True).text


print(Definition)   




