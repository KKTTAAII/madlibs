from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story


app = Flask(__name__)
app.config['SECRET_KEY'] = 'eveiscool'
debug = DebugToolbarExtension(app)

texts = {
    'Once Upon A Time...': """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""",

    'My Love Story': """I fell in love with {noun} {adverb}. I {verb} {noun} every day.
    {noun} is my {adjective} lover""",

    'My myLocker...': """My gym locker stinks because I'm always leaving
    my dirty {Article Of Clothing (Plural)} in there!"""

}

words = {
    'Once Upon A Time...': [
        "place",
        "noun",
        "verb",
        "adjective",
        "plural_noun"],
    'My Love Story': [
        "noun",
        "adverb",
        "verb",
        "adjective"],
    'My myLocker...': ["Article Of Clothing (Plural)"]}


@app.route('/')
def select_template():
    return render_template('home.html')


@app.route('/storyform')
def story_form():
    select_template = request.args.get('template')
    word = words[select_template]
    return render_template(
        'storyform.html',
        select=select_template,
        words=word)


@app.route('/story')
def show_story():
    select_template = request.args.get('template')
    story = Story(words[select_template], texts[select_template])
    input_words = story.prompts
    ans = {}
    for w in input_words:
        ans[w] = request.args[w]
    my_story = story.generate(ans)
    return render_template(
        'story.html',
        story=my_story,
        template=select_template)
