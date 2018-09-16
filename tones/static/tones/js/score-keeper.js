// // My methodology here is totally different, since I directly get the element I care about
// function checkscript() {
//     // find the element in the DOM
//     var box = document.getElementById("fillIn");
//     var score = document.getElementById("score-container")
//     // check for a value
//     if (box.value) {
//          document.getElementById("score-container").innerHTML = box.value;
//     } else {
//         alert('You haven\'t filled in ' + box.name + '!');
//         box.focus()
//         // No returns necessary, since we're not dealing with formsubmittal.
//     }
// }

// document.getElementById("button").onclick = checkscript;




// My methodology here is totally different, since I directly get the element I care about
function scoreKeeper() {
    // find the element in the DOM
    var box = document.getElementById("fillIn");
    var score = document.getElementById("score-container")
    // check for a value
    if (box.value) {
         document.getElementById("score-container").innerHTML = box.value;
    } else {
        alert('You haven\'t filled in ' + box.name + '!');
        box.focus()
        // No returns necessary, since we're not dealing with formsubmittal.
    }
}

document.getElementById("button").onclick = scoreKeeper;