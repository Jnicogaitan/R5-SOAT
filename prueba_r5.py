import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\Selenium\chrome_driver")

	def test_cotizar(self):
		driver =self.driver
		driver.get("https://soat.grupor5.com/")
		time.sleep(3)
		placa = driver.find_element_by_xpath("//*[@id='vehicleRegistration']")
		time.sleep(3)
		placa.send_keys("rzi521")
		placa.send_keys(Keys.ENTER)
		time.sleep(10)
		descuento = driver.find_element_by_xpath("//*[@id='root']/section/div/section/div/button")
		descuento.click()
		time.sleep(5)
		
		t_documento =driver.find_element_by_xpath("/html/body/div[1]/section/div/section/div[2]/form/div[1]/div/div/div[1]")  
		t_documento.click()
		time.sleep(2)
		t_documento =driver.find_element_by_xpath("/html/body/div[1]/section/div/section/div[2]/form/div[1]/div/div[2]/div/div[1]")
		t_documento.click()
		time.sleep(2)

		n_documento =driver.find_element_by_xpath("//*[@id='identification']")
		n_documento.send_keys("1020795723")
		time.sleep(2)

		correo =driver.find_element_by_xpath("//*[@id='emailAddress']")
		correo.send_keys("nicolas.gaitan@grupor5.com")
		time.sleep(2)

		telefono =driver.find_element_by_xpath("//*[@id='mobilePhone']")
		telefono.send_keys("3105564840")
		time.sleep(2)

		confirmar =driver.find_element_by_xpath("//*[@id='root']/section/div/section/div[2]/form/div[5]/label/span")
		confirmar.click()
		time.sleep(2)

		calcular =driver.find_element_by_xpath("//*[@id='root']/section/div/section/div[2]/form/button/span")
		calcular.click()
		time.sleep(15)

		medio_pago = dirver.find_element_by_xpath("//div[@id='paymentMethod']/label[2]/div/span/span/b")
		driver.implicitly_wait(30)
		medio_pago.click()
		time.sleep(4)

		pagar = driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div[2]/div/div[3]/button/span")
		pagar.click()
		time.sleep(5)

		documento_pagador = driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div[2]/div/div[3]/form/div/div[1]/div[1]/div[1]/div/div[1]/input")
		documento_pagador.click()
		time.sleep(5)

		n_documento_pagador =driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div[2]/div/div[3]/form/div/div[1]/div[1]/div[2]/input")
		n_documento_pagador.send_keys("1020795723")
		time.sleep(2)

		nombre_pagador =driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div[2]/div/div[3]/form/div/div[1]/div[1]/div[3]/input")
		nombre_pagador.send_keys("Nicolas")
		time.sleep(2)

		apellido_pagador =driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div[2]/div/div[3]/form/div/div[1]/div[1]/div[4]/input")
		apellido_pagador.send_keys("Gaitan")
		time.sleep(2)

		email_pagador =driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div[2]/div/div[3]/form/div/div[1]/div[1]/div[6]/input")
		email_pagador.send_keys("nicolas.gaitan@grupor5.com")
		time.sleep(2)

		tarjeta =driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div[2]/div/div[3]/form/div/div[1]/div[2]/input")
		tarjeta.send_keys("4915110231144809")
		time.sleep(2)

		cvc =driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div[2]/div/div[3]/form/div/div[1]/div[3]/div/div[1]/input")
		cvc.send_keys("251")
		time.sleep(2)

		cuotas =driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div[2]/div/div[3]/form/div/div[1]/div[3]/div/div[2]/input")
		cuotas.send_keys("2")
		time.sleep(2)

		exp1 =driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div[2]/div/div[3]/form/div/div[1]/div[4]/div/input[1]")
		exp1.send_keys("12")
		time.sleep(2)

		exp2 =driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div[2]/div/div[3]/form/div/div[1]/div[4]/div/input[2]")
		exp2.send_keys("2025")
		time.sleep(2)

		pagar2 = driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div[2]/div/div[3]/form/div/div[2]/button")
		pagar2.click()
		time.sleep(50)





if __name__ == '__main__':
	unittest.main()

#//*[@id='vehicleRegistration']