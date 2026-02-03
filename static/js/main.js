let deck = ["Attack", "Attack", "Attack", "Defend", "Defend", "Debuff", "Buff"];
let hand = [];
let discardPile = [];
let drawPile = [];
const HAND_SIZE = 5;

function shuffle(array) {

for (let i = array.length - 1; i > 0; i--) {
const j = Math.floor(Math.random() * (i + 1));
[array[i], array[j]] = [array[j], array[i]];
}
return array;
}

function initializeGame() {
drawPile = shuffle([deck]);
hand = [];
discardPile = [];
drawCards(HAND_SIZE);
}

function drawCards(num) {
for (let i = 0; i < num; i++) {
if (drawPile.length === 0) {
    reshuffleDiscardIntoDraw();
}
if (drawPile.length > 0) {
    if (hand.length < HAND_SIZE)
        hand.push(drawPile.pop());
    else {
        console.log("Hand is full!");
        return;}
}
}
}

function reshuffleDiscardIntoDraw() {
drawPile = shuffle([discardPile])
discardPile = [];
}

function playCard(cardName) {
if (cardName == "Attack") {
    console.log("You played an Attack card!");
}
}

console.log("hello world")  


