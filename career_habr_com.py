import requests
import lxml.html

base_url = "https://career.habr.com/vacancies?type=all"

with open("user_agent.txt") as file:
    user_agent = file.read()

headers = {
    "User-Agent": user_agent,
}

response = requests.get(base_url, headers=headers)

if response.status_code != 200:
    print("Ошибка запроса")
    exit(1)

tree = lxml.html.fromstring(response.text)
for vacancy_card in tree.xpath("""//div[@class="vacancy-card__inner"]"""):
    vacancy_title = vacancy_card.xpath(""".//a[@class="vacancy-card__title-link"]/text()""")
    vacancy_title = vacancy_title[0].strip()

    vacancy_company = vacancy_card.xpath(""".//a[@class="link-comp link-comp--appearance-dark"]/text()""")
    vacancy_company = vacancy_company[0].strip()
    print(vacancy_company, "-", vacancy_title)
