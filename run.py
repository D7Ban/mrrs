from mrrs import app

app.debug = True
app.secret_key = 'hahah'

if __name__ == '__main__':
    app.run()
