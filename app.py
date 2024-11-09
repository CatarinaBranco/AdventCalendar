from flask import Flask, render_template

app = Flask(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


# content per day
DAILY_MESSAGES = {
    # head over feet. doll picture
    1: {
        "message": "Juro que não tenho palavras para descrever a panóplia de emoções que despoltas em mim. Mas nos próximos 25 dias vou me esforçar, muito.<br> <br>Para o primeiro dia vou começar por salientar o quão especial me fazes sentir.<br><br> Fazes-me sentir uma boneca. Esta música faz-me pensar isso.",
        "music_link": "https://open.spotify.com/embed/track/735rjks7kQgWCjTQlIHMuH?utm_source=generator",  # Replace with a valid YouTube embed link
        "image": "pictures/day1.jpg"
    },
    # closing time. Amarante's picture
    2: {
        "message": "Foste a maior surpresa da minha vida<br>Não esperava que alguém fosse aparecer na minha vida assim <br>Alguém que me faz tão feliz<br>Alguém em quem eu acredito tanto <br>Continuas a ser uma surpresa todos os dias",
        "music_link": "https://open.spotify.com/embed/track/1A5V1sxyCLpKJezp75tUXn?utm_source=generator",  # Replace with another video
        "image": "pictures/day2.jpg"
    },
    # Let's do it. 
    3: {
        "message": "Antes, quando ouvia esta música deixava-me a pensar se devia deixar andar ou não <br> Escolhi bem ",
        "music_link": "https://open.spotify.com/embed/track/4Od7rEL8ehrcRr38g86OMm?utm_source=generator",  # Replace with another video
        "image": "pictures/xxx.jpg"
    },
    # Ought know
    4: {
        "message": "Ainda que uma música muito raivosa, faz-me lembrar de ti. Foste tu que ma mostras-te, uma noite no Rodas junto com o Bertinho e o Ricardo",
        "music_link": "https://open.spotify.com/embed/track/4Od7rEL8ehrcRr38g86OMm?utm_source=generator",  # Replace with another video
        "image": "pictures/xxx.jpg"
    },
    # Make it wit you. Bed
    5: {
        "message": "Ao nível do sexo, não podia ser melhor Rui. Sinto-me sempre desejada. Dás-me tesão.",
        "music_link": "https://open.spotify.com/embed/track/6GyDY0yE47rfk8pcuKhioh?utm_source=generator",  # Replace with another video
        "image": "pictures/day5.jpg"
    },
    # Fly way from here
    6: {
        "message": "Ouvia mutio esta música há uns anos. Eu não tenho uma favorita, mas gostava muito desta",
        "music_link": "https://open.spotify.com/embed/track/1OxcIUqVmVYxT6427tbhDW?utm_source=generator",  # Replace with another video
        "image": "pictures/day6.jpg"
    },
    # stuck in the middle with you
    7: {
        "message": "",
        "music_link": "",  
        "image": "pictures/day7.jpg"
    },
    # What's in your mind
    8: {
        "message": "No jantar de Natal de 2023 eu dei-te boleia. Tu ias à frente. Estava a tocar a minha playlist, e quando esta música começou tu cantaste o 'STOP'",
        "music_link": "",  
        "image": "pictures/day8.jpg"
    },
    # Bad to the bone
    9: {
        "message": "Eu derreto mesmo, como o Olaf. <br> Não quis colocar aqui a outra entre mudas de roupa, mas era essa que eu queria",
        "music_link": "https://open.spotify.com/embed/track/6s0NHplywwr1IjnQpUpWJk?utm_source=generator",  
        "image": "pictures/day9.jpg"
    },
    
    24: {
        "message": "O teu olhar enche-me o coração",
        "music_link": "https://open.spotify.com/embed/track/1OhctVvuAU8kVCtzDWsCTj?utm_source=generator",  # Replace with another video
        "image": "videos/day24.mp4"
    },
    25: {
        "message": "Os dois sabemos que nestas coisas toda a gente acha que vai durar para sempre <br> Eu nao sei se vamos durar para sempre <br> Mas sei que quero que este conto de fadas tardio nunca acabe <br> Bom Natal meu fidalguinho",
        "music_link": "https://open.spotify.com/embed/track/0QTCTu0CXv4X1JEE4gNpGv?utm_source=generator",  # Replace with another video
        "image": "pictures/xxx.jpg",
        "message2": "You and me been catching on <br> Like a wildfire",
    }    
    # Continue adding links for each day up to 25
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/day/<int:day>')
def show_day(day):
    content = DAILY_MESSAGES.get(day, {"message": "No content available for today.", "music_link": "#", "image": "pictures/default.jpg"})
    return render_template('day.html',day=day,message=content["message"],message2=content.get("message2"),music_link=content["music_link"],image=content.get("image"),video=content.get("video")  # Pass video path if it exists
    )


if __name__ == '__main__':
    app.run(debug=True)

