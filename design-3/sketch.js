let bg;
let record_player;
let song;

function setup() {
  createCanvas(1000, 800);

  record_player = loadImage('./img/record_player-removebg-preview.png')
  bg = loadImage('./img/1920s_party.webp')
  background(bg);

  song = loadSound('PATH TO MUSIC FILE') // Ponga aquí el path al file con la música. Por alguna razón cuando yo la pongo el file no funciona
}

let i = 1;
condition = 1;

function draw() {
  background(bg)
  image(record_player, -50, 300);

  if (condition == 1) {
      background(bg);
      image(record_player, -50, 300);
      noFill();
      stroke(255)
      bezier(
      600,
      100,
      300+i,
      300+i,
      400+i,
      400+i,
      250,
      450
      );
      
      noFill();
      stroke(255)
      bezier(
      610,
      110,
      300+i,
      300+i,
      400+i,
      400+i,
      260,
      460
      );
      
      noFill();
      stroke(255)
      bezier(
      620,
      120,
      300+i,
      300+i,
      400+i,
      400+i,
      270,
      470
      );
      
      noFill();
      stroke(255)
      bezier(
      630,
      130,
      300+i,
      300+i,
      400+i,
      400+i,
      280,
      480
      );
      
      noFill();
      stroke(255)
      bezier(
      640,
      140,
      300+i,
      300+i,
      400+i,
      400+i,
      290,
      490
      );
      
      if (i == 50) {
        i = 1
      }
      i++
  }

}

function mousePressed() {
  console.log('awddw')
  if (condition == 1) {
    condition = 0;
  } else {
    condition = 1;
  }
  if (song.isPlaying()) {
    song.stop();
  } else {
    song.play();
  }
}
