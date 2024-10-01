const apiUrl = 'http://127.0.0.1:5000';

async function signUp() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const response = await fetch(`${apiUrl}/signup`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    });

    const data = await response.json();
    alert(data.message || data.error);
}

async function login() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const response = await fetch(`${apiUrl}/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    });

    const data = await response.json();
    alert(data.message || data.error);
}

async function addTask() {
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const userId = 'YOUR_USER_ID';  // Replace with the actual user ID

    const response = await fetch(`${apiUrl}/tasks`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, description, userId })
    });

    const data = await response.json();
    alert(data.message || data.error);
    fetchTasks();
}

async function fetchTasks() {
    const response = await fetch(`${apiUrl}/tasks`);
    const tasks = await response.json();

    const taskList = document.getElementById('taskList');
    taskList.innerHTML = '';
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.textContent = `${task.title}: ${task.description}`;
        taskList.appendChild(li);
    });
}

// Fetch tasks on page load
window.onload = fetchTasks;
