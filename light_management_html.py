def webpage(states, temperature):
    # HTML Template for a form with 6 switches to conrol the LEDs
    led1 = states[0]
    led2 = states[1]
    led3 = states[2]
    led4 = states[3]
    led5 = states[4]
    led6 = states[5]
    temperature = temperature
    html = f"""
            <html lang="en" data-theme="light">
            <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="https://unpkg.com/@picocss/pico@1.*/css/pico.min.css">
            <script src="https://code.jquery.com/jquery-3.6.4.min.js" integrity="sha256-oP6HI9z1XaZNBrJURtCoUT5SUnxFr8s3BzRl+cbzUq8="
            crossorigin="anonymous"></script>
            <title>Document</title>
            </head>
            <body>
            <div class="container">
            <article>
            <h3>Smart Office Control</h3>
            <h4>Current Temperature: {temperature}</h4>
            <h5>Lighting Control:</h5>
            <form action="/" method="POST">
            <div class="grid">
             <div><label for="led1_switch">
             <input class="switch" type="checkbox" id="led1_switch" name="led1_switch" value="true"  role="switch"{"checked" if led1=="true" else '' }>LED 1</label>
              </div><div><label for="led2_switch"><input class="switch" type="checkbox" id="led2_switch" name="led2_switch" value="true" role="switch" {"checked" if led2=="true" else '' }>LED 2</label>
              </div> <div><label for="led3_switch">
              <input class="switch" type="checkbox" id="led3_switch" name="led3_switch" value="true" role="switch" {"checked" if
                                            led3=="true" else '' }>
                                        LED 3
                                    </label>
                                </div>
                                <div>
                                    <label for="led4_switch">
                                        <input class="switch" type="checkbox" id="led4_switch" name="led4_switch" value="true" role="switch" {"checked" if
                                            led4=="true" else '' }>
                                        LED 4
                                    </label>
                                </div>
                                <div>
                                    <label for="led5_switch">
                                        <input class="switch" type="checkbox" id="led5_switch" name="led5_switch" value="true" role="switch" {"checked" if
                                            led5=="true" else '' }>
                                        LED 5
                                    </label>
                                </div>
                                <div>
                                    <label for="led6_switch">
                                        <input class="switch" type="checkbox" id="led6_switch" name="led6_switch" value="true"  role="switch"{"checked" if
                                            led6=="true" else '' }>
                                        LED 6
                                    </label>
                                </div>
                            </div>
                            <br>
                        </form>
                        <div class="container">
                            <article>
                                <h3>Current LED Status:</h3>
                                <p><kbd>LED 1</kbd> : { "<ins>ON</ins>" if led1 == "true" else "<deleted>OFF</deleted>"}</p>
                                <p><kbd>LED 2</kbd> : { "<ins>ON</ins>" if led2 == "true" else "<deleted>OFF</deleted>"}</p>
                                <p><kbd>LED 3</kbd> : { "<ins>ON</ins>" if led3 == "true" else "<deleted>OFF</deleted>"}</p>
                                <p><kbd>LED 4</kbd> : { "<ins>ON</ins>" if led4 == "true" else "<deleted>OFF</deleted>"}</p>
                                <p><kbd>LED 5</kbd> : { "<ins>ON</ins>" if led5 == "true" else "<deleted>OFF</deleted>"}</p>
                                <p><kbd>LED 6</kbd> : { "<ins>ON</ins>" if led6 == "true" else "<deleted>OFF</deleted>"}</p>
                            </article>
                        </div>
                    </article>
                </div>
                <script>
                    $(document).ready(function () {{
                        $.get("/leds", function (data) {{
                            // Set the initial switch values based on the current LED states
                            var states = JSON.parse(data);
                            $("#led1_switch").prop("checked", states[0] == "true");
                            $("#led2_switch").prop("checked", states[1] == "true");
                            $("#led3_switch").prop("checked", states[2] == "true");
                            $("#led4_switch").prop("checked", states[3] == "true");
                            $("#led5_switch").prop("checked", states[4] == "true");
                            $("#led6_switch").prop("checked", states[5] == "true");
                        }});
                        $(".switch").change(function () {{
                            var led_states = [];
                            led_states.push("led1=" + ($("#led1_witch").is(":checked") ? "true" : "false"));
                            led_states.push("led2=" + ($("#led2_switch").is(":checked") ? "true" : "false"));
                            led_states.push("led3=" + ($("#led3_switch").is(":checked") ? "true" : "false"));
                            led_states.push("led4=" + ($("#led4_switch").is(":checked") ? "true" : "false"));
                            console.log(led_states.join("&\"));
                            $.post("/", led_states.join("&"));
                            console.log("switched")
                        }});
                    }});
                </script>
            </body>
            </html>
             """
    return str(html)
