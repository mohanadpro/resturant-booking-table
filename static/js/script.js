document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendar')
    const calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth'})
    calendar.render()
    calendarEl.addEventListener('click',function(e){
        console.log(e.target.ariaLabel);
    })})

    selectElement = document.querySelector('#number_of_geusts');
    selectElement.addEventListener('change',()=>{
        output = selectElement.value;
        console.log(output)
    })

    $(function () {
        $('.datetime-input').datetimepicker({
            format:'YYYY-MM-DD HH:mm:ss'
        });
    });