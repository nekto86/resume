from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url=str(input('Куда стучимся? '))
company = str(input('К какой компании обращаемся '))
projects_count=int(input('На скольки проектах ты там работа? '))
released = int(input('Сколько из них релизнулось? '))
already_released = int(input('Сколько из них почти релизнулось? '))
active_work_to_release = int(input('Сколько в активной разработке? '))
unknown_release_status=int(input('Сколько будут рефакториться? '))
repository='https://github.com/nekto86/resume'

browser = webdriver.Chrome()
browser.get(url)
sleep(3)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
wait=WebDriverWait(browser, 30)
element=wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'check__box')))
browser.find_element_by_name('firstName').send_keys ('Горяйнов Дмитрий')
browser.find_element_by_name('email').send_keys('rinat.mux@yandex.ru')
browser.find_element_by_name('contact-info-other').send_keys('+7922655788')
browser.find_element_by_name('city').send_keys('Нижневартовск')
browser.find_element_by_name('offer').send_keys('45000-65000')
browser.find_element_by_name('detailText').send_keys(f'Доброго времени суток, не смотря на то, что мой опыт тестирования равен лишь, почти, 8 месяцам, за это время я успел поработать на {projects_count} проектах компании: '
                                                     f'из которых {released} вышли в релиз, {already_released} в предрелизном состоянии, {active_work_to_release} ожидают рефакторинга.'
                                                     f'В рамках работы на проектах, я занимался: Тестирование ПО: веб приложений, Android и IOS мобильных приложений методами серого и чёрного ящиков;'
                                                     f' тестирование API, тестирование вёрстки, нагрузочное тестирование, написание технической документации (включаяя описание мобильного приложения на английском языке) и составление'
                                                     f'схемы проекта; работа с БД, ведение баг-репортов, взаимодействие с автоматической баг-трекинговой системой, регрессионное тестирование, тестирование'
                                                     f' иностранной (английской) версии продукта. Мне кажется, что моего опыта и понимания методик и принципов тестирования будет достаточно, чтобы пригодиться компании Playrix.'
                                                     f'Чтобы вы понимали, это письмо было отправлено с помощью написания небольшого скрипта на Python, ссылку на репозиторий также прикрепляю: {repository} .'
                                                     f'Я, как соискатель, не скрываю минусов своих знаний: пока что ни на одном проекте не было необходимости писать автотесты, поэтому, не смотря на изучение данной темы и '
                                                     f'успешного прохождения курса на Stepik.org, реального боевого опыта автотестов у меня нет, да и часть информации подзабылась за неиспользованностью. '
                                                     f'Также, в рамках моего опыта, взаимодействия с гитом заключалось лишь в получении доступа к актуальной версии сваггера и один раз я '
                                                     f'разворачивал локальный стенд у себя, для тестирования микросервисов. '
                                                     f'У меня нет проблем с коммуникацией, поэтому, если понадобится дополнительная информация - be my guest')
wait=WebDriverWait(browser, 30)
element=wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'check__box')))
browser.find_element_by_css_selector('.check__box').click()
wait=WebDriverWait(browser, 30)
element=wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'all-jobs-form__button')))
browser.find_element_by_class_name('all-jobs-form__button').click()
sleep(10)
browser.close()


