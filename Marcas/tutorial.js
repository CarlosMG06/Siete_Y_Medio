// Tutorial 1
const cards = document.querySelectorAll(".card-t1")
const cardTitles = document.querySelectorAll(".card-name-t1")
const order = document.querySelector("#tutorial-players-order")
const startTutorial1Btn = document.querySelector("#tutorial1-btn")

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
const startTutorial2Btn = document.querySelector("#tutorial2-btn")
const cardDeck = [
    {
        "id": "01O",
        "src": "images/carta_01_oros.avif",
        "name": "1 de Oros",
        "value": 1
    },
    {
        "id": "02O",
        "src": "images/carta_02_oros.avif",
        "name": "2 de Oros",
        "value": 2
    },
    {
        "id": "03O",
        "src": "images/carta_03_oros.avif",
        "name": "3 de Oros",
        "value": 3
    },
    {
        "id": "04O",
        "src": "images/carta_04_oros.avif",
        "name": "4 de Oros",
        "value": 4
    },
    {
        "id": "05O",
        "src": "images/carta_05_oros.avif",
        "name": "5 de Oros",
        "value": 5
    },
    {
        "id": "06O",
        "src": "images/carta_06_oros.avif",
        "name": "6 de Oros",
        "value": 6
    },
    {
        "id": "07O",
        "src": "images/carta_07_oros.avif",
        "name": "7 de Oros",
        "value": 7
    },
    {
        "id": "08O",
        "src": "images/carta_08_oros.avif",
        "name": "8 de Oros",
        "value": 0.5
    },
    {
        "id": "09O",
        "src": "images/carta_09_oros.avif",
        "name": "9 de Oros",
        "value": 0.5
    },
    {
        "id": "10O",
        "src": "images/carta_10_oros.avif",
        "name": "10 de Oros",
        "value": 0.5
    },
    {
        "id": "11O",
        "src": "images/carta_11_oros.avif",
        "name": "11 de Oros",
        "value": 0.5
    },
    {
        "id": "12O",
        "src": "images/carta_12_oros.avif",
        "name": "12 de Oros",
        "value": 0.5
    },
    {
        "id": "01C",
        "src": "images/carta_01_copas.avif",
        "name": "1 de Copas",
        "value": 1
    },
    {
        "id": "02C",
        "src": "images/carta_02_copas.avif",
        "name": "2 de Copas",
        "value": 2
    },
    {
        "id": "03C",
        "src": "images/carta_03_copas.avif",
        "name": "3 de Copas",
        "value": 3
    },
    {
        "id": "04C",
        "src": "images/carta_04_copas.avif",
        "name": "4 de Copas",
        "value": 4
    },
    {
        "id": "05C",
        "src": "images/carta_05_copas.avif",
        "name": "5 de Copas",
        "value": 5
    },
    {
        "id": "06C",
        "src": "images/carta_06_copas.avif",
        "name": "6 de Copas",
        "value": 6
    },
    {
        "id": "07C",
        "src": "images/carta_07_copas.avif",
        "name": "7 de Copas",
        "value": 7
    },
    {
        "id": "08C",
        "src": "images/carta_08_copas.avif",
        "name": "8 de Copas",
        "value": 0.5
    },
    {
        "id": "09C",
        "src": "images/carta_09_copas.avif",
        "name": "9 de Copas",
        "value": 0.5
    },
    {
        "id": "10C",
        "src": "images/carta_10_copas.avif",
        "name": "10 de Copas",
        "value": 0.5
    },
    {
        "id": "11C",
        "src": "images/carta_11_copas.avif",
        "name": "11 de Copas",
        "value": 0.5
    },
    {
        "id": "12C",
        "src": "images/carta_12_copas.avif",
        "name": "12 de Copas",
        "value": 0.5
    },
    {
        "id": "01B",
        "src": "images/carta_01_bastos.avif",
        "name": "1 de Bastos",
        "value": 1
    },
    {
        "id": "02B",
        "src": "images/carta_02_bastos.avif",
        "name": "2 de Bastos",
        "value": 2
    },
    {
        "id": "03B",
        "src": "images/carta_03_bastos.avif",
        "name": "3 de Bastos",
        "value": 3
    },
    {
        "id": "04B",
        "src": "images/carta_04_bastos.avif",
        "name": "4 de Bastos",
        "value": 4
    },
    {
        "id": "05B",
        "src": "images/carta_05_bastos.avif",
        "name": "5 de Bastos",
        "value": 5
    },
    {
        "id": "06B",
        "src": "images/carta_06_bastos.avif",
        "name": "6 de Bastos",
        "value": 6
    },
    {
        "id": "07B",
        "src": "images/carta_07_bastos.avif",
        "name": "7 de Bastos",
        "value": 7
    },
    {
        "id": "08B",
        "src": "images/carta_08_bastos.avif",
        "name": "8 de Bastos",
        "value": 0.5
    },
    {
        "id": "09B",
        "src": "images/carta_09_bastos.avif",
        "name": "9 de Bastos",
        "value": 0.5
    },
    {
        "id": "10B",
        "src": "images/carta_10_bastos.avif",
        "name": "10 de Bastos",
        "value": 0.5
    },
    {
        "id": "11B",
        "src": "images/carta_11_bastos.avif",
        "name": "11 de Bastos",
        "value": 0.5
    },
    {
        "id": "12B",
        "src": "images/carta_12_bastos.avif",
        "name": "12 de Bastos",
        "value": 0.5
    },
    {
        "id": "01E",
        "src": "images/carta_01_espadas.avif",
        "name": "1 de Espadas",
        "value": 1
    },
    {
        "id": "02E",
        "src": "images/carta_02_espadas.avif",
        "name": "2 de Espadas",
        "value": 2
    },
    {
        "id": "03E",
        "src": "images/carta_03_espadas.avif",
        "name": "3 de Espadas",
        "value": 3
    },
    {
        "id": "04E",
        "src": "images/carta_04_espadas.avif",
        "name": "4 de Espadas",
        "value": 4
    },
    {
        "id": "05E",
        "src": "images/carta_05_espadas.avif",
        "name": "5 de Espadas",
        "value": 5
    },
    {
        "id": "06E",
        "src": "images/carta_06_espadas.avif",
        "name": "6 de Espadas",
        "value": 6
    },
    {
        "id": "07E",
        "src": "images/carta_07_espadas.avif",
        "name": "7 de Espadas",
        "value": 7
    },
    {
        "id": "08E",
        "src": "images/carta_08_espadas.avif",
        "name": "8 de Espadas",
        "value": 0.5
    },
    {
        "id": "09E",
        "src": "images/carta_09_espadas.avif",
        "name": "9 de Espadas",
        "value": 0.5
    },
    {
        "id": "10E",
        "src": "images/carta_10_espadas.avif",
        "name": "10 de Espadas",
        "value": 0.5
    },
    {
        "id": "11E",
        "src": "images/carta_11_espadas.avif",
        "name": "11 de Espadas",
        "value": 0.5
    },
    {
        "id": "12E",
        "src": "images/carta_12_espadas.avif",
        "name": "12 de Espadas",
        "value": 0.5
    }
]

