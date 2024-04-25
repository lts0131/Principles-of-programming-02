<template>
  <div>
    <el-container class="fullscreen">
      <el-aside width="200px">
        <el-menu
            default-active="1"
            class="el-menu-vertical-demo"
            @select="handleSelect"
            background-color="#080710"
            text-color="#fff"
            style="height: calc(100vh - 0px);"
            active-text-color="#ffd04b">
          <el-menu-item index="1">
            <i class="el-icon-menu"></i>
            <span slot="title">Manage member’s</span>
          </el-menu-item>
          <el-menu-item index="2">
            <i class="el-icon-menu"></i>
            <span slot="title">Manage video library</span>
          </el-menu-item>
          <el-menu-item index="3">
            <i class="el-icon-menu"></i>
            <span slot="title">  about graph display </span>
          </el-menu-item>
          <el-menu-item index="4">
            <i class="el-icon-menu"></i>
            <span slot="title">  View total revenue  </span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <div v-show="user_table_show">
          <el-table
              :data="user_tableData"
              text-color="#fff"
              height="calc(100vh - 20px)"
              border
          >
            <el-table-column
                prop="user_name"
                label="user name">
            </el-table-column>
            <el-table-column
                prop="password"
                label="password">
            </el-table-column>
            <el-table-column
                prop="user_type"
                label="user type">
            </el-table-column>
            <el-table-column
                prop="user_nickname"
                label="user nickname">
            </el-table-column>
            <el-table-column
                fixed="right"
                label="operation"
                width="300">
              <template slot-scope="scope">
                <el-button @click="editor_user(scope.row)" type="text" size="small">editor</el-button>
                <el-button @click="delete_row_user(scope.row)" type="text" size="small">delete</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div v-show="video_table_show">
          <el-table
              height="calc(100vh - 20px)"
              border
              :data="video_tableData"
              text-color="#fff"
              style="width: 100%">
            <el-table-column
                prop="video_name"
                label="video name">
            </el-table-column>
            <el-table-column
                prop="video_type"
                label="video type">
            </el-table-column>
            <el-table-column
                prop="video_language"
                label="language">
            </el-table-column>
            <el-table-column
                prop="video_length"
                label="length">
            </el-table-column>
            <el-table-column
                prop="video_fps"
                label="video_fps">
            </el-table-column>
            <el-table-column
                prop="video_clarity"
                label="video_clarity">
            </el-table-column>
            <el-table-column
                prop="video_decoding_rate"
                label="decod rate">
            </el-table-column>
            <el-table-column
                prop="video_description"
                label="video description">
            </el-table-column>
            <el-table-column
                fixed="right"
                label="operation">
              <template slot-scope="scope">
                <el-button @click="editor_video(scope.row)" type="text" size="small">editor</el-button>
                <el-button @click="delete_row_video(scope.row)" type="text" size="small">delete</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div v-show="graph_show">
          <div class="block">
            <span class="demonstration">默认</span>
            <el-image :src="src1"></el-image>
          </div>
          <div class="block">
            <span class="demonstration">默认</span>
            <el-image :src="src2"></el-image>
          </div>
        </div>
        <div v-show="revenue_table_show">
          <div style="color: #ffffff;font-size: 50px">
            total revenue is : {{ this.sum_num }} rm
          </div>
        </div>
      </el-main>
    </el-container>
    <el-drawer
        title="editor login"
        :visible.sync="dialog_user"
        direction="ltr"
        custom-class="demo-drawer"
        ref="drawer">
      <div class="demo-drawer__content">
        <el-form :model="form">
          <el-form-item label="user name" :label-width="formLabelWidth">
            <el-input v-model="form.user_name" autocomplete="off" style="width: 200px" disabled></el-input>
          </el-form-item>
          <el-form-item label="password" :label-width="formLabelWidth">
            <el-input v-model="form.password" autocomplete="off" style="width: 200px"></el-input>
          </el-form-item>
          <el-form-item label="user type" :label-width="formLabelWidth" disabled>
            <el-select v-model="form.user_type" style="width: 200px">
              <el-option label="user" value="user"></el-option>
              <el-option label="admin" value="admin"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="member grade" :label-width="formLabelWidth">
            <el-select v-model="form.membership_grade" style="width: 200px">
              <el-option label="admin" value="0"></el-option>
              <el-option label="1" value="1"></el-option>
              <el-option label="2" value="2"></el-option>
              <el-option label="3" value="3"></el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <div class="demo-drawer__footer">
          <el-button type="primary" @click="determine_user">determine</el-button>
        </div>
      </div>
    </el-drawer>
    <el-drawer
        title="editor login"
        :visible.sync="dialog_video"
        direction="ltr"
        custom-class="demo-drawer"
        ref="drawer">
      <div class="demo-drawer__content">
        <el-form :model="form_video">
          <el-form-item label="video_name" :label-width="formLabelWidth">
            <el-input v-model="form_video.video_name" autocomplete="off" style="width: 200px"></el-input>
          </el-form-item>
          <el-form-item label="video_type" :label-width="formLabelWidth">
            <el-input v-model="form_video.video_type" autocomplete="off" style="width: 200px"></el-input>
          </el-form-item>
          <el-form-item label="video_language" :label-width="formLabelWidth">
            <el-input v-model="form_video.video_language" autocomplete="off" style="width: 200px"></el-input>
          </el-form-item>
          <el-form-item label="video_length" :label-width="formLabelWidth">
            <el-input v-model="form_video.video_length" autocomplete="off" style="width: 200px"></el-input>
          </el-form-item>
          <el-form-item label="video_fps" :label-width="formLabelWidth">
            <el-input v-model="form_video.video_fps" autocomplete="off" style="width: 200px"></el-input>
          </el-form-item>
          <el-form-item label="video_clarity" :label-width="formLabelWidth">
            <el-input v-model="form_video.video_clarity" autocomplete="off" style="width: 200px"></el-input>
          </el-form-item>
          <el-form-item label="video_decoding_rate" :label-width="formLabelWidth">
            <el-input v-model="form_video.video_decoding_rate" autocomplete="off" style="width: 200px"></el-input>
          </el-form-item>
          <el-form-item label="video_description" :label-width="formLabelWidth">
            <el-input v-model="form_video.video_description" autocomplete="off" style="width: 200px"></el-input>
          </el-form-item>
        </el-form>
        <div class="demo-drawer__footer">
          <el-button type="primary" @click="determine_video">determine</el-button>
        </div>
      </div>
    </el-drawer>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'admin',
  data() {
    return {
      formLabelWidth: '110px',
      form: {},
      form_video: {},
      dialog_user: false,
      dialog_video: false,
      sum_num: "",
      user_tableData: [],
      video_tableData: [],
      top5_customers: [],
      user_table_show: true,
      video_table_show: false,
      revenue_table_show: false,
      graph_show: false,
      src1: "",
      src2: ""
    }
  },
  mounted() {
    this.getQuery()
  },
  methods: {

    getQuery() {
      this.axios.post('/get_all_video', this.form).then(res => {
        this.video_tableData = res.data
      }).catch(res => {
        console.log(res.data)
      })
      this.axios.post('/get_all_user', this.form).then(res => {
        this.user_tableData = res.data
      }).catch(res => {
        console.log(res.data)
      })
      this.axios.post('/top10_file', this.form).then(res => {
        this.src1=res.data.base64_str
      }).catch(res => {
        console.log(res.data)
      })
      this.axios.post('/top5_customers', this.form).then(res => {
        this.src2=res.data.base64_str
      }).catch(res => {
        console.log(res.data)
      })
      this.axios.post('/sum_num', this.form).then(res => {
        this.sum_num = res.data[0].sum_num
      }).catch(res => {
        console.log(res.data)
      })
    },

    handleSelect(key, keyPath) {
      if (key == 1) {
        this.user_table_show = true
        this.video_table_show = false
        this.revenue_table_show = false
        this.graph_show = false
      } else if (key == 2) {
        this.user_table_show = false
        this.video_table_show = true
        this.revenue_table_show = false
        this.graph_show = false
      } else if (key == 4) {
        this.user_table_show = false
        this.video_table_show = false
        this.revenue_table_show = true
        this.graph_show = false
      } else if (key == 3) {
        this.user_table_show = false
        this.video_table_show = false
        this.revenue_table_show = false
        this.graph_show = true
      }
    },
    editor_user(data) {
      this.form = data
      this.dialog_user = true
    },
    delete_row_user(data) {
      this.axios.post('/delete_user', data).then(res => {
        this.getQuery()
      }).catch(res => {
        console.log(res.data)
      })
    },
    delete_row_video(data) {
      this.axios.post('/delete_video', data).then(res => {
        this.getQuery()
      }).catch(res => {
        console.log(res.data)
      })
    },
    editor_video(data) {
      this.form_video = data
      this.dialog_video = true
    },
    determine_user() {
      this.axios.post('/edit_user', this.form).then(res => {
        this.dialog = false
        this.getQuery()
      }).catch(res => {
        console.log(res.data)
      })
    },
    determine_video() {
      this.axios.post('/edit_video', this.form_video).then(res => {
        this.dialog_video = false
        this.getQuery()
      }).catch(res => {
        console.log(res.data)
      })
    },
  }
}
</script>

<style>
.el-menu {
  border: none;
}
</style>
