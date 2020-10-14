from selenium import webdriver
import time

class Piadas():
    def __init__(self):
        self.urlInicial = "http://www.piadasaqui.com.br/Piada.aspx?cod="
        self.driver = webdriver.Chrome("/home/celso/chromedriver")
        self.cod_inicial = 1
        self.cod_limite = 801
        self.caracteres_indesejaveis = ["\n","\t","\r"]
    
    def limpar_texto(self,texto):
        for caracter in self.caracteres_indesejaveis:
            texto = texto.replace(caracter,"")
        return texto
    def start(self):
        driver = self.driver
        for i in range(self.cod_inicial,self.cod_limite):
            try:
                driver.get(self.urlInicial + str(i))
                time.sleep(3)
                categoria = (driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_lblTitulo"]').text).split(" ")[1]
                texto = self.limpar_texto(driver.find_element_by_xpath('//*[@id="main-container"]/div[2]/div/div[1]/div/div[2]/div/h2').text)
                file = open("piadas.json","a")            
                file.write('{"cod":"'+str(i)+'","categoria":"'+categoria+'", "texto":"'+texto+'"},')
                file.close()
            except:
                time.sleep(1)
                continue



        




