document.addEventListener("DOMContentLoaded", function () {
  var checkboxes = document.querySelectorAll(".checkbox-input");
  for (var i = 0; i < checkboxes.length; i++) {
    checkboxes[i].addEventListener("change", function () {
      var led_states = [];
      led_states.push(
        "led1=" +
          (document.querySelector("#checkbox-1").checked ? "true" : "false")
      );
      led_states.push(
        "led2=" +
          (document.querySelector("#checkbox-2").checked ? "true" : "false")
      );
      led_states.push(
        "led3=" +
          (document.querySelector("#checkbox-3").checked ? "true" : "false")
      );
      led_states.push(
        "led4=" +
          (document.querySelector("#checkbox-4").checked ? "true" : "false")
      );
      led_states.push(
        "led5=" +
          (document.querySelector("#checkbox-5").checked ? "true" : "false")
      );
      led_states.push(
        "led6=" +
          (document.querySelector("#checkbox-6").checked ? "true" : "false")
      );
      led_states.push(
        "led7=" +
          (document.querySelector("#checkbox-7").checked ? "true" : "false")
      );
      console.log(led_states.join("&"));
      var xhr = new XMLHttpRequest();
      xhr.open("POST", "/");
      xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
      xhr.send(led_states.join("&"));
      console.log("switched");
    });
  }
});
