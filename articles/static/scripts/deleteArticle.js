document.addEventListener("DOMContentLoaded", function () {
    var deleteSelectedButton = document.getElementById("deleteArticle");
    deleteSelectedButton.addEventListener("click", function () {
      var selectedCheckboxes = document.querySelectorAll('input[type="checkbox"]:checked');
      var confirmation = confirm("Seçili makaleleri silmek istediğinizden emin misiniz?");
      if (confirmation) {
        var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        var checkboxes = Array.from(selectedCheckboxes);
        var promises = checkboxes.map(function (checkbox) {
          var articleId = checkbox.value;
          var url = "/dashboard/deleteArticle/" + articleId;
          var data = {
            csrfmiddlewaretoken: csrfToken,
          };
          return fetch(url, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": csrfToken,
            },
            body: JSON.stringify(data),
          });
        });
        Promise.all(promises)
          .then(function (responses) {
            var successful = responses.every(function (response) {
              return response.ok;
            });
            if (successful) {
              location.reload(); // Silme işlemi başarılı olduğunda sayfayı yenile
            } else {
              console.error("Silme işlemi başarısız.");
            }
          })
          .catch(function (error) {
            console.error(error);
          });
      }
    });
  });
  