from website import create_app


# Starting up the flask app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

