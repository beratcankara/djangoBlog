function publishArticle(checkbox, articleId) {
    if (checkbox.checked) {
      window.location.href = '/dashboard/publishArticle/' + articleId;
    }
    else{
      window.location.href = '/dashboard/publishArticle/' + articleId;
    }
  }