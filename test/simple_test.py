def test_exchange_rates(app):
    assert app.search.get_rates_meduza() == app.search.get_rates_yandex()


def test_search_word(app):
    app.search.get_value('коронавирус')
    app.search.google_search()
    assert app.search.find_result() > 1000


def test_search(app, data_search):
    value = data_search
    assert True == app.search.verification_of_acceptance_conditions(value)

