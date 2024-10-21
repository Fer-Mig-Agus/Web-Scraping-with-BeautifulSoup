import requests
from bs4 import BeautifulSoup



url="https://www.game.es/ACCESORIOS/AURICULARES/PC-GAMING/GAME-HX500-RGB-71-PRO-GAMING-HEADSET-PC-PS4-AURICULARES-AURICULARES-GAMING/169628"


headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/97.0.4692.99 Safari/537.36"}


try:
    response=requests.get(url,headers=headers ,timeout=10)
    response.raise_for_status()
    
    soup=BeautifulSoup(response.text,'html.parser')
    
    title=soup.find('h1',class_='product-title').text.strip()
    
    try:
        precio_anterior=float(soup.find('div',class_='buy--price').find('small').text.replace('€','').replace(',','.'))
    except:
        precio_anterior=None
    
    try:
    
        entero= soup.find('div',class_='buy--price').find(class_='int').text.strip().split('\n')[0].strip()
        
        decimal=soup.find('div',class_='buy--price').find(class_='decimal').text.replace("'",'.')
        
        price=float(entero+decimal)
    except:
        price=None
    
    
    plataforma=[]
    elementos=soup.find('dd',class_='dd').find_all('a')
    for elemento in elementos:
        plataforma.append(elemento.text.strip())
    
    try:
        valoracion=int(soup.find('a',class_='reviews-points-m').attrs['class'][-1][-1])
    
    except:
        valoracion=None
    
   # soup.find(id='product-cover')
   #otra manera de hacer los mismo seria esta
    link_image=soup.find('img',{'id':'product-cover'}).attrs.get('src')
    
    
    print('Datos encontrados de la pagina')
    print(f'\nTitulo: {title} \nPrecio Anterior: {precio_anterior}\nPrecio Actual:{price}\nLink de imagen: {link_image}')
    
    

except requests.RequestException as error:
    print(f'Huno un error en la peticion: {error}')