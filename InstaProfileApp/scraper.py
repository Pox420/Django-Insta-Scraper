from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def MyBot(name):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')

    # this below line specify the executable_path automatically
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    '''
    This line respecify the executable file that is notpresent in your coputer thats why it fails.
    i.e 
    self.driver = webdriver.Chrome(executable_path="E:\\Software\\chromedriver_win32\\chromedriver.exe",options=self.options)
    '''

    url = f'https://www.instagram.com/{name}/'

    driver.get(url)
    user_profile_image = driver.find_element_by_tag_name('img').get_attribute('src')
    # print(driver.find_element_by_tag_name('h2').text)
    user_name = driver.find_element_by_tag_name('h2').text
    # print(driver.find_elements_by_class_name('g47SY '))
    posts = driver.find_elements_by_class_name('g47SY ')[0].text
    # print(driver.find_elements_by_class_name('g47SY '))
    followers = driver.find_elements_by_class_name('g47SY ')[1].text
    # print(followers)
    following = driver.find_elements_by_class_name('g47SY ')[2].text

    images_link = []
    article = driver.find_element_by_tag_name('article')
    ps = article.find_elements_by_class_name('v1Nh3')
    for image in ps:
        image_link = image.find_element_by_class_name('KL4Bh').find_element_by_tag_name('img').get_attribute('src')
        images_link.append(image_link)

    master_dict = {
        'user_profile_image': user_profile_image,
        'user_name': user_name,
        'posts': posts,
        'followers': followers,
        'following': following,
        'images_links': images_link
    }
    # print(master_dict)
    driver.quit()
    return master_dict

# MyBot('sunilghimireofficial')