const cardPriority = {
    "O": 4,
    "C": 3,
    "E": 2,
    "B": 1
}

const playersPriorities = [
    {
        "name": "Jordi",
        "priority": 1,
        "cardId": ""
    },
    {
        "name": "Marina",
        "priority": 1,
        "cardId": ""
    },
    {
        "name": "Aurora",
        "priority": 1,
        "cardId": ""
    },
    {
        "name": "Albert",
        "priority": 1,
        "cardId": ""
    }
]

let cardsCopy = []
let points = 0

const Delay = ms => new Promise(res => setTimeout(res, ms));

const PriorityTutorial = async () => {
    startTutorial1Btn.disabled = true
    cardsCopy = [...cardDeck]
    for (let index = 0; index < playersPriorities.length; index++) {
        cardToGet = GetRandomNumber(0, cardsCopy.length - 1)
        ShowCardTutorial1(index, cardToGet, cardsCopy)
        playersPriorities[index]["cardId"] = cardsCopy[cardToGet]["id"]
        cardsCopy.splice(cardToGet, 1)
        await Delay(1500)
    }

    playersOrder = OrderPlayers(playersPriorities)

    order.innerHTML = `
    <p>
        Orden de los jugadores:
        <ol>
            <li><p>${playersOrder[0]} <span>&#x279C</span> <span class="txt-prioriry">Prioridad 1</span></p></li>
            <li><p>${playersOrder[1]} <span>&#x279C</span> <span class="txt-prioriry">Prioridad 2</span></p></li>
            <li><p>${playersOrder[2]} <span>&#x279C</span> <span class="txt-prioriry">Prioridad 3</span></p></li>
            <li><p>${playersOrder[3]} <strong/>(Banca)</strong> <span>&#x279C</span> <span class="txt-prioriry">Prioridad 4</span></p></li>
        </ol>
    </p>
    `
    order.style.visibility = "visible"
}

