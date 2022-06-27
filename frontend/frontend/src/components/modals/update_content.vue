<template>
  <div>
    <b-button id="show-btn" @click="modals_disp_ref.add_content = true"> Open modal</b-button>
    <add-content
      v-if="modals_disp_ref.add_content"
      @close="modals_disp_ref.add_content=false"
    ></add-content>
  </div>
</template>



<script>


// import axios from 'axios';
import add_content from './modals/add_content.vue';
// import update_content from './modals/update_content.vue';

  export default {
    components: {
      'add-content': add_content
    },
    data(){
      return{
        modals_disp_ref:{
          add_content: false
        }
      }
    },
    
  }
</script>

//add_content
<template>
    <div>hello word
        <b-button class="mt-3" variant="outline-danger" block @click="$emit('close')">Close Me</b-button>
    </div>
</template>

<script>
    export default {
        name: 'add_content'
    }
</script>
