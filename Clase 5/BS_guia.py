    # WebScraping
from bs4 import BeautifulSoup as BS


        
# Con la librería Beautifulsoup permite reconocer la estructura con la separación de etiquetas y la estructura jerárquica.Prettify se usa para que lo imprima bien organizado.
    
archivo_html = open('web_ejemplo.html', encoding = 'utf-8')

dom = BS(archivo_html, features = 'html.parser')
# print(dom.prettify())

# Quiero capturar el primer link.

primer_link = dom.a
print(primer_link.text)

# Otra forma es buscar la etiqueta que estoy buscando. Devolverá la primera.+

primer_link = dom.find('a')
print(primer_link.text)

# Puedo buscar todos los links

todos_los_links = dom.find_all('a')
print(todos_los_links)
type(todos_los_links) # Este elemento se comporta como una lista, por eso puedo usar indice
primer_link = todos_los_links[0]
print(primer_link.text)

# Tambien puedo buscar por los atributos como class, href, etc. Luego uso .get

print(primer_link['class'])
print(primer_link['href'])

for link in todos_los_links:
    print(link.get('href', "No existe"))

# Puedo capturar por la class (tengo que usar class_ para diferenciar de la clase de Py)
    
historias = dom.find_all(class_ = 'historia')

for historia in historias:
    print(historia.text)
    
# Tambien por ID 

elegido = dom.find(id= 'link1')
print(elegido.text)

# Puedo combinar los filtros para encontrar un fragmento

parrafo_historia = dom.find('p', class_ = 'historia')

# Si quiero utilizar un atributo que no es de los clasicos, debo hacerlo con attrs pasandole una lista.

historia2 = dom.find(attrs = {'data-minumero':'124124'})
print(historia2.text)











