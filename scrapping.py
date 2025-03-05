from requests import get
from bs4 import BeautifulSoup


def fetchWebsite(url):
    response = get(url)
    status_code = response.status_code
    if status_code == 200:
        return BeautifulSoup(response.content, "html.parser")
    else:
        return ("Error: ", status_code)


class InfoDolarScrapping:
    def __init__(self):
        self.base_url = "https://www.infodolar.com.pe/tipo-de-cambio-sunat.aspx"
        self.html_body = None

    def getHtmlBody(self):
        try:
            self.html_body = fetchWebsite(self.base_url)
            return self.html_body
        except Exception as e:
            print(f"getHTMKLBody -> {e}")

    def getTableExchange(self):
        if self.html_body:
            self.tables = self.html_body.find_all(
                "td",
                {"class": "colCompraVenta"},
            )

    def getPriceTable(self):
        if len(self.tables):
            for table in self.tables:
                print(table.get("data-order"))


scrapping = InfoDolarScrapping()
scrapping.getHtmlBody()
scrapping.getTableExchange()
scrapping.getPriceTable()
