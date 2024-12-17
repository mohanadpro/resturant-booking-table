

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));

const reservationForm = document.getElementById("reservationForm");
const editButtons = document.getElementsByClassName("btn-edit");
const submitButton = document.getElementById("submitButton");
const deleteButtons = document.getElementsByClassName("btn-delete");
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reservationId = e.target.getAttribute("data-reservation_id");
      deleteConfirm.href = `delete_reservation/${reservationId}`;
      deleteModal.show();
    });
  }

  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let reservationId = e.target.getAttribute("data-reservation_id");
      // let reservation = document.getElementById(`reservation${reservationId}`).innerText;
      // commentText.value = commentContent;
      submitButton.innerText = "Update";
      reservationForm.setAttribute("action", `edit_reservation/${reservationId}`);
    });
  }