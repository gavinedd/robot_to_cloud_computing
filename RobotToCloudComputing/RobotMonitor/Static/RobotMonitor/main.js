// import './style.css'




// Default Image folder
const imageFolder = "../static/images/";

// Get the Image elements from the DOM
let imgContainer = document.getElementById('imgContainer');
let leftImage = document.getElementById('leftImage');
let rightImage = document.getElementById('rightImage');

// Initialize an array to store default left and right images
let leftImages = [imageFolder + 'left_1644100125.889648_visual_rgb.jpg']; //'Grass_0/left_1644100125.889648_visual_rgb.jpg'
let rightImages = [imageFolder + 'right_1644100125.889648_visual_rgb.jpg']; //'Grass_0/right_1644100125.889648_visual_rgb.jpg'



// setInterval() is a built-in javascript function that repeats a given function 
//		at every given time interval specified in milliseconds. Here, I have used 
//		setInterval() to allow the image feed to loop through the arrays of pictures
let i = 0;
setInterval(function(){
	if (leftImages[i] != null){
		leftImage.src = leftImages[i];
	}
	if (rightImages[i] != null){
		rightImage.src = rightImages[i];
	}
	
	i++;
	if (i === leftImages.length) {
		i = 0;
	}
}, 200);



// Get the group of radio buttons from the DOM
let pictureTypeRadio = document.getElementsByName("pictureType");

// Add an event listener to each of the radio buttons individually
for(let i = 0; i < pictureTypeRadio.length; i++) {
	pictureTypeRadio[i].addEventListener('change', event => {
		populateImageArray();
	});
}


// Get the file selector and add an event listener to it
let fileSelect = document.getElementById("fileSelect");
fileSelect.addEventListener('change', event => {
	populateImageArray();
});



// populateImageArray() is the function to be called whenever a radio button 
//		is selected or new files are selected via the file selector. It is
//		designed to populate the image array with the appropriate pictures
//		from the list of all selected images in the file selector.
function populateImageArray(){
	
	// Retrieve FileList object from the file selector
	const files = document.querySelector('#fileSelect').files;
	
	// Retrieve the selected radio button from the DOM indicating type of 
	//		picture to be displayed
	var picType;
	for(i = 0; i < pictureTypeRadio.length; i++) {
		if (pictureTypeRadio[i].checked){
			picType = pictureTypeRadio[i].value;
			//console.log("Picture Type: " + picType);
		}
	}
	
	// Empty the image arrays
	leftImages = [];
	rightImages = [];


	// Loop through all selected files
	for (let i = 0; i < files.length; i++) {
		
		// Get the current file
		let file = files.item(i);
		//console.log(file.name);
		
		// Based off of the type of picture the user wants displayed,
		//		add the appropriate images to the image arrays. Also
		//		keep in mind that since some images are rotated, we 
		//		will need to update the image classes.
		if (picType === "rgb") {
			// RGB images need rotated. Update the image classes appropriately
			imgContainer.className = "rotatedImgContainer";
			leftImage.className = "rotatedImg";
			rightImage.className = "rotatedImg";
			
			// Check whether the file is a visual_rgb image
			if (file.name.startsWith("left") && file.name.endsWith("visual_rgb.jpg")){
				leftImages.push(imageFolder + file.name);
			}
			if (file.name.startsWith("right") && file.name.endsWith("visual_rgb.jpg")){
				rightImages.push(imageFolder + file.name);
			}
		}
		else if (picType === "depth") {
			// Depth images need rotated. Update the image classes appropriately.
			imgContainer.className = "rotatedImgContainer";
			leftImage.className = "rotatedImg";
			rightImage.className = "rotatedImg";
			
			// Check whether the image is a cv_depth image.
			if (file.name.startsWith("left") && file.name.endsWith("cv_depth.jpg")){
				leftImages.push(imageFolder + file.name);
			}
			if (file.name.startsWith("right") && file.name.endsWith("cv_depth.jpg")){
				rightImages.push(imageFolder + file.name);
			}
		}
		else if (picType === "infrared") {
			// Infrared images do not need rotated. Update the image classes to verify that
			//		these images are oriented correctly.
			imgContainer.className = "imgContainer";
			leftImage.className = "img";
			rightImage.className = "img";
			
			// Check whether the image is an infrared image.
			if (file.name.startsWith("right") && !(file.name.endsWith("visual_rgb.jpg")) && !(file.name.endsWith("cv_depth.jpg"))){
				leftImages.push(imageFolder + file.name);
			}
			if (file.name.startsWith("left") && !(file.name.endsWith("visual_rgb.jpg")) && !(file.name.endsWith("cv_depth.jpg"))){
				rightImages.push(imageFolder + file.name);
			}
		}
	}
}


////////////////////////////////// TO-DO ////////////////////////////////////////

//let url = "http://127.0.0.1:8080/RobotMonitor/data/get_data";

//fetch(url)
//	.then(response => response.json())
//	.then (data => {
//		console.log(data);
//	});
