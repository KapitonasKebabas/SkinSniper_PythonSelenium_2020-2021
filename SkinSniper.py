import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import os
import time
import random


#Kodo pradzia
print("-------------------Pradzia-------------------")

#url aprasymas
url = []
url.append("https://steamcommunity.com/market/listings/730/CZ75-Auto%20%7C%20Silver%20%28Factory%20New%29")
url.append("https://steamcommunity.com/market/listings/730/MAG-7%20%7C%20Carbon%20Fiber%20%28Factory%20New%29")
url.append("https://steamcommunity.com/market/listings/730/Desert%20Eagle%20%7C%20The%20Bronze%20%28Factory%20New%29")
url.append("https://steamcommunity.com/market/listings/730/Dual%20Berettas%20%7C%20Switch%20Board%20%28Factory%20New%29")

#Float aprasymas
TikrinimoFloutListas = []
TikrinimoFloutListas.append(0.0098) #CZ
TikrinimoFloutListas.append(0.008) #MAG-7
TikrinimoFloutListas.append(0.008) #Desert Eagle
TikrinimoFloutListas.append(0.008) #Dual Berettas

#LogIn aprasymas
LogInNustatymai = {
    "User" : "KietasVaikas01",
    "Psw" : "BotasKietas001"
}

#Extension aprasymas
unpacked_extension_path1 = r'jjicbefpemnphinccgikpdaagjebbnhg.crx'
unpacked_extension_path2 = r'kaibcgikagnkfgjnibflebpldakfhfih.crx'

#Extension pridejimas
options = Options()

options.add_extension(unpacked_extension_path1)
options.add_extension(unpacked_extension_path2)

#Paleidziam chromedriver
driver = webdriver.Chrome(executable_path=r"chromedriver.exe", chrome_options=options)
time.sleep(1)

#Atidaromas url
driver.get(url[0])
time.sleep(1)

blekoks = input("Kai pakeisi nustatymus ivesti bet koki simboli: " )

#Gmail trinimas
#gmailTrinimas()
print("Content istrintas")
time.sleep(1)


#LogIn
driver.find_element_by_class_name("global_action_link").click()
inputElement = driver.find_element_by_id("input_username")
inputElement.send_keys(LogInNustatymai["User"]) #KietasVaikas01  Cia irasyti nickname login
inputElement = driver.find_element_by_id("input_password")
inputElement.send_keys(LogInNustatymai["Psw"]) #BotasKietas001   Cia irasyti psw login
time.sleep(1)
driver.find_element_by_class_name("login_btn").click()
time.sleep(3)


x = input("Po ivedimo ivesti bet ka" )

print("Kodo pradzia po auth")
print("---------------------------------------------------------------")
# Kodas po authentifikacijos

#Laukimas kol isijungs tinkamas url
while driver.current_url == url:
    print("sleeping")
    time.sleep(3)

#Kintamieji prekiu paieskai
starteris = True
tinkamiFloat = 0
IsvisoTinkamuFlout = 0

#Prekiu paieskos kodo pradzia
MainCode()

#Kodo pabaiga programu uzdarymas
driver.close()
driver.stop_client()
print("Kodo pabaiga")

