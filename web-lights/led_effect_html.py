def webpage(temperature, state):
    # Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <head><link rel="stylesheet" href="https://unpkg.com/@picocss/pico@1.*/css/pico.min.css"></head>
            <body>
            <div class=container>
            <article>
            <form action="./waves">
            <input type="submit" value="Waves" />
            </form>
            <form action="./left-right">
            <input type="submit" value="Left_Right" />
            </form>
            <p>LED is {state}</p>
            <p>Temperature is {temperature}</p>
            </article>
            <article>
             Loading images from the server...
            </article
            </div>
            </body>
            </html>
            """
    return str(html)
