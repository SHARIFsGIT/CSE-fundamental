// Check for tasks due soon and update notification count
function checkDueTasks() {
  if (!notificationCount) return;

  const today = new Date();
  today.setHours(0, 0, 0, 0);

  const threeDaysLater = new Date(today);
  threeDaysLater.setDate(threeDaysLater.getDate() + 3);

  const dueSoon = tasks.filter((task) => {
    const dueDate = new Date(task.dueDate);
    dueDate.setHours(0, 0, 0, 0);
    return (
      task.status !== "completed" &&
      dueDate <= threeDaysLater &&
      dueDate >= today
    );
  });

  const overdue = tasks.filter((task) => {
    const dueDate = new Date(task.dueDate);
    dueDate.setHours(0, 0, 0, 0);
    return task.status !== "completed" && dueDate < today;
  });

  const totalAlerts = dueSoon.length + overdue.length;

  if (notificationCount) {
    notificationCount.textContent = totalAlerts;

    if (totalAlerts > 0) {
      notificationCount.classList.remove("hidden");
    } else {
      notificationCount.classList.add("hidden");
    }
  }

  // Check if notification should be shown
  if (userSettings.enableNotifications) {
    // Only show notification for overdue tasks that were updated today
    // (to avoid showing notifications for the same overdue tasks every time)
    const today = new Date().toISOString().split("T")[0];
    const newlyOverdue = overdue.filter((task) => {
      return task.updatedAt.split("T")[0] === today;
    });

    if (newlyOverdue.length > 0) {
      showToast(
        "Warning",
        "Overdue Tasks",
        `You have ${newlyOverdue.length} task${
          newlyOverdue.length > 1 ? "s" : ""
        } that ${newlyOverdue.length > 1 ? "are" : "is"} now overdue`,
        "warning"
      );
    }
  }

  return { dueSoon, overdue };
}

// Create a notification center view
function showNotificationCenter() {
  if (!taskDetailsModal || !taskDetailsTitle || !taskDetailsContent) return;

  const { dueSoon, overdue } = checkDueTasks();

  if (dueSoon.length === 0 && overdue.length === 0) {
    showToast(
      "Info",
      "No Alerts",
      "You don't have any tasks due soon or overdue",
      "info"
    );
    return;
  }

  // Create content for notification modal
  let content = '<div class="flex flex-col gap-6">';

  if (overdue.length > 0) {
    content += `<div>
                  <h3 class="text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase mb-2">Overdue (${overdue.length})</h3>
                  <div class="space-y-3">`;

    overdue.forEach((task) => {
      content += `
                  <div class="flex items-start gap-3 p-3 bg-gray-50 dark:bg-gray-800 rounded-lg border-l-4 border-red-500 transition duration-200 hover:-translate-y-1 hover:shadow-md" data-task-id="${
                    task.id
                  }">
                      <div class="w-10 h-10 flex-shrink-0 bg-white dark:bg-gray-900 rounded-full flex items-center justify-center text-red-500">
                          <i class="fas fa-exclamation-circle"></i>
                      </div>
                      <div class="flex-grow">
                          <div class="font-medium text-gray-800 dark:text-white mb-1">${
                            task.name
                          }</div>
                          <div class="flex flex-wrap gap-2 text-xs text-gray-500 dark:text-gray-400">
                              <span class="inline-block px-2 py-1 rounded-full priority-${
                                task.priority
                              }">${formatPriority(task.priority)}</span>
                              <span>Due: ${formatDate(task.dueDate)}</span>
                          </div>
                      </div>
                      <div class="flex gap-2">
                          <button class="view-task-btn w-8 h-8 flex items-center justify-center bg-white dark:bg-gray-900 rounded-md text-gray-700 dark:text-gray-300 
                              hover:bg-indigo-500 hover:text-white transition-colors" data-task-id="${
                                task.id
                              }">
                              <i class="fas fa-eye"></i>
                          </button>
                          <button class="move-task-btn w-8 h-8 flex items-center justify-center bg-white dark:bg-gray-900 rounded-md text-gray-700 dark:text-gray-300 
                              hover:bg-primary hover:text-white transition-colors" data-task-id="${
                                task.id
                              }">
                              <i class="fas fa-arrow-right"></i>
                          </button>
                      </div>
                  </div>
              `;
    });

    content += "</div></div>";
  }

  if (dueSoon.length > 0) {
    content += `<div>
                  <h3 class="text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase mb-2">Due Soon (${dueSoon.length})</h3>
                  <div class="space-y-3">`;

    dueSoon.forEach((task) => {
      content += `
                  <div class="flex items-start gap-3 p-3 bg-gray-50 dark:bg-gray-800 rounded-lg border-l-4 border-yellow-500 transition duration-200 hover:-translate-y-1 hover:shadow-md" data-task-id="${
                    task.id
                  }">
                      <div class="w-10 h-10 flex-shrink-0 bg-white dark:bg-gray-900 rounded-full flex items-center justify-center text-yellow-500">
                          <i class="fas fa-clock"></i>
                      </div>
                      <div class="flex-grow">
                          <div class="font-medium text-gray-800 dark:text-white mb-1">${
                            task.name
                          }</div>
                          <div class="flex flex-wrap gap-2 text-xs text-gray-500 dark:text-gray-400">
                              <span class="inline-block px-2 py-1 rounded-full priority-${
                                task.priority
                              }">${formatPriority(task.priority)}</span>
                              <span>Due: ${formatDate(
                                task.dueDate
                              )} (${getDaysLeft(task.dueDate)})</span>
                          </div>
                      </div>
                      <div class="flex gap-2">
                          <button class="view-task-btn w-8 h-8 flex items-center justify-center bg-white dark:bg-gray-900 rounded-md text-gray-700 dark:text-gray-300 
                              hover:bg-indigo-500 hover:text-white transition-colors" data-task-id="${
                                task.id
                              }">
                              <i class="fas fa-eye"></i>
                          </button>
                          <button class="move-task-btn w-8 h-8 flex items-center justify-center bg-white dark:bg-gray-900 rounded-md text-gray-700 dark:text-gray-300 
                              hover:bg-primary hover:text-white transition-colors" data-task-id="${
                                task.id
                              }">
                              <i class="fas fa-arrow-right"></i>
                          </button>
                      </div>
                  </div>
              `;
    });

    content += "</div></div>";
  }

  content += "</div>";

  // Create and show a modal with notifications
  taskDetailsTitle.textContent = "Task Notifications";
  taskDetailsContent.innerHTML = content;

  // Hide action buttons that don't apply
  if (editTaskDetailsBtn) editTaskDetailsBtn.style.display = "none";
  if (completeTaskBtn) completeTaskBtn.style.display = "none";

  taskDetailsModal.classList.remove("hidden");

  // Add event listeners to buttons
  setTimeout(() => {
    document.querySelectorAll(".view-task-btn").forEach((btn) => {
      btn.addEventListener("click", function () {
        const taskId = this.dataset.taskId;
        closeTaskDetailsModal();
        openTaskDetailsModal(taskId);
      });
    });

    document.querySelectorAll(".move-task-btn").forEach((btn) => {
      btn.addEventListener("click", function () {
        const taskId = this.dataset.taskId;
        moveTaskToNextStatus(taskId);
        closeTaskDetailsModal();
        showNotificationCenter(); // Refresh notification center
      });
    });
  }, 100);
}

