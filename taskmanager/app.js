// ============================================
// SUPABASE CONFIGURATION
// REPLACE THESE WITH YOUR ACTUAL KEYS FROM SUPABASE
// ============================================
const SUPABASE_URL = 'sb_publishable_Wnp92V8fs00ttNPIZ9Efow_0TtlpFFo';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhsbnFzdHhmbWxxb2xsbm1tbHp1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ0MTM0NjEsImV4cCI6MjA4OTk4OTQ2MX0.k8my6JEE3AUqVCyTQkwpTCkGb22aaCBWXWefSI2DITQ';

// Initialize Supabase client
const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

// ============================================
// AUTHENTICATION FUNCTIONS
// ============================================

// Check if user is logged in
async function checkUser() {
    const { data: { user }, error } = await supabase.auth.getUser();
    
    if (error) {
        console.error('Auth error:', error);
    }
    
    const currentPage = window.location.pathname.split('/').pop();
    
    if (user && currentPage === 'index.html') {
        window.location.href = 'dashboard.html';
    } else if (user && currentPage === 'dashboard.html') {
        document.getElementById('userEmail').textContent = user.email;
        loadTasks();
        updateStats();
    } else if (!user && currentPage === 'dashboard.html') {
        window.location.href = 'index.html';
    }
}

// Login function
async function login() {
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;
    
    if (!email || !password) {
        alert('Please enter both email and password');
        return;
    }
    
    const { data, error } = await supabase.auth.signInWithPassword({
        email: email,
        password: password
    });
    
    if (error) {
        alert('Login failed: ' + error.message);
    } else {
        window.location.href = 'dashboard.html';
    }
}

// Signup function
async function signup() {
    const email = document.getElementById('signupEmail').value;
    const password = document.getElementById('signupPassword').value;
    
    if (!email || !password) {
        alert('Please enter both email and password');
        return;
    }
    
    if (password.length < 6) {
        alert('Password must be at least 6 characters');
        return;
    }
    
    const { data, error } = await supabase.auth.signUp({
        email: email,
        password: password
    });
    
    if (error) {
        alert('Signup failed: ' + error.message);
    } else {
        alert('Account created! You can now login.');
        showLogin();
    }
}

// Logout function
async function logout() {
    await supabase.auth.signOut();
    window.location.href = 'index.html';
}

// ============================================
// TASK MANAGEMENT FUNCTIONS
// ============================================

// Add new task
async function addTask() {
    const title = document.getElementById('taskTitle').value.trim();
    const description = document.getElementById('taskDesc').value.trim();
    
    if (!title) {
        alert('Please enter a task title');
        return;
    }
    
    const { data: { user } } = await supabase.auth.getUser();
    
    const { error } = await supabase
        .from('tasks')
        .insert([{
            title: title,
            description: description || '',
            status: 'pending',
            user_id: user.id
        }]);
    
    if (error) {
        alert('Error adding task: ' + error.message);
    } else {
        document.getElementById('taskTitle').value = '';
        document.getElementById('taskDesc').value = '';
        loadTasks();
        updateStats();
    }
}

// Load all tasks
async function loadTasks() {
    const { data: { user } } = await supabase.auth.getUser();
    
    const { data: tasks, error } = await supabase
        .from('tasks')
        .select('*')
        .eq('user_id', user.id)
        .order('created_at', { ascending: false });
    
    if (error) {
        console.error('Error loading tasks:', error);
        return;
    }
    
    const tasksList = document.getElementById('tasksList');
    
    if (!tasks || tasks.length === 0) {
        tasksList.innerHTML = '<div class="empty-state">✨ No tasks yet. Add your first task above!</div>';
        return;
    }
    
    tasksList.innerHTML = tasks.map(task => `
        <div class="task-card" data-task-id="${task.id}">
            <div class="task-title">${escapeHtml(task.title)}</div>
            <div class="task-desc">${escapeHtml(task.description || 'No description')}</div>
            <div class="task-status ${task.status === 'pending' ? 'status-pending' : 'status-completed'}">
                ${task.status === 'pending' ? '⏳ Pending' : '✅ Completed'}
            </div>
            <div class="task-actions">
                ${task.status === 'pending' ? 
                    `<button onclick="completeTask(${task.id})" class="complete-btn">✓ Complete</button>` : 
                    ''}
                <button onclick="deleteTask(${task.id})" class="delete-btn">🗑 Delete</button>
            </div>
        </div>
    `).join('');
}

// Update statistics
async function updateStats() {
    const { data: { user } } = await supabase.auth.getUser();
    
    const { data: tasks, error } = await supabase
        .from('tasks')
        .select('*')
        .eq('user_id', user.id);
    
    if (error) {
        console.error('Error loading stats:', error);
        return;
    }
    
    const total = tasks.length;
    const completed = tasks.filter(t => t.status === 'completed').length;
    const pending = total - completed;
    
    document.getElementById('totalTasks').textContent = total;
    document.getElementById('completedTasks').textContent = completed;
    document.getElementById('pendingTasks').textContent = pending;
}

// Mark task as complete
async function completeTask(taskId) {
    const { error } = await supabase
        .from('tasks')
        .update({ status: 'completed' })
        .eq('id', taskId);
    
    if (error) {
        alert('Error updating task: ' + error.message);
    } else {
        loadTasks();
        updateStats();
    }
}

// Delete task
async function deleteTask(taskId) {
    if (confirm('Are you sure you want to delete this task?')) {
        const { error } = await supabase
            .from('tasks')
            .delete()
            .eq('id', taskId);
        
        if (error) {
            alert('Error deleting task: ' + error.message);
        } else {
            loadTasks();
            updateStats();
        }
    }
}

// ============================================
// UI HELPER FUNCTIONS
// ============================================

function showSignup() {
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('signupForm').style.display = 'block';
}

function showLogin() {
    document.getElementById('signupForm').style.display = 'none';
    document.getElementById('loginForm').style.display = 'block';
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// ============================================
// INITIALIZE
// ============================================

// Run when page loads
document.addEventListener('DOMContentLoaded', checkUser);