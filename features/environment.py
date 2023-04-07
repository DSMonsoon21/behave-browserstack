from selenium import webdriver

def before_feature(context, feature):
    desired_capabilities = {
        'browserName': 'chrome'
    }
    context.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="https://%s:%s@hub.browserstack.com/wd/hub" % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY),
        keep_alive=True

    )

def after_feature(context, feature):
    context.browser.quit()
