from selenium import webdriver
driver=webdriver.Chrome()
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36'}
for i in range(1, 3):
    url='https://www.chinabond.com.cn/cb/cn/xxpl/ywgg/tgywgg/20230129/161991420.shtml'.format(i)
    driver.get(url)
    for i in range(10, 92):
        tag_xpath1 = driver.find_element_by_xpath('//*[@id="hiddenContent"]/table/tbody/tr[' + str(i) + ']/td[1]')
        tag_xpath2 = driver.find_element_by_xpath('//*[@id="hiddenContent"]/table/tbody/tr[' + str(i) + ']/td[2]')
        tag_xpath3 = driver.find_element_by_xpath('//*[@id="hiddenContent"]/table/tbody/tr[' + str(i) + ']/td[3]')
        tag_xpath4 = driver.find_element_by_xpath('//*[@id="hiddenContent"]/table/tbody/tr[' + str(i) + ']/td[4]')
        tag_xpath5 = driver.find_element_by_xpath('//*[@id="hiddenContent"]/table/tbody/tr[' + str(i) + ']/td[5]')
        tag_xpath6 = driver.find_element_by_xpath('//*[@id="hiddenContent"]/table/tbody/tr[' + str(i) + ']/td[6]')
        text1 = tag_xpath1.get_attribute('textContent').strip()
        text2 = tag_xpath2.get_attribute('textContent').strip()
        text3 = tag_xpath3.get_attribute('textContent').strip()
        text4 = tag_xpath4.get_attribute('textContent').strip()
        text5 = tag_xpath5.get_attribute('textContent').strip()
        text6 = tag_xpath6.get_attribute('textContent').strip()
        print('序号:', text1 + "  债券代码：" + text2 + "  债券名称：" + text3,'  计息方式:'+text4 ,
          " 债券面额（万元）：" + text5 + "  年利率(%)：" + text6)
driver.close()

