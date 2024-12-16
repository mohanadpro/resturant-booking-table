

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));

const reservationForm = document.getElementById("reservationForm");
const editButtons = document.getElementsByClassName("btn-edit");
const submitButton = document.getElementById("submitButton");
const deleteButtons = document.getElementsByClassName("btn-delete");
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      console.log(e.target)
      let reservationId = e.target.getAttribute("reservation_id");
      console.log(reservationId);
      deleteConfirm.href = `delete_reservation/${reservationId}`;
      deleteModal.show();
    });
  }

  for (let button of editButtons) {
    console.log('HELLO')
    button.addEventListener("click", (e) => {
      let reservationId = e.target.getAttribute("reservation_id");

      console.log(reservationId)
      // let reservation = document.getElementById(`reservation${reservationId}`).innerText;
      // commentText.value = commentContent;
      submitButton.innerText = "Update";
      reservationForm.setAttribute("action", `edit_reservation/${reservationId}`);
    });
  }