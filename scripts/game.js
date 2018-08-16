let countdownEnding = Date.now()+10000;
let startTime = Date.now();
let score = 0;
let randomCompliment = Math.floor((Math.random() * 7))
let responses = ["Music is your forte!", "A high note!", "Blast it!", "Killed it!", "Sick!", "MusIQ off the Charts!", "Impressive!"];

const menu = document.getElementById('button');
menu.addEventListener('click', exit);
function exit(event) {
  location.href='/profile';
  }

  let countdown = setInterval(countDown, 1000);
  function countDown()
  {
    let timeLeft = countdownEnding - Date.now();
    let days = Math.floor(timeLeft / (1000*60*60*24));
    let hours = Math.floor(timeLeft % (1000*60*60*24) / (1000*60*60));
    let minutes = Math.floor(timeLeft % (1000*60*60) / (1000*60));
    let seconds = Math.floor((timeLeft+10) % (1000*60) / (1000));
    document.getElementById("timer").innerHTML = seconds;

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
<<<<<<< HEAD
  if (userAnswer.value.toLowerCase() === document.getElementById("artist").innerHTML) {
    document.getElementById('question-right').innerHTML = "Wow You Have Done It!";
=======
  if (userAnswer.value === document.getElementById("artist").innerHTML) {
    randomCompliment = Math.floor((Math.random() * 7))
    document.getElementById('question-right').innerHTML = responses[randomCompliment];
>>>>>>> 6fcbac2437639617b19c6c1250d1229f61252e6e
    document.getElementById("question-right").style.opacity = "1";
    userAnswer.value = "";
    score += 1;
    console.log(score);
    fetch(`/update-score?new=${score}`);
    await sleep(1000);
    document.getElementById("question-right").style.opacity = "0";
<<<<<<< HEAD
    fetch(`/game`)
=======
>>>>>>> 6fcbac2437639617b19c6c1250d1229f61252e6e

  }
}
