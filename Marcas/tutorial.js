bankScore = 20
bankRoundPoints = 0
playerScore = 20
playerRoundPoints = 0

const canvas = document.getElementById("tutorial-canvas")
const buttons = document.getElementsByClassName("button")

const context = canvas.getContext("2d")

const backgroundImage = new Image()
backgroundImage.src = 'images/background.avif'
context.drawImage(backgroundImage, 0, 0, 1280, 720)

context.font = "48px Arial"
context.fillStyle = "white"
context.fillText(`Bank Score: ${bankScore}`, 900, 50);
context.fillText(`Bank Round Points: ${bankRoundPoints}`, 738, 95);
context.fillStyle = "red    "
context.fillText(`Your Score: ${playerScore}`, 913, 150);
context.fillText(`Your Round Points: ${playerRoundPoints}`, 751, 195);

const btnBet = {
    "rect": (220, 100, 200, 75),
    "style": '#001122',
    "text": 'Realizar Apuesta'
}

context.fillStyle = btnBet["style"].split(',');
context.fillRect(btnBet["rect"]);
context.fillText(btnBet["text"], 320, 145, 200);

function init() {
    update()
}

function update() {
    
}

init()
