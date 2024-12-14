
console.log('Hello reservation')

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reservationId = e.target.getAttribute("reservation_id");
      deleteConfirm.href = `delete_reservation/${reservationId}`;
      deleteModal.show();
    });
  }