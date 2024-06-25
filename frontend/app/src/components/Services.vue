<script setup>
import { ref, onMounted } from 'vue';
import Header from './Header.vue';
import axios from 'axios'

const crypto = ref([])
const loading = ref(true)

const getServices = async () => {
  try {
    const {data} = await axios.get('http://127.0.0.1:8000/get-services')
    crypto.value = data
    loading.value = false
  } catch (e) {
    console.log(e)
  }
}

onMounted(() => {
  getServices()
})

</script>

<template>
  <div class="brif-section">
    <Header />
    
    <section>
      <div class="text-main">
        <h1>[rpc | api | grpc]</h1>
      </div>
    </section>

    <section class="grid-main" v-if="loading">
      <div class="grid-container">
        
        <div class="grid-item">
          <div class="main-content-services">
              <div class="main-text-services">
                <p><Skeletor width="150"/></p>
              </div>
              <div class="services-inf">
                <div class="text-a-s"><Skeletor width="100"/></div>
                <div class="text-a-s"><Skeletor width="100"/></div>
                <div class="text-a-s"><Skeletor width="100"/></div>
              </div>
          </div>
        </div>

        <div class="grid-item">
          <div class="main-content-services">
              <div class="main-text-services">
                <p><Skeletor width="150"/></p>
              </div>
              <div class="services-inf">
                <div class="text-a-s"><Skeletor width="100"/></div>
                <div class="text-a-s"><Skeletor width="100"/></div>
                <div class="text-a-s"><Skeletor width="100"/></div>
              </div>
          </div>
        </div>

        <div class="grid-item">
          <div class="main-content-services">
              <div class="main-text-services">
                <p><Skeletor width="150"/></p>
              </div>
              <div class="services-inf">
                <div class="text-a-s"><Skeletor width="100"/></div>
                <div class="text-a-s"><Skeletor width="100"/></div>
                <div class="text-a-s"><Skeletor width="100"/></div>
              </div>
          </div>
        </div>

        
      
      </div>
    </section>

    <section class="grid-main" v-else>
      <div class="grid-container">
        <div class="grid-item" v-for="item in crypto" :key="item.id">
          <div class="main-content-services">
              <div class="main-text-services">
                  <span class="text-services">{{item.name.split(' ')[1]}}</span>
              </div>
              <div class="services-inf">
                <div class="text-a-s"><a :href="item.rpc" target="_blank">RPC</a></div>
                <div class="text-a-s"><a :href="item.api" target="_blank">API</a></div>
                <div class="text-a-s"><a :href="item.grpc" target="_blank"d>GRPC</a></div>
              </div>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<style scoped>
.main-content-services {
  padding: 15px;
  border-radius: 10px;
  border: 1px solid rgb(81, 81, 81);
}


.text-services {
  font-size: 20px;
  font-weight: bold;
}

.services-inf {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.text-a-s {
  font-weight: bold;
  font-size: 16px;
  cursor: pointer;
}

</style>