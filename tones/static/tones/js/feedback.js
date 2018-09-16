
// My methodology here is totally different, since I directly get the element I care about
function feedback() {
    // find the element in the DOM
    var isRight = false;
    // check for a value
    if(isRight){
         alert('Correct!');
            box.focus();
    }
    else{
        alert('Sorry, incorrect!');
            box.focus();
    }
       
}

document.getElementById("submitButton").onclick = feedback;