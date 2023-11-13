let mic;



function setup() {

  createCanvas(400, 400);



  // Create an Audio input

  mic = new p5.AudioIn();



  // start the Audio Input.

  // By default, it does not .connect() (to the computer speakers)

  mic.start();

}



function draw() {

  background(200);



  // Get the overall volume (between 0 and 1.0)

  let vol = mic.getLevel();

  fill(255,25,0);

  stroke(0);



  // Draw an ellipse with height based on volume

  

  ellipse(width / 2, height/2, vol*200, vol*200);
}