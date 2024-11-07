from flask import Flask, render_template

app = Flask(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


# content per day
DAILY_MESSAGES = {
    1: {
        "message": "Here’s a tune to kick off the season!",
        "music_link": "https://open.spotify.com/embed/track/09gtDKL49tnLXMwN68D7JO?utm_source=generator"  # Replace with a valid YouTube embed link
    },
    2: {
        "message": "Enjoy this festive song for Day 2!",
        "music_link": "https://www.youtube.com/embed/YOUR_VIDEO_ID"  # Replace with another video
    },
    # Continue adding links for each day up to 25
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/day/<int:day>')
def show_day(day):
    content = DAILY_MESSAGES.get(day, {"message": "No content available for today.", "music_link": "#"})
    return render_template('day.html', day=day, message=content["message"], music_link=content["music_link"])


if __name__ == '__main__':
    app.run(debug=True)