// Apply filters and sort
function applyFiltersAndSort() {
  // Check if we should hide completed tasks based on settings
  let statusFilter = activeFilters.status;
  if (!userSettings.showCompletedTasks && !statusFilter) {
    statusFilter = "todo,in-progress";
  }

  // Apply search filter
  filteredTasks = tasks.filter((task) => {
    const searchMatch =
      !activeFilters.search ||
      task.name.toLowerCase().includes(activeFilters.search.toLowerCase()) ||
      (task.description &&
        task.description
          .toLowerCase()
          .includes(activeFilters.search.toLowerCase()));

    // Handle status filter with comma separation for multiple values
    let statusMatch = true;
    if (statusFilter) {
      const statusValues = statusFilter.split(",");
      statusMatch = statusValues.includes(task.status);
    }

    const priorityMatch =
      !activeFilters.priority || task.priority === activeFilters.priority;

    return searchMatch && statusMatch && priorityMatch;
  });

  // Apply sorting
  filteredTasks.sort((a, b) => {
    let aValue = a[sortField];
    let bValue = b[sortField];

    // Special handling for dates
    if (sortField === "dueDate") {
      aValue = new Date(aValue);
      bValue = new Date(bValue);
    } else {
      // Case-insensitive string comparison
      if (typeof aValue === "string") aValue = aValue.toLowerCase();
      if (typeof bValue === "string") bValue = bValue.toLowerCase();
    }

    if (aValue < bValue) return sortDirection === "asc" ? -1 : 1;
    if (aValue > bValue) return sortDirection === "asc" ? 1 : -1;
    return 0;
  });

  // Reset to first page when filters change
  currentPage = 1;

  renderTasks();
  updatePagination();
}

// Handle search
function handleSearch() {
  activeFilters.search = taskSearch ? taskSearch.value.trim() : "";
  applyFiltersAndSort();

  if (userSettings.enableNotifications) {
    showToast(
      "Info",
      "Search Results",
      activeFilters.search
        ? `Found ${filteredTasks.length} matching task${
            filteredTasks.length === 1 ? "" : "s"
          }`
        : "Showing all tasks",
      "info"
    );
  }
}

// Handle filters
function handleFilters() {
  activeFilters.status = statusFilter ? statusFilter.value : "";
  activeFilters.priority = priorityFilter ? priorityFilter.value : "";
  applyFiltersAndSort();
}

// Handle sort
function handleSort(field) {
  // If clicking the same field, toggle direction
  if (sortField === field) {
    sortDirection = sortDirection === "asc" ? "desc" : "asc";
  } else {
    sortField = field;
    sortDirection = "asc";
  }

  // Update UI to show sort direction
  if (sortableHeaders) {
    sortableHeaders.forEach((header) => {
      const icon = header.querySelector("i");
      if (icon && header.dataset.sort === sortField) {
        icon.className =
          sortDirection === "asc"
            ? "fas fa-sort-up ml-1"
            : "fas fa-sort-down ml-1";
      } else if (icon) {
        icon.className = "fas fa-sort ml-1";
      }
    });
  }

  applyFiltersAndSort();
}

// Change page
function changePage(newPage) {
  const maxPage = Math.ceil(filteredTasks.length / itemsPerPage);
  if (newPage >= 1 && newPage <= maxPage) {
    currentPage = newPage;
    renderTasks();
    updatePagination();
  }
}

// Update pagination controls
function updatePagination() {
  if (
    !itemsRange ||
    !totalItems ||
    !pageNumbers ||
    !prevPageBtn ||
    !nextPageBtn
  )
    return;

  const totalTaskCount = filteredTasks.length;
  const maxPage = Math.ceil(totalTaskCount / itemsPerPage);

  // Calculate range of visible items
  const start = totalTaskCount > 0 ? (currentPage - 1) * itemsPerPage + 1 : 0;
  const end = Math.min(start + itemsPerPage - 1, totalTaskCount);

  // Update text
  itemsRange.textContent = totalTaskCount > 0 ? `${start}-${end}` : "0-0";
  totalItems.textContent = totalTaskCount;

  // Enable/disable prev/next buttons
  prevPageBtn.disabled = currentPage <= 1;
  nextPageBtn.disabled = currentPage >= maxPage;

  // Create page numbers
  pageNumbers.innerHTML = "";

  // Only show limited page numbers if there are many
  let startPage = Math.max(1, currentPage - 2);
  let endPage = Math.min(maxPage, startPage + 4);

  // Adjust if we're near the end
  if (endPage - startPage < 4 && startPage > 1) {
    startPage = Math.max(1, endPage - 4);
  }

  for (let i = startPage; i <= endPage; i++) {
    const pageBtn = document.createElement("div");
    pageBtn.className = `flex items-center justify-center w-8 h-8 rounded-md cursor-pointer 
        transition duration-200 hover:bg-gray-100 dark:hover:bg-gray-800 
        ${
          i === currentPage
            ? "bg-primary text-white"
            : "text-gray-800 dark:text-white"
        }`;
    pageBtn.textContent = i;
    pageBtn.addEventListener("click", () => changePage(i));
    pageNumbers.appendChild(pageBtn);
  }
}

// TASK OPERATIONS

