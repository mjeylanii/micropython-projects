def webpage(states, temperature, css, javascript):
    # HTML Template for a form with 6 switches to conrol the LEDs
    yield '<!DOCTYPE html><html lang="en" data-theme="light">'
    yield  '<head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge">'
    yield '<meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="stylesheet" href="https://unpkg.com/@picocss/pico@1.*/css/pico.min.css">'
    yield '<script src="https://code.jquery.com/jquery-3.6.4.min.js" integrity="sha256-oP6HI9z1XaZNBrJURtCoUT5SUnxFr8s3BzRl+cbzUq8=" crossorigin="anonymous"></script>'
    yield f"""<title>Document</title><style>{css}</style></head>"""
    yield f"""<body> <div class="container"><article><body><div class="container"><h3>Smart Office Control</h3></div>"""
    yield f"""<h4>Current Temperature: {temperature}°C</h4>"""
    yield  '<fieldset class="checkbox-group"><legend class="checkbox-group-legend">Lighting control</legend>'
    for i, state in enumerate(states):
        yield f"""<div class="checkbox"><label class="checkbox-wrapper"><input id={"checkbox-" + str(i+1)} type="checkbox" class="checkbox-input" {"checked" if state=="true" else '' } /><span class="checkbox-tile"> <span class="checkbox-icon"><svg fill="#00000" height="200px" width="200px" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                viewBox="0 0 512 512" xml:space="preserve">
                <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                <g id="SVGRepo_iconCarrier">
                </g><g><path d="M256,0C157.885,0,78.063,79.822,78.063,177.936c0,46.98,18.144,91.296,51.088,124.784l2.627,2.664 c12.84,13.511,22.519,29.458,28.548,46.871l-0.592,0.372c-11.394,7.163-18.198,19.455-18.198,32.875 c0,13.279,6.624,25.167,17.105,32.202c-0.923,3.334-1.422,6.809-1.422,10.357c0,21.417,17.424,38.841,38.841,38.841h3.793 C205.545,492.665,228.551,512,256,512s50.455-19.336,56.147-45.099h3.793c21.417,0,38.841-17.424,38.841-38.841 c0-3.548-0.499-7.023-1.422-10.357c10.482-7.034,17.105-18.923,17.105-32.202c0-13.42-6.802-25.711-18.198-32.875l-0.592-0.372 c6.005-17.348,15.634-33.24,28.405-46.719l2.77-2.816c32.945-33.487,51.088-77.803,51.088-124.784C433.937,79.822,354.115,0,256,0 z M256,481.583c-10.465,0-19.562-5.964-24.074-14.671h48.147C275.563,475.619,266.466,481.583,256,481.583z M315.94,436.483 h-2.429v-0.105l-15.313,0.105h-84.371l-15.337-0.205v0.205h-2.429c-4.645,0-8.424-3.779-8.424-8.424 c0-1.561,0.433-3.064,1.22-4.363h134.287c0.787,1.298,1.22,2.801,1.22,4.363C324.364,432.705,320.585,436.483,315.94,436.483z M334.822,393.281h-0.966H178.145h-0.966c-3.133-1.27-5.226-4.306-5.226-7.779c0-1.745,0.538-3.405,1.51-4.792h165.075 c0.971,1.386,1.51,3.047,1.51,4.792C340.048,388.974,337.955,392.01,334.822,393.281z M239.773,350.293v-90.148h32.453v90.148 H239.773z M362.011,280.522l-0.749,0.747c-19.394,19.326-33.376,42.992-40.879,69.024h-17.738v-90.148h9.559 c22.043,0,39.976-17.934,39.976-39.977c0-22.042-17.934-39.976-39.976-39.976c-22.042,0-39.976,17.934-39.976,39.976v9.56h-32.453 v-9.56c0-22.042-17.934-39.976-39.976-39.976s-39.976,17.934-39.976,39.976c0,22.043,17.934,39.977,39.976,39.977h9.559v90.148 h-17.738c-7.503-26.033-21.486-49.699-40.88-69.024l-0.71-0.706c-26.802-27.663-41.549-64.064-41.549-102.628 c0-81.342,66.177-147.518,147.519-147.518S403.52,96.594,403.52,177.936C403.52,216.481,388.787,252.864,362.011,280.522z M302.644,229.728v-9.56c0-5.27,4.288-9.559,9.559-9.559s9.559,4.288,9.559,9.559s-4.288,9.56-9.559,9.56H302.644z M209.356,220.168v9.56h-9.559c-5.271,0-9.559-4.288-9.559-9.56c0-5.27,4.288-9.559,9.559-9.559S209.356,214.897,209.356,220.168z ">
                </path></g></g></g></svg></span><span class="checkbox-label">{"LED" + " " + str(i+1)}</span></span></label>
                </div>
                """
    yield  '</fieldset></body></article>'
    yield '</div>'
    yield f"""
          <script type="text/javascript">
          {javascript}
          </script>
    """