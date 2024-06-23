<template>
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
</template>

<style scoped>
header {
    border-bottom: 1px solid #515151;
    overflow-x: hidden;
}

.header-menu {
    display: flex;
    justify-content: space-between;
    align-items: center;
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

</style>