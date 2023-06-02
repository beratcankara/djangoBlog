// JavaScript kodunu HTML dosyasına dahil ettiyseniz, DOMContentLoaded olayını dinleyerek kodun çalışmasını sağlayabilirsiniz.
document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript kodu çalışıyor");
    // Sil butonunu seçin
    var deleteButton = document.getElementById("deleteComment");
    var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    // Sil butonuna tıklanma olayını dinleyin
    deleteButton.addEventListener("click", function() {
      // Comment ID'sini alın
      var commentId = deleteButton.getAttribute("data-comment-id");
  
      // AJAX isteği gönderin
      var xhr = new XMLHttpRequest();
      xhr.open("POST", "/deleteComment/" + commentId, true); // Silme URL'sine comment ID'sini ekleyin
      xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
      xhr.setRequestHeader("X-CSRFToken", csrfToken); // CSRF token'ını isteğe ekle
      xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
            // Silme işlemi başarılı olduğunda yapılacak işlemler
            window.location.reload(); // Sayfayı yenilemek için örnek olarak
          } else {
            // Silme işlemi başarısız olduğunda yapılacak işlemler
            console.log("Silme işlemi başarısız");
          }
        }
      };
      xhr.send();
    });
  });
  