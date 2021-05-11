
        var x =document.getElementById("login");
        var y =document.getElementById("register");
        var z =document.getElementById("btn");

        function register(){
            x.style.left="-400px";
            y.style.left="50px";
            z.style.left="110px";
        }
        function login(){
            x.style.left="50px";
            y.style.left="450px";
            z.style.left="0px";
        }


        // var objPeople=[
        //     {
        //         username: "Mohit",
        //         password: "mohit1234"
        //     },
        //     {
        //         username: "ms46678900",
        //         password: "@mohit1432"
        //     },
        //     {
        //         username: "nikhilanand",
        //         password: "nikhil1234"
        //     },

        // ]

        // function getInfo(){
        //     var username= getElementById("username").value;
        //     var password= getElementById("password").value;

        //     for(i=0;i<objPeople.length;i++){
        //         if(username == objPeople[i].username && password == objPeople[i].password)
                   
        //             return;
        //     }
                 
        // }      
        
        function loggedIn(){
            alert("You are logged In successfully. Redirecting to Home-Page")
        }
        function registered(){
            alert("Thanks for registering.We will soon redirecting to home page");
        }