const ResetPriorityTutorial = () => {
    order.style.visibility = "hidden"

    for (let index = 0; index < cards.length; index++) {
        cards[index].style.visibility = "hidden"
        cardTitles[index].innerHTML = ""
        cardTitles[index].style.visibility = "hidden"
    }

    startTutorial1Btn.disabled = false
}

const PlayTutorialPart1 = () => {
    startTutorial2Btn.disabled = true
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
    cardToGet = GetRandomNumber(0, cardsCopy.length - 1)
    ShowCardTutorial2(cardToGet, cardsCopy, playerScores)
    await Delay(500)
    demandCardForm.style.visibility = "visible"
    cardsCopy.splice(cardToGet, 1)

    if (parseFloat(playerScores[1].innerHTML) > 7.5) {
        demandCardForm.style.visibility = "hidden"
        msgText.innerHTML = "¡Te has pasado!"
        msgDiv.style.visibility = "visible"
        playerScores[0].innerHTML = parseInt(playerScores[0].innerHTML) - parseInt(playerScores[2].innerHTML)
        bankScores[0].innerHTML = parseInt(bankScores[0].innerHTML) + parseInt(playerScores[2].innerHTML)
        return 
    }    
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

    if (parseFloat(playerScores[1].innerHTML) === 7.5 && parseFloat(bankScores[1].innerHTML) != 7.5) {
        msgText.innerHTML = "¡Has ganado! Eres candidato a la banca"
        playerScores[0].innerHTML = parseInt(playerScores[0].innerHTML) + Math.min(parseInt(playerScores[2].innerHTML), parseInt(bankScores[0].innerHTML))
        bankScores[0].innerHTML = parseInt(bankScores[0].innerHTML) - parseInt(playerScores[2].innerHTML)
    }
    else if (parseFloat(bankScores[1].innerHTML) > 7.5) {
        msgText.innerHTML = "¡Has ganado!"
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

    startTutorial2Btn.disabled = false
}

const ShowCardTutorial1 = (playerIndex, cardIndex, dict) => {
    cards[playerIndex].src = dict[cardIndex]["src"]
    cardTitles[playerIndex].innerHTML = dict[cardIndex]["name"]
    cards[playerIndex].style.visibility = "visible"
    cardTitles[playerIndex].style.visibility = "visible"
}

const OrderPlayers = (playerList) => {
    let orderFull = []
    let order = []

    for (let index = 0; index < playerList.length; index++) {
        let number = parseInt(playerList[index]["cardId"].slice(0, 2))
        let palo = playerList[index]["cardId"].slice(-1)
        let position = 0

        for (let subIndex = 0; subIndex < orderFull.length; subIndex++) {
            if (number < orderFull[subIndex]["number"]) {
                position = subIndex
                break
            }

            if (number === orderFull["number"]) {
                let priorityNew = cardPriority[palo]
                let priorityCurrent = cardPriority[orderFull[subIndex]["palo"]]
                position = priorityNew < priorityCurrent ? subIndex : subIndex + 1
                break
            }
            position = subIndex + 1
        }

        player = {
            "name": playerList[index]["name"],
            "number": number,
            "palo": palo
        }
        if (position >= orderFull.length) {
            orderFull.push(player)
        }
        else {
            orderFull.splice(position, 0, player)
        }
    }

    for (let index = 0; index < orderFull.length; index++) {
        order.push(orderFull[index]["name"])
    }

    return order
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