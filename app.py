from flask import Flask, render_template

app = Flask(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


# content per day
DAILY_MESSAGES = {
    1: {
        "message": "Juro que não tenho palavras para descrever a panóplia de emoções que despoltas em mim. Mas nos próximos 25 dias vou me esforçar, muito.<br> <br>Para o primeiro dia vou começar por salientar o quão especial me fazes sentir.<br><br> Fazes-me sentir uma boneca",
        "music_link": "https://open.spotify.com/embed/track/735rjks7kQgWCjTQlIHMuH?utm_source=generator",  # Replace with a valid YouTube embed link
        "image": "pictures/day1.jpg"
    },
    2: {
        "message": "Foste a maior surpresa da minha vida<br>Não esperava que alguém fosse aparecer na minha vida assim <br>Alguém que me faz tão feliz<br>Alguém em quem eu acredito tanto <br>Continuas a ser uma surpresa todos os dias",
        "music_link": "https://open.spotify.com/embed/track/1A5V1sxyCLpKJezp75tUXn?utm_source=generator",  # Replace with another video
        "image": "pictures/day2.jpg"
    },
    3: {
        "message": "O teu olhar enche-me o coração",
        "music_link": "https://open.spotify.com/embed/track/1OhctVvuAU8kVCtzDWsCTj?utm_source=generator",  # Replace with another video
        "image": "videos/day24.mp4"
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

