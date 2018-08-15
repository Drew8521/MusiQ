let countdownEnding = Date.now()+240000;
let startTime = Date.now();

const menu = document.getElementById('button');
menu.addEventListener('click', exit);
function exit(event) {
  location.href='/profile';
  }

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
      document.getElementById("timer").innerHTML = "GAME OVER";
      window.location.replace("/end-game");

    }
  }


const userAnswer = document.getElementById('answer');

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
async function check() {
  if (userAnswer.value == "word") {
    document.getElementById('question-right').innerHTML = "Wow You Have Done It!";
    document.getElementById("question-right").style.opacity = "1";
    userAnswer.value = "";
    await sleep(1000);
    document.getElementById("question-right").style.opacity = "0";
  }
}
