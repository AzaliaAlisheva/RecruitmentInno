<template>
    <h2>Create New Vacancy</h2>
    <div class="outer-container">
        <div class="container">
    <div class="input">
        <input type="text" placeholder="Grade" id="grade">
        <input type="text" placeholder="Stack" id="stack">
        <input type="text" placeholder="Instruments" id="instruments">
        <input type="number" placeholder="Years of Experience" id="experience" min="0" step="1">
        <div class="reg">
            <input type="checkbox" id="is_regular_staff">
            <label for="is_regular_staff">Is Regular Staff</label>
        </div>
        <input type="number" placeholder="Rate (e.g., per hour)" id="rate" min="0" step="any">
        <!-- <input type="date" placeholder="Date" id="date"> -->
        <input type="text" placeholder="Location" id="location">
        <input type="text" placeholder="Citizenship" id="citizenship">
        <input type="tel" placeholder="Contact Number" id="contact">
    </div>
</div>
    </div>



</template>
<style scoped>
.outer-container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100vw; /* Full viewport width */
}

.input {
    display: flex;
    flex-direction: column;
    width: 43vw; 
    gap: 15px; 
    background-color: #ffffff;
    padding: 20px;
    border-radius: 10px; 
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
}

input[type="text"],
input[type="number"],
input[type="date"],
input[type="tel"] {
    height: 35px; 
    padding: 10px;
    font-size: 16px; 
    border: 1px solid #ccc;
    border-radius: 5px; 
}
.reg{
    display: flex;
    gap: 2%;
    align-items: center;
}

input[type="checkbox"] {
    width: 20px; 
    height: 20px; 
}

</style>