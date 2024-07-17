<template>
    <div id="window">
      <ul>
        <li v-for="tab in tabs" :key="tab.title" @click="activeTabHash = tab.hash" 
        :class="{
          'active': tab.hash === activeTabHash,
        }">{{ tab.title }}</li>
      </ul>
      <div id="content">
        <slot></slot>
      </div>
    </div>
</template>
  
<script>
  import { computed } from "vue";
  export default {
    data () {
      return {
        activeTabHash: "", // the index of the selected tab,
        tabs: []         // all of the tabs
      }
    },

    provide() {
      return {
        addTab: (tab) => {
          // console.log(this.tabs);
          const count = this.tabs.push(tab);

          if (count === 1) {
            this.activeTabHash = tab.hash;
          }
        },
        activeTabHash: computed(() => this.activeTabHash),
      };
    },

    // mounted () {
    //   this.selectTab(0)
    // },

    // methods: {
    //     selectTab (i) {
    //       console.log("click");
    //       this.selectedIndex = i
    //       // loop over all the tabs
    //       this.tabs.forEach((tab, index) => {
    //         console.log(tab.isActive);
    //         tab.isActive = (index === i)
    //       })
    //     }
    // }
  }
</script>

<style scoped>
  ul {
    /* display: block; */
    border-radius: 5px 5px 0 0;
    background-color: rgb(199, 198, 198);
    text-align: left;
    padding-left: 10px;
    margin-bottom: 0;
  }
  li {
    padding: 10px;
    margin-top: 10px;
    color: gray;
    display: inline-block;
  }

  li:hover {
    border-radius: 5px 5px 0 0;
    outline: 1px solid gray;
    cursor: pointer;
  }

  li.active {
    outline: 0;
    border-radius: 5px 5px 0 0;
    border: 1px solid #d3d3d3;
    border-bottom: 0;
    background-color: white;
    color: black;
  }

  
  #window {
    background-color: white;
    width: 70%;
    margin: 0 auto;
    /* margin-bottom: 20px; */
    padding-bottom: 20px;
    border-radius: 5px;
  }

  #content {
    height: 270px;
    padding: 0 20px;
    margin-top: 20px;
    overflow-y: scroll;
  }

  #content > *{
    height: calc(100% - 36px);
    /* margin-top: 20px; */
  }
</style>