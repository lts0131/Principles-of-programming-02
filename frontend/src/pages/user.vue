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
            <span slot="title">video history</span>
          </el-menu-item>
          <el-menu-item index="2">
            <i class="el-icon-menu"></i>
            <span slot="title">recommended videos</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <div v-show="history_show">
          <el-table
              height="calc(100vh - 20px)"
              border
              :data="history_tableData"
              style="width: 100%">
            <el-table-column
                prop="video_name"
                label="video_name"
                width="180">
            </el-table-column>
            <el-table-column
                prop="video_type"
                label="video_type"
                width="180">
            </el-table-column>
            <el-table-column
                prop="video_length"
                label="video_length">
            </el-table-column>
            <el-table-column
                prop="video_language"
                label="video_language">
            </el-table-column>
            <el-table-column
                prop="video_decoding_rate"
                label="decoding_rate">
            </el-table-column>
            <el-table-column
                prop="video_clarity"
                label="video_clarity">
            </el-table-column>
            <el-table-column
                prop="video_fps"
                label="video_fps">
            </el-table-column>
          </el-table>
        </div>
        <div v-show="video_table_show">
          <el-table
              height="calc(100vh - 80px)"
              border
              ref="multipleTable"
              :data="video_tableData"
              text-color="#fff"
              @selection-change="handleSelectionChange"
              style="width: 100%">
            <el-table-column
                type="selection"
                width="55">
            </el-table-column>
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
          </el-table>
          <el-button type="primary" style="margin-top:10px " @click="checkVideo">payment</el-button>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'user',
  data() {
    return {
      history_tableData: [],
      video_tableData: [],
      form: {},
      history_show: true,
      video_table_show: false,
      multipleSelection: []
    }
  },
  mounted() {
    this.getQuery()
  },
  methods: {
    checkVideo() {
      for (let i = 0; i < this.$refs.multipleTable.selection.length; i++) {
        let data_video = {
          video_id: this.$refs.multipleTable.selection[i].id,
          video_income: null,
          users_name: this.form.user_name
        }
        if (this.form.membership_grade == 1) {
          data_video.video_income = this.$refs.multipleTable.selection[i].video_length / 200
        } else if (this.form.membership_grade == 2) {
          data_video.video_income = this.$refs.multipleTable.selection[i].video_length / 300
        } else if (this.form.membership_grade == 3) {
          data_video.video_income = this.$refs.multipleTable.selection[i].video_length / 400
        } else if (this.form.membership_grade == 0) {
          data_video.video_income = 0
        }
        this.add_payment(data_video)
      }
      this.getQuery()
    },
    add_payment(data) {
      this.axios.post('/add_payment', data).then(res => {
        console.log(res.data)
      }).catch(res => {
        console.log(res.data)
      })
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },
    handleSelect(key, keyPath) {
      if (key == 1) {
        this.history_show = true
        this.video_table_show = false
      } else if (key == 2) {
        this.history_show = false
        this.video_table_show = true
      }
    },
    getQuery() {
      this.form = this.$cookies.get('user')
      this.axios.post('/video_history', this.form).then(res => {
        this.history_tableData = res.data
      }).catch(res => {
        console.log(res.data)
      })
      this.axios.post('/for_video',this.form ).then(res => {
        this.video_tableData = res.data
      }).catch(res => {
        console.log(res.data)
      })
    }
  }
}
</script>

<style>
.el-menu {
  border: none;
}
</style>
