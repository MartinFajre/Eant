# En La Nacion deberemos scrollear para poder tomar todas las noticias, no tenes boton

from selenium import webdriver
from bs4 import BeautifulSoup as BS
from time import sleep


driver = webdriver.Chrome('C:/Users\MARTIN\OneDrive\Escritorio\CURSO EANT PYTHON\chromedriver.exe')   # Basta con cambiar solo la primer barrita.

driver.get('https://www.lanacion.com.ar/')



script_js = """ 
let fin_de_pantalla = document.body.scrollHeight 
window.scrollTo(0,fin_de_pantalla)
return fin_de_pantalla
"""
sleep(3)

pos_actual = 0
pos_siguiente = driver.execute_script(script_js)
sleep(3)

while pos_actual != pos_siguiente:
    pos_actual = pos_siguiente
    pos_siguiente = driver.execute_script(script_js)
    sleep(3)
    print(pos_siguiente)
print('Llegamos al final')    

url = 'https://www.lanacion.com.ar/'

respuesta = requests.get(url)
respuesta.enconding = 'utf-8'
html = respuesta.text

dom = BS(html, features = 'html.parser')

articulos = dom.find_all('h2')

for articulo in noticias:
    titulo = articulo.text
    link = articulo.a['href']
    print(titulo, '-', url+link)
    break







