let userInput = prompt("write here:");

if (userInput === "false" || userInput === "true"){
    alert('boolean')
}

else if (userInput == null || userInput == ""){
    alert("null")
}

else if (!isNaN(userInput)){
    alert("number")
}

else {
    alert("string")
}