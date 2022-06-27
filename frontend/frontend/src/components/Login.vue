<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <!-- Bootswatch -->
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css"
        integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R"
        crossorigin="anonymous"
      />

      <div class="row">
        <div class="col-sm-12">
          <h1
            class="text-center bg-primary text-white"
            style="border-radius: 10px"
          >
            Group XX
          </h1>
          <hr />
          <br />

          <!-- Alert -->
          <b-alert variant="success" v-if="showMessage" show>
            {{ message }}
          </b-alert>
          <!-- Add company button -->
          <b-button
            v-b-modal="'add-content'"
            type="button"
            class="btn btn-success btn-sm"
            @click="addContent_modal('empresa')"
          >
            Add Empresa
          </b-button>
          <b-button
            v-b-modal="'add-content'"
            type="button"
            class="btn btn-success btn-sm"
            @click="addContent_modal('contribuinte')"
          >
            Add Contribuinte
          </b-button>
          <br /><br />
        </div>
        <!-- Start of Modal 1 -->
        <add-content
          v-if="modals_disp_ref.add_content"
          :content_type="content_type"
          :key="content_type"
          :company_list="company_list"
          @add_company="addCompany"
          @add_user="addUser"
          @close="modals_disp_ref.add_content = false"
        ></add-content>
      </div>
      <!-- Add a bootstrap table -->
      Tabela de Empresas:
      <table-xx
        @deleteContent="deleteContent"
        :key="table_key+content_type"
        :content_type="content_type"
        :companies="companies"
      >
      </table-xx>
      Tabela de Contribuintes:
      <table-xx
        @deleteContent="deleteContent"
        :key="table_key+1"
        :content_type="'contribuinte'"
        :users="users"
      >
      </table-xx>

      <!-- Footer -->
      <Footer
        class="bg-primary text-white text-center"
        style="border-radius: 10px"
        >Copyright &copy;. All Rights Reserved 2022 by Othavio.</Footer
      >
    </div>
  </div>
</template>



<script>
import axios from "axios";
import add_content from "./modals/add_content.vue";
import table_xx from "./Table_xx.vue";

export default {
  components: {
    "add-content": add_content,
    "table-xx": table_xx,
  },
  data() {
    return {
      company_list: ['xx group', 'sx group'],
      table_key: 0,
      content_type: "empresa",
      modals_disp_ref: {
        add_content: false,
      },
      showMessage: false,
      companies: [],
      users: [],
    };
  },

  message: "",

  methods: {
    addContent_modal(type) {
      this.content_type = type;
      this.modals_disp_ref.add_content = true;
    },
    // 1 GET METHOD
    getCompanies() {
      const path = "http://localhost:5000/login";
      // this.table_key ++;
      axios
        .get(path)
        .then((res) => {
          this.companies = res.data.companies;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getUsers() {
      const path = "http://localhost:5000/user";
      axios
        .get(path)
        .then((res) => {
          this.users = res.data.users;
        })
        .catch((error) => {
          console.error(error);
        });
    },

    // 2 Add company Button
    addCompany(payload) {
      const path = "http://localhost:5000/login";
      axios.post(path, payload)
        .then(() => {
          this.getCompanies();
          this.getUsers();

          // for message alert
          this.message ="company added 🕹️ !";

          // to show message when company is added
          this.showMessage = true;

          //update comany_list
          // this.company_list.push(payload.nome);

        })
        .catch((error) => {
          console.log(error);
          this.getCompanies();
          this.getUsers();
          location.reload();
        });
      this.modals_disp_ref.add_content = false;
    },

    // ADD user
    addUser(payload) {
      const path = "http://localhost:5000/user";
      this.table_key ++;
      axios
        .post(path, payload)
        .then(() => {
          this.getUsers();
          this.getCompanies();

          // for message alert
          this.message = "user added 🕹️ !";

          // to show message when company is added
          this.showMessage = true;
        })
        .catch((error) => {
          console.log(error);
          this.getUsers();
          this.getCompanies();
        });
      this.modals_disp_ref.add_content = false;
    },


    // Remove Company [ Delete Button ]
    removeContent(companyID, content_type) {
      const path = `http://localhost:5000/login/${companyID}`;
      axios
        .delete(path)
        .then(() => {
          this.getCompanies();
          this.getUsers();
          this.message = content_type + " Removed 🗑️!";
          this.showMessage = true;
          if(content_type == 'empresa'){
            this.remove_users_w_n_company(companyID);
          }

        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getCompanies();
        });
    },

    // removing users without companies
    remove_users_w_n_company(id){
      let company_name='';
      id = id.split(' ')[0];
      for (let i=0; i<this.companies.length; i++){
        if(this.companies[i]['id']==id){
          company_name = this.companies[i]['empresa']
        }
      }
      for (let i=0; i<this.users.length; i++){
        if(this.users[i]['empresa'] == company_name){
          this.removeContent(this.users[i]['id'] + ' user','company and user')
        }
      }
    },

    // Handle Delete Button
    deleteContent(content, content_type) {
      this.removeContent(content.id + " " + content_type, content_type);
    },
  },

  created() {
    this.getCompanies();
    this.getUsers();
  },
  watch: {
    table_key(){
      location.reload();
    },
    users() {
      this.getCompanies();
    },
    companies(){
      this.company_list=[]
      for(let i=0; i<this.companies.length; i++){
        this.company_list[i]=this.companies[i].['empresa'];
      }
    }
  },
};
</script>