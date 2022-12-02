/******* Student Name: Inars Birins, Student Nr:40504590 Edinburgh Napier Univerity *******/

let saveUserAvatar = localStorage.getItem("avatarImage");
let saveUsername = localStorage.getItem("clientUserName");
function setUserSetting(){
    document.getElementById("GameUsername").innerHTML='<h2>Username: '+saveUsername+' </h2>';
    document.getElementById("GameAvatar").innerHTML=`<img src='/static/img/avatar/${saveUserAvatar}'>`
};

/******* Student Name: Inars Birins, Student Nr:40504590 Edinburgh Napier Univerity *******/