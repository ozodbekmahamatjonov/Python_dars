import turtle
a = 0 
b = 0

turtle.penup()
turtle.speed(0)
turtle.bgcolor('black')

turtle.pencolor('darkgreen')
turtle.pensize(3)
turtle.hideturtle()
turtle.goto(0, 200)
turtle.pendown()
while True:
	turtle.forward(a)
	turtle.right(b)
	a+=3
	b+=1
	if b == 210:
		break
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Findstory</title>
    <link rel="stylesheet" href="./bootstrap.css">    
    <link rel="stylesheet" href="./bootstrap.js">
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="icon" type="image/x-icon" href="./photo_2022-07-09_13-57-42.jpg">
</head>
<body>
    
        <div class="rowq">
            <div class="col">
                    <img class="img" src="./photo_2022-07-09_13-57-42.jpg" alt="">
                    <!--  -->
                   <a href="./index1.html"> <input type="text" class="w-98" style="border-radius: 30px; border:1px solid red"   placeholder="Find your things"></a>
                    <i class="fa-solid fa-magnifying-glass ms-5" style="font-size: 20px; color: red; position: absolute; top:20.5%; left: 38%; "></i>
                    <img src="./jp.jpg" width="20%" style="margin: 0 10%;" class="text-center " alt="">
                </div>
                <h1 class="text-center  text-light" style="background-color: red; text-decoration: none; "><a href="">FindStory.com</a></h1>
        </div> 
        <hr class="opacity-100">
        
           <div class="rowcha d-flex">
            <div class="cola">
                <h2><a href="./inde2.html" class="produc" style="color: blue;">Products</a></h2>
            <hr class="opacity-100 ms-2" style="width: 800%; margin-top: -1.8%;">
            </div>
            <div class="cola">
                <h2><a href="./index3.html" class="produc" style="color: red;">Your cards</a></h2>
           
            </div>
           </div>
        <div class="row">
            <div class="col">
                <h1 class="ms-2">For Your Business</h1>
            </div>
        </div>
        <div class="row d-flex">
            <div class="col d-flex">
                <a href="./index4.html" >
                    <button class="bbbb"><h1>All <br> Categories</h1> <i class="fa-solid fa-window-restore" style="font-size: 50px;"></i></button>
                   
                </a>
            </div>
            <div class="col d-flex">
                <a href="./index6.html" >
                    <button class="bbb"><h1>Your <br> BitcoinCashup</h1><i class="fa-brands fa-bitcoin" style="font-size: 50px;"></i></button>
                   
                </a>
            </div>
            <div class="col d-flex">
                <a href="index7.html" >
                    <button class="bbb1"><h1>Your Dollar <br>Cashup   </h1><i class="fa-solid fa-circle-dollar-to-slot"style="font-size: 50px;"></i></button>
                   
                </a>
            </div>
            <div class="col d-flex">
                <a href="./index8.html" >
                    <button class="bbb2"><h1>Your Euro <br>Cashup   </h1><i class="fa-solid fa-euro-sign"style="font-size: 50px;"></i></button>
                   
                </a>
            </div>
           <div class="container">
            <div class="row">
                <div class="col ">
                    <h1 class="ms-52 p-3 ps-2">Shop our best top products and accessories</h1>
                </div>
            </div>
           </div>
        </div>



 
            <div class="row p-3 ps-5">
                <div class="col d-flex">
                    <div class="card d-block">
                        <div class="col ">
                            <img src="./i.jpg" class="text-center ms-3" width="80%" alt="">
                        </div>
                        <div class="col text-center h1 ">
                            1000$
                            <br>
                            Ipod
                        </div>
                    </div>
                    <div class="card ms-5 d-block">
                        <div class="col text-center p-1">
                            <img src="./scuter.jpg" class="text-center ms-3" alt="">
                        </div>
                        <div class="col text-center h1 ">
                            2500$
                            <br>
                            Electronic Sccoter  
                        </div>
                    </div>
                    <div class="card ms-5 d-block">
                        <div class="col text-center p-1">
                            <img src="./kaska.jpg" width="80%" alt="">
                        </div>
                        <div class="col text-center h1 ">
                            3000$
                            <br>
                            Vertuval Box
                        </div>
                        
                    </div>
                    <div class="card ms-5 d-block">
                        <div class="col text-center p-1">
                            <img src="./computer.jpg"   width="80%" alt="">
                        </div>
                        <div class="col text-center h1 ">
                            1000$
                            <br>
                            Laptop
                        </div>
                        
                    </div>
                </div>
            </div>
    
        </div>
        <div class="row mt-3 d-flex">
            <div class="col">
                <video src="./video1.mp4"  controls></video>
                <div class="col text-center ">
                    <h1>About VertualBox</h1>
                </div>
            </div>
            <div class="col">
                <video src="./video2.mp4"  controls></video>
                <div class="col text-center ">
                    <h1>About Watches</h1>
                </div>
            </div>
        </div>
        <div class="container text-center d-block mt-5">
            Your Name: <br>
            <input type="text" style="border: 1px solid blue; border-radius: 5px mt-3; "  placeholder="Your Name"> <br><br>
            Your Email: <br>
            <input type="text" style="border: 1px solid blue; border-radius: 5px mt-3; "  placeholder="Your Email"> <br> <br>
            Your phone number: <br>
            <input type="tel" placeholder="Your phone">
            <select style="margin:0 64.3%; background-color: green; color: #fff; border: 1px solid green; padding: 10px 40px; border-radius: 5px;">
                
                <option value="hello" class="text-light" disabled>Your Number</option>
                <option value="+1 USA">+1 USA</option>
                <option value="+7 Russian">+7 Russian</option>
                <option value="+997 Kirkiztan">+997 Kirkiztan</option>
                <option value="+998 Uzbekistan">+998 Uzbekistan</option>
            </select> 
            <br><br>
            <a href="">
                <button class="n">Send</button>
            </a>

        </div>








        <div id="header">
            <div class="container">
            <h1>
                <span class="logo">CityTech</span>	Coding School
            </h1>
                <ul class="navbar">
                    <li>

                        <a href="./index.html">Home</a>
                    </li>
                        <li>
                        <a href="./about.html">About</a>
                    </li>
                        <li>
                        <a href="./services.html">Services</a>
                    </li>
                </ul>
            </div>
        </div>
        
</body>
</html>
turtle.done()

