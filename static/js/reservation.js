const reservationForm = document.getElementById("reservationForm");
const editButtons = document.getElementsByClassName("btn-edit");
const submitButton = document.getElementById("submitButton");
const deleteButtons = document.getElementsByClassName("btn-delete");
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reservationId = e.target.getAttribute("data-reservation_id");
      deleteConfirm.href = `delete_reservation/${reservationId}`;
    });
  }

  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let reservationId = e.target.getAttribute("data-reservation_id");
      // reservationForm.setAttribute("action", `edit_reservation/${reservationId}`);
      submitButton.href = `edit_reservation/${reservationId}`;
      console.log(document.getElementById('my-paragraph'))
    });
  }