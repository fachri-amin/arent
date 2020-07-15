$(document).ready(function () {
  const default_option = document.querySelector("select option:first-child");

  default_option.value = "default";

  $(".btn-cari").click(function (e) {
    e.preventDefault();
    $.ajax({
      url: "",
      type: "get",
      data: {
        cari: $(".cari").val(),
        cari_provinsi: $(".cari-provinsi").val(),
        cari_jenis_kendaraan: $("input[name=jenis_kendaraan]:checked").val(),
      },
      success: function (response) {
        console.log(response);
      },
    });
  });
});