// Render tasks in the table
function renderTasks() {
  if (!taskTableBody) return;

  taskTableBody.innerHTML = "";

  // Calculate pagination
  const startIndex = (currentPage - 1) * itemsPerPage;
  const paginatedTasks = filteredTasks.slice(
    startIndex,
    startIndex + itemsPerPage
  );

  if (paginatedTasks.length === 0) {
    taskTableBody.innerHTML = `
              <tr>
                  <td colspan="5" class="p-8 text-center text-gray-500 dark:text-gray-400">
                      <div>
                          <i class="fas fa-clipboard-list text-5xl mb-4 text-gray-400 dark:text-gray-600"></i>
                          <p>${
                            activeFilters.search ||
                            activeFilters.status ||
                            activeFilters.priority
                              ? "No tasks match your filter criteria."
                              : 'No tasks found. Click "Add Task" to create a new task.'
                          }</p>
                      </div>
                  </td>
              </tr>
          `;
    return;
  }

  paginatedTasks.forEach((task) => {
    const tr = document.createElement("tr");
    tr.dataset.taskId = task.id;
    tr.className =
      "hover:bg-gray-50 dark:hover:bg-gray-800 transition duration-150 cursor-pointer";
    tr.addEventListener("click", (e) => {
      // Don't open details if clicking on action buttons
      if (!e.target.closest(".action-buttons")) {
        openTaskDetailsModal(task.id);
      }
    });

    // Create task name with description tooltip
    const taskNameTd = document.createElement("td");
    taskNameTd.className = "p-5 border-b border-gray-200 dark:border-gray-700";
    taskNameTd.innerHTML = `
              <div class="task-name" title="${
                task.description ? task.description : ""
              }">
                  ${task.name}
                  ${
                    task.description && userSettings.showTaskDescriptions
                      ? '<i class="fas fa-info-circle text-gray-400 ml-1"></i>'
                      : ""
                  }
              </div>
          `;

    // Create status badge
    const statusTd = document.createElement("td");
    statusTd.className = "p-5 border-b border-gray-200 dark:border-gray-700";
    const statusBadge = document.createElement("span");
    statusBadge.className = `inline-block px-3 py-1 rounded-full text-xs font-medium status-${task.status}`;
    let statusText = task.status.charAt(0).toUpperCase() + task.status.slice(1);
    if (statusText === "In-progress") statusText = "In Progress";
    statusBadge.textContent = statusText;
    statusTd.appendChild(statusBadge);

    // Due date with days left indicator
    const dueDateTd = document.createElement("td");
    dueDateTd.className = "p-5 border-b border-gray-200 dark:border-gray-700";
    const daysLeft = getDaysLeft(task.dueDate);
    dueDateTd.innerHTML = `
              <div>
                  <div class="text-gray-800 dark:text-white">${formatDate(
                    task.dueDate
                  )}</div>
                  <div class="text-xs ${
                    daysLeft === "Overdue"
                      ? "text-red-600"
                      : daysLeft === "Due today"
                      ? "text-orange-500"
                      : daysLeft === "Due tomorrow"
                      ? "text-yellow-500"
                      : "text-gray-500 dark:text-gray-400"
                  }">
                      ${daysLeft}
                  </div>
              </div>
          `;

    // Create priority badge
    const priorityTd = document.createElement("td");
    priorityTd.className = "p-5 border-b border-gray-200 dark:border-gray-700";
    const priorityBadge = document.createElement("span");
    priorityBadge.className = `inline-block px-3 py-1 rounded-full text-xs font-medium priority-${task.priority}`;
    priorityBadge.textContent =
      task.priority.charAt(0).toUpperCase() + task.priority.slice(1);
    priorityTd.appendChild(priorityBadge);

    // Create action buttons
    const actionsTd = document.createElement("td");
    actionsTd.className = "p-5 border-b border-gray-200 dark:border-gray-700";
    const actionButtons = document.createElement("div");
    actionButtons.className = "flex gap-2 action-buttons";

    const editButton = document.createElement("button");
    editButton.className =
      "flex items-center justify-center w-8 h-8 bg-indigo-100 text-indigo-700 dark:bg-indigo-900 dark:text-indigo-300 rounded " +
      "hover:bg-indigo-200 dark:hover:bg-indigo-800 hover:-translate-y-1 transition duration-200";
    editButton.innerHTML = '<i class="fas fa-edit"></i>';
    editButton.title = "Edit task";
    editButton.addEventListener("click", (e) => {
      e.stopPropagation(); // Prevent row click event
      openEditTaskModal(task);
    });

    const deleteButton = document.createElement("button");
    deleteButton.className =
      "flex items-center justify-center w-8 h-8 bg-red-100 text-red-700 dark:bg-red-900 dark:text-red-300 rounded " +
      "hover:bg-red-200 dark:hover:bg-red-800 hover:-translate-y-1 transition duration-200";
    deleteButton.innerHTML = '<i class="fas fa-trash"></i>';
    deleteButton.title = "Delete task";
    deleteButton.addEventListener("click", (e) => {
      e.stopPropagation(); // Prevent row click event
      openDeleteModal(task.id);
    });

    actionButtons.appendChild(editButton);
    actionButtons.appendChild(deleteButton);
    actionsTd.appendChild(actionButtons);

    // Build the table row
    tr.appendChild(taskNameTd);
    tr.appendChild(statusTd);
    tr.appendChild(dueDateTd);
    tr.appendChild(priorityTd);
    tr.appendChild(actionsTd);

    taskTableBody.appendChild(tr);
  });
} // DOM Elements
const loginContainer = document.getElementById("loginContainer");
const dashboardContainer = document.getElementById("dashboardContainer");
const loginForm = document.getElementById("loginForm");
const loginEmail = document.getElementById("loginEmail");
const loginPassword = document.getElementById("loginPassword");
const demoAccounts = document.querySelectorAll(".demo-account");
const userProfileBtn = document.getElementById("userProfileBtn");
const userInitials = document.getElementById("userInitials");
const userName = document.getElementById("userName");
const userEmail = document.getElementById("userEmail");
const userDropdown = document.getElementById("userDropdown");
const taskTableBody = document.getElementById("taskTableBody");
const addTaskBtn = document.getElementById("addTaskBtn");
const taskModal = document.getElementById("taskModal");
const closeButtons = document.querySelectorAll(".close-button");
const modalTitle = document.getElementById("modalTitle");
const taskForm = document.getElementById("taskForm");
const taskIdInput = document.getElementById("taskId");
const taskNameInput = document.getElementById("taskName");
const taskDescriptionInput = document.getElementById("taskDescription");
const taskStatusInput = document.getElementById("taskStatus");
const taskDueDateInput = document.getElementById("taskDueDate");
const taskPriorityInput = document.getElementById("taskPriority");
const taskAssigneeInput = document.getElementById("taskAssignee");
const saveTaskBtn = document.getElementById("saveTaskBtn");
const cancelTaskBtn = document.getElementById("cancelTaskBtn");
const deleteModal = document.getElementById("deleteModal");
const confirmDeleteBtn = document.getElementById("confirmDeleteBtn");
const cancelDeleteBtn = document.getElementById("cancelDeleteBtn");
const closeDeleteModalBtn = document.getElementById("closeDeleteModal");
const taskSearch = document.getElementById("taskSearch");
const searchBtn = document.getElementById("searchBtn");
const statusFilter = document.getElementById("statusFilter");
const priorityFilter = document.getElementById("priorityFilter");
const sortableHeaders = document.querySelectorAll(".sortable");

// Settings modal elements
const settingsModal = document.getElementById("settingsModal");
const closeSettingsModalBtn = document.getElementById("closeSettingsModal");
const themeSelector = document.getElementById("themeSelector");
const itemsPerPageSelector = document.getElementById("itemsPerPageSelector");
const defaultSortSelector = document.getElementById("defaultSortSelector");
const showCompletedTasks = document.getElementById("showCompletedTasks");
const showTaskDescriptions = document.getElementById("showTaskDescriptions");
const enableNotifications = document.getElementById("enableNotifications");
const resetSettingsBtn = document.getElementById("resetSettingsBtn");
const saveSettingsBtn = document.getElementById("saveSettingsBtn");

