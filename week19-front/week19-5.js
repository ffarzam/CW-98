let username = document.getElementById('uname');
let password = document.getElementById('psw');
let checkbox = document.getElementById('chk');



let username1 =getCookie("username")
let password1 =getCookie("password")
if(username1.length != 0)
 {
  location.href = "week19-5-1.html"
 }

document.getElementById("btn").addEventListener("click", myFunction)

function myFunction() {

  if( checkbox.checked ){

  setCookie("username", username, 10)
  setCookie("password", password, 10)
  }
}

function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  let expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}


function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
