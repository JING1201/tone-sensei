var userScore = 0;
function scoreKeeper() {
    var isRight = true;
    if(isRight){
        alert('Correct!');
        userScore+=25;
        document.getElementById("score-container").innerHTML = userScore;
    }
    else{
        alert('Sorry, incorrect!');
    }
}

document.getElementById("submitButton").onclick = scoreKeeper;