// Task details modal elements
const taskDetailsModal = document.getElementById("taskDetailsModal");
const taskDetailsTitle = document.getElementById("taskDetailsTitle");
const taskDetailsContent = document.getElementById("taskDetailsContent");
const closeTaskDetailsModalBtn = document.getElementById(
  "closeTaskDetailsModal"
);
const editTaskDetailsBtn = document.getElementById("editTaskDetailsBtn");
const completeTaskBtn = document.getElementById("completeTaskBtn");

// Pagination elements
const prevPageBtn = document.getElementById("prevPageBtn");
const nextPageBtn = document.getElementById("nextPageBtn");
const pageNumbers = document.getElementById("pageNumbers");
const itemsRange = document.getElementById("itemsRange");
const totalItems = document.getElementById("totalItems");

// Toast notification
const notificationToast = document.getElementById("notificationToast");
const toastTitle = document.getElementById("toastTitle");
const toastMessage = document.getElementById("toastMessage");
const toastIcon = document.getElementById("toastIcon");
const toastCloseBtn = document.querySelector(".toast-close");

// Stat counters
const totalTaskCount = document.getElementById("totalTaskCount");
const completedTaskCount = document.getElementById("completedTaskCount");
const inProgressTaskCount = document.getElementById("inProgressTaskCount");
const todoTaskCount = document.getElementById("todoTaskCount");
const totalTaskDate = document.getElementById("totalTaskDate");
const completedTaskDate = document.getElementById("completedTaskDate");
const inProgressTaskDate = document.getElementById("inProgressTaskDate");
const todoTaskDate = document.getElementById("todoTaskDate");
const notificationCount = document.getElementById("notificationCount");

// Additional elements
const notificationBell = document.getElementById("notificationBell");
const exportTasksLink = document.getElementById("exportTasksLink");
const logoutLink = document.getElementById("logoutLink");

// Task data and state
let tasks = [];
let taskToDelete = null;
let currentTaskDetails = null;
let currentPage = 1;
let itemsPerPage = 5;
let sortField = "dueDate";
let sortDirection = "asc";
let filteredTasks = [];
let activeFilters = {
  search: "",
  status: "",
  priority: "",
};

// Current logged in user
let currentUser = null;

// Team members data - in a real app this would come from a server
const teamMembers = [
  {
    id: "1",
    name: "Shariful Islam",
    avatar: "SI",
    email: "sharifaiub15@gmail.com",
  },
  {
    id: "2",
    name: "Safira Husna",
    avatar: "SH",
    email: "s.husna@gmail.com",
  },
  {
    id: "3",
    name: "Shariful Islam",
    avatar: "SI",
    email: "mdsharif@uni-bremen.de",
  },
];

// Toggle user dropdown
function toggleUserDropdown() {
  if (userDropdown) {
    userDropdown.classList.toggle("hidden");
  }
}

// Show toast notification
function showToast(type, title, message, iconType) {
  // Only show notifications if enabled in settings or if it's an error
  if (!userSettings.enableNotifications && type !== "Error") {
    return;
  }

  if (!toastTitle || !toastMessage || !toastIcon || !notificationToast) return;

  // Set toast content
  toastTitle.textContent = title;
  toastMessage.textContent = message;

  // Set icon based on type
  toastIcon.className = `fas fa-${
    iconType === "success"
      ? "check-circle"
      : iconType === "error"
      ? "exclamation-circle"
      : iconType === "warning"
      ? "exclamation-triangle"
      : "info-circle"
  } ${
    iconType === "success"
      ? "text-green-500"
      : iconType === "error"
      ? "text-red-500"
      : iconType === "warning"
      ? "text-yellow-500"
      : "text-indigo-500"
  }`;

  // Show the toast
  notificationToast.classList.remove("hidden");

  // Auto-hide after 5 seconds
  setTimeout(hideToast, 5000);
}

// Hide toast notification
function hideToast() {
  if (notificationToast) notificationToast.classList.add("hidden");
}

// Setup login event listeners
function setupLoginEvents() {
  if (loginForm) {
    loginForm.addEventListener("submit", handleLogin);
  }

  // Set up demo account click events
  if (demoAccounts) {
    demoAccounts.forEach((account) => {
      account.addEventListener("click", () => {
        const email = account.dataset.email;
        if (loginEmail) loginEmail.value = email;
        if (loginPassword) loginPassword.value = "password"; // Simple demo password
      });
    });
  }
}

// Handle login
function handleLogin(e) {
  e.preventDefault();

  const email = loginEmail ? loginEmail.value : "";
  const password = loginPassword ? loginPassword.value : "";

  // In a real app, this would validate against a server
  const user = teamMembers.find((u) => u.email === email);

  if (user && password === "password") {
    // Simple password for demo
    currentUser = user;
    localStorage.setItem("currentUser", JSON.stringify(user));
    showLoginSuccess();
    setupDashboard();
  } else {
    showToast("Error", "Login Failed", "Invalid email or password", "error");
  }
}

// Show login success and transition to dashboard
function showLoginSuccess() {
  showToast(
    "Success",
    "Login Successful",
    "Welcome back, " + currentUser.name,
    "success"
  );

  // Hide login container and show dashboard
  if (loginContainer) loginContainer.classList.add("hidden");
  if (dashboardContainer) dashboardContainer.classList.remove("hidden");

  // Update user info in the UI
  if (userInitials) userInitials.textContent = currentUser.avatar;
  if (userName) userName.textContent = currentUser.name;
  if (userEmail) userEmail.textContent = currentUser.email;
}

// Handle logout
function handleLogout() {
  localStorage.removeItem("currentUser");
  currentUser = null;

  // Show login container and hide dashboard
  if (dashboardContainer) dashboardContainer.classList.add("hidden");
  if (loginContainer) loginContainer.classList.remove("hidden");

  // Reset login form
  if (loginForm) loginForm.reset();

  showToast(
    "Info",
    "Logged Out",
    "You have been logged out successfully",
    "info"
  );
}

