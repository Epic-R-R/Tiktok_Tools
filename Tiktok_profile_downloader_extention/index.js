const downloadBtnEl = document.getElementsByClassName("btn");
const inputEl = document.getElementById("name");

downloadBtnEl[0].addEventListener("click", function () {
  console.log(inputEl.value);
  const imgs = [];
  $(document).ready(function () {
    $.post(
      "https://www.howtotechies.com/pinterest-video-downloader",
      {
        "video-url": inputEl.value,
      },
      function (data, status) {
        console.log(status);
        $(data)
          .find("img")
          .each(function () {
            imgs.push($(this).attr("src"));
          });
        window.open(imgs[1]);
      }
    );
  });
});
