function myFunction(elmnt) {
  console.log(elmnt);
  kala = elmnt._id
  console.log(kala.$oid);
  console.log("/api/product?id=" + kala.$oid)
  window.location.replace("/api/product?id=" + kala.$oid)
}