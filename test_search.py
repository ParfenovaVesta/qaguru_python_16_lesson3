from selene import browser, be, have

def test_search_ok(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_search_ok(browser_open):
    browser.element('[name="q"]').should(be.blank).type('hfga657%4hdfg463').press_enter()
    browser.element('[id="search"]').should(have.text('По запросу hfga657%4hdfg463 ничего не найдено.'))
