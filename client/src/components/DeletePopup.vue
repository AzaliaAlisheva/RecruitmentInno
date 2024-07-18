<template>
    <main>
        <div class="popup">
            <h1>Do you really want to delete this vacancy?</h1>
            <div class="" popup-inner>
                <slot />

            </div>
        </div>
    </main>
</template>

<script>
export default {

}
</script>

<style scoped>
.popup {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 99;
    background-color: black;
    display: flex;
    align-items: center;
    justify-content: center;
}

.popup-inner {
    background-color: aliceblue;
    padding: 32px;
}
</style>