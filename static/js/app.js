// Function to display form to add new feature
function toggleFeatureRequestForm() {
  let button = document.getElementById("formButton");
  let form = document.getElementById("form1");
  /* Condition looks inverse as script is looking into inline style to form tag 
  and couldn't locate there so irrespective of display property it's going to else block on first load */
  if (form.style.display == "block") {
    form.style.display = "none";
    button.textContent = "New Feature Request";
  } else {
    form.style.display = "block";
    button.textContent = "Cancel";
  }
}
