let key1 = 0;
let key2 = 0;

screenX = window.innerWidth
screenY = window.innerHeight

console.log(screenX)

function setup() {
  createCanvas(screenX, screenY);

  for (i=1;i<7000;i++) {
    fill(240,240,250);
    stroke(240,240,250);
    circle(random(1,screenX), random(1,screenY), random(1,2))
  }
}

//* button press code
const input1 = document.getElementById('div-submit-1');
const input2 = document.getElementById('div-submit-2');

input1.addEventListener(keyPressed, (event) => {
  console.log('key pressed')
  if (event.key === 'A') {
    console.log('key pressed');
  }
})

// function keypressed(key) {

//   const input1 = document.getElementById('div-submit-1')
//   const input2 = document.getElementById('div-submit-2')

//   if (key === 1) {
//     if (input1.key === 'A') {
//       console.log('key1 is pressed');
//       key1 = 1;
//       } else if (key1 == 1) {
//         key1 = 0;
//         console.log('key1 is no longer pressed')
//     }
//     if (input1.key === 'D') {
//       console.log('key1 is pressed');
//       key2 = 1;
//       } else if (key2 == 1) {
//         key2 = 0;
//         console.log('key1 is no longer pressed')
//     }
//   }
//   if (key === 2) {
//     if (input2.key === 'A') {
//       console.log('key1 is pressed');
//       key1 = 1;
//       } else if (key1 == 1) {
//         key1 = 0;
//         console.log('key1 is no longer pressed')
//     }
//     if (input2.key === 'D') {
//       console.log('key1 is pressed');
//       key2 = 1;
//       } else if (key2 == 1) {
//         key2 = 0;
//         console.log('key1 is no longer pressed')
//     }
//   }
  
// }
