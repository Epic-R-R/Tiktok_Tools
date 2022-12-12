const imgs = [];
$(document).ready(function () {
  $("button").click(function () {
    $.post(
      "https://www.howtotechies.com/pinterest-video-downloader",
      {
        "video-url": "_sullivan__z",
      },
      function (data, status) {
        console.log(status);
        $(data)
          .find("img")
          .each(function () {
            imgs.push($(this).attr("src"));
          });
        console.log(imgs[1]);
      }
    );
  });
});