// Set up event listeners
function setupEventListeners() {
  // User profile dropdown
  if (userProfileBtn) {
    userProfileBtn.addEventListener("click", toggleUserDropdown);
  }

  // Notification bell
  if (notificationBell) {
    notificationBell.addEventListener("click", showNotificationCenter);
  }

  // Task actions
  if (addTaskBtn) {
    addTaskBtn.addEventListener("click", openAddTaskModal);
  }

  if (taskForm) {
    taskForm.addEventListener("submit", saveTask);
  }

  if (cancelTaskBtn) {
    cancelTaskBtn.addEventListener("click", closeTaskModal);
  }

  // Close buttons for modals
  if (closeButtons) {
    closeButtons.forEach((btn) => {
      btn.addEventListener("click", function () {
        const modal = this.closest(".modal");
        if (modal) modal.classList.add("hidden");
      });
    });
  }

  // Delete task actions
  if (confirmDeleteBtn) {
    confirmDeleteBtn.addEventListener("click", deleteTask);
  }

  if (cancelDeleteBtn) {
    cancelDeleteBtn.addEventListener("click", closeDeleteModal);
  }

  if (closeDeleteModalBtn) {
    closeDeleteModalBtn.addEventListener("click", closeDeleteModal);
  }

  // Search and filters
  if (searchBtn) {
    searchBtn.addEventListener("click", handleSearch);
  }

  if (taskSearch) {
    taskSearch.addEventListener("keyup", function (e) {
      if (e.key === "Enter") handleSearch();
    });
  }

  if (statusFilter) {
    statusFilter.addEventListener("change", handleFilters);
  }

  if (priorityFilter) {
    priorityFilter.addEventListener("change", handleFilters);
  }

  // Sorting
  if (sortableHeaders) {
    sortableHeaders.forEach((header) => {
      header.addEventListener("click", function () {
        if (this.dataset && this.dataset.sort) {
          handleSort(this.dataset.sort);
        }
      });
    });
  }

  // Pagination
  if (prevPageBtn) {
    prevPageBtn.addEventListener("click", () => changePage(currentPage - 1));
  }

  if (nextPageBtn) {
    nextPageBtn.addEventListener("click", () => changePage(currentPage + 1));
  }

  // Toast close
  if (toastCloseBtn) {
    toastCloseBtn.addEventListener("click", hideToast);
  }

  // Settings modal
  if (document.getElementById("settingsLink")) {
    document.getElementById("settingsLink").addEventListener("click", (e) => {
      e.preventDefault();
      openSettingsModal();
      if (userDropdown) userDropdown.classList.add("hidden");
    });
  }

  // Export tasks
  if (exportTasksLink) {
    exportTasksLink.addEventListener("click", (e) => {
      e.preventDefault();
      exportTasksToCSV();
      if (userDropdown) userDropdown.classList.add("hidden");
    });
  }

  // Logout
  if (logoutLink) {
    logoutLink.addEventListener("click", (e) => {
      e.preventDefault();
      handleLogout();
    });
  }

  if (closeSettingsModalBtn) {
    closeSettingsModalBtn.addEventListener("click", closeSettingsModal);
  }

  if (saveSettingsBtn) {
    saveSettingsBtn.addEventListener("click", saveSettings);
  }

  if (resetSettingsBtn) {
    resetSettingsBtn.addEventListener("click", resetSettings);
  }

  // Task details modal
  if (closeTaskDetailsModalBtn) {
    closeTaskDetailsModalBtn.addEventListener("click", closeTaskDetailsModal);
  }

  if (editTaskDetailsBtn) {
    editTaskDetailsBtn.addEventListener("click", handleEditTaskFromDetails);
  }

  if (completeTaskBtn) {
    completeTaskBtn.addEventListener("click", handleCompleteTaskFromDetails);
  }

  // Sample navigation functionality
  if (document.getElementById("profileLink")) {
    document.getElementById("profileLink").addEventListener("click", (e) => {
      e.preventDefault();
      showToast("Info", "Profile", "Profile page would open here", "info");
      if (userDropdown) userDropdown.classList.add("hidden");
    });
  }

  // Close modals when clicking outside
  window.addEventListener("click", function (event) {
    if (taskModal && event.target === taskModal) {
      closeTaskModal();
    }
    if (deleteModal && event.target === deleteModal) {
      closeDeleteModal();
    }
    if (settingsModal && event.target === settingsModal) {
      closeSettingsModal();
    }
    if (taskDetailsModal && event.target === taskDetailsModal) {
      closeTaskDetailsModal();
    }
    if (
      userDropdown &&
      !event.target.matches("#userProfileBtn") &&
      !userDropdown.classList.contains("hidden")
    ) {
      userDropdown.classList.add("hidden");
    }
  });
}

// Initialize the application when DOM is loaded
document.addEventListener("DOMContentLoaded", initApp);

// Main initialization function
function initApp() {
  setupLoginEvents();
  checkAuthState();
}

// Check if user is already logged in
function checkAuthState() {
  const savedUser = localStorage.getItem("currentUser");
  if (savedUser) {
    currentUser = JSON.parse(savedUser);
    setupDashboard();
  } else {
    // Show login screen
    if (loginContainer) loginContainer.classList.remove("hidden");
    if (dashboardContainer) dashboardContainer.classList.add("hidden");
  }
}

// Setup dashboard after login
function setupDashboard() {
  // Show dashboard container and hide login
  if (loginContainer) loginContainer.classList.add("hidden");
  if (dashboardContainer) dashboardContainer.classList.remove("hidden");

  // Update user info
  if (userInitials) userInitials.textContent = currentUser.avatar;
  if (userName) userName.textContent = currentUser.name;
  if (userEmail) userEmail.textContent = currentUser.email;

  // Load data and setup dashboard
  loadUserSettings();
  applyUserSettings();
  loadTasksFromLocalStorage();
  applyFiltersAndSort();
  updateStatistics();
  setCurrentDate();
  checkDueTasks();
  setupEventListeners();
}

// Open Settings Modal
function openSettingsModal() {
  if (!settingsModal) return;

  // Ensure settings form is populated with current values
  if (themeSelector) themeSelector.value = userSettings.theme;
  if (itemsPerPageSelector)
    itemsPerPageSelector.value = userSettings.itemsPerPage;
  if (defaultSortSelector) defaultSortSelector.value = userSettings.defaultSort;
  if (showCompletedTasks)
    showCompletedTasks.checked = userSettings.showCompletedTasks;
  if (showTaskDescriptions)
    showTaskDescriptions.checked = userSettings.showTaskDescriptions;
  if (enableNotifications)
    enableNotifications.checked = userSettings.enableNotifications;

  settingsModal.classList.remove("hidden");
}

// Close Settings Modal
function closeSettingsModal() {
  if (settingsModal) settingsModal.classList.add("hidden");
}

// Save Settings
function saveSettings() {
  userSettings = {
    theme: themeSelector ? themeSelector.value : "light",
    itemsPerPage: itemsPerPageSelector
      ? parseInt(itemsPerPageSelector.value)
      : 5,
    defaultSort: defaultSortSelector ? defaultSortSelector.value : "dueDate",
    defaultSortDirection: sortDirection,
    showCompletedTasks: showCompletedTasks ? showCompletedTasks.checked : true,
    showTaskDescriptions: showTaskDescriptions
      ? showTaskDescriptions.checked
      : true,
    enableNotifications: enableNotifications
      ? enableNotifications.checked
      : true,
  };

  saveUserSettings();
  closeSettingsModal();
  showToast(
    "Success",
    "Settings Saved",
    "Your settings have been updated",
    "success"
  );
}

