from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


# content per day
DAILY_MESSAGES = {
    # head over feet
    # doll picture
    1: {
        "message": "Juro que não tenho palavras para descrever a panóplia de emoções que despoltas em mim. <br> Mas nos próximos 25 dias vou me esforçar, muito.<br> <br>Para o primeiro dia vou começar por salientar o quão especial me fazes sentir.<br><br> Fazes-me sentir uma boneca. Esta música faz-me pensar isso.",
        "music_link": "https://open.spotify.com/embed/track/735rjks7kQgWCjTQlIHMuH?utm_source=generator",  # Replace with a valid YouTube embed link
        "image": "pictures/day1.jpg"
    },
    # closing time. 
    # Amarante's picture
    2: {
        "message": "Foste a maior surpresa da minha vida<br>Não esperava que alguém fosse aparecer na minha vida assim <br>Alguém que me faz tão feliz<br>Alguém em quem eu acredito tanto <br>Continuas a ser uma surpresa todos os dias",
        "music_link": "https://open.spotify.com/embed/track/1A5V1sxyCLpKJezp75tUXn?utm_source=generator",  # Replace with another video
        "image": "pictures/day2.jpg"
    },
    # Let's do it. 
    # Magusto
    3: {
        "message": "Antes, quando ouvia esta música deixava-me a pensar se devia deixar andar ou não <br> Escolhi bem ",
        "music_link": "https://open.spotify.com/embed/track/4Od7rEL8ehrcRr38g86OMm?utm_source=generator",  # Replace with another video
        "image": "pictures/day3.jpg"
    },
    # Ought know
    # Foto com nina
    4: {
        "message": "Um sonho tornado realidade <br> <br> <br> PS.: Ainda que uma música muito raivosa, faz-me lembrar de ti. <br> Foste tu que me mostras-te, uma noite no Rodas junto com o Bertinho e o Ricardo",
        "music_link": "https://open.spotify.com/embed/track/17ZAZ24Eyh5fKqQ06u4R3d?utm_source=generator",  # Replace with another video
        "image": "pictures/day4.jpg"
    },
    # Make it wit you. 
    # Bed
    5: {
        "message": "Ao nível do sexo, não podia ser melhor Rui. Sinto-me sempre desejada. Dás-me tesão.",
        "music_link": "https://open.spotify.com/embed/track/6GyDY0yE47rfk8pcuKhioh?utm_source=generator",  # Replace with another video
        "image": "pictures/day5.jpg"
    },
    # Fly way from here
    6: {
        "message": "Objetivo de vida: preparar contigo 80% dos jantares que ainda vou ter na vida",
        "music_link": "https://open.spotify.com/embed/track/5PxQhGYkbGXzjOLaUfAYMf?utm_source=generator",  # Replace with another video
        "image": "pictures/day6.jpg"
    },
    # stuck in the middle with you
    7: {
        "message": "Para sempre 'STUCK IN THE MIDDLE WITH YOU'",
        "music_link": "https://open.spotify.com/embed/track/3Vby4nGmtbDo7HDJamOWkT?utm_source=generator",  
        "image": "pictures/day7.jpg"
    },
    # What is my mind
    8: {
        "message": "No jantar de Natal de 2023 eu dei-te boleia. <br> Tu ias à frente. Estava a tocar a minha playlist, e quando esta música começou tu cantaste o 'STOP'",
        "music_link": "https://open.spotify.com/embed/track/6mcxQ1Y3uQRU0IHsvdNLH1?utm_source=generator",  
        "image": "pictures/day8.jpg"
    },
    # Bad to the bone
    # Fotografia no quarto
    9: {
        "message": "Eu derreto mesmo, como o Olaf. <br> Não quis colocar aqui a outra entre mudas de roupa, mas era essa que eu queria",
        "music_link": "https://open.spotify.com/embed/track/6s0NHplywwr1IjnQpUpWJk?utm_source=generator",  
        "image": "pictures/day9.jpg"
    },
    # My girl's pussy
    # Eu
    10: {
        "message": "Vê lá a namorada que arranjaste. A dona da pussy que tanto gostas",
        "music_link": "https://open.spotify.com/embed/track/0jFFufzSe60jJ0XeksFy5J?utm_source=generator",  
        "image": "pictures/day10.jpg"
    },
    # Lilac Wine
    # 
    11: {
        "message": "Os teus lábios <br> <br> <br> PS.: Adorei acampar contigo. <br>Parece que já vai tão longe o Verão",
        "music_link": "https://open.spotify.com/embed/track/1StXVL5gClph4z4XzanYko?utm_source=generator",  
        "image": "pictures/day11.jpg"
    },
    # Cosmic Girl
    12: {
        "message": "Ouvimos Jamiroquai uma das nossas primeiras vezes, talvez na segunda ou terceira vez<br> Creio que ouve uma vez incluso onde tentaste colorar esta música a tocar <br> Mas eu não consegui estar contigo com esta música <br> Ia-me ficar na memória <br> Ficou",
        "music_link": "https://open.spotify.com/embed/track/2fiRJjWb9uk21Gva6oHpKs?utm_source=generator",  
        "image": "pictures/day12.jpg"
    },
    # Polly 
    13: {
        "message": "Fazes-me muito feliz mesmo <br> <br> <br> PS.: Esta música não é muito bonita <br> Quando era mais nova vi a história e ficou me marcada <br> Não era a minha música preferida (de longe), mas dizia-me alguma coisa",
        "music_link": "https://open.spotify.com/embed/track/2SJ38LDlkNjwWSUq98r4Q5?utm_source=generator",  
        "image": "videos/day13.mp4"
    },
    # Submarine 
    # Férias. A beiça.
    14: {
        "message": "Foi a recomendação de Junho 2024. <br> Gostei muito. Na altura ainda pensavas tatuar o submarino <br> <br> <br> PS.: A beiça da tua namorada",
        "music_link": "https://open.spotify.com/embed/track/5S3NpJBqacEUrxceiAy5lI?utm_source=generator",  
        "image": "pictures/day14.jpg"
    },
    # What you dont do 
    # Halloween
    15: {
        "message": "Alinhares nas minhas macacadas",
        "music_link": "https://open.spotify.com/embed/track/4mityPmJpqtHea3y9qZLg6?utm_source=generator",  
        "image": "pictures/day15.jpg",
        "message2": "I've been saving up my time <br> So I could spend it all on you <br> All I need is to see you smile"
    },
    # Dancing cheek to cheek
    # Jantar da Bea
    16: {
        "message": "O teu toque. Estou no céu",
        "music_link": "https://open.spotify.com/embed/track/5TNpCThzzXHEipXGKgNG8T?utm_source=generator",  
        "image": "pictures/day16.gif"
    },
    # Taras e manias
    # Careta Rui
    17: {
        "message": "A tua maturidade infantil",
        "music_link": "https://open.spotify.com/embed/track/3n1vpIDGakzAbo2p2etvhN?utm_source=generator",  
        "image": "pictures/day17.jpg"
    },
    # De gatas que eu gosto
    # Foto C+R
    18: {
        "message": "Alinhares na minha imaturidade infantil",
        "music_link": "https://open.spotify.com/embed/track/5eQofNuMVXMF07dzP5qBtN?utm_source=generator",  
        "image": "pictures/day18.jpg"
    },
    # I was made for loving you
    # Corrida
    19: {
        "message": "Por seres o yin do meu yang",
        "music_link": "https://open.spotify.com/embed/track/07q0QVgO56EorrSGHC48y3?utm_source=generator",  
        "image": "pictures/day19.jpg"
    },
    # I dont trust with loving you
    20: {
        "message": "Confio em ti com todo o meu coração",
        "music_link": "https://open.spotify.com/embed/track/7peh6LUcdNPcMdrSH4JPsM?utm_source=generator",  
        "image": "pictures/day20.jpg"
    },
    # Echo
    21: {
        "message": "A tua paciência para o mundo <br> <br> <br> PS.: qualquer semelhança com a realidade é pura coincidência",
        "music_link": "https://open.spotify.com/embed/track/3ypXaNibspfxvUIKpzUkfz?utm_source=generator",  
        "image": "pictures/day21.jpg"
    },
    # Everlong
    # screenshot Braga
    22: {
        "message": "A viagem de carro nas férias de verão 2023",
        "music_link": "https://open.spotify.com/embed/track/3QmesrvdbPjwf7i40nht1D?utm_source=generator",  
        "image": "pictures/day22.jpg"
    },
    # Emoji of a wave
    # Praia
    23: {
        "message": "Transmites-me paz",
        "music_link": "https://open.spotify.com/embed/track/5ddXMXmXZ2FN4iliTG20nO?utm_source=generator",  # Replace with another video
        "image": "pictures/day23.jpg"
    },
    # Secret smile
    # video
    24: {
        "message": "O teu olhar enche-me o coração <br> <br> <br> PS.: roubada da tua playlist",
        "music_link": "https://open.spotify.com/embed/track/1OhctVvuAU8kVCtzDWsCTj?utm_source=generator",  # Replace with another video
        "image": "videos/day24.mp4"
    },
    # Wildfire
    # eu natal
    25: {
        "message": "Os dois sabemos que nestas coisas toda a gente acha que vai durar para sempre <br> Eu não sei se vamos durar para sempre <br> Mas sei que quero que este conto de fadas tardio nunca acabe <br> Bom Natal meu fidalguinho",
        "music_link": "https://open.spotify.com/embed/track/0QTCTu0CXv4X1JEE4gNpGv?utm_source=generator",  # Replace with another video
        "image": "pictures/day25.jpg",
        "message2": "Like a wildfire",
    }  
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/day/<int:day>')
def show_day(day):
    today = datetime.now().day  # Get today's day of the month

    if day > today:
        # If the day is in the future, show a warning message
        warning_message = "Não sejas batoteiro!"
        warning_image = "pictures/warning.jpg"
        return render_template('day.html', day=day, warning_message=warning_message, warning_image=warning_image)
    content = DAILY_MESSAGES.get(day, {"message": "No content available for today.", "music_link": "#", "image": "pictures/default.jpg"})
    return render_template('day.html',day=day,message=content["message"],message2=content.get("message2"),music_link=content["music_link"],image=content.get("image"),video=content.get("video"), warning_message=None  # Pass video path if it exists
    )

if __name__ == '__main__':
    app.run(debug=True)

