     /*  AVATAR CREATE SECTION Variables */
     const avatar = ["avatar1.png","avatar2.png","avatar3.png","avatar4.png","avatar5.png","avatar6.png","avatar7.png","avatar8.png",];
     let randVal; //Randomizer variable.
     let goBack=8; // Variable for moving avatar image back
     let goNext=-1; // Variable for moving avatar image front
     let newAvatarSet; // Variable for set avatar inage which will see user on the screen
     let avatarChoise=newAvatarSet; // variable for check which avatar is right now active.
     let userAvatarChoise=document.getElementById('setAvatar');// variable for save Avatar;  
     let saveAvatarChoise; // Variable for save user choise.





/* BEGINING USERNAME CREATE SECTION */
             //enter user name variable
             let saveUserName
             function createUserName(){
                 let userName=document.getElementById('userNameData').value;
                 var infoText = document.getElementById("infoUser");
                 let systemUserName;
                //  console.log(userName);
                 if (userName===""){
                   randNameNumber1= Math.floor(Math.random()*9);
                   randNameNumber2= Math.floor(Math.random()*9);
                   randNameNumber3= Math.floor(Math.random()*9);
                   randNameNumber4= Math.floor(Math.random()*9);
                   systemUserName= `PlayerNr${randNameNumber1}${randNameNumber2}${randNameNumber3}${randNameNumber4}`
                   infoText.innerHTML=`<p style="color: darkred;"> Sorry you do not enter your <b>Username</b>, 
                   a system generate for you username - <b>${systemUserName}</b>,<br/> if you want your name 
                   then please Enter again username and press Save Username. Thank you! </p> `;
                   saveUserName=systemUserName;
                 } else{
                   infoText.innerHTML=`<p> Your username is ==> <b>${userName}</b></p>`;
                   saveUserName=userName;
                   let cleanInputbox = document.querySelectorAll('input[type=text]');
                   for (i = 0; i < cleanInputbox.length; i++) {
                     cleanInputbox[i].value = "";
                    };
                 };
                //  console.log(saveUserName);
               };//end function
             /* END USERNAME CREATE SECTION */


             
   
      /// begining randomizer function. 
  function randomAvatar(){
            let checkAvatar=avatar[randVal];
            randVal= Math.floor(Math.random()*avatar.length);
            ///// if randomizer will create this same index, it will be add up one index higher.
            if(checkAvatar=== avatar[randVal]){
                avatar[randVal+=1];
                newAvatarSet=avatar[randVal];
                //// if index is higer than avatar.length then it will create for one index lower. 
                  if(avatar[randVal]=== undefined){
                    avatar[randVal-=1];
                    newAvatarSet=avatar[randVal];
                    document.getElementById("showAvatar").innerHTML=`<img src="/static/img/avatar/${newAvatarSet}">`;
                    console.log(`third console.log ${avatar[randVal]}`);
                  };
                  document.getElementById("showAvatar").innerHTML=`<img src="/static/img/avatar/${newAvatarSet}">`; 
            };
            newAvatarSet=avatar[randVal];
            document.getElementById("showAvatar").innerHTML=`<img src="/static/img/avatar/${newAvatarSet}">`;
  };/// END RANDOMIZER FUNCTION

      /// begining button PREVIOUS function. 
     /********************************************
    When the user presses the button "previous", the function first checks
    did the user already used the randomizer if NO then second check if the 
    user uses the "next" button. After that function starts to use a correct 
    index, which allow the user to move back from the object where he stop before. 
      ********************************************/
  function moveBack(){
              if(randVal=== undefined){
                  if(avatarChoise=== undefined){
                    goBack--;
                    newAvatarSet=avatar[goBack];
                    document.getElementById("showAvatar").innerHTML=`<img src="/static/img/avatar/${newAvatarSet}">`;
                       //if it is last image then next images will have last one in Array list.
                    if(goBack<=0){
                          goBack=8;
                          document.getElementById("showAvatar").innerHTML=`<img src="/static/img/avatar/${newAvatarSet}">`;
                        };// end if statment where index is less than 0
                  }else{
                    goBack=avatarChoise;
                    goBack--;
                    newAvatarSet= avatar[goBack];
                    document.getElementById("showAvatar").innerHTML=`<img src="/static/img/avatar/${newAvatarSet}">`;
                        if(goBack<=0){
                          goBack=8;
                          document.getElementById("showAvatar").innerHTML=`<img src="/static/img/avatar/${newAvatarSet}">`;
                        };// end if statment where index is less than 0
                  }; 
              }else {
                randVal--;
                  newAvatarSet= avatar[randVal];
                  document.getElementById("showAvatar").innerHTML=`<img src="/static/img/avatar/${newAvatarSet}">`;
                    if(randVal<=0){
                      randVal= 8;
                      document.getElementById("showAvatar").innerHTML=`<img src="/static/img/avatar/${newAvatarSet}">`;
                    };
              };
            };
 /// End previous button function

        /// begining button NEXT function. 
      /********************************************
      When the user presses the button "next", the function first checks
      did the user already used the randomizer if NO then second check if the 
      user uses the "previous" button. After that function starts to use a correct 
      index, which allow the user to move back from the object where he stop before. 
        ********************************************/
 function moveFront(){
              if(randVal=== undefined){
                  if(avatarChoise=== undefined){
                    goNext++;
                    newAvatarSet=avatar[goNext];
                    document.getElementById("showAvatar").innerHTML=`<img src="/static/img/avatar/${newAvatarSet}">`;
                        if(goNext>=7){
                          goNext=-1;
                          document.getElementById("showAvatar").innerHTML=`<img src="/static/img/avatar/${newAvatarSet}">`;
                        };
                  }else{
                    goNext=avatarChoise;
                    goNext++;
                    newAvatarSet= avatar[goNext];
                    document.getElementById("showAvatar").innerHTML=`<img src="/static/img/avatar/${newAvatarSet}">`;
                        if(goNext>=7){
                          goNext=0;
                          document.getElementById("showAvatar").innerHTML=`<img src="/static/img/avatar/${newAvatarSet}">`;
                        };
                  };
              }else {
                  randVal++;
                  newAvatarSet= avatar[randVal];
                  document.getElementById("showAvatar").innerHTML=`<img src="/static/img/avatar/${newAvatarSet}">`;
                    if(randVal>=7){
                      randVal= 0;
                      document.getElementById("showAvatar").innerHTML=`<img src="/static/img/avatar/${newAvatarSet}">`;
                    };
              };
            };
 /// End previous button function

            /*************** Save AVATAR Image ***************/
  function saveAvatar(){
                if (newAvatarSet===undefined){
                  saveAvatarChoise=avatar[3];
                  document.getElementById('avatarText').innerHTML="Your Avatar";
                  userAvatarChoise.innerHTML=`<img src="/static/img/avatar/avatar4.png">`;
                }else{
                  saveAvatarChoise=newAvatarSet;
                document.getElementById('avatarText').innerHTML="Your Avatar";
                userAvatarChoise.innerHTML=`<img src="{{url_for('static', filename='img/avatar/${newAvatarSet}')}}">`;
              };
             }; //End if statment
              // console.log(userAvatarChoise);
        //End function

            /*************** END Save function ***************/
                /* END AVATAR CREATE TASKS */

        /* END USER BACKGROUND CREATE SECTION */
//////////////////////////   Data Base SECTION   //////////////////////////
function startGame(){
  let userReady=confirm("Do you ready Start a game?");
  if(userReady=== true){
    localStorage.clear();
    
    if(newAvatarSet===undefined){
        saveAvatarChoise=avatarChoise;
      };
    if(saveUserName === undefined){
          createUserName();
         };// end if statment Avatar undefined. 
    // localStorage.setItem("clientUserName",saveUserName);  
    // localStorage.setItem("avatarImage",saveAvatarChoise);
    // console.log("Local DATABASE information "+saveUserName+" "+backGroundColour+" "+saveAvatarChoise);
    window.location.href="/quest/";
  }else{
    alert("Ouu... don't worry, start when you are ready.")
  };
};//if statment end.
/******** //////  END Data Base section   //// ********/ 
