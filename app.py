from quart import Quart

app = Quart('quart-dev-error-repro')
app.debug = True

@app.route('/')
async def root():
    return 'yes this is running'

@app.route('/test')
async def banana():
    return 'e'

app.run(host="0.0.0.0")