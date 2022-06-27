<template>
    <div>
        <table v-if="content_type=='empresa'" class="table table-hover">
          <thead>
            <tr>
              <!-- table header cells -->
              <th scope="col">Empresa</th>
              <th scope="col">Código</th>
              <th scope="col">CNPJ</th>
              <th scope="col">Email</th>
              <th scope="col">Telefone</th>
              <th scope="col">Endereço</th>
              <th scope="col">Ação</th>
            </tr>
          </thead>
          <tbody>
            <!-- tr: table row -->
            <tr v-for="(company) in companies" :key="company.id">
              <!-- td : table data -->
              <td>{{company.empresa}}</td>
              <td>{{company.id}}</td>
              <td>{{company.cnpj}}</td>
              <td>{{company.email}}</td>
              <td>{{company.telefone}}</td>
              <td>{{company.endereco}}</td>
              <td>
                <tr class="btn-group" role="group">
                  <button 
                    type="button" 
                    class="btn btn-danger btn-sm" 
                    @click="$emit('deleteContent',company,'empresa')"> Delete
                  </button>
                  
                </tr>
              </td>
            </tr>
          </tbody>
        </table>
        <table v-else-if="content_type=='contribuinte'" class="table table-hover">
          <thead>
            <tr>
              <!-- table header cells -->
              <th scope="col">Nome</th>
              <th scope="col">Empresa</th>
              <th scope="col">Código</th>
              <th scope="col">CPF</th>
              <th scope="col">Email</th>
              <th scope="col">Telefone</th>
              <th scope="col">Endereço</th>
              <th scope="col">Ação</th>
            </tr>
          </thead>
          <tbody>
            <!-- tr: table row -->
            <tr v-for="(user) in users" :key="user.id">
              <!-- td : table data -->
              <td>{{user.nome}}</td>
              <td>{{user.empresa}}</td>
              <td>{{user.id}}</td>
              <td>{{user.cpf}}</td>
              <td>{{user.email}}</td>
              <td>{{user.telefone}}</td>
              <td>{{user.endereco}}</td>
              <td>
                <tr class="btn-group" role="group">
                  <button 
                    type="button" 
                    class="btn btn-danger btn-sm" 
                    @click="$emit('deleteContent',user,'user')"> Delete
                  </button>
                  
                </tr>
              </td>
            </tr>
          </tbody>
        </table>
    </div>
</template>

<script>
    export default {
        name: 'table_xx',
        props:{
            content_type: {required:true},
            companies: {required:false},
            users: {required:false}
        },
        data(){
            return{
                title:'',
            }
        },
        methods:{
        },
        watch:{
          users(){
            // console.log(this.users)
          }
        },
        mounted(){
        }
    }
</script>

