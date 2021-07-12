from selenium import webdriver
from bs4 import BeautifulSoup as BS
from time import sleep


driver = webdriver.Chrome('C:/Users\MARTIN\OneDrive\Escritorio\CURSO EANT PYTHON\chromedriver.exe')   # Basta con cambiar solo la primer barrita.

driver.get('https://www.olx.com.ar/items/q-aspiradoras-de-auto')

# Codigo de Java Script para poder apretar el boton que carga más elementos en la pag, es decir desplegar todo el DOM

script_js = """ 
let boton = document.querySelector('[data-aut-id="btnLoadMore"]')
if (boton) {
        boton.click()
            }
else{
     return "No existe"
     }
"""
sleep(3)    #Espera 3 segs para que cargue bien la pag.

while driver.execute_script(script_js) != 'No existe': 
    sleep(3)
 
sleep(3)

# Ahora si capturo la info deseada
html = driver.execute_script("return document.documentElement.outerHTML")  #capturo el html

driver.quit()

dom = BS(html, features = 'html.parser')
productos = dom.find_all(class_ = 'IKo3_')
print('Cantidad de productos: ',len(productos))

for producto in productos:
    precio = producto.find(class_ = '_89yzn').text    
    titulo = producto.find(class_ = '_2tW1I').text    
    print(titulo + ' - ' + precio)




