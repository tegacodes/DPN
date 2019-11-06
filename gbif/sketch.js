let table;
let links = [];
let images = [];
let p = 0;

function preload() {
  //my table is comma separated value "csv"
  //and has a header specifying the columns labels
  table = loadTable('data/multimedia.csv', 'csv', 'header');
  //the file can be remote
  //table = loadTable("http://p5js.org/reference/assets/mammals.csv",
  //                  "csv", "header");
  //cycle through the table
    //print(table.getColumn('name'));


}

function setup() {
  createCanvas(400, 600);
   for (let r = 0; r < table.getRowCount(); r++) {
    //   for (let c = 0; c < table.getColumnCount(); c++){
    links[r] = table.getString(r, 2);
    print(links[r]);
}
  for (let i = 0; i < 100; i++) {
    images[i]=createImg(links[i]);
    images[i].hide();
  }


  
}

function draw() {
  //background(220);
    image(images[0],0,0, width, height);


  p++;
  noLoop();

}