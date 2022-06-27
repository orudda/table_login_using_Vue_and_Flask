<template>

    <b-modal centered id="add-content" title= "Adicionar"> {{title}}:
            
        <div class="mt-4 add-content" tabindex="-1" role="dialog">
            <form>
                <i v-if="content_type=='empresa'">
                    <div class="form-group" v-for="(row, index) in empresa" :key="index">
                        <i v-if="index == 'nome'">
                            <label for="recipient-name" class="col-form-label">{{index}} * :</label>
                            <input v-model="empresa[index]" type="text" class="form-control" id="recipient-name">
                       </i>
                       <i v-else>
                            <label for="recipient-name" class="col-form-label">{{index}}:</label>
                            <input v-model="empresa[index]" type="text" class="form-control" id="recipient-name">
                        </i>
                    </div>
                </i>
                <i v-else>
                    <div class="form-group" v-for="(row, index) in contribuinte" :key="index">
                        <i v-if="index == 'empresa'"> 
                            <label for="recipient-name" class="col-form-label">{{index}} * :</label>
                            <b-form-select
                            v-model="contribuinte[index]"
                            :options="company_list">
                            </b-form-select>
                        </i>
                        <i v-else-if="index == 'nome'">
                            <label for="recipient-name" class="col-form-label">{{index}} * :</label>
                            <input v-model="contribuinte[index]" type="text" class="form-control" id="recipient-name">
                       </i>
                        <i v-else>
                            <label for="recipient-name" class="col-form-label">{{index}}:</label>
                            <input v-model="contribuinte[index]" type="text" class="form-control" id="recipient-name">
                        </i>
                    </div>
                </i>
            </form>
            <div v-if="content_type == 'empresa'" class="add-content d-flex flex-row-reverse">
                <i v-if="check_gaps()">
                    <button  type="button" class="btn btn-success" data-dismiss="modal" @click="$emit('add_company',empresa)">Adicionar</button>
                </i>
                <!-- <button type="button" class="btn btn-primary">Send message</button> -->
            </div>
            <div v-else class="add-content d-flex flex-row-reverse">
                <i v-if="check_gaps()">
                    <button type="button" class="btn btn-success" data-dismiss="modal" @click="$emit('add_user',contribuinte)">Adicionar</button>
                </i>
                <!-- <button type="button" class="btn btn-primary">Send message</button> -->
            </div>
        </div>

        
        <template v-slot:modal-footer="{}" class="d-flex justify-content-between">
            
                <div>Elements with '*' cannot be empty </div>
                <div> {{'          '}} </div>
                <div class="text-danger">Copy rights by Rudda</div>
        </template>
    </b-modal>

</template>

<script>
    export default {
        name: 'add_content',
        props:{
            content_type: {required:true},
            company_list: {required:false}
        },
        data(){
            return{
                title:'',
                empresa:{
                    cnpj:'',
                    nome:'',
                    local:'',
                    telefone:'',
                    email:''
                },
                contribuinte:{
                    empresa:'',
                    cpf: '',
                    nome:'',
                    local:'',
                    telefone:'',
                    email:''
                }
            }
        },
        methods:{
            check_gaps(){
                if(this.content_type=='empresa')
                    if(this.empresa['nome']==''){
                        return false;
                    }
                    else{
                        return true;
                    }
                else{
                    if(this.contribuinte['nome'] == '' || this.contribuinte['empresa'] == ''){
                        return false;
                    }
                    else{
                        return true;
                    }
                }
            },
            print(){
                // console.log(this.empresa)
            }
        },
        watch:{
        },
        mounted(){
            this.title = this.content_type;
            this.cnpj=this.content_type;
            this.check_gaps();
            console.log(this.empresa['local'])

        }
    }
</script>
