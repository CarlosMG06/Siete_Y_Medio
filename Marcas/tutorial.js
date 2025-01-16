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
const msgDiv = document.querySelector("#msg-div")
const msgText = document.querySelector("#msg-text")
const setBetBtn = document.querySelector("#btn-submit-bet")
const demandCardBtn = document.querySelector("#btn-demand-card")
const standBtn = document.querySelector("#btn-stand")
const betInput = document.querySelector("#input-bet")
const playerCardsDict = [
    {
        "src": "images/tutorial01_card01.avif",
        "name": "12 de Espadas",
        "value": 0.5
    },
    {
        "src": "images/tutorial01_card02.avif",
        "name": "1 de Copas",
        "value": 1
    }
]
const bankCardsDict = [
    {
        "src": "images/tutorial01_card01.avif",
        "name": "12 de Espadas",
        "value": 0.5
    },
    {
        "src": "images/tutorial01_card02.avif",
        "name": "1 de Copas",
        "value": 1
    },
    {
        "src": "images/tutorial01_card01.avif",
        "name": "12 de Espadas",
        "value": 0.5
    },
    {
        "src": "images/tutorial01_card02.avif",
        "name": "1 de Copas",
        "value": 1
    },
    {
        "src": "images/tutorial01_card01.avif",
        "name": "12 de Espadas",
        "value": 0.5
    },
    {
        "src": "images/tutorial01_card02.avif",
        "name": "1 de Copas",
        "value": 1
    }
]

let cardIndex = 0
let points = 0

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

const PlayTutorialPart2 = async () => {
    insertBetForm.style.visibility = "hidden"

    ShowCardTutorial2(cardIndex, playerCardsDict, playerScores)

    await Delay(500)
    demandCardForm.style.visibility = "visible"
    cardIndex++
}

const PlayTutorialPart3 = async () => {
    if (cardIndex > playerCardsDict.length || cardIndex === playerCardsDict.length) {
        demandCardForm.style.visibility = "hidden"
        msgText.innerHTML = "¡Te has pasado!"
        msgDiv.style.visibility = "visible"
        playerScores[0].innerHTML = parseInt(playerScores[0].innerHTML) - parseInt(playerScores[2].innerHTML)
        bankScoresScores[0].innerHTML = parseInt(playerScores[2].innerHTML)
        playerScores[1].innerHTML = 0
        bankScores[1].innerHTML = 0
        return 
    }

    ShowCardTutorial2(cardIndex, playerCardsDict, playerScores)
    await Delay(500)
    demandCardForm.style.visibility = "visible"
    cardIndex++
}

const PlayTutorialPart4 = async () => {
    demandCardForm.style.visibility = "hidden"
    HideCardTutorial2()

    msgText.innerHTML = "Juga la banca"
    msgDiv.style.visibility = "visible"
    await Delay(5000)
    msgDiv.style.visibility = "hidden"

    // Randomizamos el número de cartas que va a recoger la banca de su lado
    cardToGet = GetRandomNumber(1, bankCardsDict.length - 1)
    points = 0
    ShowCardTutorial2(0, bankCardsDict, bankScores)
    for (let index = 1; index < cardToGet; index++) {
        if (parseFloat(bankScores[1].innerHTML) === 7.5 || parseFloat(bankScores[1].innerHTML) > 7.5 || parseFloat(bankScores[1].innerHTML) > parseFloat(playerScores[1].innerHTML) || parseFloat(bankScores[1].innerHTML) === parseFloat(playerScores[1].innerHTML )) {
            break
        }
        await Delay(2000)
        ShowCardTutorial2(index, bankCardsDict, bankScores)
    }

    if (parseFloat(bankScores[1].innerHTML) < parseFloat(playerScores[1].innerHTML)) {
        msgText.innerHTML = "¡Has ganado!"
        bankScores[0].innerHTML = parseInt(bankScores[0].innerHTML) - parseInt(playerScores[2].innerHTML)
        playerScores[0].innerHTML = parseInt(playerScores[0].innerHTML) + parseInt(playerScores[2].innerHTML)
        playerScores[1].innerHTML = 0
        bankScores[1].innerHTML = 0
    }
    else if (parseFloat(playerScores[1].innerHTML) == 7.5 && parseFloat(bankScores[1].innerHTML) != 7.5) {
        msgText.innerHTML = "¡Has ganado! Eres candidato a la banca"
        bankScores[0].innerHTML = parseInt(bankScores[0].innerHTML) - parseInt(playerScores[2].innerHTML)
        playerScores[0].innerHTML = parseInt(playerScores[0].innerHTML) + parseInt(playerScores[2].innerHTML)
        playerScores[1].innerHTML = 0
        bankScores[1].innerHTML = 0
    }
    else if (parseFloat(bankScores[1].innerHTML) === parseFloat(playerScores[1].innerHTML)) {
        console.log("Empate")
        msgText.innerHTML = "¡Gana la banca por empate!"
        playerScores[0].innerHTML = parseInt(playerScores[0].innerHTML) - parseInt(playerScores[2].innerHTML)
        bankScoresScores[0].innerHTML = parseInt(bankScoresScores[0].innerHTML) + parseInt(playerScores[2].innerHTML)
        playerScores[1].innerHTML = 0
        bankScores[1].innerHTML = 0
    }
    else if (parseFloat(bankScores[1].innerHTML) === 7.5 || parseFloat(bankScores[1].innerHTML) < 7.5 && parseFloat(bankScores[1].innerHTML) > parseFloat(playerScores[1].innerHTML)) {
        msgText.innerHTML = "¡Gana la banca!"
        playerScores[0].innerHTML = parseInt(playerScores[0].innerHTML) - parseInt(playerScores[1].innerHTML)
        bankScoresScores[0].innerHTML = parseInt(bankScoresScores[0].innerHTML) + parseInt(playerScores[2].innerHTML)
        playerScores[1].innerHTML = 0
        bankScores[1].innerHTML = 0
    }
    playerScores[2].innerHTML = 0
    msgDiv.style.visibility = "visible"
}

const ShowCardTutorial2 = (cardIndex, dict, scores) => {
    cardImg.src = dict[cardIndex]["src"]
    cardName.innerHTML = dict[cardIndex]["name"]
    points += dict[cardIndex]["value"]
    scores[1].innerHTML = points
    cardImg.style.visibility = "visible"
    cardName.style.visibility = "visible"
}

const HideCardTutorial2 = () => {
    cardImg.src = ""
    cardName.innerHTML = ""
    cardImg.style.visibility = "hidden"
    cardName.style.visibility = "hidden"
}

const GetRandomNumber = (min, max) => {
    return Math.random() * (max - min) + min
}

setBetBtn.addEventListener("click", async (event) => {
    event.preventDefault()
    if (parseInt(betInput.value) <= parseInt(playerScores[0].innerHTML) && parseInt(betInput.value) > 0) {
        playerScores[2].innerHTML = betInput.value
        PlayTutorialPart2()
    }
    else {
        betInput.disabled = true
        setBetBtn.disabled = true
        msgText.innerHTML = "Apuesta no válida"
        msgDiv.style.visibility = "visible"
        await Delay(3000)
        msgDiv.style.visibility = "hidden"
        betInput.disabled = false
        setBetBtn.disabled = false
    }
})
demandCardBtn.addEventListener("click", (event) => {
    event.preventDefault()
    demandCardForm.style.visibility = "hidden"
    PlayTutorialPart3()
})
standBtn.addEventListener("click", (event) => {
    event.preventDefault()
    PlayTutorialPart4()
})