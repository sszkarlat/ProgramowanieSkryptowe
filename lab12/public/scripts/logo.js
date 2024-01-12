function draw() {
  "use strict";

  var canvas = document.getElementById("canvas");
  var ctx = canvas.getContext("2d");

  // Rysuj samochod
  ctx.beginPath();
  ctx.moveTo(2 + 1.5, 40 - 15);
  ctx.lineTo(8 + 1.5, 32 - 15);
  ctx.lineTo(30.6 + 1.5, 32 - 15);
  ctx.arc(30 + 1.5, 36 - 15, 4, 30, 2 * Math.PI);
  ctx.lineTo(34 + 1.5, 36 - 15);
  ctx.lineTo(34 + 1.5, 40 - 15);
  ctx.lineTo(42 + 1.5, 40 - 15);
  ctx.arc(42 + 1.5, 44 - 15, 4, 30, 2 * Math.PI);
  ctx.lineTo(46 + 1.5, 48 - 15);
  ctx.lineTo(37.4 + 1.5, 48 - 15);
  ctx.lineTo(13.6 + 1.5, 48 - 15);
  ctx.lineTo(2 + 1.5, 48 - 15);
  ctx.lineTo(2 + 1.5, 40 - 15);
  ctx.fillStyle = "#F3D723";
  ctx.fill();
  ctx.stroke();

  // Rysuj okna
  ctx.beginPath();
  ctx.moveTo(8 + 2.5, 36 - 11);
  ctx.lineTo(8 + 2.5, 32 - 12);
  ctx.lineTo(30.6 - 2.5, 32 - 12);
  ctx.arc(30 - 2.5, 36 - 12, 4, 30, 2 * Math.PI);
  ctx.lineTo(34 - 2.5, 36 - 11);
  ctx.lineTo(34 - 2.5, 36 - 11);
  ctx.lineTo(8 + 2.5, 36 - 11);
  ctx.fillStyle = "#898888";
  ctx.fill();
  ctx.stroke();

  // Rysuj kola
  ctx.beginPath();
  ctx.arc(34 + 1.5, 46 - 15, 4, 0, 2 * Math.PI);
  ctx.fillStyle = "black";
  ctx.fill();
  ctx.stroke();

  ctx.beginPath();
  ctx.arc(34 + 1.5, 46 - 15, 1, 0, 2 * Math.PI);
  ctx.fillStyle = "white";
  ctx.fill();
  ctx.stroke();

  ctx.beginPath();
  ctx.arc(10 + 1.5, 46 - 15, 4, 0, 2 * Math.PI);
  ctx.fillStyle = "black";
  ctx.fill();
  ctx.stroke();

  ctx.beginPath();
  ctx.arc(10 + 1.5, 46 - 15, 1, 0, 2 * Math.PI);
  ctx.fillStyle = "white";
  ctx.fill();
  ctx.stroke();
}
