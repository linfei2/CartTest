from selenium.webdriver.common.by import By


class Loc:
    NEW_IN_BTN = (By.XPATH, '//*[@id="menu-item-21"]/a')
    FIRST_PRODUCT = (By.XPATH, "//ul[@class='products columns-3']/li[1]")
    ADD_TO_CART_BTN = (By.XPATH, "//button[@name='add-to-cart']")
    CART_ICON = (By.XPATH, '//*[@id="site-header-cart"]/div/a/span/span')
    REMOVE_BTN = (By.XPATH, '//*[@id="post-3035"]/div/div/form/table/tbody/tr[1]/td[1]/a')
    EMPTY_CART_NOTIFICATION = (By.XPATH, "//p[@class='cart-empty woocommerce-info']")