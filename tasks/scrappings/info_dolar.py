from session.helpers.scrapper import fetchWebsite


class InfoDolarScrapping:
    def __init__(self):
        self.base_url = "https://www.infodolar.com.pe/tipo-de-cambio-sunat.aspx"
        self.html_body = None
        self.tables = []
        self.exchanges = {}

        self.start()

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
            keys = {"compra", "venta"}
            values = {table.get("data-order") for table in self.tables}
            self.exchanges = dict(zip(keys, values))

    def start(self):
        self.getHtmlBody()
        self.getTableExchange()
        self.getPriceTable()
