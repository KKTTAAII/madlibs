from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)
app.config['SECRET_KEY'] = 'eveiscool'
debug = DebugToolbarExtension(app)

texts = {
    'onceUponATime': """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
    
    'loveStory': """I fell in love with {noun} {adverb}. I {verb} {noun} every day. 
    {noun} is my {adjective} lover""",

    'myLocker': """My gym locker stinks because I'm always leaving 
    my dirty {Article Of Clothing (Plural)} in there!"""

}

words = {
    'onceUponATime': ["place", "noun", "verb", "adjective", "plural_noun"],
    'loveStory': ["noun", "adverb", "verb", "adjective"],
    'myLocker': ["Article Of Clothing (Plural)"]
}



@app.route('/')
def select_template():
    return render_template('home.html')

@app.route('/storyform')
def story_form():
    words = story.prompts
    return render_template('storyform.html', words=words)

@app.route('/story')
def show_story():
    words = story.prompts
    ans = {}
    for w in words:
        ans[w] = request.args[w]
    my_story = story.generate(ans)
    return render_template('story.html', story=my_story)