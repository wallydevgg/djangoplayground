from .scrappings.info_dolar import InfoDolarScrapping
from models import Exchange
from datetime import datetime


def exchangeDateNow():
    scrapping = InfoDolarScrapping()
    prices = scrapping.exchanges
    date_now = datetime.now().date().isoformat()
    Exchange.objects.update_or_create(
        date=date_now,
        defaults={
            "date": date_now,
            "buy_price": prices["compra"],
            "sell_price": prices["venta"],
        },
    )
