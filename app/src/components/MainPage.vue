<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router';
import axios from 'axios';


const router = useRouter()
const crypto = ref([])
const loading = ref(true)

const getInformation = async () => {
  try {
    const { data } = await axios.get('http://127.0.0.1:8000/fetch_data')
    crypto.value = data
    loading.value = false
  } catch (e) {
    console.log(e)
  }
}




onMounted(() => {
  getInformation()
})

const stargaze = () => {
  router.push('/stargaze')
}


</script>

<template>
  <div class="brif-section">
    <header>
      <div class="header-menu">
        <div>
          <h4>testovi.ch</h4>
        </div>

        <div>
          <ul class="header-child-menu">
            <li class="header-child-menu-li">[main]</li>
            <li class="header-child-menu-li" @click="stargaze">[services]</li>
          </ul>
        </div>

        <div>
          
        </div>
      </div>
    </header>

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
  </div>
</template>

<style scoped>
header {
  border-bottom: 1px solid gray;
  overflow-x: hidden;
}

a {
  text-decoration: none;
  color: white;
}

.vue-skeletor {
  background-color: #2d2d2d;
}

.main-circle {
  text-align: center;
}

.grid-main {
  margin-top: 100px;
}

.tt-center {
  text-align: center;
}

.main-content-mom {
  padding: 15px;
  border-radius: 10px;
  border: 1px solid transparent;
  transition: all 0.15s ease-in;
}

.main-content-title{
  font-weight: 900;
}

.main-content-mom:hover {
  border: 1px solid rgb(81, 81, 81);
}

.main-content {
  display: flex;
  text-align: left;
}

.main-content-child {
  margin-left: 20px;
}

.text-main {
  text-align: center;
}

.header-child-menu {
  display: flex;
  list-style: none;
  padding: 0;
  margin: 0;
}

.header-child-menu-li {
  margin-right: 10px;
  margin-left: 10px;
  color: #dedede;
  transition: all 0.3s ease-in-out;
}

.header-child-menu-li:last-child {
  margin-right: 95px;
}

.header-child-menu-li:hover{
  cursor: pointer;
  color: white;
  font-weight: 900;
}

.header-menu {
  display: flex;
  justify-content: space-between;
  align-items: center;
}


.brif-section {
  padding: 0 calc(50% - 590px);
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  padding: 20px;
}

.grid-item {
  text-align: center;
}


.text-desc {
  color: rgb(68, 68, 68);
}


@media (min-width: 575.98px){
  .brif-section {
    padding: 0 calc(50% - 270px);
  }
}

@media (min-width: 767.98px){
  .brif-section {
    padding: 0 calc(50% - 360px);
  }
}

@media (min-width: 991.98px) {
  .brif-section {
    padding: 0 calc(50% - 480px);
  }
}

@media (min-width: 1199.98px){
  .brif-section {
    padding: 0 calc(50% - 590px);
  }
}
</style>