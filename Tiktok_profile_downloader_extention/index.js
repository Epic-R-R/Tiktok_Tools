const downloadBtnEl = document.getElementsByClassName("btn");
const inputEl = document.getElementsByClassName("form__field");

downloadBtnEl[0].addEventListener("click", function () {
  let imgSrc = "";
  $(document).ready(function () {
    $.post(
      "https://www.howtotechies.com/pinterest-video-downloader",
      {
        "video-url": inputEl.value,
      },
      function (data) {
        $(data)
          .find("img")
          .each(function () {
            imgSrc = $(this).attr("src");
          });
        console.log(imgSrc);
      }
    );
  });
});
