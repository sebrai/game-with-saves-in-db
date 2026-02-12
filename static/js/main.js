let deck = ["Attack", "Attack", "Attack", "Defend", "Defend", "Debuff", "Buff"]; //mostly just a placeholder for an actual deck but it works for now, the deck is just an array of strings representing card types.
let hand = []; // the players hand, filled on initalize game and when cards are drawn.
let discardPile = []; // the discard pile, cards are added when played and reshuffled into the draw pile when the draw pile is empty.
let drawPile = []; //the draw pile, filled/shuffled on initalize game and then moved into hand when drawing cards
const HAND_SIZE = 5; //its the hand size, what did you expect?

function shuffle(array) { //function that takes an array (usually called with ... aka spread to copy the content out of the list (theres more to it than that but thats basically what it does))

for (let i = array.length - 1; i > 0; i--) { //basically, it starts by selecting the last element in the array and moves backwards for each loop, the current index is i.
const j = Math.floor(Math.random() * (i + 1)); //then it selects a random value between 0 and i (+1 to make it inclusive) and sets it to j
[array[i], array[j]] = [array[j], array[i]]; //swaps the string at the randomly selected value (j) with the string at the current index (i)
}
return array; //returns the newly shuffled array
}

function initializeGame() { 
    if (document.getElementById("hp").value == 0 ) { // chechs if you have already won or lost
        lose()
        return;
    }
    else if ( document.getElementById("e_hp").value == 0){
        win()
        return;
    }
drawPile = shuffle([...deck]); //shuffles the deck into the drawpile, deck remains unchanged as its a copy
hand = []; //resets the hand
discardPile = []; //resets the discard pile
drawCards(HAND_SIZE); //draw the max amount of cards to begin
}

function drawCards(num) { // draws cards based on the number when called
for (let i = 0; i < num; i++) { //loop where as long as i < the inputted number, it will keep drawing cards until it reaches the number or the max hand size
if (drawPile.length === 0) {
    reshuffleDiscardIntoDraw(); //if the draw pile is empty, shuffle discard into draw
}
if (drawPile.length === 0) {
    console.log("No cards left to draw!"); //console logging, shocking i know
    return; //stops it from drawing more cards
}
if (hand.length < HAND_SIZE) {
    hand.push(drawPile.pop()); //as long as theres space in the hand, it takes the last element from the draw pile and puts it in the hand (pop means it disappears from the drawpile after its moved basically)
    animateDrawCard(hand.length - 1,hand[hand.length-1]); // gets the index and the string to animate and style
} else {
    console.log("Hand is full!"); //pretty much self explanatory
    return;
}
}
}

function animateDrawCard(slotIndex,type) {
    const template = document.getElementById("test"); // gets the card template
    const card = template.cloneNode(true); // makes a copy of the template

    card.removeAttribute("id"); // to avoid duplicate IDs
    card.classList.add("draw-animation"); //adds the animation to the copy
    const spacing = 15; // vw between each card
    card.style.setProperty( "--draw-distance", `${(slotIndex + 1) * spacing}vw` //sets the spacing aka how far the card moves
    );
    
    card.style.backgroundColor //different bg colors for the different card types
    = type=="Attack" ? "#de2a2a" : type === "Defend" ? "#2ab4de" : type === "Debuff" ? "#41d167" : "#de2a99";
    let icon = document.createElement("img")
    card.addEventListener("click",()=>{
        console.log(type)
        playCard(type)
    })
    card.appendChild(icon) // creates image, puts the icon in the template copy, and then decides which icon to use depending on the card type
    icon.src = "/static/img/icons/"+ type +".png" // add style
    
card.style.animationDelay = `${slotIndex * 200}ms`; // delay between each card being animated, using the index to space the timing out evenl
    document.body.appendChild(card);
}
function reshuffleDiscardIntoDraw() {
drawPile = shuffle([...discardPile]) 
discardPile = []; //this function is pretty self explanatory
}

function playCard(cardName) {
if (cardName == "Attack") {
    console.log("You played an Attack card!");
    hit_e(10) 
}
}
function gethit(dmg = 5){
    let hp = Number(document.getElementById("hp").value) // get hp value from form
    hp-= dmg // remove dmg
    document.getElementById("hp").value = hp // set value back into form
    console.log("player hp is: " + hp) //log for clarity
    if (hp<=0) {
       lose()
        
    }
}
console.log("hello world")  

function hit_e(dmg){
    let hp = Number(document.getElementById("e_hp").value)
    hp-= dmg
    document.getElementById("e_hp").value = hp
    console.log("enemy hp is: " + hp)
    if (hp<=0) {
       win()
        
    }
}

function lose(){
     document.getElementById("done").value = 1 // marks game as complete
    let screen = document.getElementById("fadeOverlay")
    screen.style.pointerEvents = ""
    screen.style.opacity = 100+"%"
    let s_btn = document.createElement("button")
    s_btn.addEventListener("click",()=>{
        document.getElementById("save").click()
        console.log("lost")
    })
    screen.textContent ='"you lost"'
    screen.appendChild(s_btn)
    s_btn.textContent = "continue"
    
}
function win() {
     document.getElementById("done").value = 1 // marks game as complete
    let screen = document.getElementById("fadeOverlay")
    screen.style.opacity = 100+"%"
    let s_btn = document.createElement("button")
    s_btn.addEventListener("click",()=>{
        document.getElementById("save").click()
        console.log("lost")
    })
    screen.style.color ="yellowgreen"
    screen.textContent ='"you win"'
    screen.appendChild(s_btn)
    s_btn.textContent = "continue"
}
initializeGame();