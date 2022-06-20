let jcrop;

function readURL(input) {
  let el = document.getElementById("searchbutton");

  let imageDiv = document.getElementById("resultImage");

  while (imageDiv.firstChild) imageDiv.removeChild(imageDiv.firstChild);

  if (el) {
    el.remove();
  }

  if (jcrop) {
    jcrop.destroy();
  }

  if (input.files && input.files[0]) {
    const reader = new FileReader();
    reader.onload = function (e) {
      $("#queryImage").attr("src", e.target.result);

      let btn = document.createElement("button");
      btn.innerHTML = "Search";
      btn.id = "searchbutton";
      btn.addEventListener("click", async () => {
        btn.style.display = "none";

        let loadingIcon = document.createElement("div");
        loadingIcon.className = "loader";

        document.getElementById("searchdiv").append(loadingIcon);

        let data = new FormData();
        data.append("file", input.files[0]);

        let responseData;

        await fetch("/test", {
          method: "POST",
          body: data,
        })
          .then((response) => response.json())
          .then((respData) => (responseData = respData));

        let resultText = document.createElement("h2");
        text = document.createTextNode(`Result: `);
        resultText.appendChild(text);

        let resultBox = document.getElementById("resultImage");
        resultBox.appendChild(resultText);

        // Create text element
        // Display beautified json
        let result = document.createElement("pre");
        // Increase text size of this
        result.style.fontSize = "2.5em";
        result.innerHTML = JSON.stringify(responseData[0], null, 2);
        resultBox.appendChild(result);

        if (responseData[0].have_ninedash === 1) {
          // Get image from static folder
          let image = document.createElement("img");
          image.src = `/static/upload.jpg`;
          resultBox.appendChild(image);
        }

        resultBox.style.display = "block";
        loadingIcon.style.display = "none";
      });
      document.getElementById("searchdiv").appendChild(btn);
    };
    reader.readAsDataURL(input.files[0]);
  }
}

window.addEventListener("DOMContentLoaded", () => {
  const imageInput = document.getElementById("imageInput");

  imageInput.addEventListener("change", (e) => {
    readURL(e.target);
  });
});
