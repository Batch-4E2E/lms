
function sendOTP(){
    const email = document.getElementById('floatingInput');
    let mail=email.value.toLowerCase();

    $.ajax({
        type: "POST",
        url: "/verify",
        data: {"mail":mail}
    })
    .done(function( response ) {
        if(response.message=="exists") {
            email.value="";
        
            alert("User already exists");
        }
       else{
    const otpverify = document.getElementsByClassName('otpverify')[0];
    otpbutton=document.getElementsByClassName("otpbutton")[0];
    const floatingform = document.getElementsByClassName("floatingform")[0];
    let otp_val = Math.floor(Math.random()*10000);
    // let emailbody = `
    //     <h1>Your Verification Code</h1> <br>
    //     <h2>Your OTP is </h2>${otp_val}
    // `;

    emailjs.init("KNP4f0ozaRaaQsdzD");

    // Send email
        var params = {
            to_email: mail,
            from_name: "VVIT LMS BOT",
            message: "Verify your account with"+otp_val,
            to_name: mail.match(/(.*)@/)[1],

        };
        

        // Send the email
        emailjs.send("service_nnwjrro", "template_3b7cmt4", params)
            .then(function(response) {
                alert("OTP sent to your email "+email.value+otp_val);
                otpverify.style.display = "block";
            otpbutton.style.display="none";
            email.readOnly=true;
            const otp_inp = document.getElementById('otp_inp');
            const otp_btn = document.getElementById('otp-btn');
            otp_btn.addEventListener('click',()=>{
                // now check whether sent email is valid
                otpbutton.style.display="none";
                if(otp_inp.value == otp_val){
                    otpverify.style.display = "none";
                    floatingform.style.display = "block";
                    $.ajax({
                        type: "POST",
                        url: "/clear",
                        data: {"mail":mail}
                    })
                }
                else{
                    alert("Invalid OTP");
                }
            })
            }, function(error) {
                console.error("Email sending failed:", error);
                alert("Email sending failed!");
            });
    }
    // Email.send({
    //     SecureToken :  "1a96ed32-a352-402e-9855-de08cc17f852",
    //     To :mail,
    //     From : "lmsvvit@gmail.com",
    //     Subject : "",
    //     Body : emailbody
    // }).then(
    //   function(message) {
    //     if(message === "OK"){
    //         alert("OTP sent to your email "+email.value+otp_val);

    //         // now making otp input visible
    //         otpverify.style.display = "block";
    //         otpbutton.style.display="none";
    //         email.readOnly=true;
    //         const otp_inp = document.getElementById('otp_inp');
        //     const otp_btn = document.getElementById('otp-btn');

        //     otp_btn.addEventListener('click',()=>{
        //         // now check whether sent email is valid
        //         if(otp_inp.value == otp_val){
        //             otpverify.style.display = "none";
        //             floatingform.style.display = "block";
        //             $.ajax({
        //                 type: "POST",
        //                 url: "/clear",
        //                 data: {"mail":mail}
        //             })
        //         }
        //         else{
        //             alert("Invalid OTP");
        //         }
        //     })
        // }
    //     else{
    //         alert("Error in sending otp");
    //     }

    //   }
    // );

});
}
function forgotsendOTP(){
    const email = document.getElementById('floatingInput');
    let mail=email.value.toLowerCase();
    $.ajax({
        type: "POST",
        url: "/verify",
        data: {"mail":mail}
    })
    .done(function( response ) {
        if (response.message!="ok"){

    const otpverify = document.getElementsByClassName('otpverify')[0];
    const otpbutton=document.getElementsByClassName("otpbutton")[0];
    const floatingform = document.getElementsByClassName("floatingform")[0];
    let otp_val = Math.floor(Math.random()*10000);
    let emailbody = `
        <h1>Your Verification Code</h1> <br>
        <h2>Your OTP is </h2>${otp_val}
    `;


    Email.send({
        SecureToken :  "1a96ed32-a352-402e-9855-de08cc17f852",
        To :mail,
        From : "lmsvvit@gmail.com",
        Subject : "This is the subject",
        Body : emailbody
    }).then(
      function(message) {
        if(message === "OK"){
            alert("OTP sent to your email "+email.value+otp_val);

            // now making otp input visible
            otpverify.style.display = "block";
            otpbutton.style.display="none";
            email.readOnly=true;
            const otp_inp = document.getElementById('otp_inp');
            const otp_btn = document.getElementById('otp-btn');

            otp_btn.addEventListener('click',()=>{
                // now check whether sent email is valid
                if(otp_inp.value == otp_val){
                    otpverify.style.display = "none";
                    floatingform.style.display = "block";
                }
                else{
                    alert("Invalid OTP");
                }
            })
        }
        else{
            alert("Error in sending otp");
        }

      }
    );
}
    else{
    email.value="";

    alert("User doesnot exists");
}
});
}

function validate(){
    const pass1 = document.getElementById("floatingPassword1");
    const pass2 = document.getElementById("floatingPassword2");
        if (pass1.value==pass2.value){
            document.getElementById("submitbutton").type="submit";
            }
        else{
            pass1.value=pass2.value="";
            alert("passwords do not match");
        
        }
}
function handleInput(input){
    if (input.value.length==10){
        input.value+="@vvit.net";
        document.getElementsByClassName("otpbutton")[0].style.display = "block";
        input.addEventListener("keydown", function(event) {
            if (event.key === "Backspace") {
              input.value="";
              document.getElementsByClassName("otpbutton")[0].style.display = "none";
            }
          });
    }
    else{
        document.getElementsByClassName("otpbutton")[0].style.display = "none";
    }
}