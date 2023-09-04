function copyToClipboard(value) {
  var input = document.createElement("input");
  input.style.position = "absolute";
  input.style.left = "-9999px";
  document.body.appendChild(input);
  input.value = value;
  input.select();

  var response_message = document.execCommand("copy");

  document.body.removeChild(input);

  if (response_message) {
    alert("Copied to clipboard");
  } else {
    alert("Failed to copy");
  }
}

function editDetails(detailType) {
  var editElementID = detailType == "email_edit" ? "myemail" : "myupi";
  var currentValue = document.getElementById(editElementID).textContent;

  var form = document.createElement("form");
  form.setAttribute("method", "get");
  form.setAttribute("action", "/home/edit/");

  var inputHidden = document.createElement("input");
  inputHidden.type = "hidden";
  inputHidden.name = "editType";
  inputHidden.value = editElementID;

  var input = document.createElement("input");
  input.type = editElementID == "myemail" ? "email" : "number";
  input.value =
    editElementID == "myemail" ? currentValue : parseInt(currentValue);
  input.name = "newInfo";

  var submit = document.createElement("button");
  submit.type = "submit";
  submit.innerHTML = "Edit";

  form.appendChild(inputHidden);
  form.appendChild(input);
  form.appendChild(submit);

  document.getElementById(editElementID).appendChild(form);
  document.getElementById(editElementID).id = "";
}
