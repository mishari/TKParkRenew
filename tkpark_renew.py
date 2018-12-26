from selenium import webdriver

login_id = open("id.txt").read().strip()

d = webdriver.Firefox()
d.get("http://search.tkpark.or.th/tkpark/Member/Login.aspx")
d.find_element_by_name('ctl00$cphContent$txtUsername').send_keys(login_id)
d.find_element_by_name('ctl00$cphContent$btnLogin').click()

d.get("http://search.tkpark.or.th/tkpark/Member/ItemNotReturn.aspx")

for i in xrange(0,6):
    try:
        d.find_element_by_id("cphContent_grdItemnotreturn_RowSelectorColumnSelector_%d" % i).click()
    except NoSuchElementException:
        break

d.find_element_by_id("cphContent_btrenew").click()


alert = webdriver.common.alert.Alert

alert(d).accept()

