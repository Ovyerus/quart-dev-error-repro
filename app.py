from quart import Quart

app = Quart('quart-dev-error-repro')
app.debug = True

@app.route('/')
async def root():
    return 'yes this is running'

@app.route('/test')
async def banana():
    return 'e'


@app.route('/woops')
async def badboy():
    raise Exception('uh oh')

@app.errorhandler(500)
def five_hundred():
    return 'oh no', 500

app.run()