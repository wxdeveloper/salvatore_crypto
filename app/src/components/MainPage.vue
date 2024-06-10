<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios';

const getHeight = async () => {
  const { data } = await axios.get('https://stargaze-api.testovi.ch/cosmos/base/tendermint/v1beta1/blocks/latest')
  return data.block.header.height
}

const height = async () => {
  const { data } = await axios.get(`https://stargaze-api.testovi.ch/cosmos/staking/v1beta1/validators/starsvaloper1tnx3z8ke9za65v32qxhu65mav2282jru8989a6/delegations?height${await getHeight()}`)
  console.log(data.pagination.total)
}

onMounted(() => {
  height()
})


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
            <li class="header-child-menu-li">[services]</li>
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

    <section>
      <div class="grid-container">
        <div class="grid-item">STAKE JACKAL</div>
        <div class="grid-item">STAKE SHENTU</div>
        <div class="grid-item">123</div>  
        <div class="grid-item">3</div>
        <div class="grid-item"></div>
        <div class="grid-item"></div>  
        <div class="grid-item"></div>
        <div class="grid-item"></div>
        <div class="grid-item"></div>  
      </div>
    </section>

  </div>
</template>

<style scoped>
header {
  border-bottom: 1px solid gray;
  overflow-x: hidden;
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
  padding: 20px;
  text-align: center;
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