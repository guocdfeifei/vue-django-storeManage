<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-lx-cascades"></i> 计量单位维护
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="container">
      <div class="handle-box">
        <el-input
          placeholder="关键字搜索"
          prefix-icon="el-icon-search"
          class="input-search"
          @input="find"
          clearable
          v-model="search">
        </el-input>
        <el-button type="primary" icon="el-icon-plus" @click="handleAlter" class="alter-button">新增</el-button>
      </div>
      <el-table
        :data="tableDataNew"
        class="table"
        ref="multipleTable"
        :row-class-name="tableRowClassName"
        header-cell-class-name="table-header"
      >
        <el-table-column type="index" width="50"></el-table-column>
        <el-table-column prop="meterage_iden" sortable label="编码" align="center"></el-table-column>
        <el-table-column prop="meterage_name" sortable label="名称" :filters="meterage_nameSet"
                         :filter-method="filter" align="center"></el-table-column>
        <el-table-column prop="meterage_dimension" sortable label="量纲" :filters="meterage_dimSet"
                         :filter-method="filter" align="center">
          <template slot-scope="scope">
            <span>{{meteragetype[scope.row.meterage_dimension].label}}</span>
          </template>
        </el-table-column>
        <el-table-column prop="meterage_creator" sortable label="创建人" :filters="meterage_creatorSet"
                         :filter-method="filter" align="center"></el-table-column>
        <el-table-column prop="meterage_createDate" sortable label="创建日期" align="center"></el-table-column>
        <el-table-column label="操作" align="center">
          <template slot-scope="scope">
            <el-button
              type="text"
              icon="el-icon-edit"
              @click="handleEdit(scope.row)"
            >编辑
            </el-button>
            <el-button
              type="text"
              icon="el-icon-unlock"
              class="red"
              @click="handleStop(scope.row)"
              v-if="scope.row.meterage_status===1"
            >停用
            </el-button>
            <el-button
              type="text"
              icon="el-icon-lock"
              class="green"
              @click="handleStart(scope.row)"
              v-if="scope.row.meterage_status===0"
            >启用
            </el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="pagination">
        <el-pagination
          @current-change="handlePageChange"
          @size-change="handleSizeChange"
          :page-sizes="[5, 10, 20, 50, 100, 200, 500]"
          :current-page="query.pageIndex"
          :page-size="query.pageSize"
          background
          layout="total, sizes, prev, pager, next, jumper"
          :total="pageTotal">
        </el-pagination>
      </div>
    </div>

    <!-- 新增弹出框 -->
    <el-dialog title="新增" :visible.sync="alterVisible" width="35%" :close-on-click-modal="false">
      <div class="container">
        <el-form ref="form" :model="form" label-width="70px"  class="form" >
          <el-row>
            <el-form-item label="编码" class="inputs" align="left">
              <el-col :span="10">
                <el-input v-model="form.meterage_iden" ></el-input>
              </el-col>
            </el-form-item>
          </el-row>
          <el-row>
            <el-form-item label="名称" class="inputs" align="left">
              <el-col :span="10">
                <el-input v-model="form.meterage_name" ></el-input>
              </el-col>
            </el-form-item>
          </el-row>
          <el-row>
            <el-form-item label="量纲"  align="left">
              <el-select v-model="form.meterage_dimension" placeholder="请选择"  class="option" >
                <el-option v-for="item in meteragetype" v-bind:key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </el-form-item>
          </el-row>
        </el-form>
      </div>
      <el-row :gutter="20" class="el-row-button-save">
        <el-col :span="1" :offset="15">
          <el-button @click="alterVisible = false">取 消</el-button>
        </el-col>
        <el-col :span="1" :offset="4">
          <el-button type="primary" @click="saveAlter">确 定</el-button>
        </el-col>
      </el-row>
    </el-dialog>

    <!-- 编辑弹出框 -->
    <el-dialog title="编辑" :visible.sync="editVisible" width="35%" :close-on-click-modal="false">
      <div class="container">
        <el-form ref="form" :model="editform" label-width="70px">
          <el-row>
            <el-form-item label="编码" class="inputs" align="left">
              <el-col :span="10">
                <el-input v-model="editform.meterage_iden" ></el-input>
              </el-col>
            </el-form-item>
          </el-row>
          <el-row>
            <el-form-item label="名称" class="inputs" align="left">
              <el-col :span="10">
                <el-input v-model="editform.meterage_name" ></el-input>
              </el-col>
            </el-form-item>
          </el-row>
          <el-row>
            <el-form-item label="量纲"  align="left">
              <el-select v-model="editform.meterage_dimension" placeholder="请选择"  class="option" >
                <el-option v-for="item in meteragetype" v-bind:key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </el-form-item>
          </el-row>
        </el-form>
      </div>
      <el-row :gutter="20" class="el-row-button-save">
        <el-col :span="1" :offset="15">
          <el-button @click="editVisible = false">取 消</el-button>
        </el-col>
        <el-col :span="1" :offset="4">
          <el-button type="primary" @click="saveEdit">确 定</el-button>
        </el-col>
      </el-row>
    </el-dialog>
  </div>
