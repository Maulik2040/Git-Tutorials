// Alert in-browser JavaScript - Does not return anything
// alert("This is a message");

// Promt in JS
// let name = prompt("What is you Name", "Guest");
// console.log(name);

//Confirm in JS
let deletepost = confirm("Do you really want to delete this post?");

if (deletepost) {
    // Code to delete the post
    console.log("Your post has been deleted successfully");
} else {
    // Code to cancel deletion of the post
    console.log("Your post is not been deleted");
}
console.log(deletepost);