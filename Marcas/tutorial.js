// Tutorial 1
const titles = ["12 de Espadas", "1 de Copas", "1 de Bastos", "4 de Oros"]
const cards = document.querySelectorAll(".card-t1")
const cardTitles = document.querySelectorAll(".card-name-t1")
const order = document.querySelector("#tutorial-players-order")

// Tutorial 2
const cardImg = document.querySelector("#card-t2")
const cardName = document.querySelector("#card-name-t2")
const bankScores = document.querySelectorAll(".bank-scores")
const playerScores = document.querySelectorAll(".player-scores")
const insertBetForm = document.querySelector("#insert-bet")
const demandCardForm = document.querySelector("#demand-card")
const setBetBtn = document.querySelector("#btn-submit-bet")
const demandCardBtn = document.querySelector("#btn-demand-card")
const standBtn = document.querySelector("#btn-stand")
const betInput = document.querySelector("#input-bet")
const cardsDict = [
    {
        "src": "images/tutorial01_card01.avif",
        "name": "12 de Espadas",
        "value": 0.5
    }
]
let cardIndex = 0
let playerPoints = 0

const Delay = ms => new Promise(res => setTimeout(res, ms));

const PriorityTutorial = async () => {
    for (let index = 0; index < cards.length; index++) {
        cards[index].style.visibility = "visible"
        cardTitles[index].innerHTML = titles[index]
        cardTitles[index].style.visibility = "visible"

        await Delay(1750);
    }

    order.style.visibility = "visible"
}

const ResetPriorityTutorial = () => {
    order.style.visibility = "hidden"

    for (let index = 0; index < cards.length; index++) {
        cards[index].style.visibility = "hidden"
        cardTitles[index].innerHTML = ""
        cardTitles[index].style.visibility = "hidden"
    }
}

const PlayTutorialPart1 = () => {
    insertBetForm.style.visibility = "visible"
}

const PlayTutorialPart2 = () => {
    insertBetForm.style.visibility = "hidden"

    cardImg.src = cardsDict[cardIndex]["src"]
    cardName.innerHTML = cardsDict[cardIndex]["name"]
    playerPoints += cardsDict[cardIndex]["value"]
    playerScores[2].innerHTML = playerPoints
    cardImg.style.visibility = "visible"
    cardName.style.visibility = "visible"

    Delay(500)
    demandCardForm.style.visibility = "visible"
    cardIndex++
}

const PlayTutorialPart3 = () => {
    


    cardIndex++
    if (cardIndex >= cardsDict.length) {
        // Mostrar que se ha pasado
    }

    PlayTutorialPart4()
}

const PlayTutorialPart4 = () => {

}

setBetBtn.addEventListener("click", (event) => {
    event.preventDefault()
    if (parseInt(betInput.value) <= parseInt(playerScores[0].innerHTML)) {
        playerScores[1].innerHTML = betInput.value
        PlayTutorialPart2()
    }
})
demandCardBtn.addEventListener("submit", (event) => {
    event.preventDefault()
    PlayTutorialPart3()
})
standBtn.addEventListener("submit", (event) => {
    event.preventDefault()
    console.log("Set Bet Button Clicked")
    Delay(5000)
    cardImg.src = "images/tutorial01_card01.avif"
})