from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

def es_multiplo(numero, multiplo):
    if numero % multiplo == 0:
        return True
    else:
        return False  
def changeCaracter(value, string):
    index = 77
    new_character = value
    string = string[:index] + new_character + string[index+1:]
    return string
def helpScroll(x,driver):
        x = x-4
        sx = str(x)
        txt1 = changeCaracter(sx,txt)
        print('scroll',txt1)
        python = driver.find_element(By.XPATH, txt1)
        driver.execute_script('arguments[0].scrollIntoView(true)',python)
        time.sleep(5)
        
        x = x+2
        sx = str(x)
        txt1 = changeCaracter(sx,txt)
        print('scroll',txt1)
        python = driver.find_element(By.XPATH, txt1)
        driver.execute_script('arguments[0].scrollIntoView(true)',python)
        time.sleep(5)
        
        x = x-2
        sx = str(x)
        txt1 = changeCaracter(sx,txt)
        print('scroll',txt1)
        python = driver.find_element(By.XPATH, txt1)
        driver.execute_script('arguments[0].scrollIntoView(true)',python)
        time.sleep(5)
        
        x = x+2
        sx = str(x)
        txt1 = changeCaracter(sx,txt)
        print('scroll',txt1)
        python = driver.find_element(By.XPATH, txt1)
        driver.execute_script('arguments[0].scrollIntoView(true)',python)
        time.sleep(5)
        
        
        x = x-2
        return x
def downScroll(x,driver): 
        x = x+2
        sx = str(x)
        txt1 = changeCaracter(sx,txt)
        print('scroll',txt1)
        python = driver.find_element(By.XPATH, txt1)
        driver.execute_script('arguments[0].scrollIntoView(true)',python)
        time.sleep(25)    
        x = x-2
        return x
def extractdata(driver,listNames,listAverage,listAbout,listReview,listDir,listEmail,listPhone,info):
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    names = soup.find("h1", class_= "DUwDvf")
    lugares = soup.find_all("div", class_= "Io6YTe")
    typeB = soup.find("button", class_= "DkEaL")
    block = soup.find_all("div", class_= "F7nice")
    count = 0
    name = ''
    star = 0
    data = ''
    value = []
    if(len(names)==5):
        for search in names:
            if(count == 1):
                name = search.string
            count = count + 1
        count = 0
        try:
            listNames.index(name)
            print("Repeat",name)
            print("it does not save")
            return True
        except:
            listNames.append(name)
            listAbout.append(typeB.string)
            for search in block:
                i = search.find_all("span")
                for re in i:
                    if(re.string != None):
                        count = count + 1
                        if(count == 1):
                            star = re.string
                            listAverage.append(star)
                        if(count == 2):
                            data = re.string
                            listReview.append(data)
            a=''
            b=''
            c=''
            listUrl =['.com', '.co', '.net', '.org', '.gob', '.es', '.info', '.me' ] 
            for search in lugares:
                if(search.string != None):
                    value.append(search.string)
                    dat=search.string
                    if(dat.find("+1") != -1):
                        a = dat
                        listPhone.append(dat)
                    if(dat.find("Estados Unidos") != -1):
                        b = dat
                        listDir.append(dat)
                    if(c==''):
                        for endUrl in listUrl:
                            if(dat.find(endUrl) != -1):
                                c = dat
                                listEmail.append(dat)
                                break
            if(a == ''):
                listPhone.append('')
            if(b == ''):
                listDir.append('')
            if(c == ''):
                listEmail.append('')
            info.append(value)
            print("-------------------------------------------------------------------------------------------------------")
            print(name)
            #print(star)
            #print(typeB.string)
            #print(data)
            #print(value)º
            print("-------------------------------------------------------------------------------------------------------")
            return False
driver = webdriver.Chrome()
print("write Url to web scraping on google maps")
url = input()
driver.get(url)
time.sleep(2)
txt =  '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div/a'

listNames = []
listAverage = []
listAbout = []
listReview = []
listDir = []
listEmail = []
listPhone = []
info = []

x = 1
j = 1
t = 5
count = 0
value = 10000
print("number or items")
numberCounts = int(input())
for i in range(value):
    print("count: ",len(listNames))
    if(numberCounts!= len(listNames) ):
        x = x+2
        sx = str(x)
        txt1 = changeCaracter(sx,txt)
        output = es_multiplo(i+1,5)
        if(output):
            try:
                n = x-2
                sn = str(n)
                ant = changeCaracter(sn,txt)
                print('scroll',ant)
                python = driver.find_element(By.XPATH, ant)
                driver.execute_script('arguments[0].scrollIntoView(true)',python)
                time.sleep(3)
                print('scroll',txt1)
                python = driver.find_element(By.XPATH, txt1)
                driver.execute_script('arguments[0].scrollIntoView(true)',python)
                time.sleep(3)
                x = x-2
            except:
                #print(txt1)
                try:
                    print("FIX-0·································································")
                    x = downScroll(x,driver)
                    print("FIX-0·································································")
                except:
                    print("FIX-1$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    x =  helpScroll(x,driver)
                    print("FIX-1$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                
        else:
            try:
                driver.find_element(By.XPATH, txt1 ).click()
                time.sleep(10)
            except:
                print("FIX-2*******************************************************************************")
                x = helpScroll(x,driver)
                print("FIX-2*******************************************************************************") 
            flag = extractdata(driver,listNames,listAverage,listAbout,listReview,listDir,listEmail,listPhone,info)
            if(flag):
                print("repeat count", count)
                count = count + 1
            else:
                count = 0
        if(count == 15):
            print("repeat count", count)
            print("cycle breaks")
            break
    else:
        print("number of items are ready")
        break

print('end script')

print("it will create excel with data")
col1 = "Nombres"
col2 = "Promedio"
col3 = "Tipo"
col4 = "Reseñas"
col5 = "info"
data = pd.DataFrame({col1:listNames,col2:listAverage,col3:listAbout,col4:listReview,col5:info})
data.to_excel('a_data.xlsx', sheet_name='sheet1', index=False)

col1 = "Nombres"
col2 = "Promedio"
col3 = "Tipo"
col4 = "Reseñas"
col5 = "lugar"
col6 = "email"
col7 = "phone"
data = pd.DataFrame({col1:listNames,col2:listAverage,col3:listAbout,col4:listReview,col5:listDir,col6:listEmail,col7:listPhone})
data.to_excel('b_data.xlsx', sheet_name='sheet1', index=False)
print("END THE PROGRAM")