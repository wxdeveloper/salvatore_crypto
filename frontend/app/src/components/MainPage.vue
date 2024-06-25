<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router';
import axios from 'axios';
import Header from './Header.vue';
import Footer from './Footer.vue';


const router = useRouter()
const crypto = ref([])
const loading = ref(true)

const getInformation = async () => {
  try {
    const { data } = await axios.get('http://127.0.0.1:8000/get-data')
    crypto.value = data
    loading.value = false
  } catch (e) {
    console.log(e)
  }
}

onMounted(() => {
  getInformation()
})


</script>

<template>
  <div class="brif-section">
    <Header/>

    <section>
      <div class="text-main">
        <h1>[testovich]</h1>
      </div>
    </section>

    <section class="grid-main" v-if="loading">
      <div class="grid-container">
        
      
        <div class="grid-item">
          <div class="main-content-mom">
            <div class="main-content">
              <Skeletor circle size="150"/>
              <div class="main-content-child">
                <Skeletor width="100"/>
                <div class="information">
                  <p><Skeletor width="130"/></p>
                  <p><Skeletor width="150"/></p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="grid-item">
          <div class="main-content-mom">
            <div class="main-content">
              <Skeletor circle size="150"/>
              <div class="main-content-child">
                <Skeletor width="100"/>
                <div class="information">
                  <p><Skeletor width="130"/></p>
                  <p><Skeletor width="150"/></p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="grid-item">
          <div class="main-content-mom">
            <div class="main-content">
              <Skeletor circle size="150"/>
              <div class="main-content-child">
                <Skeletor width="100"/>
                <div class="information">
                  <p><Skeletor width="130"/></p>
                  <p><Skeletor width="150"/></p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="grid-item">
          <div class="main-content-mom">
            <div class="main-content">
              <Skeletor circle size="150"/>
              <div class="main-content-child">
                <Skeletor width="100"/>
                <div class="information">
                  <p><Skeletor width="130"/></p>
                  <p><Skeletor width="150"/></p>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="grid-item">
          <div class="main-content-mom">
            <div class="main-content">
              <Skeletor circle size="150"/>
              <div class="main-content-child">
                <Skeletor width="100"/>
                <div class="information">
                  <p><Skeletor width="130"/></p>
                  <p><Skeletor width="150"/></p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="grid-item">
          <div class="main-content-mom">
            <div class="main-content">
              <Skeletor circle size="150"/>
              <div class="main-content-child">
                <Skeletor width="100"/>
                <div class="information">
                  <p><Skeletor width="130"/></p>
                  <p><Skeletor width="150"/></p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>


    <section class="grid-main" v-else>
      <div class="grid-container">
        

        <div v-for="items in crypto" :key="items.id">
            <div class="grid-item" v-for="item in items" :key="item.id">
              <a :href="item.link" target="_blank">
                <div class="main-content-mom">
                  <div class="main-content">
                    <img src="/comdex.png" alt="">
                    <div class="main-content-child">
                      <span class="main-content-title">{{ item.img }}</span>
                      <div class="information">
                        <p>amount: {{ item.amount }}</p>
                        <p>total staking: {{ item.total }}</p>
                      </div>
                    </div>
                  </div>
              </div>
              </a>
            </div>
        </div>

      </div>
    </section>
    <Footer/>
  </div>
</template>