// Reset Settings to Default
function resetSettings() {
  const defaultSettings = {
    theme: "light",
    itemsPerPage: 5,
    defaultSort: "dueDate",
    defaultSortDirection: "asc",
    showCompletedTasks: true,
    showTaskDescriptions: true,
    enableNotifications: true,
  };

  userSettings = defaultSettings;
  saveUserSettings();

  // Update form values
  if (themeSelector) themeSelector.value = defaultSettings.theme;
  if (itemsPerPageSelector)
    itemsPerPageSelector.value = defaultSettings.itemsPerPage;
  if (defaultSortSelector)
    defaultSortSelector.value = defaultSettings.defaultSort;
  if (showCompletedTasks)
    showCompletedTasks.checked = defaultSettings.showCompletedTasks;
  if (showTaskDescriptions)
    showTaskDescriptions.checked = defaultSettings.showTaskDescriptions;
  if (enableNotifications)
    enableNotifications.checked = defaultSettings.enableNotifications;

  showToast(
    "Success",
    "Settings Reset",
    "Settings have been reset to default values",
    "success"
  );
}

// Mark task as complete
function completeTask(taskId) {
  const taskIndex = tasks.findIndex((task) => task.id === taskId);
  if (taskIndex !== -1) {
    tasks[taskIndex].status = "completed";
    tasks[taskIndex].updatedAt = new Date().toISOString();
    saveTasksToLocalStorage();
    applyFiltersAndSort();
    updateStatistics();
    checkDueTasks();

    showToast(
      "Success",
      "Task Completed",
      `"${tasks[taskIndex].name}" marked as completed`,
      "success"
    );
  }
}

// Open Task Details Modal
function openTaskDetailsModal(taskId) {
  if (!taskDetailsModal || !taskDetailsTitle || !taskDetailsContent) return;

  const task = tasks.find((t) => t.id === taskId);
  if (!task) return;

  currentTaskDetails = task;

  // Set modal title
  taskDetailsTitle.textContent = task.name;

  // Update "Mark as Complete" button visibility
  if (completeTaskBtn) {
    completeTaskBtn.style.display =
      task.status === "completed" ? "none" : "block";
  }

  // Generate task details content
  taskDetailsContent.innerHTML = `
          <div class="mb-6">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div class="flex flex-col gap-1">
                      <div class="text-xs text-gray-500 dark:text-gray-400">Status</div>
                      <div>
                          <span class="inline-block px-3 py-1 rounded-full text-xs font-medium status-${
                            task.status
                          }">
                              ${formatStatus(task.status)}
                          </span>
                      </div>
                  </div>
                  <div class="flex flex-col gap-1">
                      <div class="text-xs text-gray-500 dark:text-gray-400">Priority</div>
                      <div>
                          <span class="inline-block px-3 py-1 rounded-full text-xs font-medium priority-${
                            task.priority
                          }">
                              ${formatPriority(task.priority)}
                          </span>
                      </div>
                  </div>
                  <div class="flex flex-col gap-1">
                      <div class="text-xs text-gray-500 dark:text-gray-400">Due Date</div>
                      <div class="text-gray-800 dark:text-white font-medium">
                          ${formatDate(task.dueDate)} (${getDaysLeft(
    task.dueDate
  )})
                      </div>
                  </div>
                  <div class="flex flex-col gap-1">
                      <div class="text-xs text-gray-500 dark:text-gray-400">Assignee</div>
                      <div class="text-gray-800 dark:text-white font-medium">
                          ${getAssigneeName(task.assignee)}
                      </div>
                  </div>
              </div>
          </div>
          
          <div class="mb-6">
              <h3 class="text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase mb-2">Description</h3>
              <div class="bg-gray-50 dark:bg-gray-800 p-4 rounded-lg text-gray-800 dark:text-white leading-relaxed">
                  ${
                    task.description
                      ? task.description
                      : "<em class='text-gray-500 dark:text-gray-400'>No description provided</em>"
                  }
              </div>
          </div>
          
          <div>
              <h3 class="text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase mb-2">Activity</h3>
              <div class="space-y-3">
                  <div class="flex gap-3 pb-3 border-b border-gray-200 dark:border-gray-700">
                      <div class="flex-shrink-0 w-8 h-8 rounded-full bg-gray-100 dark:bg-gray-800 flex items-center justify-center text-gray-500 dark:text-gray-400">
                          <i class="fas fa-clock"></i>
                      </div>
                      <div>
                          <div class="font-medium text-gray-800 dark:text-white">Last updated</div>
                          <div class="text-xs text-gray-500 dark:text-gray-400">${getTimeDifference(
                            task.updatedAt
                          )}</div>
                      </div>
                  </div>
                  <div class="flex gap-3">
                      <div class="flex-shrink-0 w-8 h-8 rounded-full bg-gray-100 dark:bg-gray-800 flex items-center justify-center text-gray-500 dark:text-gray-400">
                          <i class="fas fa-plus"></i>
                      </div>
                      <div>
                          <div class="font-medium text-gray-800 dark:text-white">Created</div>
                          <div class="text-xs text-gray-500 dark:text-gray-400">${getTimeDifference(
                            task.createdAt
                          )}</div>
                      </div>
                  </div>
              </div>
          </div>
      `;

  taskDetailsModal.classList.remove("hidden");
}

// Close Task Details Modal
function closeTaskDetailsModal() {
  if (taskDetailsModal) taskDetailsModal.classList.add("hidden");
  currentTaskDetails = null;
}

// Handle Edit Task from Details Modal
function handleEditTaskFromDetails() {
  if (currentTaskDetails) {
    closeTaskDetailsModal();
    openEditTaskModal(currentTaskDetails);
  }
}

// Handle Complete Task from Details Modal
function handleCompleteTaskFromDetails() {
  if (currentTaskDetails) {
    completeTask(currentTaskDetails.id);
    closeTaskDetailsModal();
  }
}

// Open the task modal for adding a new task
function openAddTaskModal() {
  if (!modalTitle || !taskForm || !taskModal) return;

  modalTitle.textContent = "Add New Task";
  taskForm.reset();
  setCurrentDate();
  if (taskIdInput) taskIdInput.value = "";
  if (taskAssigneeInput && currentUser)
    taskAssigneeInput.value = currentUser.id;
  taskModal.classList.remove("hidden");
}

// Open the task modal for editing a task
function openEditTaskModal(task) {
  if (!modalTitle || !taskForm || !taskModal) return;

  modalTitle.textContent = "Edit Task";
  if (taskIdInput) taskIdInput.value = task.id;
  if (taskNameInput) taskNameInput.value = task.name;
  if (taskDescriptionInput) taskDescriptionInput.value = task.description || "";
  if (taskStatusInput) taskStatusInput.value = task.status;
  if (taskDueDateInput) taskDueDateInput.value = task.dueDate;
  if (taskPriorityInput) taskPriorityInput.value = task.priority;
  if (taskAssigneeInput) taskAssigneeInput.value = task.assignee || "";
  taskModal.classList.remove("hidden");
}

// Close task modal
function closeTaskModal() {
  if (taskModal) taskModal.classList.add("hidden");
}

// Open delete confirmation modal
function openDeleteModal(taskId) {
  if (!deleteModal) return;

  taskToDelete = taskId;
  deleteModal.classList.remove("hidden");
}

