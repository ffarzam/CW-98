let p = document.getElementById("demo")

document.getElementById("btn").addEventListener("click", myFunction)

function myFunction() {

  if(p.style.display == "none"){

  p.style.display = "block";
  }

  else {
  p.style.display = "none";
  }
}
