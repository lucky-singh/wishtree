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

Date.prototype.toDateInputValue = function() {
  var local = new Date(this);
  local.setMinutes(this.getMinutes() - this.getTimezoneOffset());
  return local.toJSON().slice(0, 10);
};

$(document).ready(function() {
  $("#featureTitle").blur(function formValidator() {
    let title = $("#featureTitle").val();

    $(".error").remove();

    if (title.length < 1) {
      $(this).after('<span class= "error" >Title is required.</span>');
      $(this).addClass("is-invalid");
    } else {
      $(this).removeClass("is-invalid");
    }
  });

  $("#featureDescription").blur(function formValidator() {
    let description = $("#featureDescription").val();

    $(".error").remove();

    if (description.length < 1) {
      $(this).after('<span class= "error" >Description is required.</span>');
      $(this).addClass("is-invalid");
    } else {
      $(this).removeClass("is-invalid");
    }
  });

  // Setting date to todays date as default
  $("#featureTargetDate").val(new Date().toDateInputValue());
});