def MainCode():
    while starteris:
        for PslX in range(len(url)):
            try:
                #kintamuju atstatymas
                tinkamiFloat = 0

                #TimeOut ir url keitimas/perkrovimas
                time.sleep(random.randint(5,10))
                if driver.current_url == url[PslX]:
                    driver.refresh()
                else:
                    driver.get(url[PslX])

                #Sort
                '''
                element = driver.find_element_by_xpath("//*[@id='csgofloat_sort_by_float']")
                driver.execute_script("arguments[0].scrollIntoView();", element)
                element.click()
                '''

                #Gaunamas ginklo vardas
                text = driver.find_element_by_class_name("hover_item_name").text
                print(text)
                time.sleep(1)

                #Kainos maximumas
                kainosMaxEl = driver.find_elements_by_xpath("//*[@class='market_commodity_orders_header_promote']")
                kainosMax = 0
                kaina = ""
                tmepantro = 0
                for kainosMaxEl2 in kainosMaxEl:
                    if tmepantro == 1:
                        listasskaiciu = kainosMaxEl2.get_attribute('innerHTML')
                        for simbolis in listasskaiciu:
                            if ord(simbolis) >= 48 and ord(simbolis) <= 57:
                                kaina += simbolis
                            if ord(simbolis) == 44:
                                kaina += simbolis
                            if ord(simbolis) == 45:
                                kaina += "0"
                        kaina = kaina.split(",")
                        #print(kaina)
                        kainosMax = float(kaina[0])+(float(kaina[1])/100)
                    tmepantro = 1
                kainosMax = kainosMax + kainosMax*0.1
                print("Ieskoma kaina zemesne arba lygi: " , kainosMax , " Float: " , TikrinimoFloutListas[PslX])

                #Balansas
                BalansoEl = driver.find_element_by_id("header_wallet_balance").get_attribute('innerHTML')
                kaina = ""
                balansas = 0
                for simbolis in BalansoEl:
                    if ord(simbolis) >= 48 and ord(simbolis) <= 57:
                        kaina += simbolis
                    if ord(simbolis) == 44:
                        kaina += simbolis
                    if ord(simbolis) == 45:
                        kaina += "0"
                kaina = kaina.split(",")
                #print(kaina)
                balansas = float(kaina[0])+(float(kaina[1])/100)
                #tikrinimas balanso ir max kainos
                if balansas >= kainosMax:

                    #Radimas vidurkiu pirkimui

                    #Kainos Listas
                    kainosListas = driver.find_elements_by_xpath("//*[@class='market_listing_price market_listing_price_with_fee']")
                    Fkaina = []
                    temp = 0
                    for x in kainosListas:
                        y = x.get_attribute('innerHTML')
                        y.strip()
                        kaina = ""
                        for simbolis in y:
                            if ord(simbolis) >= 48 and ord(simbolis) <= 57:
                                kaina += simbolis
                            if ord(simbolis) == 44:
                                kaina += simbolis
                            if ord(simbolis) == 45:
                                kaina += "0"
                        if kaina == "":
                            Fkaina.append(0.00)
                        else:
                            kaina = kaina.split(",")
                            Fkaina.append(float(kaina[0])+(float(kaina[1])/100))
                        temp += 1

                    #Float listas
                    FlaotuListas = driver.find_elements_by_xpath("//*[@class='csgofloat-itemfloat']")
                    temp = 0
                    FFloutas = []
                    for x in FlaotuListas:
                        y = x.get_attribute('innerHTML')
                        y = y[y.find('Float:')+7:]
                        stringas = ""
                        if "Rank" in y:
                            for simbolis in y:
                                if ord(simbolis) == 60:
                                    break
                                if simbolis != "":
                                    stringas += simbolis
                        else:
                            stringas = y
                        FFloutas.append(float(stringas))

                    #Tikrinimas ir mygtuko spaudimas
                    PrekesID = -1
                    soldButtonvnt = 0
                    for x in range(len(Fkaina)):
                        #print("Floatas: " , FFloutas[x] , " Kaina: " , Fkaina[x])
                        if Fkaina[x] > 0:
                            if Fkaina[x] <= kainosMax and Fkaina[x] > 0.0 and FFloutas[x] <= TikrinimoFloutListas[PslX]: #0.01
                                print("Perkama: " , Fkaina[x] , " "  , FFloutas[x])
                                PrekesID = x
                                break
                        if Fkaina[x] == 0:
                            soldButtonvnt += 1
                        if Fkaina[x] <= kainosMax and FFloutas[x] <= TikrinimoFloutListas[PslX]: #0.01
                            tinkamiFloat += 1
                            IsvisoTinkamuFlout += 1
                    print("Isviso galimu flout rasta: " , IsvisoTinkamuFlout)
                    print("Galimi Flout rasta: " , tinkamiFloat)
                    for x in range(len(Fkaina)):
                        if FFloutas[x] <= TikrinimoFloutListas[PslX]: #0.01
                            tinkamiFloat += 1
                    print("Tinkami Floaut rasti: " , tinkamiFloat)
                    if PrekesID != -1:

                        #Buy mygtukas
                        MygtukuListas = driver.find_elements_by_xpath("//*[@class='market_listing_buy_button']")
                        temp = 0
                        mygtukoID = PrekesID - soldButtonvnt
                        print(mygtukoID)
                        for x in MygtukuListas:
                            if temp == mygtukoID:
                                x.click()
                                print("paspausta")
                            temp += 1

                        #SSA patvirtinimas ir purshase spaudimas
                        try:
                            #csgofloat-itemfloat
                            flaoutas = driver.find_element_by_xpath("//*[@class='csgofloat-itemfloat']").get_attribute('innerHTML')
                            floutINT = 0
                            strFlaot = ""
                            for simbolis in flaoutas:
                                if ord(simbolis) >= 48 and ord(simbolis) <= 57:
                                    strFlaot += simbolis
                                if ord(simbolis) == 44:
                                    strFlaot += "."
                                if ord(simbolis) == 46:
                                    strFlaot += "."
                            floutINT = float(strFlaot)

                            if floutINT <= TikrinimoFloutListas[PslX]:
                                element = driver.find_element_by_xpath("//*[@id='market_buynow_dialog_accept_ssa']")
                                driver.execute_script("arguments[0].scrollIntoView();", element)
                                element.click()
                                driver.find_element_by_id("market_buynow_dialog_purchase").click()
                                print("Nupirkta preke")
                            else:
                                print("Erorr blogas flaot" +  flaoutas)
                        except:
                            kazkasBelekas = input("Ivyko klaida: " )
                    print("Kodo prekiu paieskos pabaiga")
                else:
                    #Per mazas balansas
                    print("Per mazas balansas")
            except:
                #Error excepct refresh
                print("Buvo Erorr")
                PslX = PslX - 1