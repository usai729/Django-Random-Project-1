function getPairsJSON() {
  fetch("pair", {
    method: "GET",
  })
    .then((resp) => {
      return resp.json();
    })
    .then((respFinal) => {
      for (
        let i = 0;
        i <= respFinal.confirmed_transactions.data.length - 1;
        i++
      ) {
        console.log(respFinal.confirmed_transactions.data[i].datetime);
      }
    });
}

window.onload = getPairsJSON();
