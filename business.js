var counter = 0;
var velocityStream;
var batteryVoltageStream;
var rpmStream;
var headingStream;
var engineCoolantStream;
var throttleStream;
var intakeAirTempStream;
var engineLoadStream;
var engineoiltemp;
var mafStream;

var vehicle;

var mpgReadings = 0;
var prevMpg = 0;
var curVss;

function calcAverageMpg(newMpg) {
	prevMpg += parseInt(newMpg);
	mpgReadings++;

	var averageMpg = prevMpg / mpgReadings;
	$("#avgmpg").text(Math.floor(averageMpg));
}


var velReadings = 0;
var prevVel = 0;

function calcAverageVelocity(newVel) {
	prevVel += parseInt(newVel);
	velReadings++;

	var averageVel = prevVel / velReadings;
	$("#avgspeed").text(Math.floor(averageVel));
}

window.onload = function()
{
    var vehicle = tizen.vehicle

    var velocityUnits = $('#velocityUnits');
    velocityUnits.click(function() {
                              if(velocityUnits.text() === "MPH")
                              {
                                  velocityUnits.text("KPH");
                              }
                              else velocityUnits.text("MPH");
                        });

   vehicle.vehicleSpeed.subscribe(function(data) {
				  console.log("Vehicle data" + data.speed);
                                  adjvalue = data.speed;
                                  curVss = adjvalue;
                                  var velocityUnits = $('#velocityUnits');

                                  if(velocityUnits.text() === "MPH")
                                      adjvalue = Math.floor(adjvalue * 0.62137);

                                  $('#velocity').text(adjvalue);

                                  calcAverageVelocity(adjvalue);
                              });

   vehicle.engineSpeed.subscribe(function(data) {
                                  var value = data.speed;
                                  if(value > 10000) value =10000;
                                  var needleDegs = value / 10000 * 180;
                                  $('#rpms').text(value);
                                  $('#rpmNeedle').css("-webkit-transform","rotate("+needleDegs+"deg)");
                              });

    vehicle.transmission.subscribe(function(data) {
                                  value = data.gear;
                                  if(value == 128)
                                      $('#gear').text('Reverse');
                                  else if(value == 0)
                                      $('#gear').text('Neutral');
                                  else $('#gear').text(value);

                              });

    vehicle.steeringWheel.subscribe(function(data) {
                                  value = data.angle;
                                  $('#wheel').css("-webkit-transform","rotate("+value+"deg)");
                                  $('#machinegun').css("-webkit-transform","rotate("+value+"deg)");
                              });

    vehicle.throttlePosition.subscribe(function(data) {
                                  value = data.value;
                                  var needleDegs = (value / 100 * 180) + 270

                                  $('#throttleNeedle').css("-webkit-transform","rotate("+needleDegs+"deg)");

                              });

    vehicle.engineCoolant.subscribe(function(data) {
                                  value = data.temperature;
                                  var needleDegs = (value / 180 * 70) + 270

                                  $('#engineCoolantNeedle').css("-webkit-transform","rotate("+needleDegs+"deg)");

                              });
}
