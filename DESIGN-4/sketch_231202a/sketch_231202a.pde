import processing.sound.*;

//Image
PImage img;

SoundFile file;

void setup() {
  size(1000, 800);
  img = loadImage("./img.jpg");

  file = new SoundFile(this, "./AUDIO.mp3");
}

void draw() {

  image(img, 0, -180, 1000, 1000);
  println(mouseX);
  
    if (mouseX > 500) {
    file.play();
  } else if (mouseX < 500 && file.isPlaying()){
    file.stop();
  }
  
  println(file.isPlaying());
}
