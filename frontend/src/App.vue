<template>
  <div id="app">
    <div class="header-div">
      <el-button type="primary" size="mini" icon="el-icon-delete" @click="kill()"></el-button>
    </div>
    <div class="header-div">
      <el-button type="primary" size="mini" icon="el-icon-switch-button" @click="logout()"></el-button>
    </div>
    <div class="header-div">
      <el-button type="primary" size="mini" icon="el-icon-edit" @click="editor_login()"></el-button>
    </div>
    <router-view/>
    <el-drawer
        title="editor login"
        :visible.sync="dialog"
        direction="ltr"
        custom-class="demo-drawer"
        ref="drawer">
      <div class="demo-drawer__content">
        <el-form :model="form">
          <el-form-item label="user name" :label-width="formLabelWidth">
            <el-input v-model="form.user_name" autocomplete="off" style="width: 200px" disabled></el-input>
          </el-form-item>
          <el-form-item label="password" :label-width="formLabelWidth">
            <el-input v-model="form.password" autocomplete="off"  style="width: 200px"></el-input>
          </el-form-item>
          <el-form-item label="user type" :label-width="formLabelWidth" disabled>
            <el-select v-model="form.user_type"  style="width: 200px">
              <el-option label="user" value="user"></el-option>
              <el-option label="admin" value="admin"></el-option>
            </el-select>
          </el-form-item>
            <el-form-item label="member grade" :label-width="formLabelWidth">
              <el-select v-model="form.membership_grade"  style="width: 200px">
                <el-option label="admin" value="0"></el-option>
                <el-option label="1" value="1"></el-option>
                <el-option label="2" value="2"></el-option>
                <el-option label="3" value="3"></el-option>
              </el-select>
          </el-form-item>
        </el-form>
        <div class="demo-drawer__footer">
          <el-button @click="cancelForm">cancel</el-button>
          <el-button type="primary"  @click="determine_user">determine</el-button>
        </div>
      </div>
    </el-drawer>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      formLabelWidth: '110px',
      dialog: false,
      loading: false,
      form:{
        id:null,
        user_name:null,
        password:null,
        user_type:null,
        user_nickname:null,
        membership_grade:null
      }
    }
  },
  methods: {
    determine_user(){
      this.axios.post('/edit_user',this.form).then(res => {
        this.dialog=false
      }).catch(res => {
        console.log(res.data)
      })
    },
    cancelForm() {
      this.dialog = false;
    },
    logout() {
      this.$cookies.remove( 'user')
      this.$router.push({path: '/'})
    },
    editor_login() {
      this.form=this.$cookies.get('user')
      this.dialog = true
    },
    kill() {
      this.axios.post('/kill').then(res => {
        console.log(res.data)
      }).catch(res => {
        console.log(res.data)
      })
    }
  }
}
</script>

<style>
.header-div2{
  height: 20px;
  color: #ffffff !important;
  font-size: 14px;
}
.header-div {
  position: relative;
  top:10px;
  width: 40px;
  float: right;
  margin: 5px;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  width: 100%;
}
</style>

<style media="screen">
*,
*:before,
*:after {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

body {
  background-color: #080710;
}

</style>
