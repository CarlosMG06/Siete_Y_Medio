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
const cardDeck = [
    {
        "src": "images/carta_01_oros.avif",
        "name": "1 de Oros",
        "value": 1
    },
    {
        "src": "images/carta_02_oros.avif",
        "name": "2 de Oros",
        "value": 2
    },
    {
        "src": "images/carta_03_oros.avif",
        "name": "3 de Oros",
        "value": 3
    },
    {
        "src": "images/carta_04_oros.avif",
        "name": "4 de Oros",
        "value": 4
    },
    {
        "src": "images/carta_05_oros.avif",
        "name": "5 de Oros",
        "value": 5
    },
    {
        "src": "images/carta_06_oros.avif",
        "name": "6 de Oros",
        "value": 6
    },
    {
        "src": "images/carta_07_oros.avif",
        "name": "7 de Oros",
        "value": 7
    },
    {
        "src": "images/carta_08_oros.avif",
        "name": "8 de Oros",
        "value": 0.5
    },
    {
        "src": "images/carta_09_oros.avif",
        "name": "9 de Oros",
        "value": 0.5
    },
    {
        "src": "images/carta_10_oros.avif",
        "name": "10 de Oros",
        "value": 0.5
    },
    {
        "src": "images/carta_11_oros.avif",
        "name": "11 de Oros",
        "value": 0.5
    },
    {
        "src": "images/carta_12_oros.avif",
        "name": "12 de Oros",
        "value": 0.5
    },
    {
        "src": "images/carta_01_copas.avif",
        "name": "1 de Copas",
        "value": 1
    },
    {
        "src": "images/carta_02_copas.avif",
        "name": "2 de Copas",
        "value": 2
    },
    {
        "src": "images/carta_03_copas.avif",
        "name": "3 de Copas",
        "value": 3
    },
    {
        "src": "images/carta_04_copas.avif",
        "name": "4 de Copas",
        "value": 4
    },
    {
        "src": "images/carta_05_copas.avif",
        "name": "5 de Copas",
        "value": 5
    },
    {
        "src": "images/carta_06_copas.avif",
        "name": "6 de Copas",
        "value": 6
    },
    {
        "src": "images/carta_07_copas.avif",
        "name": "7 de Copas",
        "value": 7
    },
    {
        "src": "images/carta_08_copas.avif",
        "name": "8 de Copas",
        "value": 0.5
    },
    {
        "src": "images/carta_09_copas.avif",
        "name": "9 de Copas",
        "value": 0.5
    },
    {
        "src": "images/carta_10_copas.avif",
        "name": "10 de Copas",
        "value": 0.5
    },
    {
        "src": "images/carta_11_copas.avif",
        "name": "11 de Copas",
        "value": 0.5
    },
    {
        "src": "images/carta_12_copas.avif",
        "name": "12 de Copas",
        "value": 0.5
    },
    {
        "src": "images/carta_01_bastos.avif",
        "name": "1 de Bastos",
        "value": 1
    },
    {
        "src": "images/carta_02_bastos.avif",
        "name": "2 de Bastos",
        "value": 2
    },
    {
        "src": "images/carta_03_bastos.avif",
        "name": "3 de Bastos",
        "value": 3
    },
    {
        "src": "images/carta_04_bastos.avif",
        "name": "4 de Bastos",
        "value": 4
    },
    {
        "src": "images/carta_05_bastos.avif",
        "name": "5 de Bastos",
        "value": 5
    },
    {
        "src": "images/carta_06_bastos.avif",
        "name": "6 de Bastos",
        "value": 6
    },
    {
        "src": "images/carta_07_bastos.avif",
        "name": "7 de Bastos",
        "value": 7
    },
    {
        "src": "images/carta_08_bastos.avif",
        "name": "8 de Bastos",
        "value": 0.5
    },
    {
        "src": "images/carta_09_bastos.avif",
        "name": "9 de Bastos",
        "value": 0.5
    },
    {
        "src": "images/carta_10_bastos.avif",
        "name": "10 de Bastos",
        "value": 0.5
    },
    {
        "src": "images/carta_11_bastos.avif",
        "name": "11 de Bastos",
        "value": 0.5
    },
    {
        "src": "images/carta_12_bastos.avif",
        "name": "12 de Bastos",
        "value": 0.5
    },
    {
        "src": "images/carta_01_espadas.avif",
        "name": "1 de Espadas",
        "value": 1
    },
    {
        "src": "images/carta_02_espadas.avif",
        "name": "2 de Espadas",
        "value": 2
    },
    {
        "src": "images/carta_03_espadas.avif",
        "name": "3 de Espadas",
        "value": 3
    },
    {
        "src": "images/carta_04_espadas.avif",
        "name": "4 de Espadas",
        "value": 4
    },
    {
        "src": "images/carta_05_espadas.avif",
        "name": "5 de Espadas",
        "value": 5
    },
    {
        "src": "images/carta_06_espadas.avif",
        "name": "6 de Espadas",
        "value": 6
    },
    {
        "src": "images/carta_07_espadas.avif",
        "name": "7 de Espadas",
        "value": 7
    },
    {
        "src": "images/carta_08_espadas.avif",
        "name": "8 de Espadas",
        "value": 0.5
    },
    {
        "src": "images/carta_09_espadas.avif",
        "name": "9 de Espadas",
        "value": 0.5
    },
    {
        "src": "images/carta_10_espadas.avif",
        "name": "10 de Espadas",
        "value": 0.5
    },
    {
        "src": "images/carta_11_espadas.avif",
        "name": "11 de Espadas",
        "value": 0.5
    },
    {
        "src": "images/carta_12_espadas.avif",
        "name": "12 de Espadas",
        "value": 0.5
    }
]

