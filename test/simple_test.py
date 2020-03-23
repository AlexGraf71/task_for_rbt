

def test_search_word(app):
    app.search.search_value()
    app.search.google_search()
    assert app.search.find_result() > 1000
