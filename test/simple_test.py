
def test_exchange_rates(app):
    assert app.search.get_rates_meduza() == app.search.get_rates_yandex()


def test_search_word(app):
    app.search.search_value()
    app.search.google_search()
    assert app.search.find_result() > 1000


