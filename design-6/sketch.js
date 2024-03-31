//drawing
let buildingHeight0 = 0;
let buildingHeight1 = 0;
let buildingHeight2 = 0;
let buildingHeight3 = 0;
let buildingHeight4 = 0;
let buildingHeight5 = 0;
let buildingHeight6 = 0;
let windowWidth = 30;
let windowHeight = 30;
let windowGap = 20;
let windowColor = (137, 137, 138);

//speed
let speed = 5;
let x;
let y;
let dir;
//juego
let points = 1;

//batman
let batman;
let alphaValue = 0;
let batty;
let guason;
let boom, song1, song2, song3;

let contador;

function preload() {
  song1 = loadSound("Music Summative - Hero.mp3");
  song2 = loadSound("Music Summative. - Happy.mp3");
  song3 = loadSound("sAD SONMG sUMMATIVE.mp3");
}

function setup() {
  createCanvas(1000, 600);
  x = 0;
  y = 0;
  dir = 1;

  //images
  batman = loadImage("BATMAN 2.jpeg");
  batty = loadImage("Batman_personaje-removebg-preview.png");
  guason = loadImage("guasom-removebg-preview.png");
  boom = loadImage("boom.png");

 
  contador = 0;

  song2.play();
}

function draw() {
  background(0);

  //songss

  // Draw the building continuously
  if (buildingHeight0 < height - 200) {
    buildingHeight0 += 2;
  }

  if (buildingHeight1 < height - 50) {
    buildingHeight1 += 2;
  }

  if (buildingHeight2 < height - 300) {
    buildingHeight2 += 2;
  }

  if (buildingHeight3 < height - 80) {
    buildingHeight3 += 2;
  }

  if (buildingHeight4 < height - 200) {
    buildingHeight4 += 2;
  }

  if (buildingHeight5 < height - 400) {
    buildingHeight5 += 2;
  }

  if (buildingHeight6 < height - 80) {
    buildingHeight6 += 2;
  }

  // Draw the building
  fill(150);
  rect(0, height - buildingHeight0, 100, buildingHeight0);

  rect(100, height - buildingHeight1, 170, buildingHeight1);

  rect(270, height - buildingHeight2, 130, buildingHeight2);

  rect(400, height - buildingHeight3, 210, buildingHeight3);

  rect(610, height - buildingHeight4, 140, buildingHeight4);

  rect(750, height - buildingHeight5, 210, buildingHeight5);

  rect(960, height - buildingHeight6, 100, buildingHeight6);

  // Draw windows
  if (contador > 0 && contador <1000) {
    fill(random(255), random(255), random(255)); //color
  } else {
    fill(0);
  }

  //building #1
  for (
    let y = windowGap;
    y < height - windowGap;
    y += windowHeight + windowGap
  ) {
    for (let x = 0; x < 60; x += windowWidth + windowGap) {
      rect(x, height - buildingHeight4 + y, windowWidth, windowHeight);
    }
  }

  //building #2
  for (
    let y = windowGap;
    y < height - windowGap;
    y += windowHeight + windowGap
  ) {
    for (let x = 120; x < 270; x += windowWidth + windowGap) {
      rect(x, height - buildingHeight1 + y, windowWidth, windowHeight);
    }

    //building#6
    for (
      let y = windowGap;
      y < height - windowGap;
      y += windowHeight + windowGap
    ) {
      for (let x = 770; x < 950; x += windowWidth + windowGap) {
        rect(x, height - buildingHeight5 + y, windowWidth, windowHeight);
      }
    }

    //building #5
    for (
      let y = windowGap;
      y < height - windowGap;
      y += windowHeight + windowGap
    ) {
      for (let x = 650; x < 710; x += windowWidth + windowGap) {
        rect(x, height - buildingHeight0 + y, windowWidth, windowHeight);
      }
    }

    //building #3
    for (
      let y = windowGap;
      y < height - windowGap;
      y += windowHeight + windowGap
    ) {
      for (let x = 300; x < 370; x += windowWidth + windowGap) {
        rect(x, height - buildingHeight2 + y, windowWidth, windowHeight);
      }
    }

    //building #6
    for (
      let y = windowGap;
      y < height - windowGap;
      y += windowHeight + windowGap
    ) {
      for (let x = 440; x < 590; x += windowWidth + windowGap) {
        rect(x, height - buildingHeight3 + y, windowWidth, windowHeight);
      }
    }

    //Building 7
    for (
      let y = windowGap;
      y < height - windowGap;
      y += windowHeight + windowGap
    ) {
      for (let x = 980; x < 1000; x += windowWidth + windowGap) {
        rect(x, height - buildingHeight6 + y, windowWidth, windowHeight);
      }
    }
  }


  if (contador >= 1200){
    song2.stop();
        song3.play();

  }else if (contador == 2800) {
    song3.stop();
    song1.play();
  }

  if (song1.isPlaying()) {
    tint(255, alphaValue);
    image(batman, 750, 240, batman.width / 4.7, batman.height / 4.7);

    image(batty, mouseX, 390, 120, 200);

    if (alphaValue < 255) {
      alphaValue += 2;
    }
  }

  
  if (song3.isPlaying && contador > 1000) { //?
    tint(255, alphaValue);


    image(guason, x, 390, 120, 200);

    x = x + 5 * dir;

    if (x >= width) {
      dir = -1;
    }
    if (x <= 0) {
      dir = 1;
    }
  
  
      // image(boom, 150, 100, 850, 450);
   

    if (alphaValue < 255) {
      alphaValue += 2;
    }
    
    
    
    
    
  }
  
  
  if(contador == 1200){
fill(random(255), random(255), random(255));
    for (
      let y = windowGap;
      y < height - windowGap;
      y -= windowHeight - windowGap
    ) {
      for (let x = 440; x < 590; x += windowWidth + windowGap) {
        rect(x, height - buildingHeight0 + y, windowWidth, windowHeight);
      }
    
    }
  }
  //floor
  fill(91, 91, 91);
  rect(0, 570, 1000, 200);

  //songs

  //   //game part
  //   print = "Points:";

  //   if (mouseX == x) {
  //     points++;
  //   }
  //   console.log(points);
 
  contador = contador +1;
  print (contador);
}