// Close delete confirmation modal
function closeDeleteModal() {
  if (!deleteModal) return;

  deleteModal.classList.add("hidden");
  taskToDelete = null;
}

// Save a new task or update existing task
function saveTask(event) {
  if (event) event.preventDefault();

  const taskId = taskIdInput ? taskIdInput.value : "";
  const task = {
    name: taskNameInput ? taskNameInput.value : "",
    description: taskDescriptionInput ? taskDescriptionInput.value : "",
    status: taskStatusInput ? taskStatusInput.value : "todo",
    dueDate: taskDueDateInput
      ? taskDueDateInput.value
      : new Date().toISOString().split("T")[0],
    priority: taskPriorityInput ? taskPriorityInput.value : "medium",
    assignee: taskAssigneeInput ? taskAssigneeInput.value : "",
    updatedAt: new Date().toISOString(),
  };

  if (taskId) {
    // Update existing task
    const index = tasks.findIndex((t) => t.id === taskId);
    if (index !== -1) {
      task.id = taskId;
      task.createdAt = tasks[index].createdAt;
      tasks[index] = task;
      showToast(
        "Success",
        "Task Updated",
        "Task has been updated successfully",
        "success"
      );
    }
  } else {
    // Add new task
    task.id = generateId();
    task.createdAt = new Date().toISOString();
    tasks.push(task);
    showToast(
      "Success",
      "Task Created",
      "New task has been created successfully",
      "success"
    );
  }

  saveTasksToLocalStorage();
  applyFiltersAndSort();
  updateStatistics();
  checkDueTasks();
  closeTaskModal();
}

// Delete a task
function deleteTask() {
  if (taskToDelete) {
    const taskIndex = tasks.findIndex((task) => task.id === taskToDelete);
    if (taskIndex !== -1) {
      const taskName = tasks[taskIndex].name;

      tasks = tasks.filter((task) => task.id !== taskToDelete);
      saveTasksToLocalStorage();
      applyFiltersAndSort();
      updateStatistics();
      checkDueTasks();
      closeDeleteModal();

      showToast(
        "Success",
        "Task Deleted",
        `"${taskName}" has been deleted successfully`,
        "success"
      );
    }
  }
}

// Export tasks to CSV
function exportTasksToCSV() {
  let csvContent = "data:text/csv;charset=utf-8,";

  // Add header row
  csvContent +=
    "Task Name,Description,Status,Due Date,Priority,Assignee,Created At,Updated At\n";

  // Add data rows
  tasks.forEach((task) => {
    const assigneeName = getAssigneeName(task.assignee);
    const row = [
      `"${task.name.replace(/"/g, '""')}"`,
      `"${(task.description || "").replace(/"/g, '""')}"`,
      formatStatus(task.status),
      formatDate(task.dueDate),
      formatPriority(task.priority),
      assigneeName,
      formatDate(task.createdAt),
      formatDate(task.updatedAt),
    ];
    csvContent += row.join(",") + "\n";
  });

  // Create download link
  const encodedUri = encodeURI(csvContent);
  const link = document.createElement("a");
  link.setAttribute("href", encodedUri);
  link.setAttribute(
    "download",
    `tasks_export_${new Date().toISOString().split("T")[0]}.csv`
  );
  document.body.appendChild(link);

  // Trigger download and clean up
  link.click();
  document.body.removeChild(link);

  showToast(
    "Success",
    "Export Complete",
    "Tasks have been exported to CSV",
    "success"
  );
}

// Move task to next status
function moveTaskToNextStatus(taskId) {
  const taskIndex = tasks.findIndex((task) => task.id === taskId);
  if (taskIndex === -1) return;

  const task = tasks[taskIndex];
  let newStatus;

  switch (task.status) {
    case "todo":
      newStatus = "in-progress";
      break;
    case "in-progress":
      newStatus = "completed";
      break;
    default:
      return; // No transition for completed tasks
  }

  // Update task status
  tasks[taskIndex].status = newStatus;
  tasks[taskIndex].updatedAt = new Date().toISOString();

  saveTasksToLocalStorage();
  applyFiltersAndSort();
  updateStatistics();
  checkDueTasks();

  const statusText = formatStatus(newStatus);
  showToast(
    "Success",
    "Task Updated",
    `"${task.name}" moved to ${statusText}`,
    "success"
  );
}

// User settings with defaults
let userSettings = {
  theme: "light",
  itemsPerPage: 5,
  defaultSort: "dueDate",
  defaultSortDirection: "asc",
  showCompletedTasks: true,
  showTaskDescriptions: true,
  enableNotifications: true,
};

// UTILITY FUNCTIONS

// Generate unique ID
function generateId() {
  return Date.now().toString(36) + Math.random().toString(36).substr(2);
}

// Format date for display
function formatDate(dateString) {
  const options = { year: "numeric", month: "short", day: "numeric" };
  return new Date(dateString).toLocaleDateString(undefined, options);
}

// Get time difference in words
function getTimeDifference(dateString) {
  const date = new Date(dateString);
  const now = new Date();
  const diffInMs = now - date;
  const diffInDays = Math.floor(diffInMs / (1000 * 60 * 60 * 24));

  if (diffInDays === 0) {
    return "Today";
  } else if (diffInDays === 1) {
    return "Yesterday";
  } else if (diffInDays < 30) {
    return `${diffInDays} days ago`;
  } else if (diffInDays < 365) {
    const months = Math.floor(diffInDays / 30);
    return `${months} ${months === 1 ? "month" : "months"} ago`;
  } else {
    const years = Math.floor(diffInDays / 365);
    return `${years} ${years === 1 ? "year" : "years"} ago`;
  }
}

// Get days left until due date
function getDaysLeft(dateString) {
  const dueDate = new Date(dateString);
  dueDate.setHours(23, 59, 59, 999);

  const now = new Date();
  const diffInMs = dueDate - now;
  const diffInDays = Math.ceil(diffInMs / (1000 * 60 * 60 * 24));

  if (diffInDays < 0) {
    return "Overdue";
  } else if (diffInDays === 0) {
    return "Due today";
  } else if (diffInDays === 1) {
    return "Due tomorrow";
  } else {
    return `${diffInDays} days left`;
  }
}

// Get assignee name from ID
function getAssigneeName(assigneeId) {
  if (!assigneeId) return "Unassigned";
  const assignee = teamMembers.find((member) => member.id === assigneeId);
  return assignee ? assignee.name : "Unknown";
}

// Format task priority for display
function formatPriority(priority) {
  return priority.charAt(0).toUpperCase() + priority.slice(1);
}

// Format task status for display
function formatStatus(status) {
  let statusText = status.charAt(0).toUpperCase() + status.slice(1);
  if (statusText === "In-progress") statusText = "In Progress";
  return statusText;
}

// CORE FUNCTIONS

