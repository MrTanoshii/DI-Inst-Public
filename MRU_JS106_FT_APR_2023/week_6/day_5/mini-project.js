const submit_task = (e) => {
  e.preventDefault();
  const new_task = {
    name: document.ftask.fname.value,
    description: document.ftask.fdesc.value,
    start_date: document.ftask.fstart.value,
    end_date: document.ftask.fend.value,
    done: false,
  };
  task_list.push(new_task);
  localStorage.setItem("task_list", JSON.stringify(task_list));
  render_tasks(task_list_el);
};

const clear_tasks = (task_list_el) => {
  task_list_el.textContent = "";
};

const delete_task = (index) => {
  task_list.splice(index, 1);
  localStorage.setItem("task_list", JSON.stringify(task_list));
  render_tasks(task_list_el);
};

const render_tasks = (task_list_el) => {
  clear_tasks(task_list_el);
  task_list
    .sort((a, b) => {
      return a.start_date.localeCompare(b.start_date);
    })
    .forEach((task, index) => {
      const task_el = document.createElement("div");
      task_el.classList.add("task-item");
      task_el.classList.add("col-12");
      task_el.classList.add("col-sm-6");
      task_el.classList.add("col-md-4");
      task_el.classList.add("col-lg-3");
      const days_remaining = Math.round(
        (Date.parse(task.end_date) - new Date()) / (24 * 60 * 60 * 1000)
      );
      let task_status;

      if (task.done) {
        task_status = "completed";
      } else {
        if (days_remaining > 0) {
          task_status = "uncompleted";
        } else {
          task_status = "missed";
        }
      }
      task_el.innerHTML = `
        <div class="task-item task-item__${task_status} card card-body">
            <div data-bs-toggle="collapse" href="#description-${index}">
                <div class="task-item__name">
                    <label>Name: </label>
                    <span>${task.name}</span>
                </div>
                <div class="task-item__description collapse" id="description-${index}">
                    <label>Description: </label>
                    <span>${task.description}</span>
                </div>
                <div class="task-item__start_date">
                    <label>Starting date: </label>
                    <span>${task.start_date}</span>
                </div>
                <div class="task-item__end_date">
                    <label>End date: </label>
                    <span>${task.end_date}</span>
                </div>
                <div class="task-item__days_left">
                    <label>Days remaining: </label>
                    <span>${days_remaining}</span>
                </div>
                <div class="task-item__done">
                    <label>Done: </label>
                    <input type="checkbox" id="checkbox-${index}" ${
        task.done ? "checked" : ""
      }>
                    <span>${task.done}</span>
                </div>
            </div>
            <button type="button" class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#modal-${index}">X</button>
        </div>

        <div class="modal fade" id="modal-${index}">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-body">
                        Are you sure you want to delete this task?
                    </div>
                    <div class="modal-footer">
                        <button type="button" id="btn__delete-${index}" class="btn btn-danger" data-bs-dismiss="modal">Yes</button>
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">No</button>
                    </div>
                </div>
            </div>
        </div>
        `;
      task_list_el.appendChild(task_el);
    });

  // Add event listener to checkboxes
  document.querySelectorAll("input[type='checkbox']").forEach((checkbox) => {
    checkbox.addEventListener("change", (e) => {
      e.preventDefault();
      task_list[e.target.id.split("-")[1]].done = e.target.checked;
      localStorage.setItem("task_list", JSON.stringify(task_list));
      render_tasks(task_list_el);
    });
  });

  // Add event listener to confirm delete buttons
  document.querySelectorAll(".modal-footer .btn-danger").forEach((button) => {
    button.addEventListener("click", (e) => {
      e.preventDefault();
      e.stopPropagation();
      console.log(e.target);
      console.log("The id is " + e.target.id.split("-")[1]);
      delete_task(e.target.id.split("-")[1]);
    });
  });
};

// Event listeners
document.ftask.addEventListener("submit", submit_task);

var task_list = localStorage.getItem("task_list");
if (!task_list) {
  task_list = [];
} else {
  task_list = JSON.parse(task_list);
}

var task_list_el = document.getElementById("task-list");
render_tasks(task_list_el);
