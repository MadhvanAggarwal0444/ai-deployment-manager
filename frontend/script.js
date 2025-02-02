async function handleRequest(endpoint) {
    try {
        const response = await fetch(`http://127.0.0.1:8000${endpoint}`);
        const data = await response.json();
        document.getElementById('response').innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error("Error fetching data:", error);
        document.getElementById('response').innerText = "Failed to connect to the backend!";
    }
}