// Load tasks from localStorage
function loadTasksFromLocalStorage() {
  const storedTasks = localStorage.getItem("tasks");
  if (storedTasks) {
    tasks = JSON.parse(storedTasks);
  } else {
    // Default tasks if none exist
    tasks = [
      {
        id: generateId(),
        name: "Complete project proposal",
        description:
          "Finalize the project proposal document with all requirements and submit for approval.",
        status: "completed",
        dueDate: "2024-04-01",
        priority: "high",
        assignee: "1",
        createdAt: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000).toISOString(),
        updatedAt: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(),
      },
      {
        id: generateId(),
        name: "Review client feedback",
        description:
          "Go through client feedback on the latest deliverable and make necessary adjustments for the next iteration.",
        status: "in-progress",
        dueDate: "2024-04-28",
        priority: "medium",
        assignee: "2",
        createdAt: new Date(Date.now() - 5 * 24 * 60 * 60 * 1000).toISOString(),
        updatedAt: new Date(Date.now() - 1 * 24 * 60 * 60 * 1000).toISOString(),
      },
      {
        id: generateId(),
        name: "Set up team meeting",
        description:
          "Schedule a team meeting for next week to discuss project timeline and delegate upcoming tasks. Prepare agenda in advance.",
        status: "todo",
        dueDate: "2024-05-10",
        priority: "low",
        assignee: "3",
        createdAt: new Date(Date.now() - 1 * 24 * 60 * 60 * 1000).toISOString(),
        updatedAt: new Date(Date.now() - 1 * 24 * 60 * 60 * 1000).toISOString(),
      },
      {
        id: generateId(),
        name: "Update documentation",
        description:
          "Update project documentation with latest changes and ensure all technical specifications are accurate.",
        status: "todo",
        dueDate: "2024-05-15",
        priority: "medium",
        assignee: "",
        createdAt: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(),
        updatedAt: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(),
      },
      {
        id: generateId(),
        name: "Fix reported bugs",
        description:
          "Address reported bugs in the application. Prioritize critical issues affecting user experience.",
        status: "in-progress",
        dueDate: "2024-04-30",
        priority: "high",
        assignee: "1",
        createdAt: new Date(Date.now() - 3 * 24 * 60 * 60 * 1000).toISOString(),
        updatedAt: new Date(Date.now() - 3 * 24 * 60 * 60 * 1000).toISOString(),
      },
      {
        id: generateId(),
        name: "Prepare monthly report",
        description:
          "Compile monthly progress report for stakeholders with key metrics and accomplishments.",
        status: "todo",
        dueDate: "2024-05-05",
        priority: "medium",
        assignee: "2",
        createdAt: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(),
        updatedAt: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(),
      },
    ];
    saveTasksToLocalStorage();
  }
}

// Save tasks to localStorage
function saveTasksToLocalStorage() {
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

// Load user settings from localStorage
function loadUserSettings() {
  const storedSettings = localStorage.getItem("userSettings");
  if (storedSettings) {
    userSettings = { ...userSettings, ...JSON.parse(storedSettings) };
  }
}

// Apply user settings to the UI
function applyUserSettings() {
  // Apply theme
  applyTheme(userSettings.theme);

  // Set items per page
  itemsPerPage = userSettings.itemsPerPage;

  // Set default sort
  sortField = userSettings.defaultSort;
  sortDirection = userSettings.defaultSortDirection;

  // Update settings form
  if (themeSelector) themeSelector.value = userSettings.theme;
  if (itemsPerPageSelector)
    itemsPerPageSelector.value = userSettings.itemsPerPage;
  if (defaultSortSelector) defaultSortSelector.value = userSettings.defaultSort;
  if (showCompletedTasks)
    showCompletedTasks.checked = userSettings.showCompletedTasks;
  if (showTaskDescriptions)
    showTaskDescriptions.checked = userSettings.showTaskDescriptions;
  if (enableNotifications)
    enableNotifications.checked = userSettings.enableNotifications;

  // Apply filters based on settings
  if (!userSettings.showCompletedTasks && activeFilters.status === "") {
    activeFilters.status = "todo,in-progress";
    if (statusFilter) statusFilter.value = activeFilters.status;
  }
}

// Apply theme to the document
function applyTheme(theme) {
  if (theme === "system") {
    // Check system preference
    if (
      window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches
    ) {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }

    // Listen for changes in system theme
    window
      .matchMedia("(prefers-color-scheme: dark)")
      .addEventListener("change", (e) => {
        if (e.matches) {
          document.documentElement.classList.add("dark");
        } else {
          document.documentElement.classList.remove("dark");
        }
      });
  } else if (theme === "dark") {
    document.documentElement.classList.add("dark");
  } else {
    document.documentElement.classList.remove("dark");
  }
}

// Save user settings to localStorage
function saveUserSettings() {
  localStorage.setItem("userSettings", JSON.stringify(userSettings));
  applyUserSettings();
  applyFiltersAndSort();
}

// Set current date in the form
function setCurrentDate() {
  if (taskDueDateInput) {
    const today = new Date().toISOString().split("T")[0];
    taskDueDateInput.value = today;
    taskDueDateInput.min = today;
  }
}

// Update dashboard statistics
function updateStatistics() {
  if (!totalTaskCount) return;

  const total = tasks.length;
  const completed = tasks.filter((task) => task.status === "completed").length;
  const inProgress = tasks.filter(
    (task) => task.status === "in-progress"
  ).length;
  const todo = tasks.filter((task) => task.status === "todo").length;

  // Update counters
  totalTaskCount.textContent = total;
  completedTaskCount.textContent = completed;
  inProgressTaskCount.textContent = inProgress;
  todoTaskCount.textContent = todo;

  // Get latest update times
  const latestTasks = [...tasks].sort(
    (a, b) => new Date(b.updatedAt) - new Date(a.updatedAt)
  );
  const latestCompleted = tasks
    .filter((task) => task.status === "completed")
    .sort((a, b) => new Date(b.updatedAt) - new Date(a.updatedAt))[0];
  const latestInProgress = tasks
    .filter((task) => task.status === "in-progress")
    .sort((a, b) => new Date(b.updatedAt) - new Date(a.updatedAt))[0];
  const latestTodo = tasks
    .filter((task) => task.status === "todo")
    .sort((a, b) => new Date(b.updatedAt) - new Date(a.updatedAt))[0];

  // Update dates
  if (latestTasks.length > 0) {
    totalTaskDate.textContent = getTimeDifference(latestTasks[0].updatedAt);
  }

  if (latestCompleted) {
    completedTaskDate.textContent = getTimeDifference(
      latestCompleted.updatedAt
    );
  } else {
    completedTaskDate.textContent = "-";
  }

  if (latestInProgress) {
    inProgressTaskDate.textContent = getTimeDifference(
      latestInProgress.updatedAt
    );
  } else {
    inProgressTaskDate.textContent = "-";
  }

  if (latestTodo) {
    todoTaskDate.textContent = getTimeDifference(latestTodo.updatedAt);
  } else {
    todoTaskDate.textContent = "-";
  }
}