</template>

<script>
import {postAPI, getAPI} from '../../api/api'
export default {
  name: 'test',
  data () {
    return {
      query: {
        pageIndex: 1,
        pageSize: 5
      },
      meteragetype: [
        {
          value: 0,
          label: '重量'
        },
        {
          value: 1,
          label: '长度'
        },
        {
          value: 2,
          label: '面积'
        },
        {
          value: 3,
          label: '体积'
        },
        {
          value: 4,
          label: '件数'
        }
      ],
      search: '',
      form: {
        meterage_iden: '',
        meterage_name: '',
        meterage_dimension: ''
      },
      meterage_iden: '',
      meterage_nameSet: [],
      meterage_dimSet: [],
      meterage_creatorSet: [],
      editform: {
        meterage_iden: '',
        meterage_name: '',
        meterage_dimension: '',
        id: ''
      },
      tableData: [],
      tableDataNew: [],
      multipleSelection: [],
      delList: [],
      alterVisible: false,
      editVisible: false,
      pageTotal: 0
    }
  },
  created () {
    this.getData()
  },
  methods: {
    getData () {
      let _this = this
      getAPI('/base/meterages').then(function (res) {
        if (!res.data.meterages) {
          return
        }
        _this.tableData = res.data.meterages
        _this.pageTotal = res.data.meterages.length
        _this.find()
        _this.meterage_nameSet = []
        _this.meterage_dimSet = []
        _this.meterage_creatorSet = []
        let nameset = new Set()
        let dimset = new Set()
        let creatorset = new Set()
        for (let i in _this.tableData) {
          nameset.add(_this.tableData[i]['meterage_name'])
          dimset.add(_this.tableData[i]['meterage_dimension'])
          creatorset.add(_this.tableData[i]['meterage_creator'])
        }
        for (let i of nameset) {
          _this.meterage_nameSet.push({
            text: i,
            value: i
          })
        }
        for (let i of dimset) {
          _this.meterage_dimSet.push({
            text: _this.meteragetype[i].label,
            value: i
          })
        }
        for (let i of creatorset) {
          _this.meterage_creatorSet.push({
            text: i,
            value: i
          })
        }
      }).catch(function (err) {
        console.log(err)
      })
    },
    // 表格每行的class样式
    tableRowClassName ({row, rowIndex}) {
      this.pageTotal = rowIndex + 1
      if (rowIndex >= (this.query.pageIndex - 1) * this.query.pageSize && rowIndex < this.query.pageIndex * this.query.pageSize) {
        return ''
      }
      return 'tableRowDisplay'
    },
    // 表格下拉筛选
    filter (value, row, column) {
      const property = column['property']
      if (row[property] === value) {
        return true
      }
      return false
    },
    // 新增
    handleAlter () {
      this.alterVisible = true
      let _this = this
      getAPI('/base/meterages').then(function (res) {
        let maxiden
        if (res.data.message) {
          maxiden = '000001'
        } else {
          maxiden = String(parseInt(res.data.max_iden) + 1)
        }
        _this.form.meterage_iden = maxiden
        for (let i = 0; i < 6 - maxiden.length; i++) {
          _this.form.meterage_iden = '0' + _this.form.meterage_iden
        }
      })
    },
    // 一键清除新增表单
    clearform () {
      this.form.meterage_dimension = ''
      this.form.meterage_iden = ''
      this.form.meterage_name = ''
    },
    // 启用
    handleStart (row) {
      this.$confirm('确定要启用吗？', '提示', {
        type: 'warning'
      })
        .then(() => {
          let _this = this
          row.meterage_status = 1
          postAPI('/base/meterageStatus', row).then(function (res) {
            if (res.data.signal === 0) {
              _this.$message.success(`启用成功`)
              _this.getData()
            } else {
              _this.$message.error(res.data.message)
            }
          }).catch(function (err) {
            console.log(err)
            _this.$message.error(`启用失败`)
          })
        })
        .catch(() => {
          this.$message({
            type: 'info',
            message: '取消启用'
          })
        })
    },
    // 停用操作
    handleStop (row) {
      this.$confirm('确定要停用吗？', '提示', {
        type: 'warning'
      })
        .then(() => {
          let _this = this
          row.meterage_status = 0
          postAPI('/base/meterageStatus', row).then(function (res) {
            if (res.data.signal === 0) {
              _this.$message.success(`停用成功`)
              _this.getData()
            } else {
              _this.$message.error(res.data.message)
            }
          }).catch(function (err) {
            console.log(err)
            _this.$message.error(`停用失败`)
          })
        })
        .catch(() => {
          this.$message({
            type: 'info',
            message: '取消停用'
          })
        })
    },
    // 查询
    find () {
      this.pageTotal = 0
      this.tableDataNew = this.tableData.filter(data => !this.search ||
          String(data.meterage_name).toLowerCase().includes(this.search.toLowerCase()) ||
          String(data.meterage_iden).toLowerCase().includes(this.search.toLowerCase()) ||
          String(data.meterage_remarks).toLowerCase().includes(this.search.toLowerCase()) ||
          String(data.meterage_creator).toLowerCase().includes(this.search.toLowerCase()))
    },
    // 编辑操作
    handleEdit (row) {
      this.editform.meterage_iden = row.meterage_iden
      this.editform.meterage_name = row.meterage_name
      this.editform.meterage_dimension = row.meterage_dimension
      this.editform.id = row.id
      this.editform.meterage_status = row.meterage_status
      this.editVisible = true
    },
    // 保存编辑
    saveEdit () {
      let _this = this
      if (_this.editform.meterage_iden === '') {
        _this.$message.error(`编码不能为空`)
        return
      }
      if (_this.editform.meterage_iden.length > 6) {
        _this.$message.error(`编码最长为6位`)
        return
      }
      if (_this.editform.meterage_name === '') {
        _this.$message.error(`名称不能为空`)
        return
      }
      postAPI('/base/meterageUpdate', _this.editform).then(function (res) {
        if (res.data.signal === 0) {
          _this.editVisible = false
          _this.$message.success(`修改成功`)
          _this.getData()
        } else {
          _this.$message.error(res.data.message)
        }
      }).catch(function (err) {
        _this.$message.error(`修改失败`)
        console.log(err)
      })
    },
    // 保存新增
    saveAlter () {
      let _this = this
      if (_this.form.meterage_iden === '') {
        _this.$message.error(`编码不能为空`)
        return
      }
      if (_this.form.meterage_iden.length > 6) {
        _this.$message.error(`编码最长为6位`)
        return
      }
      if (_this.form.meterage_name === '') {
        _this.$message.error(`名称不能为空`)
        return
      }
      _this.form.meterage_status = 0
      postAPI('/base/meterageAdd', _this.form).then(function (res) {
        if (res.data.signal === 0) {
          _this.$message.success(`新增成功`)
          _this.alterVisible = false
          _this.getData()
          _this.clearform()
        } else {
          _this.$message.error(res.data.message)
        }
      }).catch(function (err) {
        _this.$message.error(`新增失败`)
        console.log(err)
      })
    },
    // 分页导航
    handlePageChange (val) {
      this.query.pageIndex = val
    },
    handleSizeChange (val) {
      this.query.pageSize = val
    }
  }
}</script>

<style>
  .tableRowDisplay {
    display: none;
  }
  .el-row-button-save {
    top: 15px;
  }
</style>

<style scoped>
  .handle-box {
    margin-bottom: 20px;
    position: relative;
  }

  .input-search {
    width: 50%;
  }
  .alter-button{
    position: absolute;
    right:0;
  }

  .table {
    width: 100%;
    font-size: 14px;
  }
  .red {
    color: #ff0000;
  }
  .green {
    color: GREEN;
  }
  .inputs {
    width: 590px;
  }
</style>