let cardsCopy = []
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

    cardsCopy = [...cardDeck]
    cardToGet = GetRandomNumber(0, cardsCopy.length - 1)
    ShowCardTutorial2(cardToGet, cardsCopy, playerScores)

    await Delay(500)
    demandCardForm.style.visibility = "visible"
    cardsCopy.splice(cardToGet, 1)
}

const PlayTutorialPart3 = async () => {
    if (parseFloat(playerScores[1]) > 7.5) {
        demandCardForm.style.visibility = "hidden"
        msgText.innerHTML = "¡Te has pasado!"
        msgDiv.style.visibility = "visible"
        playerScores[0].innerHTML = parseInt(playerScores[0].innerHTML) - parseInt(playerScores[2].innerHTML)
        bankScores[0].innerHTML = parseInt(bankScores[0].innerHTML) + parseInt(playerScores[2].innerHTML)
        return 
    }

    cardToGet = GetRandomNumber(0, cardsCopy.length - 1)
    ShowCardTutorial2(cardToGet, cardsCopy, playerScores)
    await Delay(500)
    demandCardForm.style.visibility = "visible"
    cardsCopy.splice(cardToGet, 1)
}

const PlayTutorialPart4 = async () => {
    demandCardForm.style.visibility = "hidden"
    HideCardTutorial2()

    msgText.innerHTML = "Juga la banca"
    msgDiv.style.visibility = "visible"
    await Delay(1500)
    msgDiv.style.visibility = "hidden"

    points = 0
    cardsCopy = [...cardDeck]
    while (parseFloat(bankScores[1].innerHTML) < 7.5 && parseFloat(bankScores[1].innerHTML) < parseFloat(playerScores[1].innerHTML) && cardsCopy.length > 0) {
        await Delay(1500)
        cardImg.style.visibility = "hidden"
        cardName.style.visibility = "hidden"
        await Delay(1000)
        cardToGet = GetRandomNumber(0, cardsCopy.length - 1)
        ShowCardTutorial2(cardToGet, cardsCopy, bankScores)
        cardsCopy.splice(cardToGet, 1)
    }

    if (parseFloat(bankScores[1].innerHTML) < parseFloat(playerScores[1].innerHTML)) {
        msgText.innerHTML = "¡Has ganado!"
        playerScores[0].innerHTML = parseInt(playerScores[0].innerHTML) + Math.min(parseInt(playerScores[2].innerHTML), parseInt(bankScores[0].innerHTML))
        bankScores[0].innerHTML = parseInt(bankScores[0].innerHTML) - parseInt(playerScores[2].innerHTML)
        
    }
    else if (parseFloat(playerScores[1].innerHTML) === 7.5 && parseFloat(bankScores[1].innerHTML) != 7.5) {
        msgText.innerHTML = "¡Has ganado! Eres candidato a la banca"
        playerScores[0].innerHTML = parseInt(playerScores[0].innerHTML) + Math.min(parseInt(playerScores[2].innerHTML), parseInt(bankScores[0].innerHTML))
        bankScores[0].innerHTML = parseInt(bankScores[0].innerHTML) - parseInt(playerScores[2].innerHTML)
    }
    else if (parseFloat(bankScores[1].innerHTML) === parseFloat(playerScores[1].innerHTML)) {
        msgText.innerHTML = "¡Gana la banca por empate!"
        playerScores[0].innerHTML = parseInt(playerScores[0].innerHTML) - parseInt(playerScores[2].innerHTML)
        bankScores[0].innerHTML = parseInt(bankScores[0].innerHTML) + parseInt(playerScores[2].innerHTML)
    }
    else if (parseFloat(bankScores[1].innerHTML) === 7.5 || (parseFloat(bankScores[1].innerHTML) < 7.5 && parseFloat(bankScores[1].innerHTML) > parseFloat(playerScores[1].innerHTML))) {
        msgText.innerHTML = "¡Gana la banca!"
        playerScores[0].innerHTML = parseInt(playerScores[0].innerHTML) - parseInt(playerScores[1].innerHTML)
        bankScores[0].innerHTML = parseInt(bankScores[0].innerHTML) + parseInt(playerScores[2].innerHTML)
    }
    playerScores[2].innerHTML = 0
    msgDiv.style.visibility = "visible"
}

const ResetPlayTutorial = () => {
    bankScores[0].innerHTML = 15
    bankScores[1].innerHTML = 0
    playerScores[0].innerHTML = 20
    playerScores[1].innerHTML = 0
    playerScores[2].innerHTML = 0

    cardImg.style.visibility = "hidden"
    cardName.style.visibility = "hidden"

    msgText.innerHTML = ""
    msgDiv.style.visibility = "hidden"

    demandCardForm.style.visibility = "hidden"
    insertBetForm.style.visibility = "hidden"

    points = 0
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
    return Math.floor(Math.random() * (max - min) + min)
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