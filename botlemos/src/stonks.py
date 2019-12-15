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


def frasear():

    url = 'https://allugofrases.herokuapp.com/fraseAleatoria'
    r = requests.get(url)
    data = r.json()
    f = data['frase']
    return f
