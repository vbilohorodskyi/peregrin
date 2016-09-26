# -*- coding: utf-8 -*-
__author__ = 'vbilohorodskyi'

from selenium import webdriver

MAP_FILE = 'map.txt'
TRIES_COUNT = 3
TIME_THRESHOLD = 2.8


def measure_page_performance_time(driver, tries_count, url):
    average = 0
    print "url: ", url
    for n in range(tries_count):
        driver.get(url)
        stext = driver.execute_script(
            "return ( window.performance.timing.loadEventEnd - window.performance.timing.navigationStart )")
        average = average + int(stext)
        print "trying ", n + 1, " time", "........Value is: %s" % float(float(stext) / 1000), "seconds"

    total_load_time = (float(float(average) / float(tries_count)) / 1000)

    if total_load_time < TIME_THRESHOLD:
        warning_msg = " - OK"
    else:
        warning_msg = "!!!WARNING!!! THIS PAGE PERFORMANCE IS TOO SLOW"

    print "||url: ", url, "AVERAGE is: %s" % total_load_time, "seconds" + warning_msg + "||"
    print ""


def count_performance(driver, TRIES_COUNT):

    driver.maximize_window()
    url_list = [line.rstrip('\n') for line in open(MAP_FILE)]

    for url in url_list:
        measure_page_performance_time(driver, TRIES_COUNT, url)

    driver.quit()


drivers = [webdriver.Chrome(), webdriver.Firefox()]

for driver in drivers:
    print("=============================")
    driver_name = driver.capabilities['browserName']
    print("Measuring with " + driver_name + ":")
    count_performance(driver, TRIES_COUNT)
