const editButtons = document.getElementsByClassName("btn-edit");
const submitButton = document.getElementById("submitButton");
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reservationId = e.target.getAttribute("data-reservation_id");
      deleteConfirm.href = `delete_reservation/${reservationId}`;
    });
  }

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let reservationId = e.target.getAttribute("data-reservation_id");
    submitButton.href = `edit_reservation/${reservationId}`;
  });
}