<script setup>
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

const test = () => {
    navigator.clipboard.writeText('tstvch');
    toast.success("Copied!", {
        autoClose: 1000,
        "theme": "dark",
        "hideProgressBar": true,
        "transition": "zoom",
    }); // ToastOptions
}

</script>

<template>
    <footer>
        <div class="footer-content">
            <p class="footer-m-r">
                <a @click="test" target="_blank" ><v-icon name="bi-discord" scale="1.3" fill="gray" animation="wrench" speed="fast" :hover=true /></a>
            </p>
            <p class="footer-m-r">
                <a href="https://github.com/ptts55" target="_blank"><v-icon name="bi-github" scale="1.3" fill="gray" animation="wrench" speed="fast" :hover=true /></a>
            </p>
            <p>
                <a href="https://twitter.com/kovshbeats" target="_blank"><v-icon name="bi-twitter" scale="1.3" fill="gray" animation="wrench" speed="fast" :hover=true /></a>
            </p>
        </div>
    </footer>
</template>


<style scoped>
footer {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
}

.footer-content {
    display: flex;
    justify-content: center;
    border-top: 1px solid #515151;
    background-color: #111111;
    align-items: center;
}

.footer-m-r {
    margin-right: 15px;
}
</style>