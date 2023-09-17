import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_browser(use_static_proxy='', headles=False):

    options = Options()

    script_location = os.path.dirname(os.path.realpath(__file__))
    options.add_argument('--profile-directory=Default')
    options.add_argument("--user-data-dir=C:\\Users\\<USER>\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument("--log-level=3")
    

    if use_static_proxy != "":
        PROXY = use_static_proxy

        # depending on the proxy type uncomment what is needed below
        # options.add_argument('--proxy-server=socks5://' + PROXY)
        options.add_argument('--proxy-server=%s' % PROXY)


    if headles:
        options.add_argument("--headless")


    # Uncomment the below extentions if needed
    # options.add_extension(f'{script_location}/static/extentions/ublock_origin/extension_1_31_2_0.crx')
    # options.add_extension(f'{script_location}/static/extentions/web_rtc_control/0.2.7_0.crx')
    # options.add_extension(f'{script_location}/static/extentions/css_block/CSS-Block_v1.0.0.crx')
  
    options.add_argument('--disable-webgl')
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 2,
        "profile.default_content_setting_values.media_stream_camera": 2,
        "profile.default_content_setting_values.geolocation": 2,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.images": 2
    })

    
    browser = webdriver.Chrome(options=options)
    browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    return browser

if __name__ == '__main__':
    get_browser()
