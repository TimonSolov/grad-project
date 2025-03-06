# BANK MANAGER MAIN PAGE
ADD_CUSTOMER_TAB = "//button[normalize-space()='Add Customer']"
OPEN_ACCOUNT_TAB = "//button[normalize-space()='Open Account']"
CUSTOMERS_TAB = "//button[normalize-space()='Customers']"

# ADD CUSTOMER TAB
FIRST_NAME = "//input[@placeholder='First Name']"
LAST_NAME = "//input[@placeholder='Last Name']"
POSTCODE_FIELD = "//input[@placeholder='Post Code']"
ADD_CUSTOMER_BUTTON = "//button[@type='submit']"

# OPEN ACCOUNT TAB
CUSTOMER_SELECTOR = "//select[@id='userSelect']"
CURRENCY_SELECTOR = "//select[@id='currency']"
PROCESS_BUTTON = "//button[@type='submit']"

# CUSTOMERS TAB
SEARCH_FIELD = "//input[@placeholder='Search Customer']"
FIRST_NAME_SORTING = "//a[normalize-space()='First Name']"
LAST_NAME_SORTING = "//a[normalize-space()='Last Name']"
POSTCODE_SORTING = "//a[normalize-space()='Post Code']"
DELETE_CUSTOMER_BUTTON = "button[ng-click='deleteCust(cust)']"
NEW_USER_FIRST_NAME = "//td[normalize-space()='New']"
NEW_USER_LAST_NAME = "//td[normalize-space()='User']"
NEW_USER_POSTCODE = "//td[normalize-space()='1234']"
NEW_USER_ACCOUNT_NUMBER = "//span[normalize-space()='1016']"

USER_FIRST_NAME = "//td[normalize-space()='Harry']"
USER_FIRST_NAME_IN_ROW = "tbody td:nth-child(1)"
FIRST_NAME_ON_SORTING = 'tbody tr:nth-child(1) td:nth-child(1)'
LAST_NAME_ON_SORTING = 'tbody tr:nth-child(1) td:nth-child(2)'
POSTCODE_ON_SORTING = 'tbody tr:nth-child(1) td:nth-child(3)'
