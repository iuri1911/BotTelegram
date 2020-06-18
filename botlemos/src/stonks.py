from PIL import Image, ImageDraw, ImageFont
import requests


def cotar(corno):
    usdurl = 'https://economia.awesomeapi.com.br/all/USD-BRL'
    usd = requests.get(usdurl)
    data = usd.json()
    usdf = float(data['USD']['ask'])

    audurl = 'https://economia.awesomeapi.com.br/all/AUD-BRL'
    aud = requests.get(audurl)
    data = aud.json()
    audf = float(data['AUD']['ask'])

    image = Image.open('stonksl.png')

    font_type = ImageFont.truetype('impact.ttf', 40)
    font_type2 = ImageFont.truetype('impact.ttf', 30)

    draw = ImageDraw.Draw(image)

    draw.text(xy=(190, 180), text='{} É CORNO'.format(corno), fill=(255, 255, 255),
              font=font_type2, stroke_fill=2, stroke_width=2)
    draw.text(xy=(300, 380), text='USD : R${:.2f}'.format(usdf), fill=(255, 255, 255),
              font=font_type, stroke_fill=2, stroke_width=2)
    draw.text(xy=(300, 430), text='AUD : R${:.2f}'.format(audf), fill=(255, 255, 255),
              font=font_type, stroke_fill=2, stroke_width=2)

    image.save('cotacao.png')

def coronar(corno):
    coronabrurl = 'https://coronavirus-19-api.herokuapp.com/countries/brazil'
    cbr = requests.get(coronabrurl)
    data = cbr.json()
    casosbr = float(data['cases'])
    acasosbr = float(data['active'])
    mortosbr = float(data['deaths'])
    mortosbr = float(data['deaths'])

    coronaauurl = 'https://coronavirus-19-api.herokuapp.com/countries/australia'
    cau = requests.get(coronaauurl)
    data = cau.json()
    casosau = float(data['cases'])
    acasosau = float(data['active'])
    mortosau = float(data['deaths'])

    image = Image.open('coronafofoel.png')

    font_type = ImageFont.truetype('impact.ttf', 30)
    font_type2 = ImageFont.truetype('impact.ttf', 30)

    draw = ImageDraw.Draw(image)

    draw.text(xy=(15, 100), text='{} É CORNO'.format(corno), fill=(255, 255, 255),
              font=font_type2, stroke_fill=2, stroke_width=2)
              #BRAZIL
    draw.text(xy=(280, 15), text='CASOS: {}'.format(round(casosbr)), fill=(255, 255, 255),
              font=font_type, stroke_fill=2, stroke_width=2)
    draw.text(xy=(280, 50), text='ATIVOS: {}'.format(round(acasosbr)), fill=(255, 255, 255),
              font=font_type, stroke_fill=2, stroke_width=2)
    draw.text(xy=(280, 85), text='MORTOS: {}'.format(round(mortosbr)), fill=(255, 255, 255),
              font=font_type, stroke_fill=2, stroke_width=2)
              #AUSTRALIA
    draw.text(xy=(280, 260), text='CASOS: {}'.format(round(casosau)), fill=(255, 255, 255),
              font=font_type, stroke_fill=2, stroke_width=2)
    draw.text(xy=(280, 295), text='ATIVOS: {}'.format(round(acasosau)), fill=(255, 255, 255),
              font=font_type, stroke_fill=2, stroke_width=2)
    draw.text(xy=(280, 330), text='MORTOS: {}'.format(round(mortosau)), fill=(255, 255, 255),
              font=font_type, stroke_fill=2, stroke_width=2)

    draw.text(xy=(100, 470), text='FIDELIZA NO LIKE, FAVELA VENCEU', fill=(255, 255, 255),
              font=font_type, stroke_fill=2, stroke_width=2)
    image.save('coronafofoelfinal.png')


def frasear():

    url = 'https://allugofrases.herokuapp.com/frases/random'
    r = requests.get(url)
    data = r.json()
    f = data['frase']
    return f
