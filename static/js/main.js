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
drawPile = shuffle([...deck]);
hand = [];
discardPile = [];
drawCards(HAND_SIZE);
}

function drawCards(num) { // draws cards based on the number when called
for (let i = 0; i < num; i++) { //loop where as long as i < the inputted number, it will keep drawing cards until it reaches the number or the max hand size
if (drawPile.length === 0) {
    reshuffleDiscardIntoDraw();
}
if (drawPile.length === 0) {
    console.log("No cards left to draw!");
    return;
}
if (hand.length < HAND_SIZE) {
    hand.push(drawPile.pop());
    animateDrawCard(hand.length - 1);
} else {
    console.log("Hand is full!");
    return;
}
}
}

function animateDrawCard(slotIndex) {
    const template = document.getElementById("test");
    const card = template.cloneNode(true);

    card.removeAttribute("id");          // avoid duplicate IDs
    card.classList.add("draw-animation");
    const spacing = 15; // vw per card
    card.style.setProperty( "--draw-distance", `${(slotIndex + 1) * spacing}vw`
    );
card.style.animationDelay = `${slotIndex * 200}ms`;
    document.body.appendChild(card);
}
function reshuffleDiscardIntoDraw() {
drawPile = shuffle([...discardPile])
discardPile = [];
}

function playCard(cardName) {
if (cardName == "Attack") {
    console.log("You played an Attack card!");
}
}
function gethit(dmg = 5){
    let hp = Number(document.getElementById("hp").value)
    hp-= dmg
    document.getElementById("hp").value = hp
    console.log(hp)
}
console.log("hello world")  

function hit_e(dmg){
    let hp = Number(document.getElementById("e_hp").value)
    hp-= dmg
    document.getElementById("e_hp").value = hp
    console.log(hp)
}
initializeGame();