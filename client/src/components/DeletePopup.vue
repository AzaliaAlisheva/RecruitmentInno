<template>
    <main>
        <div class="popup">
            <h1 class="popup_header">Do you really want to delete this vacancy?</h1>
            <div class="popup-inner">
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
.popup_header {
    color: black;
}

.popup {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 99;
    background-color: aliceblue;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 30%;
    /* width: 30%; */
    align-self: center;
}
</style>