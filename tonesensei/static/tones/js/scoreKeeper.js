var userScore = 0;
var isRight = true;
function scoreKeeper() {
    
    if(isRight){
        alert('Correct!');
        userScore+=25;
        document.getElementById("score-container").innerHTML = userScore;
    }
    else{
        alert('Sorry, incorrect!');
    }
    var x = Math.floor(Math.random() * 10);
    if( x % 2 == 0){
    	isRight = false;
    }
}

document.getElementById("submitButton").onclick = scoreKeeper;