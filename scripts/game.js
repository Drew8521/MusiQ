let countdownEnding = Date.now()+60000;
let startTime = Date.now();

  let countdown = setInterval(countDown, 1000);

  function countDown()
  {
    let timeLeft = countdownEnding - Date.now();
    console.log(timeLeft);
    let days = Math.floor(timeLeft / (1000*60*60*24));
    let hours = Math.floor(timeLeft % (1000*60*60*24) / (1000*60*60));
    let minutes = Math.floor(timeLeft % (1000*60*60) / (1000*60));
    let seconds = Math.floor((timeLeft+10) % (1000*60) / (1000));
    document.getElementById("timer").innerHTML = seconds + "s";

    if (timeLeft<0)
    {
      clearInterval(countDown);
      document.getElementById("timer").innerHTML = "GAME OVER BITCH";
    }
  }

console.log(startTime);